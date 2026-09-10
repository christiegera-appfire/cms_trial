# admRemoveGroup

## Description

Removes a group from Jira.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admRemoveGroup(groupToRemove, swapGroup) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | removeGroup(groupToRemove, swapGroup) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| Group to remove | String | Yes | The group to be removed. |
| Swap group | String | Yes | The swap group that identifies the group to change comment and worklog visibility to. |

## Return Type

**Boolean**

Returns "true" if operation succeeded.

## Example

```javascript
admRemoveGroup("Group1","Group2");
```

Result: "Group1" will be removed from Jira and "Group2" is used to change comment and worklog visibility to.

This method will remove the group from any notifications schemes, any associated permissions, and any associated project roles. This method will also update any comments and work-logs that have visibility restrictions set to the current group such that their restrictions will be changed to the swapGroup.

## See also