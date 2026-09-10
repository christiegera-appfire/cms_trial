# matchStart

## Description

Returns the position where the match starts or -1 if it doesn't match.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | matchStart(input, regex) | **Package** |  |
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
wret = matchStart("This will return ?", "will.*");
print("Return " + wret);
```

Matches the string starting with will and will return 5 (the position of w character).

For more information on regular expressions, see [Oracle documentation]( http://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html).

## See also