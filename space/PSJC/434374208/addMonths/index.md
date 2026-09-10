# addMonths

## Description

Adds a number of months to a specified date, preserving the day of month where possible.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | addMonths(date, noMonths) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Specifies a Date expression. |
| noMonths | Number | Yes | Number of months to add. If given a negative number, will do subtract. |

## Return Type

**Date**

## Example

```javascript
function addMonthsInDesc(date d, int noMonths){
    desc += "Date " + d + " + " + noMonths + " months = " + addMonths(d, noMonths) + "\n";
}
desc = "";
addMonthsInDesc("2012-01-31", 1);
addMonthsInDesc("2012-04-30", -2);
addMonthsInDesc("2013-01-31", 1);
addMonthsInDesc("2013-04-30", -2);
addMonthsInDesc("2012-01-31", 12);
addMonthsInDesc("2012-01-31", -1);
```

Outputs to description:

Date 2012-01-31 00:00:00 + 1 months = 2012-02-29 00:00:00

Date 2012-04-30 00:00:00 + -2 months = 2012-02-29 00:00:00

Date 2013-01-31 00:00:00 + 1 months = 2013-02-28 00:00:00

Date 2013-04-30 00:00:00 + -2 months = 2013-02-28 00:00:00

Date 2012-01-31 00:00:00 + 12 months = 2013-01-31 00:00:00

Date 2012-01-31 00:00:00 + -1 months = 2011-12-31 00:00:00

## See also