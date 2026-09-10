# trim

## Description

Returns a trimmed copy of the string passed as parameter with the leading and trailing whitespaces removed.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | trim(str) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| str | String | Yes | String to trim. |

## Return Type

**String**

## Example

```javascript
string original = "   foobar   ";
string trimmed = trim(original);
print(">>" + original + "<<"); // will print ">>   foobar   <<"
print(">>" + trimmed + "<<");  // will print ">>foobar<<"
```

This also works if the string passed in as parameter only has leading or trailing whitespaces. If the string has no leading or trailing whitespaces, a copy of the original string will be returned.

## See also