# appendToWebhookResponse

## Description

Adds an object to the response that will be returned to the Webhook caller, as the HTTP body.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | appendToWebhookResponse(responsePart) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| responsePart | String | Yes | The object to be added to the response |

## Return Type

**None**

## Example

```javascript
//getting the REST/HTTP call input parameters:
WebhookPayload httpRequestPayload = getWebhookPayload();
//getting the used HTTP method:
string httpMethod = httpRequestPayload.httpMethod;//This can be something like "GET", "POST", "PUT" etc.
//getting the http request payload (body):
string httpPayload = httpRequestPayload.payload;
//getting the http query parameters:
WebhookParam[] httpQueryParams = httpRequestPayload.queryParams;
string firstQueryParamName = httpQueryParams[0].name;
string firstQueryParamValue = httpQueryParams[0].values[0];
//sending the response back to the caller:
appendToWebhookResponse("http method:");
appendToWebhookResponse(httpMethod);
appendToWebhookResponse("payload:");
appendToWebhookResponse(httpPayload);
appendToWebhookResponse("firstQueryParamName:");
appendToWebhookResponse(firstQueryParamName);
appendToWebhookResponse("firstQueryParamValue:");
appendToWebhookResponse(firstQueryParamValue);
//returning a custom HTTP status code:
return true, 1234;
```

If the **responsePart** parameter has another type but string, a conversion to string will be attempted.

## See also