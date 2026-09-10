# httpCreateParameter

## Description

Creates an HttpQueryParam object.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | httpCreateParameter(name, value) | **Package** | http |
| **Alias** |  | **Pkg Usage** | createParam(name, value) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | String | Yes | The name of the query parameter. |
| value | String | Yes | The value of the query parameter. |

## Return Type

[**HttpQueryParam**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
HttpRequest request;
HttpQueryParam param = httpCreateParameter("name", "John");
request.parameters += param;
```

## See also