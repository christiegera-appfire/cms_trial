# isLower

## Description

Returns "true" if the provided argument **str**is a string containing only lowercase letters.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | isLower(str) | **Package** |  |
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
wret = isLower("foobar");
print(wret);
```

Print **true**

### Example 2

```javascript
wret = isLower("aaa2345f.ff");
print(wret);
```

Print **false**

### Example 3

```javascript
wret = isLower("");
print(wret);
```

Print **false**

isLower returns "false" if the character string **str** contains blanks or special characters or is a null string.

## See also