# httpPatch

## Description

Executes an HTTP PATCH for the given URL using the specified HttpRequest object. The data used for the PATCH can be either included in the request object (as name-value parameters) or it can be added as a separate parameter (in the case of JSON, struct and so on). Requests can also be sent through a proxy.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | httpPatch(url, request [[, proxy] [, patchDataObject]]) | **Package** | http |
| **Alias** |  | **Pkg Usage** | patch(url, request [[, proxy] [, patchDataObject]]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| url | String | Yes | The URL |
| request | HttpRequest | Yes | An HttpRequest object containing headers, cookies, parameters |
| proxy | HttpProxy | No | An HttpProxy object containing the host and port of the proxy server. |
| patchDataObject | variable: string, array or struct | No | Data to be used for the PATCH method |

## Return Type

**String**

Variable return type depends on the left hand side operator type.

The request parameter should have the HttpRequest type described [here](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/). The HttpProxy type is described [here](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/).

## See also