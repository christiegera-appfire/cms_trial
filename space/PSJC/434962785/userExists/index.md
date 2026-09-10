# userExists

## Description

Verifies if the selected user is registered Jira user.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | userExists(user) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| user | String | Yes | Username or userkey of the verified user. Search is done by the user key only. |

## Return Type

**Boolean**

A "true" return value means that there is a registered Jira user associated with the specified username or userkey.

## Example

```javascript
userExists("Administrator");
```

Returns "true" if **Administrator** is the username of a registered Jira user and "false" otherwise.

The look-up is first made after the userkey, then after the username.

## See also