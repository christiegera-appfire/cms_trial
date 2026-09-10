# getWebhookPayload

## Description

Gets the Webhook payload from the calling client.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getWebhookPayload() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

[**WebhookPayload**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Examples

### Example 1 - Getting the Webhooks payload from the calling client

```javascript
//getting the REST/HTTP call input parameters:
WebhookPayload httpRequestPayload = getWebhookPayload();
//getting the used HTTP method:
string httpMethod = httpRequestPayload.httpMethod;//This can be something like "GET", "POST", "PUT", etc.
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

## See also