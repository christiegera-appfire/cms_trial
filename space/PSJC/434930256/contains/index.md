# contains

## Description

Returns **true** if character expression **str2** is in character expression **str1**.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | contains(str1, str2) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| str1 | String | Yes | Specifies a character expression to search for str2. |
| str2 | String | Yes | Specifies a character expression to search for in str1. |

## Return Type

**Boolean (true/false)**

## Examples

### Example 1

```javascript
wret = contains("This will return ?", "will");
print("Return " + wret);
```

Print **Return true**

### Example 2

```javascript
wret = contains("This will return ?", "Will");
print("Return " + wret);
```

Print **Return false**

### Example 3

```javascript
wret = contains("This will return ?", "This");
print("Return " + wret);
```

Print **Return true**

If you need to find **str2** multiple times, use **substring( )** function.

## See also