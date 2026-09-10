# httpBasicAuthHeader

## Description

Creates an HttpHeader object to be used as Authorization header for a Basic authentication of a user.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | httpBasicAuthHeader(username, password) | **Package** | http |
| **Alias** |  | **Pkg Usage** | basicAuth(username, password) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| username | String | Yes | The username. |
| password | String | Yes | The password. |

## Return Type

[**HttpHeader**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
HttpHeader authHeader = httpBasicAuthHeader("admin", "admin");
```

## See also