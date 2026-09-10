# httpOptions

## Description

Executes an HTTP OPTIONS for the given URL using the specified HttpRequest object. Returns the message body of the response converted to the requested left operand type (if any).Requests can also be sent through a proxy.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | httpOptions(url, request [, proxy]) | **Package** | http |
| **Alias** |  | **Pkg Usage** | options(url, request [, proxy]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| url | String | Yes | The URL. |
| request | HttpRequest | Yes | An HttpRequest object containing headers, cookies, parameters. |
| proxy | HttpProxy | No | An HttpProxy object containing the host and port of the proxy server. |

## Return Type

**String**

Variable return type depends on the left hand side operator type.

## Example

```javascript
HttpRequest request;
request.headers += httpCreateHeader("Host", "appfire.com");
string url = "http://example.org";
httpOptions(url, request);
number statusCode = httpGetStatusCode();
if (statusCode>= 200 && statusCode < 300) {
	return httpGetHeader("Allow");
}
```

The request parameter should have the HttpRequest type described [here](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/). The HttpProxy type is described [here](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/).

## See also