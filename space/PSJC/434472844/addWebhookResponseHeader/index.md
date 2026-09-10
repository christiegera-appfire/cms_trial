# addWebhookResponseHeader

## Description

Adds an HTTP header to the response that will be returned to the Webhook caller.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | addWebhookResponseHeader(httpHeader) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| httpHeader | HttpHeader | Yes | The header to be added to the response |

## Return Type

**None**

## Example

```javascript
....
// webhook logic
....
//setting a custom HTTP header to the webhook response:
HttpHeader header = httpCreateHeader("Content-Type", "application/javascript");
addWebhookResponseHeader(header);
//returning success
return true, 200;
```

## See also