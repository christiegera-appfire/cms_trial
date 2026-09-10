# replace

## Description

Replaces the **search\_str** string with **replacement\_str** in **str** and returns the resulting string. The string **str** is not modified.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | replace(str, search\_str, replacement\_str) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| str | String | Yes | Specifies the string to replace characters for. |
| search\_str | String | Yes | Specifies a character expression to search for in str. |
| replacement\_str | String | Yes | Specifies the string that replaces search\_str. |

## Return Type

**String**

## Examples

### Example 1

```javascript
wret = replace("foobar", "foo", "bar");
print(wret);
```

Print **barbar**

### Example 2

```javascript
wret = replace("aaa", "aa", "b");
print(wret);
```

Print **ba**

## See also