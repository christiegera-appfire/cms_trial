# urlEncode

## Description

Encodes text in URL format. This is useful when constructing a URL address used by a REST command.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | urlEncode(textToEncode) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| textToEncode | String | Yes | Text to encode in URL format. |

## Return Type

**String**

Returns the input text URL format

## Example

```javascript
string addon = "power scripts";
string url = "https://marketplace.atlassian.com/search?query=";
string urlText = urlEncode(url + addon);
return urlText;
```

Returns <https://marketplace.atlassian.com/search?query=power%20scripts>

## See also