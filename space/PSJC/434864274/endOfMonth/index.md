# endOfMonth

## Description

Returns a date set on the last day of the month for the given date. Also sets hours / minutes / seconds / milliseconds to their respective maximum value.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | endOfMonth(date) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Specifies a Date expression. |

## Return Type

**Date**

## Example

```javascript
function endOfMonthToDesc(date d){
    desc += "End of month for date " + d + " is " + endOfMonth(d) + "\n";
}
desc = "";
endOfMonthToDesc("2013-01-26 20:19:18");
endOfMonthToDesc("2013-02-01 20:19:18");
endOfMonthToDesc("2012-02-01 20:19:18");
endOfMonthToDesc("2013-02-28 20:19:18");
endOfMonthToDesc("2012-02-29 20:19:18");
endOfMonthToDesc("2012-12-31 23:59:59");
endOfMonthToDesc("2012-12-31 00:00:00");
endOfMonthToDesc("2012-12-01 23:59:59");
endOfMonthToDesc("2012-12-01 00:00:00");
```

Outputs to description:  
End of month for date 2013-01-26 20:19:18 is 2013-01-31 23:59:59  
End of month for date 2013-02-01 20:19:18 is 2013-02-28 23:59:59  
End of month for date 2012-02-01 20:19:18 is 2012-02-29 23:59:59  
End of month for date 2013-02-28 20:19:18 is 2013-02-28 23:59:59  
End of month for date 2012-02-29 20:19:18 is 2012-02-29 23:59:59  
End of month for date 2012-12-31 23:59:59 is 2012-12-31 23:59:59  
End of month for date 2012-12-31 00:00:00 is 2012-12-31 23:59:59  
End of month for date 2012-12-01 23:59:59 is 2012-12-31 23:59:59  
End of month for date 2012-12-01 00:00:00 is 2012-12-31 23:59:59

## See also