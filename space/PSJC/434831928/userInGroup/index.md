# userInGroup

## Description

Verifies if the selected user is in the selected group(s).

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | userInGroup(group, user) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| group | string / string[] | Yes | Name(s) of the group(s) the user should belong to. |
| user | String | Yes | Name or key of the user that needs to be verified. It searches by the user key first and if there is no result by the user name as well. |

## Return Type

**Boolean**

A "true" return value means that the user associated with the specified username or userkey belongs to the given group(s).

## Examples

### Example 1

```javascript
userInGroup("Administrators", "Admin1");
```

Returns "true" if Admin1 is included in Administrators group and "false" if Admin1 is not included in Administrators group.

### Example 2

```javascript
userInGroup("Users", currentUser());
```

Returns: **True** if the current user is included in **"Users"** group or **False** if the current user is not included in **"Users"** group.

### Example 3

```javascript
string[] groups = {"Administrators", "Users"};
userInGroup(groups, currentUser());
```

Returns "true" if the current user is included in Users or Administrators group and "false" if the current user is not included neither in Users nor in Administrators group.

The look -up is first made after the userkey, then after the username.

## See also