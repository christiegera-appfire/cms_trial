# createIssue

‌

## Description

Creates an issue based on the provided arguments.

| **Syntax** | createIssue(projectKey, parentIssueKey, issueType, summary[, priority, description, components, due date, security\_level, field\_mappings]) | **Package** |  |
| --- | --- | --- | --- |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | Yes | Key of the project, where the issue will be created, as it is saved in the Administration part. |
| parentIssueKey | String | Yes | Key of the parent issue. Though the parameter is required, it can take an empty value to specify that the issue is not a sub-task, but a regular issue. |
| issueType | String | Yes | Type of the issue that will be created. |
| summary or issueSummary | String | Yes | Summary of the issue that will be created. |
| priority | String | No | Priority. |
| description | String | No | Description of the issue that will be created. |
| components | array of strings | No | Components of the issue that will be created. |
| due date | date | No | Due date of the issue that will be created. |
| security level | String | No | Security level of the issue that will be created. |
| custom fields mappings/field mappings | JFieldValue[] | No | Mappings of the custom and system fields of the issue that will be created. |

## Return Type

**String**

The key of the created issue

## Example

```javascript
string issue_priority;//Possible values: "Major", "Critical" etc.
string issue_description;
string[] issue_components;
string issue_security_level;
issue_priority = "Critical";
issue_description = "Description of the issue";
issue_components = components; //an array containing all the components of the current project
issue_security_level = "Administrator";
JFieldValue[] custom_fields_mapping = {
    "STDUP", "fmanaila",
    "STDGP", {"jira-users", "jira-admin"}
};
string k = createIssue(
            "PROJECT",
            "PRJ-300",
            "Sub-task",
            "Summary of the sub task" ,
            issue_priority,
            issue_description,
            issue_components,
            currentDate() + "30d",
            issue_security_level,
            custom_fields_mapping
           );
print ("On the project " + project + ", issue " + k + "is created.");
```

Will create an Improvement with no components and the assignee set for user with the username "someUserName".