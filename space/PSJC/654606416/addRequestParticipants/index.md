# addRequestParticipants

## Description

Adds one or multiple users as request participants to a customer request.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | addRequestParticipants(requestId\_or\_Key, usersIds) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| requestId\_or\_Key | String | Yes | The key or id of the customer request. |
| usersIds | String [] | Yes | The accountIds of the users to be added as request participants. |

## Return Type

**String[]**

Returns a string array containing the added accountIds.

## Example

```javascript
return addRequestParticipants("SM-23", {"one_user_account_id", "two_user_account_id"});
```

## See also