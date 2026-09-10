# removeRequestParticipants

## Description

Removes one or multiple users from request participants, from a specified customer request.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | removeRequestParticipants(requestId\_or\_Key, usersIds) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| requestId\_or\_Key | String | Yes | The key or id of the customer request. |
| usersIds | String [] | Yes | The accountIds of the users to be removed from request participants. |

## Return Type

**Boolean**

Returns "true" if the operation didn't end in error.

## Example

```javascript
return removeRequestParticipants("SM-23", {"one_user_account_id", "two_user_account_id"})
```

## See also