# toLower

## Description

Returns the string only with **lower case letters**. If the string contains other characters than letters the chars that are not letters will not be converted.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | toLower(string) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| string | String | Yes | Specifies a character expression that will be converted to lower case. |

## Return Type

**String**

## Examples

### Example 1

```javascript
wret = toLower("FOoBaR");
print(wret);
```

Prints **"foobar"**

### Example 2

```javascript
wret = toLower("ABC2345f.ff");
print(wret);
```

Prints **"abc2345f.ff"**

## See also