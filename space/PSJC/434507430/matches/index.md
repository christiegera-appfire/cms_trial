# matches

## Description

Returns "true" if character expression string matches the regular expression regex.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | matches(string, regex) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| string | String | Yes | Specifies a character expression to match the regex against. |
| regex | String | Yes | Specifies a regular expression to match the specified string. |

## Return Type

**Boolean (true/false)**

## Examples

### Example 1

```javascript
wret = matches("This will return ?", ".*will.*");
print("Return " + wret);
```

Matches any string containing "will". Prints **Return true**

### Example 2

```javascript
wret = matches("This will return ?", "will");
print("Return " + wret);
```

Matches only the string "will ". Prints **Return false**

### Example 3

```javascript
wret = matches("This will return ?", ".*will[^\?]*\?");
print("Return " + wret);
```

Matches any string containing "will" and ending with a question mark. Prints **Return true**

- As shown in Example 3, use double backslash (\) instead of a single backslash where needed.
- For more information on regular expressions, see [Oracle documentation](http://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html).

## See also