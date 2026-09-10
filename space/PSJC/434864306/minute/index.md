# minute

## Description

Returns the minutes of the provided date: 0-59.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | minute(date) | **Package** |  |
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
print("Minute is " + minute(currentDate()));
```

### Example 2

```javascript
date varDateTime = "2011-08-17T18:30:55";
print("Minute is " + minute(varDateTime));
```

Print **Minute is 30**

## See also