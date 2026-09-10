# getSubscriptionStatus

## Description

Returns the notification subscription status for the provided user.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getSubscriptionStatus(requestId\_or\_Key, userAccountId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| requestId\_or\_Key | String | Yes | The ID or Key of the customer request from which the subscription status will be retrieved |
| userAccountId | Integer | Yes | The account ID of the user to be checked |

## Return Type

**Boolean**

## Example

```javascript
return getSubscriptionStatus("SM-1", currentUserKey());
```

Returns true if the user is subscribed to that request or false otherwise.

## See also