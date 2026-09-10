# matchEnd

## Description

Returns the position where the match ends or -1 if it doesn't match.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | matchEnd(input, regex) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| input | String | Yes | Specifies a character expression to match the regex against. |
| regex | String | Yes | Specifies a regular expression to match the specified string. |

## Return Type

**Number**

## Example

```javascript
wret = matchEnd("This will return ?", ".*will");
print("Return " + wret);
```

Matches the string ending with "will" and will return 9 (the position of "l" character).

For more information on regular expressions see [Oracle documentation]( http://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html).

## See also