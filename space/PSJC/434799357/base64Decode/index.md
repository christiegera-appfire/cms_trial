# base64Decode

[Unmapped macro: button-handy — no content to fall back on]

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | base64Decode(textToDecode) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Description

Decodes from Base64. This is useful when transferring data like retrieving images stored in a database.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| textToDecode | String | Yes | Text to decode from Base64. |

## Return Type

**String**

Returns the input text decoded from base64

## Example

```javascript
return base64Decode("RW5jb2RlIHRoaXMgdGV4dCE=");
```

Returns "Encode this text!"

## See also