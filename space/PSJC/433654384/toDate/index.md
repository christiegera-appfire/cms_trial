# toDate

## Description

Creates a date value from the specified parameters.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | toDate(year, month, day[, hour, minute, second[, millis[, timeZone]]]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| year | Number | Yes | Specifies the year value. |
| month | Number | Yes | Specifies the month value. This value is 1-based (e.g 1 = January, 12 = December). Accepted values are [1-12]. |
| day | Number | Yes | Specifies the day of month value. Providing an invalid day value for the specified month/year (e.g. 30 Feb 2013, 29 Feb 2013) will throw an exception **at runtime**. Accepted values are [1-28-29-30-31]. |
| hour | Number | No | Specifies the hour of day value. Accepted values are [0-23]. |
| minute | Number | No | Specifies the minutes value. Accepted values are [0-59]. |
| second | Number | No | Specifies the number of seconds. Accepted values are [0-59]. |
| millis | Number | No | Specifies the number of milliseconds. Accepted values are [0-999]. |
| timeZone | String | No | Specifies the time zone using a format compatible with [TimeZone](http://docs.oracle.com/javase/6/docs/api/java/util/TimeZone.html). See [TimeZone](http://docs.oracle.com/javase/6/docs/api/java/util/TimeZone.html) for more details. |

## Return Type

**Date**

## Example

```javascript
function toDate7Descr(number year, number month, number day, number hour, number minute, number second, string timeZone) { 
  string format = "dd-MMM-yyyy HH:mm:ss Z"; 
  desc += "Converted year " + year + ", month " + month + ", day " + day + ", hour " + hour + ", minute " + minute + ", second " + second + ", timeZone " + timeZone; 
  desc += " to date " + formatDate(toDate(year, month, day, hour, minute, second, 0, timeZone), format) + "\n"; 
}
function toDate6Descr(number year, number month, number day, number hour, number minute, number second){
 desc += "Converted year " + year + ", month " + month + ", day " + day + ", hour " + hour + ", minute " + minute + ", second " + second;
 desc += " to date " + toDate(year, month, day, hour, minute, second) + "\n";
}
function toDate3Descr(number year, number month, number day){
 desc += "Converted year " + year + ", month " + month + ", day " + day;
 desc += " to date " + toDate(year, month, day) + "\n";
}
desc = "";
toDate3Descr(2013, 12, 31);
toDate3Descr(2013, 2, 28);
toDate3Descr(2012, 2, 29);
toDate3Descr(2013, 2, 29); 
toDate6Descr(2013, 12, 31, 23, 59, 59);
toDate6Descr(2013, 2, 28, 0, 0, 0);
toDate6Descr(2012, 2, 29, 14, 15, 16);
toDate6Descr(2013, 1, 1, 24, 1, 1);

toDate7Descr(2012, 01, 20, 0, 0, 0, "GMT+2");
```

Outputs to description:

Converted year 2013, month 12, day 31 to date 2013-12-31 00:00:00

Converted year 2013, month 2, day 28 to date 2013-02-28 00:00:00

Converted year 2012, month 2, day 29 to date 2012-02-29 00:00:00

Converted year 2013, month 2, day 29 to date

Converted year 2013, month 12, day 31, hour 23, minute 59, second 59 to date 2013-12-31 23:59:59

Converted year 2013, month 2, day 28, hour 0, minute 0, second 0 to date 2013-02-28 00:00:00

Converted year 2012, month 2, day 29, hour 14, minute 15, second 16 to date 2012-02-29 14:15:16

Converted year 2013, month 1, day 1, hour 24, minute 1, second 1 to date

Converted year 2012, month 1, day 20, hour 0, minute 0, second 0, timeZone GMT+2 to date 20-Jan-2012 00:00:00 +0200

The created date will use the locale of the JVM. If any of the parameters are outside of the specified interval (e.g attempting to create 32 January), the function will return an empty date, such that isNull(date) is "true".

## See also