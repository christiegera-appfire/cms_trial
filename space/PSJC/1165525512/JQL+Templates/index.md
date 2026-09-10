# JQL Templates

User template scripts are scripts that directly related to specific users in Jira. These are scripts that may set field values with specific users or control behaviors based on the specific user session using Jira.

The templates will create the user script by adding the script to the configuration that corresponds to the individual script.

**NOTE:** Because the user scripts are a collection of other script types there isn’t a standard way to configure and test the template scripts. See each template definition for details regarding configuration and testing.

## Templates

## Assign issue

Assign an issue to a selected user after the issue is transitioned.

Script Type: **Workflow Action**  
For more information about configuring and testing action templates [click here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=DRAFT_Post-Function%20Templates&linkCreation=true&fromPageId=1165525512).

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

## User is

User is a defined user. If not, the option to transition the issue will not be shown to the user.

Script Type: **Condition**  
For more information about configuring and testing condition templates [click here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=DRAFT_Conditions%20Templates&linkCreation=true&fromPageId=1165525512).

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| Select user | YES | The specified user who is allowed to complete the transition. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
return currentUser() == "jmuse";
```