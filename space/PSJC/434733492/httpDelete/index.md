# httpDelete

## Description

Executes an HTTP DELETE for a given URL using the specified HttpRequest object. The needed parameters can either be included in the initial url or they can be created using the httpCreateParameter function and added to the HttpRequest parameter.Requests can also be sent through a proxy.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | httpDelete(url, request [, proxy]) | **Package** | http |
| **Alias** |  | **Pkg Usage** | delete(url, request [, proxy]) |

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

The following example calls an HTTP DELETE using the JIRA REST API that results in deleting the user with the "guest1" username from the "jira-guests" group.

```javascript
string baseUrl = ();
string requestUrl = baseUrl + "/rest/api/2/group/user";
HttpRequest request;
HttpHeader authHeader = httpBasicAuthHeader("admin", "admin");
request.headers += authHeader;
request.parameters += httpCreateParameter("groupname", "jira-guests");
request.parameters += httpCreateParameter("username", "guest1");
httpDelete(requestUrl, request);
```

The request parameter should have the HttpRequest type described [here](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/). The HttpProxy type is described [here](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/).

## See also