# httpGet

## Description

Executes an HTTP GET for the given URL using the specified HttpRequest object. The needed parameters can either be included in the initial url or they can be created using the httpCreateParameter function and added to the HttpRequest parameter.Requests can also be sent through a proxy.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | httpGet(url, request [, proxy]) | **Package** | http |
| **Alias** |  | **Pkg Usage** | get(url, request [, proxy]) |

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

You can check whether something exists in the external system. For instance, you can check whether a certain user exists in Salesforce and get the user parameters if such exist.

```javascript
struct serverInfo{
	string baseUrl;
	string version;
	number [] versionNumbers;
	string deploymentType;
	number buildNumber;
	string buildDate;
	string serverTime;
	string serverTitle;
}
//Create request
HttpRequest request;
HttpHeader authHeader = httpBasicAuthHeader("admin", "admin");
request.headers += authHeader;
//Post data and get response
serverInfo si = httpGet("http://localhost:8080/rest/api/2/serverInfo?doHealthCheck=false", request);
return si.baseUrl;
```

The request parameter should have the HttpRequest type described [here](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/). The HttpProxy type is described [here](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/).

## See also