# toUpper

## Description

Returns the given string that has it's letters converted to **upper case**. If the string contains other characters than letters the chars that are not letters will not be converted.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | toUpper(string) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| string | String | Yes | Specifies a character expression that will be converted to **upper case**. If the string contains other characters than letters the chars that are not letters will not be converted. |

## Return Type

**String**

## Examples

### Example 1

```javascript
wret = toUpper("fOoBaR");
print(wret);
```

Prints **"FOOBAR"**

### Example 2

```javascript
wret = toUpper("AbC2w&345f.ff");
print(wret);
```

Prints **"ABC2W&345F.FF"**

## See also