# httpGetStatusCode

## Description

Retrieves the HTTP status code of the latest HTTP response.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | httpGetStatusCode() | **Package** | http |
| **Alias** |  | **Pkg Usage** | statusCode() |

## Return Type

**Number**

The value of the status code

## Example

```javascript
number statusCode = httpGetStatusCode();
if (statusCode>= 200 && statusCode < 300) {
	print("Successful response!");
}
```

## See also