# httpPut

## Description

Executes an HTTP PUT for the given URL using the specified HttpRequest object. The data used for the PUT can be either included in the request object (as name-value parameters) or it can be added as a separate parameter (in the case of JSON, struct etc).Requests can also be sent through a proxy.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | httpPut(url, request [, putDataObject]) | **Package** | http |
| **Alias** |  | **Pkg Usage** | put(url, request [, putDataObject]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| url | String | Yes | The URL. |
| request | HttpRequest | Yes | An HttpRequest object containing headers, cookies, parameters. |
| proxy | HttpProxy | No | An HttpProxy object containing the host and port of the proxy server. |
| putDataObject | variable: string, array or struct | No | Data to be used for the PUT method. |

## Return Type

**String**

Variable return type depends on the left hand side operator type.

## Example

The following example calls an HTTP PUT using the JIRA REST API that updates the assignee for the current ticket.

```javascript
string baseUrl = ();
string requestUrl = baseUrl + "/rest/api/2/issue/" + key;
HttpRequest request;
HttpHeader authHeader = httpBasicAuthHeader("admin", "admin");
request.headers += authHeader;
request.headers += httpCreateHeader("Content-Type", "application/json");
string updateInfo =  "{\"fields\": {\"assignee\":{\"name\":\"guest1\"}}}";
httpPut(requestUrl, request, updateInfo);
```

## See also