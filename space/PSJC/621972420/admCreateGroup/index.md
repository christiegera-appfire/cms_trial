# admCreateGroup

## Description

Create a single group to a project role if the group does not already exist.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admCreateGroup(groupName) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | createGroup(groupName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| Group name | String | Yes | The name that describes the group. |

## Return Type

**Boolean**

Returns "true" if operation succeeded.

## Example

```javascript
admCreateGroup("Test");
```

Result: A new group "Test" will be created.

## See also