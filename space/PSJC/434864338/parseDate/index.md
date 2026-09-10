# parseDate

## Description

Returns the parsed date according to the format you provided. If parse fails, it will return a null date.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | parseDate(format, date\_as\_string[, locale\_as\_string]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| format | String | Yes | Valid Java format, as defined here: <http://docs.oracle.com/javase/6/docs/api/java/text/SimpleDateFormat.html> . |
| date\_as\_string | String | Yes | String which represents the date. |
| locale\_as\_string | String | No | Language tag which should be used to parse a date. It can be leveraged to parse dates like this: 5/???/18.This parameter accepts well-formed BCP 47 language tag. See this link for more details on possible values. |

## Return Type

**Date**

## Example

```javascript
print("(1) Parsed date is:" + parseDate("yyyy.MM.dd", "2000.01.01"));       // returns a valid date
print("(2) Parsed date is:" + parseDate("yyyy.MM.dd", "2000/01/01"));       // returns an empty date (null)
print("(3) Parsed date is:" + parseDate("dd/MMM/yy", "5/???/18", "ru-RU")); // returns a valid date which is parsed using ru-RU locale
```

## See also