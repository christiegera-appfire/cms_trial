# httpGetHeader

## Description

Retrieves the value of the specified header (if existing) from the latest HTTP response.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | httpGetHeader(headerName) | **Package** | http |
| **Alias** |  | **Pkg Usage** | getHeader(headerName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| headerName | String | Yes | The name of the reponse header. |

## Return Type

**String**

The value of the response header.

## Example

```javascript
string hdrValue = httpGetHeader("Content-Type");
```

## See also