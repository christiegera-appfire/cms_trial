# urlDecode

## Description

Decodes text from URL format. This is useful when parsing a URL address used by a REST command.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | urlDecode(textToDecode) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| textToDecode | String | Yes | Text to decode from URL format. |

## Return Type

**String**

Returns the input text decodeed from the URL format

## Example

```javascript
string url = "https://marketplace.atlassian.com/search?query=power%20scripts";
string product = substring(url, indexOf(url, "=") +1, length(url));
return urlDecode(product);
```

Returns "power scripts"

## See also