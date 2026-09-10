# decrypt

[Unmapped macro: button-handy — no content to fall back on]

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | decrypt(textToDecrypt, cipherKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Description

Decrypts text with AES Decryption using a 16, 32, 64, or 128 bit cipher. This is useful when retrieving password stored in  [Persistent variables](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=%20Persistent%20variables&linkCreation=true&fromPageId=434440032).

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| textToDecrypt | String | Yes | Text to decrypt |
| cipherKey | String | Yes | Secret cipher key text used for encryption and decryption. Must be 16, 32, 64, or 128 characters in length. |

## Return Type

**String**

## Example

```javascript
return decrypt(""&#184;&#248;b!v&#8222;&#246;&#201;&#217;&#39;&#228;W1&#8225;", "secretKeyPhrase7");
```

Returns "adminPassword"

## See also