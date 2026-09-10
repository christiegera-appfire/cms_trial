# httpCreateCookie

## Description

Creates an HttpCookie object.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | httpCreateCookie(name, value) | **Package** | http |
| **Alias** |  | **Pkg Usage** | createCookie(name, value) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | String | Yes | The name of the cookie. |
| value | String | Yes | The value of the cookie. |

## Return Type

[**HttpCookie**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
HttpRequest request;
HttpCookie cookie = httpCreateCookie("sessionId", "298zf09hf012fh2");
request.cookies += cookie;
```

## See also