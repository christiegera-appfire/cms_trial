# lastIndexOf

## Description

Returns the index within a string of the last occurrence of the specified substring. Returns the index of the last match of the str2 in str1 or -1 if str2 is nowhere to be found in str1.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | lastIndexOf(str1, str2) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| str1 | String | Yes | Specifies a character expression to search for str2. |
| str2 | String | Yes | Specifies a character expression to search for in str1. |

## Return Type

**Number**

## Examples

### Example 1

```javascript
wret = lastIndexOf("f1/f2/f3", "/f");
print("Return " + wret);
```

Print **Return 5**

### Example 2

```javascript
wret = lastIndexOf("f1/f2/f3", "/fi");
print("Return " + wret);
```

Print **Return -1**

### Example 3

```javascript
wret = lastIndexOf("f1/f2", "");
print("Return " + wret);
```

Print **Return 5**

The last occurrence of the empty string "" is considered to occur at the index value `str1.length().`  
If you need to find **str2** multiple times use [substring()](/cms_trial/space/PSJC/434440070/substring/) function.

## See also