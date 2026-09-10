# day

## Description

Returns a number representing the day of month: 1-31.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | day(date) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Specifies a Date or DateTime expression. |

## Return Type

**Number**

## Examples

### Example 1

```javascript
print("Today is " + day(currentDate()));
```

### Example 2

```javascript
date varDateTime = "2011-08-17T18:30:55";
print("Day is " + day(varDateTime));
```

Print **Day is 17**

## See also