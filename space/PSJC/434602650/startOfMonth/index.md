# startOfMonth

## Description

Returns a date set on the first day of the month for the given date. Also sets hours/minutes/seconds to 0.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | startOfMonth(date) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Specifies a Date expression. |

## Return Type

**Date**

## Example

```javascript
function startOfMonthToDesc(date d){
    desc += "Start of month for date " + d + " is " + startOfMonth(d) + "\n";
}
desc = "";
startOfMonthToDesc("2013-01-26 20:19:18");
startOfMonthToDesc("2013-02-01 20:19:18");
startOfMonthToDesc("2013-02-28 20:19:18");
startOfMonthToDesc("2012-02-29 20:19:18");
startOfMonthToDesc("2012-12-31 23:59:59");
startOfMonthToDesc("2012-12-01 23:59:59");
startOfMonthToDesc("2012-12-01 00:00:00");
```

Outputs to description:

Start of month for date 2013-01-26 20:19:18 is 2013-01-01 00:00:00

Start of month for date 2013-02-01 20:19:18 is 2013-02-01 00:00:00

Start of month for date 2013-02-28 20:19:18 is 2013-02-01 00:00:00

Start of month for date 2012-02-29 20:19:18 is 2012-02-01 00:00:00

Start of month for date 2012-12-31 23:59:59 is 2012-12-01 00:00:00

Start of month for date 2012-12-01 23:59:59 is 2012-12-01 00:00:00

Start of month for date 2012-12-01 00:00:00 is 2012-12-01 00:00:00

## See also