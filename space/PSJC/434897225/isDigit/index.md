# isDigit

## Description

Returns "true" if the provided argument **str** is a string containing only digits.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | isDigit(str) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| str | String | Yes | Specifies a character expression. |

## Return Type

**Boolean (true/false)**

## Examples

### Example 1

```javascript
wret = isDigit("2345");
print(wret);
```

Print **true**

### Example 2

```javascript
wret = isDigit("aaa2345f.ff");
print (wret );
```

Print **false**

### Example 3

```javascript
wret = isDigit("2.34");
print(wret);
```

Print **false**

## See also