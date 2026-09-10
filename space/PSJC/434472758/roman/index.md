# roman

## Description

Converts an Arabic numeral to Roman numeral, as text, of course.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | roman(arabic number) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| arabic number | Number | Yes | Arabic numeral you want converted. |

## Return Type

**String**

## Example

```javascript
string a = roman(7);
print("a= " + a);
string b = roman(2034);
print("b= " + b);
```

Prints: a= VII;  
 b= MMXXXIV;

If number is less than 0 and greater than 3999 an empty string is returned.

## See also