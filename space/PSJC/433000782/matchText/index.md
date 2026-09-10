# matchText

## Description

Returns the text matched or empty string if it doesn't match.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | matchText(input, regex) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| input | String | Yes | Specifies a character expression to match the regex against. |
| regex | String | Yes | Specifies a regular expression to match the specified string. |

## Return Type

**String**

## Example

```javascript
wret = matchText("This will return ?", ".*will");
print("Return " + wret);
```

Returns the string matched at the beginning of the string until "will" word.

For more information on regular expressions, see [Oracle documentation]( http://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html).

## See also