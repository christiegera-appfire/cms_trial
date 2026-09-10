# How to associate and unlink Jira items using Apex code with the Salesforce Developer Console

## Before you start

Before running the code, verify the following:

- Confirm manual push/pull operations work without errors
- Verify manual associations work without errors
- Test your field mapping

This Apex code has no built-in error handling. If the manual push, pull, or creation doesn't work and you get an error, the APEX will not generate an error message while executing.

Always test the mappings first!

## Instructions

Run the following code in the Salesforce Developer Console > Execute anonymous windows. Please change the Jira key and Case ID, respectively. This is to check if the API is working correctly or not.

### Associate Jira item with Salesforce Case example

```text
String jiraKey = 'KP-1859'; // Replace with your JIRA key
String CaseId = '5000K00002YbWWwQAN'; // Replace with your Case ID

List<Case> cases = [SELECT Id from Case where Id =:CaseId];
System.debug(cases);
JCFS.API.associateJiraIssue(jiraKey, cases);
```

#### Associate API

`JCFS.API.associateJiraIssue(jiraKey, cases);`

#### Unlink Jira item from Salesforce Case example

```text
String jiraKey = 'CSF-414'; // Replace with your JIRA key
String CaseId = '5005e00000J9rubAAB'; // Replace with your Case ID

List<Case> cases = [SELECT Id from Case where Id =:CaseId];
System.debug(cases);
JCFS.API.unlinkJiraIssue(jiraKey, cases);
```

#### Unlink API

`JCFS.API.unlinkJiraIssue(jiraKey, cases);`

### Associate with default post-action

The association with this code will follow the auto push/pull configuration.

```text
JCFS.API.associateJiraIssue(jiraKey, sObjects, Boolean defaultPostActions)

// Example: JCFS.API.associateJiraIssue('JIRA-01', cases, true);
```

Custom Apex development falls outside our support scope.

Please note that while we can offer assistance, creating or troubleshooting custom Apex triggers is outside the scope of our support. We will provide guidance to the best of our ability.