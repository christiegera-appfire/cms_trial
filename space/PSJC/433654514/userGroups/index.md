# userGroups

## Description

Returns the groups the selected user belongs to.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | userGroups(user) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| user | String | Yes | Username or userkey of the selected user. The search is done by the user key only. |

## Return Type

**String []**

## Examples

### Example 1

```javascript
userGroups("username");
```

Result: The list of groups that the user with account username belongs to.

### Example 2

```javascript
userGroups(currentUser());
```

Result: The list of groups that the current user belongs to.

The look-up is first made after the userkey, then after the username.

## See also