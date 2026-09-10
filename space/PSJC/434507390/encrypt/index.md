# encrypt

## Description

Encrypts text with AES encryption using a 16, 32, 64, or 128 bit cipher. This is useful when using [Persistent variables](/cms_trial/space/PSJC/496205909/Persistent+variables/) to store passwords. Returns the encrypted input text.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | encrypt(textToEncrypt, cipherKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| textToEncrypt | String | Yes | Text to encrypt |
| cipherKey | String | Yes | Secret cipher key text used for encryption and decryption. Must be 16, 32, 64, or 128 characters in length. |

## Return Type

**String**

Returns the encrypted input text

## Example

```javascript
return encrypt("adminPassword", "secretKeyPhrase7");
```

## See also