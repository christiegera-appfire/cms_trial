# endsWith

## Description

Returns **true** if **str1** ends with **str2**.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | endsWith(str1, str2) | **Package** |  |
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
wret = endsWith("This will return ?", "will");
print("Return " + wret);
```

Print **false**

### Example 2

```javascript
wret = endsWith("This will return ?", "n ?");
print("Return " + wret);
```

Print **true**

### Example 3

```javascript
wret = endsWith("This will return ?", "N ?");
print("Return " + wret);
```

Print **false**

## See also