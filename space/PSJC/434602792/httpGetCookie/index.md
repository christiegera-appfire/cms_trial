# httpGetCookie

## Description

Retrieves the value of the specified cookie (if existing) from the latest HTTP response.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | httpGetCookie(cookieName) | **Package** | http |
| **Alias** |  | **Pkg Usage** | getCookie(cookieName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| cookieName | String | Yes | The name of the cookie. |

## Return Type

**String**

## Example

```javascript
string cookieVal = httpGetCookie("sessionToken");
```

## See also