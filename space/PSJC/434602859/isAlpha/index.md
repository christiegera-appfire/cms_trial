# isAlpha

## Description

Returns "true" if the provided argument **str** is a string containing only letters.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | isAlpha(str) | **Package** |  |
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
wret = isAlpha("foobar");
print(wret);
```

Print **true**

### Example 2

```javascript
wret = isAlpha("aaa2345f.ff");
print(wret);
```

Print **false**

### Example 3

```javascript
wret = isAlpha("Once upon a time... !");
print(wret);
```

Print **false**

IsAlpha returns "false" if the character string **str** contains blanks or special characters.

## See also