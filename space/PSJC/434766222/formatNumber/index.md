# formatNumber

## Description

Formats a number according to a format string.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | formatNumber(number, format) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| number | Number | Yes | Number to be formatted. |
| format | String | Yes | String that specifies the format. |

## Return Type

**String**

## Example

```javascript
string a = formatNumber(123456.789 ,"###,###.###");
//The pound sign (#) denotes a digit, the comma is a placeholder for the grouping separator, and the period is a placeholder for the decimal separator.
print("a= " + a);
string b = formatNumber(12345.67, "$###,###.###");
print("b= " + b);
string c = formatNumber(123.78, "000000.000");
//The format specifies leading and trailing zeros, because the 0 character is used instead of the pound sign (#).
print("c= " + c);
string d = formatNumber(123456.789, "###.##");
// The number has three digits to the right of the decimal point, but the format has only two. The format method handles this by rounding up.
print("d=" + d);
```

Prints:

a= 123,456.789

b = $12,345.67

c= 000123.780

d=123456.79

The symbols are described in the following table:

| Symbol | Description |
| --- | --- |
| 0 | a digit |
| # | a digit, zero shows as absent |
| . | placeholder for decimal separator |
| , | placeholder for grouping separator |
| E | separates mantissa and exponent for exponential formats |
| ; | separates formats |
| - | default negative prefix |
| % | multiply by 100 and show as percentage |
| ? | multiply by 1000 and show as per mille |
| $ | currency sign; replaced by currency symbol; if doubled, replaced by international currency symbol; if present in a pattern, the monetary decimal separator is used instead of the decimal separator |
| X | any other characters can be used in the prefix or suffix |
| ' | used to quote special characters in a prefix or suffix |

## See also