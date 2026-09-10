# split

## Description

Returns the array of strings computed by splitting this string around matches of the given regular expression.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | split(str, regex) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| str | String | Yes | Specifies the string that will be split. |
| regex | String | Yes | Delimiting regular expression. |

## Return Type

**String[]**

## Examples

### Example 1

```javascript
return split("boo:and:foo", ":");
```

Returns  **{ "boo", "and", "foo" }**.

### Example 2

```javascript
return split("I went to the store. I bought some milk.", "\. ");
//period symbol is a special character in regex so it must be escaped
```

Returns  **{ "I went to the store", "I bought some milk" }**.

### Example 3

```javascript
return split("1:Part one2:Part two3:Part 3", "([0-9]:)");
```

Returns  **{ "Part one", "Part two", "Part 3" }**.

## See also