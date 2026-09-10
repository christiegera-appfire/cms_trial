# groupExists

## Description

Verifies if the selected group is a registered Jira group.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | groupExists(grp) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| group name | String | Yes | Name of the group that will be verified. |

## Return Type

**Boolean**

Returns "true" if the specified group name denotes a registered Jira group or "false" if the group name is unknown.

## Example

```javascript
groupExists("Administrators");
```

Result: "True" if **Administrators** is a registered Jira group. "False" if **Administrators** is not a registered Jira group.

## See also