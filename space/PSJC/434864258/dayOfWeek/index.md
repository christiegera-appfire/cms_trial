# dayOfWeek

## Description

Returns the day of week. English only. One of the following string values: "Sun","Mon","Tue","Wed","Thu","Fri","Sat".

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | dayOfWeek(date) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Specifies a Date or DateTime expression. |

## Return Type

**String**

## Examples

### Example 1

```javascript
print("Today is " + dayOfWeek(currentDate()));
```

### Example 2

```javascript
date varDateTime = "2011-08-17T18:30:55";
print("Day of week is " + dayOfWeek(varDateTime));
```

Print **Day of week is Wed**

## See also