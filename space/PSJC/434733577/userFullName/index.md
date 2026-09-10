# userFullName

## Description

Returns the full name (firstname, lastname) of the user.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | userFullName(user) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| user | String | Yes | Username or userkey of selected user. It searches by the user key first and if there is no result by the user name as well. |

## Return Type

**String**

Returns the **full name** (first name and last name) of the user associated with the specified username or userkey.

## Examples

### Example 1

```javascript
userFullName("Admin");
```

Returns the full name (first name and last name) of the user **Admin**.

### Example 2

```javascript
userFullName(currentUser());
```

Returns the full name (first name and last name) of the current user.

The look-up is first made after the userkey, then after the username.

## See also