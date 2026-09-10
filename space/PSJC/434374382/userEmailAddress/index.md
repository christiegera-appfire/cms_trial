# userEmailAddress

## Description

Returns the email address of the selected user. The email address may be needed to supply it to various external systems.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | userEmailAddress(user) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| user | String | Yes | User key or name of the user the email should be provided for. Searches by the user key first and if there is no result by the user name as well. |

## Return Type

**String**

Returns the e-mail address associated with the specified userkey/username.

## Examples

```javascript
userEmailAddress("Admin");
```

Returns: If exists, returns the email address of the user **Admin**.

```javascript
userEmailAddress(currentUser());
```

Returns: If exists, returns the email address of the current user.

The look-up is first made after the userkey, then after the username. If the email of the selected user doesn't exist the function returns an empty string.

## See also