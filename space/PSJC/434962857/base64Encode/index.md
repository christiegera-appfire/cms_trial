# base64Encode

[Unmapped macro: button-handy — no content to fall back on]

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | base64Encode(textToEncode) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Description

Encodes text in Base64. This is useful when transferring data like attaching a signature to the bottom of an email or storing images in a database. Returns the input text base64 encoded.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| textToEncode | String | Yes | Text to encode in Base64. |

## Return Type

**String**

## Example

```javascript
return base64Encode("Encode this text!");
```

Returns "RW5jb2RlIHRoaXMgdGV4dCE="

## See also