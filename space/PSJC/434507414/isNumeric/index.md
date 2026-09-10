# isNumeric

## Description

Returns "true" if the provided argument **str**is actually a number.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | isNumeric(str) | **Package** |  |
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
wret = isNumeric("2345");
print(wret);
```

Print **true**

### Example 2

```javascript
wret = isNumeric("-2345.678");
print(wret);
```

Print **true**

### Example 3

```javascript
wret = isNumeric("2345.678abcd");
print(wret);
```

Print **false**

## See also