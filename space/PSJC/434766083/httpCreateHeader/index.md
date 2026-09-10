# httpCreateHeader

## Description

Creates an HttpHeader object.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | httpCreateHeader(key, value) | **Package** | http |
| **Alias** |  | **Pkg Usage** | createHeader(key, value) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| key | String | Yes | The key for the http header. |
| value | String | Yes | The value for the http header. |

## Return Type

[**HttpHeader**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
HttpRequest request;
HttpHeader header = httpCreateHeader("Content-Type", "application/json");
request.headers += header;
```

## See also