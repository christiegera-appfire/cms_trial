# Scripted Custom Field Templates

Custom fields template scripts are scripts that directly affect the value, appearance, configuration, or behavior of a custom field. With Power Scripts, there isn’t a concept of a custom field specific script/trigger, instead the scripts in this category are actually types like, workflow actions, listeners, and Live Fields scripts. These different script types accomplish the goal of updating and controlling the custom field types that are natively found in Jira. However, if you have advanced and complex problems that can’t be solved using standard Jira fields, [Power Custom Fields](https://marketplace.atlassian.com/apps/1210749/power-custom-fields-for-jira?hosting=datacenter&tab=overview) introduces new custom field types that are directly controlled by SIL scripts.

The templates will create the custom field script by adding the script to the configuration that corresponds to the individual script.

**NOTE:** Because the custom field scripts are a collection of other script types there isn’t a standard way to configure and test the template scripts. See each template definition for details regarding configuration and testing.

## Templates

## Copy Field from Parent

A SIL action that will copy a custom field from parent.

Script type: **Action**  
For more information about configuring and testing action templates [click here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=DRAFT_Post-Function%20Templates&linkCreation=true&fromPageId=1165525454).

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

## Set Field Value

Set a field to a value.

Script Type: **Action**  
For more information about configuring and testing action templates [click here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=DRAFT_Post-Function%20Templates&linkCreation=true&fromPageId=1165525454).

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

---

## Disable Field

Disable a field in the UI when the issue page loads.

Script Type: **Live Fields**  
For more information about configuring and testing Life Fields templates [click here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=DRAFT_Live%20Field%20Templates&linkCreation=true&fromPageId=1165525454).

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| Custom Field | YES | The custom field that should be disabled for the user. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
lfDisable("customfield_10204");
```

**NOTE:** The custom field id (customfield\_10204) is an example, the id of custom fields will be unique for every Jira instance. To check the id for a custom field see more information about the [Custom Field Usage tool](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15487329) included in Power Scripts.

---

## Hide Field

Hide a field from the UI when the issue page loads.

Script Type: **Live Fields**  
For more information about configuring and testing Life Fields templates [click here](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=DRAFT_Live%20Field%20Templates&linkCreation=true&fromPageId=1165525454).

### Inputs

| **Name** | **Required** | **Description** |
| --- | --- | --- |
| Custom Field | YES | The custom field that should be hidden from the user. |
| Description | NO | The description text will be added to a comment at the head of the script so other users can be informed of the purpose of the script. |

### Script

```text
lfHide("customfield_10204");
```

**NOTE:** The custom field id (customfield\_10204) is an example, the id of custom fields will be unique for every Jira instance. To check the id for a custom field see more information about the [Custom Field Usage tool](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15487329) included in Power Scripts.