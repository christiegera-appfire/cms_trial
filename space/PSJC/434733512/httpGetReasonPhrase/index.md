# httpGetReasonPhrase

## Description

Retrieves the HTTP reason phrase of the latest HTTP response. For instance, "OK", "Not Found", "Unsupported Media Type", and so on.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | httpGetReasonPhrase() | **Package** | http |
| **Alias** |  | **Pkg Usage** | reeasonPhrase() |

## Return Type

**String**

The reason phrase extracted from the latest HTTP response.

## Example

```javascript
string reasonPh = httpGetReasonPhrase();
print("Last response: " + reasonPh);
```

## See also