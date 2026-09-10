# indexOf

## Description

Returns the index of the first match of the str2 in str1 or -1 if str2 is nowhere to be found in str1. Returns an integer indicating the position of the first character for a character expression within another character expression, beginning from the leftmost character.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | indexOf(str1, str2) | **Package** |  |
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
wret = indexOf("This will return ?", "will");
print("Return " + wret);
```

Print **Return 5**

### Example 2

```javascript
wret = indexOf("This will return ?", "Will");
print("Return " + wret);
```

Print **Return -1**

### Example 3

```javascript
wret = indexOf("This will return ?", "This");
print("Return " + wret);
```

Print **Return 0**

If the first occurrence of **str2** is the first caracter of **str1**, indexOf( ) returns **0**.  
If you need to find **str2** multiple times, use **substring**( ) function.

## See also