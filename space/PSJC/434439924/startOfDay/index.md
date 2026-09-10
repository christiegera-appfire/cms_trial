# startOfDay

## Description

Returns a date, but strips off the hours, minutes and seconds.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | startOfDay(date) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Specifies a Date expression. |

## Return Type

**Date**

## Examples

### Example 1

```javascript
if(datepicker < startOfDay(currentDate())){
    return false;
}
```

### Example 2

```javascript
date varDate = "2011-08-17";
print("Date is " + startOfDay(varDate));
```

Print **Date is 17/Aug/11**

## See also