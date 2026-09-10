# isAlphaNumeric

## Description

Returns "true" if the provided argument **str** is a string containing only letters and digits.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | isAlphaNumeric(str) | **Package** |  |
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
wret = isAlphaNumeric("foobar");
print(wret);
```

Print **true**

### Example 2

```javascript
wret = isAlphaNumeric("aaa2345G");
print(wret);
```

Print **false**

### Example 3

```javascript
wret = isAlphaNumeric("23asd.*;45");
print(wret);
```

Print **false**

isAlphaNumeric returns "false" if the character string **str** contains blanks or special characters or is a null string.

## See also