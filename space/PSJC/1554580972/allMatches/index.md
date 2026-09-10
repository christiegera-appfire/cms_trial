# allMatches

## Description

Returns all the matches or empty string if the regex doesn't match anything.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | allMatches(input, regex) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| input | string | Yes | Specifies a character expression to match the regex against. |
| regex | string | Yes | Specifies a regular expression to match the specified string. |

## Return Type

**string[]**

## Example

```javascript
string text = "The quick brown fox jumps over the lazy dog";
string[] matched = allMatches(text,"The quick (.*) fox jumps over the (.*) dog");
return "Entire: " + matched[0] + "\nFirst: " + matched[1] + "\nSecond: " + matched[2];
```

## See also