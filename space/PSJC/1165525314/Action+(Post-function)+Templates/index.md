# Action (Post-function) Templates

Actions are actions that occur after an issue is transitioned. Actions represent one of the largest categories of use cases for automation.

The templates will create the action by adding a new action script to an existing workflow transition within Jira.

## Setting up the Post-Function Templates

Because the action script needs to live in an existing workflow transition the first two steps to creating a action script template will be selecting the workflow and transition for where the action should be place.

![Power Scripts for Jira Cloud action postfunction template configuration interface](/cms_trial/assets/b713516e-7cf3-4903-861d-fdfda92772ed.png)

If you are unsure which workflow to use an easy way to check is through the “view workflow” link that will present on any issue in Jira. Make sure you use an issue for the project and issue type you wish to add the action to.

![Power Scripts for Jira Cloud postfunction template selection dialog](/cms_trial/assets/afa5171a-677c-4fcd-9311-fac48fc33f02.png)

This “view workflow” link may not always be present due to permission settings. You may need to look in the project settings in order to determine which workflow you should select.

**NOTE:** Because the action script occurs at the end of the transition, transition screens are not relevant to the action script.

## Testing the Script

Testing the script is as simple as completing the transition and checking if the action action occurred. For example, if the script was designed to create subtasks after the transition, check to see if the subtasks were created. If not, see this section about troubleshooting scripts.

## Templates

## Assign issue

Assign an issue to a selected user after the issue is transitioned.

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| User | YES | The specific user for which the issue will be assigned. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
assignee = "jmuse";
```

---

## Add Comment

Add a comment to the current issue after the issue has been transitioned to a certain status.

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| User | NO | If a default user is specified, this user will be recorded as the user who created the comment. If no user is specified then the user who transitioned the issue will be recorded as the user who created the comment. |
| Comment | YES | The text that should be added to the issue as a comment. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
string selectedUser = "";
string comment = "Hello World";

if(selectedUser == ""){
 	addComment(key, currentUser(), comment);
}else{
	addComment(key, selectedUser, comment);
}
```

---

## Add Watcher

A SIL action that will add a watcher on the current issue after the issue is transitioned.

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| User | YES | The specific user who should be added as a watcher for the issue. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
watchers = watchers + "jmuse";
```

---

## Send an Email

A SIL action that will send a custom email to the desired address, project role, or user group after the issue is transitioned.

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| From | NO | The address that the email should be sent from. |
| To | YES | The recipients email address. |
| CC | NO | List of CC email addresses. |
| Subject | YES | The subject of the email. |
| Body | YES | The text body of the email. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
string from = "jira@company.com";
string [] to = "users@company.com";
string [] cc = "propertymanagement@building.com";
string subject = "Building is on fire";
string body = "Please help, my hot yoga class is getting too hot!";

sendEmail(from, to, cc, subject, body);
```

**NOTE:** In order for this action to successfully send an email Power Scripts must first be [configured for sending emails](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15488160). The default setting will not send out any emails.

**NOTE:** If using the “From” field the mail account specified in the [email configuration](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15488160) must be set up to be allowed to send from multiple addresses. An example of this is when an assistant can send an email as their boss from their own email account. Otherwise, the email account specified in the email configuration will be who the email is sent from.

**NOTE:** HTML tags can be used within the body of the email.

---

## Clone Issue

A SIL action that will clone a Jira issue after the issue is transitioned.

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| Link Type | NO | If specified, this link type will be used to link the original issue to its clone. |
| Parent Key | NO | If specified, the cloned issue will be added as a subtask to the parent issue. The original issue must be of subtask type in order for this to occur. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
cloneIssue(key, "Cloners", "TP-1");
```

**NOTE:** The name of a link type is not the same as its inward and outward description. For example, the link type of “Cloners” has an inward description of “is cloned by” and an outward description of “clones”. Understand that the values you see when linking issues are the descriptions and not the name of the link type. To view a list of link types in your system see the Issue Linking page in the Jira admin.

---

## Copy Field from Parent

A SIL action that will copy a custom field from parent after the issue is transitioned.

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| Custom field | YES | The specific custom field that should be copied from the parent. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
if(!isNull(parent)) {
    customfield_10807 = parent.customfield_10807;
 }
```

**NOTE:** The custom field must be in context for both the parent issue and the child in order for this copy to succeed.

**NOTE:** The custom field id (customfield\_10807) is an example, the id of custom fields will be unique for every Jira instance. To check the id for a custom field see more information about the [Custom Field Usage tool](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15487329) included in Power Scripts.

---

## Copy Field to Subtasks

A SIL action that will copy a custom field's value from a task to it subtasks after the issue is transitioned.

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| Custom field | YES | The specific custom field that should be copied to the child subtasks. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
string[] subtasks = subtasks(key);
for(string subtask in subtasks) {
    %subtask%.customfield_10807 = key.customfield_10807
}
```

**NOTE:** Please be aware that this script will copy the parent value to all subtasks for the parent issue.

**NOTE:** The custom field id (customfield\_10807) is an example, the id of custom fields will be unique for every Jira instance. To check the id for a custom field see more information about the [Custom Field Usage tool](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15487329) included in Power Scripts.

---

## Create Subtask

A SIL action that will create a subtask after the issue is transitioned.

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| Summary | YES | Summary of the subtask being created. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
createIssue(project, key, "Sub-task", "This is the summary");
```

---

## Link Issue

A SIL action that will link another issue to the current one after the issue is transitioned.

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| Issue Key | YES | Issue key for which the issue should be linked to. |
| Link Type | YES | Link type that should be used when linking the issues. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
linkIssue(key, "TP-1", "Blocks");
```

**NOTE:** The name of a link type is not the same as its inward and outward description. For example, the link type of “Cloners” has an inward description of “is cloned by” and an outward description of “clones”. Understand that the values you see when linking issues are the descriptions and not the name of the link type. To view a list of link types in your system see the Issue Linking page in the Jira admin.

---

## Set Field Value

Set a field to a value after the issue is transitioned.

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| Custom Field | YES | The custom field that should be set by the script. |
| Field Value | NO | The value that should be given to the custom field. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
customfield_10400 = "Some value";
```

**NOTE:** The custom field id (customfield\_10400) is an example, the id of custom fields will be unique for every Jira instance. To check the id for a custom field see more information about the [Custom Field Usage tool](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15487329) included in Power Scripts.

## Transition Parent

A SIL action that will transition the parent to a new status.

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| Transition status | YES | The new status for the parent issue to be transitioned to. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
string transitionName = "Done";
if(!isNull(parent)) {
   autotransition(transitionName, parent);
}
```

**NOTE:** The new status for the parent must already exist in the parent workflow and be available from the parent current status.