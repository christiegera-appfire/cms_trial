# month

## Description

Returns a number representing the month of the provided date (1-12).

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | month(date) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Specifies a Date or a DateTime expression. |

## Return Type

**Number**

## Examples

### Example 1

```javascript
print("Month is " + month(currentDate()));
```

### Example 2

```javascript
date varDateTime = "2011-08-17T18:30:55";
print("Month is " + month(varDateTime));
```

Print - Month is 8

## See also