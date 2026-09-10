# Converting Groovy scripts to SIL

Power Scripts will be unavailable during scheduled maintenance on July 18-19, 2026. Don't start a Data Center to Cloud migration during this time. Once maintenance is complete, update both your Data Center app and Power Scripts Cloud to the latest version before starting a migration.

Converting scripts from Groovy to Simple Issue Language (SIL) can be simpler than expected, as SIL has been simplified and requires fewer programming steps than used in Groovy code. This page presents a few key concepts and steps to help prepare Groovy scripts for conversion, especially when using a tool like [WorkFlow Pro - AI assistant for Jira](https://marketplace.atlassian.com/apps/1235422/workflow-pro-ai-assistant-for-jira?hosting=cloud&tab=overview).

## Basic differences between Groovy and SIL

### Import statements

Import statements in programming (lines 1-4 in the example Groovy script below) enable access to code from other modules or packages, making their functions, classes, and variables available in your program. Groovy depends heavily on these modules and packages, particularly Atlassian packages that provide the API to interact with the system.

SIL does not rely on import statements, so they can be deleted from the code. This eliminates time spent researching API documentation to determine which class files need to be imported or contain specific functionality.

This approach also protects scripts from system updates that change imported class files. Since SIL scripts don't directly access these classes, they aren't affected by such changes. Instead, Power Scripts handles API class updates, allowing scripts to continue functioning normally after updates.

When using AI tools to convert Groovy scripts to SIL, remove import statements before starting the conversion process. Even though AI tools are trained on SIL, they tend to replicate Groovy patterns in their output. Removing imports prevents the AI from attempting to reproduce patterns that shouldn't exist in SIL.

### Class initialization

SIL is designed to avoid direct use of Atlassian API classes, making it simpler to use. This approach makes SIL easier to use, protects scripts from class-level changes, and eliminates the class initialization step that Groovy requires (as shown in lines 12-13 of the example below).

While removing initialization code lines before AI conversion is optional, they should be deleted if the AI attempts to replicate this pattern in SIL.

#### Example 1

Example Groovy Script 1

This Groovy script identifies projects where a specific Jira group is used in the project’s permission scheme, either directly or through a project role.

```text
import com.atlassian.confluence.user.DisabledUserManager
import com.atlassian.crowd.embedded.api.CrowdService
import com.atlassian.sal.api.component.ComponentLocator
import com.onresolve.scriptrunner.parameters.annotation.ShortTextInput

@ShortTextInput(label = "Users", description = "Type usernames of deactivated users you would like to reactivate, seperated by spaces")
String names
assert names

def disabledUsers = names.split()

def disabledUserManager = ComponentLocator.getComponent(DisabledUserManager)
def crowdService = ComponentLocator.getComponent(CrowdService)

disabledUsers.each { userName ->
    def user = crowdService.getUser(userName)
    if (user) {
        if (disabledUserManager.isDisabled(user)) {
            disabledUserManager.enableUser(user)
            log.info("User $user.name has been enabled")
        } else {
            log.info("User $user.name is not disabled")
        }
    } else {
        log.debug("User $userName was not found.")
    }
}
```

### Issue initialization

In SIL, you don't need to initialize an issue to make it editable, unlike Groovy, which requires this initialization step (shown in line 7 in [Example 2](https://appfire.atlassian.net/wiki/spaces/PSJC/pages/edit-v2/1940488637#Example-2) below). This is particularly true when the script runs in the issue's context. This example shows the difference:

```text
//Groovy approach
def issue = Issues.getByKey('SR-1') as MutableIssue

//SIL approach
string key = "SR-1";
```

Groovy gets the issue and makes it editable (MutableIssue); SIL simply stores the issue key as a string.

### Setting values

Unlike Groovy, SIL doesn't require a function to set field values (shown in lines 12-13 in [Example 2](https://appfire.atlassian.net/wiki/spaces/PSJC/pages/edit-v2/1940488637#Example-2)). AI conversion tools often incorrectly retain this Groovy pattern when converting to SIL.

This example shows the difference in setting values:

```text
//Groovy approach
setPriority('Highest')

//SIL approach
priority = "Highest";
```

Groovy uses a function call (`setPriority`) and takes the priority as a parameter; SIL uses direct assignment and treats priority like a regular variable.

### Function for storing issue data

The `saveModifiedIssues()` function in SIL (Cloud only) serves for memory optimization, not for saving changes; it's not required for storing issue data. Unlike Groovy's explicit save operation (shown in line 16 in [Example 2](https://appfire.atlassian.net/wiki/spaces/PSJC/pages/edit-v2/1940488637#Example-2)), SIL automatically commits all changes when the script completes.

### Reindexing

SIL automatically reindexes issues when changes are made, making Groovy's explicit reindex command (shown in line 17) unnecessary; it can be deleted.

#### Example 2

Example Groovy Script 2

This script performs bulk issue updates without triggering emails, modifying last update times, or creating change history records.

```text
import com.adaptavist.hapi.jira.issues.Issues
import com.atlassian.jira.component.ComponentAccessor
import com.atlassian.jira.issue.MutableIssue
import com.atlassian.jira.issue.index.IssueIndexingParams
import com.atlassian.jira.issue.index.IssueIndexingService

def issueIndexingService = ComponentAccessor.getComponent(IssueIndexingService)

def issue = Issues.getByKey('SR-1') as MutableIssue

issue.set {
    setPriority('Highest')
    setSummary('my new summary')
}

issue.store()
issueIndexingService.reIndex(issue, IssueIndexingParams.INDEX_ISSUE_ONLY)
```

### Basic error handling

SIL simplifies coding by automating common tasks. Most functions in SIL come with built-in protection against data that is null, missing, or invalid in ways that can cause code error and result in code crashes. This makes Groovy's explicit error handling (as shown in lines 15-21 in [Example 3](https://appfire.atlassian.net/wiki/spaces/PSJC/pages/edit-v2/1940488637#Example-3) below) unnecessary in SIL.

SIL provides [error-handling](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15487896) capabilities and can throw specific error types, giving you control over how scripts handle errors.

### Type conversion

SIL is very flexible when it comes to [type conversion](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15488650); it handles most conversions automatically.

#### Example 3

Example Groovy Script 3

This script validates a custom template field, returning false if no template is selected and true if a template value exists. It logs the validation status through error messages.

```text
import com.atlassian.jira.component.ComponentAccessor
import com.atlassian.jira.issue.fields.CustomField
import com.atlassian.jira.issue.CustomFieldManager


CustomFieldManager cfm = ComponentAccessor.getCustomFieldManager();
CustomField templateCF = cfm.getCustomFieldObject(10112L);
log.error('[LOG] templateCF: ' + templateCF)

Map templateValue = issue.getCustomFieldValue(templateCF)
log.error('[LOG] templateValue: ' + templateValue)

boolean templateIsEmpty = templateValue.get("SELECTED_TEMPLATE") == null;

if (templateIsEmpty) {
    log.error("Template is empty")
    return false;
}

log.error("Template is not empty")
return true;
```

---

## Best practices

### SIL aliases

SIL includes a built-in feature called [SIL aliases](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15486340) that simplifies managing custom field IDs in your code. Using aliases makes code more readable and migrations easier, making it a good practice when converting from Groovy to SIL.

### Troubleshooting

#### runnerLog()

When writing scripts in the [SIL Manager](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15488465), you can use a special function called [runnerLog()](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15489023) to write output to the console. These output messages are only visible in the SIL Manager or the SIL Runner Gadget and can safely remain in your code, even when scripts run elsewhere (such as post functions).

The output messages are helpful for understanding script execution and debugging.

#### Run and debug scripts

To test and troubleshoot scripts, you can run them as if they were triggered by a specific issue. To do this:

1. In SIL Manager, open the script you want to test.
2. From the **Run** menu, select **Default Script Context**.

   ![This screenshot shows the Default Script Context option in the Run drop-down menu in SIL Manager.](/cms_trial/assets/87f95cf2-532d-4fe5-907a-2f29a7d5b040.png)
3. In the **Script context configuration** dialog window that opens, select a specific issue.

   ![Power Scripts for Jira Cloud script context configuration panel](/cms_trial/assets/2c1aa6aa-cca7-4d13-928a-2f8b9f45bc32.png)
4. Click **Run** to test your script.
5. Use the script debugger for troubleshooting.