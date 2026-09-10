# toRawWorkingInterval

## Description

Returns a date interval converted to the specified number of hours per day. This function re-writes a 24h day interval in an interval that is based on 8h (for instance). It is not sensitive for weekends, holidays, leave without pay, and so on. The result interval is converted using the workingHours/day parameter that is optional and is an integer between 1 and 24. This function can be used to view how much hours can a user work during a week, for instance.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | toRawWorkingInterval (interval, [workingHours/day]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| interval | Interval | Yes | Specifies a date interval that will be converted from 24 hours/day to working hours/day. |
| format | Number | No | Specifies the number of working hours per day the interval will be converted to. The default number is 8, if another number isn't specified. |

## Return Type

**Interval**

The return value represents the converted interval from the interval given as argument.

## Examples

### Example 1

Let us consider the following SIL code:

```javascript
date begin = "2013-01-17T12:30:00";
date end = "2013-01-28T16:30:00";
return toRawWorkingInterval(end - begin, 6);
```

This will return "**2d 22h**" due to:

1. The interval between begin date and end date is 11d 4h.
2. If we convert a day from **24 hours** to a **6 hour** per day we will make the following computation: **11d \* 6h + 4h = 66h + 4h = 70h** that will be viewed as **2d 22h**.

### Example 2

By running this code:

```javascript
date begin = "2013-01-17T02:30:00";
date end = "2013-01-28T16:30:00";
return toRawWorkingInterval(end - begin);
```

The result will return "**4d**" due to:

1. The interval is "**11d 12h**" long.
2. The conversion is based on this computation: **12d \* 8h(default hours) = 96h** that means "**4d**".
3. This is done so because the number of hours in the 12th day of the interval exceeds the number of working hours per day (by default 8) and a new day is added.

## See also