# subscribeNotifications

## Description

Subscribe an user to request notification for a specific customer request.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | subscribeNotifications(requestId\_or\_Key, userAccountId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| requestId\_or\_Key | string | Yes | The key or the id of the customer request |
| userAccountId | string | Yes | The account id of the user that will be subscribed. |

## Return Type

**boolean**

Returns 'true' if it does not end in error.

## Example

```javascript
subscribeNotifications("SM-92", "user_account_id");
```

## See also