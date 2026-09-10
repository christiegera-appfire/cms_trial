# monthName

## Description

Returns the month name of the provided date. English only. One of the following string values: " Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov","Dec".

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | monthName(date) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Specifies a Date or a DateTime expression. |

## Return Type

**String**

## Examples

### Example 1

```javascript
print("Month is " + monthName(currentDate()));
```

### Example 2

```javascript
date varDateTime = "2011-08-17T18:30:55";
print("Month is " + monthName(varDateTime));
```

Print **Month is Aug**

## See also