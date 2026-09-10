# formatDate

## Description

Formats the given date into a date/time string accordingly to the given format expression.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | formatDate(date, format) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Specifies a Date or DateTime expression. |
| format | String | Yes | Specifies a pattern expression representing the desired date format. |

## Return Type

**String**

The return value represents the formatted string representation for the given date.

## Examples

### Example 1

```javascript
string format = "yyyy.MM.dd G 'at' HH:mm:ss z";
print("Current time is " + formatDate(currentDate(), format));
```

Assuming that current date is 30.10.2011 and time 12:08, prints **Today is 2011.10.30 AD at 12:08:00 PDT**

### Example 2

```javascript
date varDateTime = "2011 -08 -17 T18: 30: 55";
string format = "EEE, d MMM yyyy HH:mm:ss Z";
print ("Formatted date is" + formatDate(varDateTime,format));
```

Print **Formatted date is Wed, 17 Aug 2011 18:30:55 +0300**

For a full set of date formats that can be used, check out the [SimpleDateFormat](http://download.oracle.com/javase/6/docs/api/java/text/SimpleDateFormat.html) documentation from Oracle.

## See also