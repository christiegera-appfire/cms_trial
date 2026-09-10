# SIL scripts migration guide

Power Scripts will be unavailable during scheduled maintenance on August 8-9, 2026. Don't start a Data Center to Cloud migration during this time. Once maintenance is complete, update both your Data Center app and Power Scripts Cloud to the latest version before starting a migration.

## Overview

This guide provides comprehensive instructions for migrating Power Scripts from Jira Data Center (DC) to Jira Cloud. The migration process requires careful planning and execution to ensure the continued functionality of your scripts in the cloud environment.

Power Scripts migration involves moving scripts between fundamentally different environments. Key differences include:

- Modified execution context
- Different API availability
- Updated security constraints
- Changed performance characteristics

The guide focuses on maintaining script functionality while adapting to cloud-specific requirements.

| **See also:**   - [Useful tools and scripts for post-migration script adjustment](/cms_trial/space/PSJC/1940488576/Useful+tools+and+scripts+for+post-migration+script+adjustment/) - [SIL functions differences between Jira DC and Cloud](/cms_trial/space/PSJC/1940488545/SIL+functions+differences+between+Jira+Data+Center+and+Cloud/) - [How to convert Groovy scripts to SIL](/cms_trial/space/PSJC/1940488637/Converting+Groovy+scripts+to+SIL/) |
| --- |

---

## Prerequisites

- Administrator access to both Jira DC and Jira Cloud instances
- Inventory of existing Power Scripts
- Knowledge of Simple Issue Language (SIL)
- Understanding of cloud environment constraints
- Review the [Jira DC to Cloud script migration reference](https://appfire.atlassian.net/wiki/spaces/PSJC/pages/edit-v2/1940488352#Jira-DC-to-Cloud-script-migration-reference) to learn which scripts migrate successfully and which scripts require readjustment.

---

## Migration method

You can use an automated or manual migration method.

### Automated migration

For automated script migration, use a tool such as [Jira Cloud Migration Assistant](https://marketplace.atlassian.com/apps/1222010/jira-cloud-migration-assistant?tab=overview&hosting=datacenter) (JCMA) or [Configuration Manager for Jira](https://marketplace.atlassian.com/apps/1211611/configuration-manager-for-jira-cmj?hosting=cloud&tab=overview) (CMJ). When using a tool, the following consistencies help ensure script compatibility:

- Project and issue type names remain exact matches between Jira DC and Jira Cloud. This ensures project keys or issue type names used directly in scripts will continue to operate after migration.
- Custom field names are preserved as exact matches between Jira DC and Jira Cloud, but custom field IDs will be different.

  - If [SIL aliases](/cms_trial/space/PSJC/496206057/Custom+fields+aliases/) were used, which is a best practice, you can update the SIL aliases settings in Power Scripts for Jira Cloud. This way, the scripts will automatically work with the new IDs.
  - If custom field aliases were not used, the migration is a good opportunity to start using them.
- Status and transition names remain exact matches between Jira DC and Jira Cloud. This ensures scripts using status names, transition names, or IDs should continue to operate after migration.

A critical step before using JCMA is to update your Power Scripts apps to the latest versions. This prevents a known issue where validators and conditions are incorrectly migrated as post functions. This is fixed in Power Scripts for Jira Cloud v. 3.2.15 and Power Scripts for Jira Data Center v. 6.2.820.12 and v. 7.0.1000.7. For detailed instructions on how to prevent and resolve this issue, please see our [Known issue: Incorrect placement of validators and conditions after migration to Jira Cloud](/cms_trial/space/PSJC/2268889432/Known+issue%3A+Incorrect+placement+of+validators+and+conditions+after+migration+to+Jira+Cloud/).

Steps for automated script migration

### Manual migration

If you aren’t using a migration tool, scripts can still be migrated by uploading them to the SIL manager or through the **Apps** > **Power Scripts** > **Self Help** menu in Jira Cloud admin settings and then configuring them manually.

Steps for manual script migration

---

## Post-migration testing

After the migration, test your scripts by performing a [syntax check](/cms_trial/space/PSJC/490997104/Menu+and+toolbar+items/) in the SIL Manager (in Power Scripts for Jira Cloud).

If a script passes the syntax test, it means that:

- The functions shown in this code are compatible with both Jira DC and Cloud environments.
- The syntax of the script it correct.
- Custom field IDs are correct or have been updated in the alias file.

Passing the syntax test does not mean the script will operate exactly the same way between Jira DC and Jira Cloud.

Some scripts may not work identically between DC and cloud environments and can require adjustments due to differences in project names, issue type names, JQL queries, or other script-contained information. While using migration tools (JMCA or CMJ) improves the chances of successful script migration, these elements may still need to be adjusted to ensure the scripts operate in the cloud instance as expected.

See the [Jira DC to Cloud script migration reference](https://appfire.atlassian.net/wiki/spaces/PSJC/pages/edit-v2/1940488352#Jira-DC-to-Cloud-script-migration-reference) to learn which scripts migrate from Jira DC to Cloud and which will require adjustment.

To avoid issues in the target cloud environment, testing all scripts after the migration is strongly recommended.

---

## Required post-migration script changes

When migrated between Jira DC and Jira Cloud, the following script types require additional changes: conditions and validator scripts, Live Fields, and mail handler scripts. In addition, all existing scripted JQL functions/keywords must be updated for Jira Cloud.

### Conditions and validator scripts

Jira Cloud uses [Jira Expressions](https://developer.atlassian.com/cloud/jira/software/jira-expressions/) language for conditions and validators; scripted conditions and validators are not currently supported in Jira Cloud. While many users find Jira Expressions challenging and time-intensive to work with, there are alternative approaches. As with other features in Jira Cloud, rather than directly converting scripts and replicating Data Center solutions, consider rethinking your approach. To learn about ways to continue using SIL scripted conditions and validators in Jira Cloud, see [this article](/cms_trial/space/PSJC/804552898/Scripted+Conditions+and+Validators+in+cloud+-+a+new+paradigm/).

Jira Expressions example

```text
issue.issueType.name.match('^(Dev Task)$') == null || 
(issue.issueType.name.match('^(Dev Task)$') != null && 
issue.parent.subtasks.filter(subtask => subtask.assignee != null).length == 
issue.parent.subtasks.length)? true : false
```

SIL plus Jira Expressions example

```text
//SIL code
boolean passConditionValue = true;
if(issueType == "Dev Task") {
    for(string s in subtasks(parent)) {
        if(s.issueType == "Dev Task && isNull(s.assignee)) {
            passConditionValue = false;
        }
    }
}
setIssueEntityPropertyValue(key, "passCondition", passConditionValue);
```

```text
//Jira Expression
JSON.stringify(issue.properties['passCondition']).includes('true')
```

### Live Fields scripts

Live Fields works differently in Jira DC versus Jira Cloud.

| **In Jira DC** | **In Jira Cloud** |
| --- | --- |
| - Live Fields is a collection of functions in Power Scripts. - Used to manipulate issue screens and UI. - Uses SIL language for scripting. | - Live Fields is a standalone application. See [Live Fields](https://appfire.atlassian.net/wiki/spaces/LF) documentation for details. - It is built separately for Cloud architecture requirements. - Uses JavaScript/TypeScript instead of SIL. - Requires [an API written by Atlassian](https://appfire.atlassian.net/wiki/spaces/LF/pages/1497662612). |

Because of these differences, all Live Fields scripts must be converted from SIL to JavaScript when migrating.

#### Example

```text
//SIL (Data Center)
lfSet("summary", "Value to set");

//JavaScript (Cloud)
getFieldById("summary").setValue("Value to set");
```

### Mail handler scripts

The Power Scripts [incoming email service](/cms_trial/space/PSJC/994018140/Incoming+Mail+configuration/) works differently in Jira Cloud than in Data Center. Due to Atlassian’s Cloud architecture, email scripts In Jira Cloud:

- Cannot intercept messages sent to your primary Atlassian address ([youremail@atlassian.net](mailto:youremail@atlassian.net)).
- Can only intercept emails going to an external email accounts, such as Gmail.

Due to the differences in email handling between DC and Cloud, email scripts require different functions in each environment. Existing DC email scripts must be updated to use the [new Cloud-compatible functions](/cms_trial/space/PSJC/999162356/Incoming+Mail+Processing+Functions/).

Data Center email handler script example

```text
IncomingEmail mail = getIncomingEmail();
string issueKey = matchText(mail.subject, "[A-Z][A-Z]+-[0-9]+"); // find an issue key in the subject
if(isNull(issueKey)) {
	// if no issue key found, create a new issue
    string [] fields = {};
    fields += {"reporter", currentUserKey()};
    fields += {"assignee", getUserByEmail(mail.cc[0]).key}; 
    string newIssue = createIssue("TEST", "", "Task", mail.subject, "Minor", mail.body, {}, "", "", 0, fields);
    attachAllFilesFromEmail(newIssue);
    %newIssue%.watchers = getUserKeysFromEmails(mail.cc); 
} else {
	// if issue key found in subject, add a comment
    addComment(issueKey, currentUserKey(), mail.body);
}
```

Cloud incoming email processing script example

```text
IncomingEmail mail = getIncomingEmail();
string issueKey = mail.subject;
if(issueExists(issueKey)) {
    // add comment
    string commentText = mail.body;
    string userCommenting = getUserByEmail(mail.from).key;
    addComment(issueKey, userCommenting, commentText);
    attachAllFilesFromEmail(issueKey);
} else {
    // create issue
    string summary = mail.subject;
    string description = mail.body;
    string [] fields = {};
    fields += {"reporter", getUserByEmail(mail.from).key};
    createIssue("SCRUM", "", "Task", summary , "Minor", description, {}, "", "", fields);
}
```

### Scripted JQL functions and their keywords

When users write JQL queries that include custom scripted functionality (via keywords), Jira DC and Jira Cloud handle the execution of the [scripted JQL functions/keywords](/cms_trial/space/PSJC/490997951/Custom+Keywords/) in fundamentally different ways. This difference stems from Jira's core architecture, not from Power Scripts functionality.

| **In Jira DC** | **In Jira Cloud** |
| --- | --- |
| - The JQL scripts execute during the search operation when their associated keywords are used. - Each issue is evaluated individually through separate JQL searches. - Results are calculated in real-time when the JQL query runs. | - The JQL scripts execute before the search operation. - Results are pre-calculated and stored with each issue. - When users run JQL queries with scripted keywords, Cloud references these pre-calculated and stored values to determine which issues to include in the results. |

These architectural differences require the following changes to JQL script construction for Jira Cloud:

- Scripts no longer contain their own JQL searches within their code.
- Return statements require [additional Cloud-specific operations](/cms_trial/space/PSJC/490997951/Custom+Keywords/).
- JQL scripts in Jira Cloud can update the search values of parent and child issues as well as the value within the issue that triggered the script.

Due to these differences in script execution, all existing scripted JQL functions must be updated to use the new cloud methods, even though the keywords users type in their JQL queries remain the same.

---