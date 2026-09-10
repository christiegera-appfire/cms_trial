# Script Snippets Code

There are two types of snippets code. Syntax snippets contain code that is used to create common code syntaxes like loops or conditional statements. Functional snippets consist of code that is used to perform a function or operation such as creating a new Jira issue.

Please note that many script snippets contain notes or information that is commented out. These notes contain important information for the script user but can make the script look longer and more complicated then it actually is. If these comments are distracting to see they can be removed without impacting the script.

Comments are lines of code that start with “//” or “/\*”.

## Syntax Snippets

Syntax snippets are helpful for new or experienced script creators who are looking to quickly add functionality to a script without typing and without memorizing the specific syntax. They do not perform any action by themselves but can easily be combined with a functional snippet to create a custom script.

See this video to learn how to use syntax snippets in your code:

**FOR loop objects** - inserts the basic syntax for a loop that iterates through an object such as an array or array of structs. This is commonly used when importing data from CSV for JSON. See the [documentation about FOR loops](/cms_trial/space/PSJC/434472559/Statements/) for more information.

Snippet code

```java
for(string s in array_of_string) {
    // do something
}
```

**FOR loop with index** - inserts the basic syntax for a loop that iterates a fixed number of times using an index. See the [documentation about FOR loops](/cms_trial/space/PSJC/434472559/Statements/) for more information.

Snippet code

```java
for(int i = 0; i < size(array); i++) {
    // do something
}
```

**IF - ELSE** - The most common conditional logic statement will be used in almost any script. See the [documentation about IF - ELSE statements](/cms_trial/space/PSJC/434472559/Statements/) for more information.

Snippet code

```java
if(condition) {
    // do something
} else {
    // do something else
}
```

**WHILE** - A less popular type of loop then the FOR loop but no less important. This form evaluates the condition first and then executes the instructions in the body. See the [documentation about WHILE loops](/cms_trial/space/PSJC/434472559/Statements/) for more information.

Snippet code

```java
while(condition) {
    // do something
```

**DO WHILE** - A less popular type of loop than the FOR loop and even less popular than the WHILE loop. Similar to the WHILE loop except the condition is evaluated after the execution of the encapsulated block. So, even if the condition is false, the instructions will still be evaluated once. See the [documentation about DO WHILE loops](/cms_trial/space/PSJC/434472559/Statements/) for more information.

Snippet code

```java
do {
    // do something
} while(condition);
```

## Functional Snippets

Unlike the syntax based snippets, functional snippets actually perform an action or an operation to achieve a desired outcome.

## General

General script snippets are scripts that don’t fit into a specific category. This does not mean they are any less useful only that they may not be triggered from a specific place.

When scripts are not triggered from an issue as part of a workflow or other automation trigger it can change how the script is written. Some scripts are written so that they update multiple issues in bulk. It is important to understand how issue context works. For more information about scripts using the issue context the [Issue Context and Default Script Context](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15483099) documentation page.

**Create an issue** - Create a new issue in Jira using the [createIssue()](/cms_trial/space/PSJC/434507110/createIssue/) function. This function is popularly used in postfunctions for creating subtasks.

Snippet code

```java
string newKey = createIssue("TEST", "", "Story", "This issue was created by SIL"); //basic example of creating an issue
if(newKey != null) {
    //some additional changes to the issue after it is created.
    %newKey%.assignee = "admin";
    %newKey%.labels += "sil_ticket";
}
```

**Bulk change issues** - A very useful bit of code, this snippet uses standard Jira JQL to select issues using the [selectIssues()](/cms_trial/space/PSJC/434831783/selectIssues/) function. Then, the issues are iterated over using a loop giving the script creator to perform some type of scripted change to each issue that was selected. This type of script is very useful for [scheduled scripts](/cms_trial/space/PSJC/490998807/SIL+Scheduler/) such as escalation scripts, scripts that can be used in the [SIL Runner gadget](/cms_trial/space/PSJC/490998486/SIL+Runner+Gadget/), or ad-hoc scripts run directly from the SIL Manager.

Snippet code

```java
const string jql = "project = TEST"; // change the JQL to match your reality 
for(string k in selectIssues(jql, 100)) { // select first 100 issues 
    //%k%.newCustomField = %k%.customfield_12345; //migrate values from a CF to another using 'newCustomField' alias.
    //%k%.description = "[CHANGED]" + %k%.description; //add a prefix to description
    runnerLog("Selected issue " + k + ", summary :" + %k%.summary); //prints to the editor console
}
```

This script is an example where the script is not running in the context of an issue and special syntax is needed. See the [Variable Resolution](/cms_trial/space/PSJC/434602568/Variable+types+and+reference+methods/) page for more information about this syntax.

**Select a row from a table** - This script is a basic example of the code needed to select a single row of data from a database. Please note that a [data source configuration](https://appfire.atlassian.net/wiki/spaces/PSJC/pages/490996168) is required for this script to function.

Snippet code

```java
struct country {
    int id;
    string name;
    string code;
};

string param = "RO";
country c = sql("External_DB_CHANGEME", "SELECT id, name, iso_code FROM countries WHERE iso_code = ?", param); //match field for field in the structure
```

**Select multiple rows from a table -** This script is a basic example of the code needed to select multiple rows of data from a database. Please note that a [data source configuration](https://appfire.atlassian.net/wiki/spaces/PSJC/pages/490996168) is required for this script to function.

Snippet code

```java
struct country {
    int id;
    string name;
    string code;
};

string param = "RO";
country [] allcountries = sql("External_DB_CHANGEME", "SELECT id, name, iso_code FROM countries"); //match field for field in the structure
```

**Send email -** A basic example of how to send an email from a SIL script. Please note that the mail configuration must be in place in order to send emails. A quick way to test sending emails is to set the [mail configuration](/cms_trial/space/PSJC/490996015/Outgoing+Mail+configuration/) to Container Sender. See the mail configuration documentation for more information.

Snippet code

```java
//sends an email to the project leader and PMGroup group, CC to component leader for 'mycomponent'
string [] tos = { projectPM(project), "PMGroup", "somedirectemail@fooandgoo.com" };
sendEmail(tos, getProjectComponentLead(project, "mycomponent"), 
         "[SUBJECT] Snippet email subject", 
         "BODY of email: You should be informed that " + currentUser() + " has sent you this message via a PowerScripts automation");
```

## Current Issue

Script snippets under the current issue category are focused on reading/writing data to Jira issues. They can be executed in a variety of different methods including workflow triggers and listeners.

**Change the issue** - An example for changing or updating fields on an issue. For more information about accessing data for regular Jira fields or custom fields see the [Variable Resolution](/cms_trial/space/PSJC/434602568/Variable+types+and+reference+methods/) documentation page.

Snippet code

```java
//This assumes we're in the context of an issue.
runnerLog("Current issue " + key + ", summary :" + summary); //prints to the editor console. 
//Uncomment one or more of the following:
//newCustomField = customfield_12345; //migrate value from a CF to another using 'newCustomField' alias.
//description += "[CHANGED]; //add a sufffix to description
//#{Story Points} = 5; //addressing a CF by name
```

**Subtasks** - An example for accessing and iterating through the subtasks for an issue. This is useful for keeping data and statuses in sync between subtasks and the parent issue.

Snippet code

```java
for(string s in subtasks(key)) { //iterate over subtasks of current issue
    //if the subtask isn't closed
    if(%s%.status != "Closed") {
        //do something to the subtask
        runnerLog("Subtask is:" + s);
    }
}
```

**Linked issues** - An example for accessing and iterating through the linked issues for an issue. This is useful for keeping data and statuses in sync between linked issues and the main issue.

Snippet code

```java
for(string l in linkedIssues(key)) { //iterate over linked issues of the current issue
    //do something with those issues
    runnerLog("Linked issue:" + l); //print it to the editor console
}
```

**Attachments** - An example for accessing and iterating through the attachments for an issue. This could be useful in condition or validator scripts that check to see if an attachment has been added to the issue.

Snippet code

```java
for(string a in attachments) { //iterate over the attachments of the current issue
    //do something to the attachments:
    runnerLog("Attachment :" + a);
}
```

**Add a comment** - Example code for adding a comment to an issue. This can be useful for informing users of changes or updates that were performed by script automation so they are aware of the changes.

Snippet code

```java
addComment(key, currentUser(), 
            "Comment from SIL logged for the current user (" + currentUser() + 
            ") against the current issue: " + key);
```

## Listeners

Listener scripts are very similar to workflow scripts with the difference being on how they are triggered. Listeners can be triggered for many other events then the workflow is capable of triggering, such as when a field is updated on an issue. For more information about configuring listeners see the [SIL Listeners](/cms_trial/space/PSJC/490997990/SIL+Listeners/) documentation page.

**React to a field change only** - This listener snippet contains code that will only be executed if a specific field was updated as part of the change event.

Snippet code

```java
if(isIssueFieldChanged("description")) { //check if the field of interest was changed
    JFieldChange change = getEventIssueFieldChange("description"); //get the change
    logPrint("INFO", "Old value >>" + change.oldVal + "<< New value >>" + change.newVal + "<<"); //do something
}
```

**React to multiple field changes** - This listener snippet contains code that will be executed if any change is detected on the issue. The code can be further refined to respond to specific change types as needed.

Snippet code

```java
JFieldChange [] changes = getEventIssueChanges();
for(JFieldChange change in changes) {
    //see if the changes are of interest and do something with them:
    logPrint("INFO", "Field " + change.field + "; old value >>" + change.oldVal + "<< New value >>" + change.newVal + "<<");
}
```

## Workflows

Workflow snippets contain examples of scripts that would be triggered from a workflow. This includes condition scripts, validator scripts, and postfunction scripts. For more information about adding automation to workflows see the [Workflow Automation](/cms_trial/space/PSJC/490999005/Workflow+Automation/) documentation page.

**Simple postfunction** - This snippet gives example code for a simple postfunction. One of the most popular places for adding scripted automation postfunction scripts are good for setting custom field values automatically. For more information about accessing data for regular Jira fields or custom fields see the [Variable Resolution](/cms_trial/space/PSJC/434602568/Variable+types+and+reference+methods/) documentation page.

Snippet code

```java
//You can do any change to the issue in postfunctions. key and project are implied
//assign the issue to the current user
assignee = currentUser();
//set the due date to be 2 weeks from today
dueDate = currentDate() + "2w";
//add user as an approver using the approver custom field
customfield_12345 = projectPM(project);
logPrint("INFO", "Postfunction for issue " + key + " was executed"); //prints a message in the log
```

**Postfunction to increase priority -** This snippet gives example code for setting the priority as part of a postfunction.

Snippet code

```text
//increase priority for the current issue
if(priority == "Lowest" || priority == "Low") {
    priority = "High";
} else if(priority == "Normal") {
    priority = "Highest";
}
logPrint("INFO", "Priority for " + key + " is now :" + priority); //prints a message in the log
```