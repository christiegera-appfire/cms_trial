# week

## Description

Returns the week number in the year of the provided date.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | week(date) | **Package** |  |
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
print("Week is " + week(currentDate()));
```

### Example 2

```javascript
date varDateTime = "2011-08-17T18:30:55";
print("Week is " + week(varDateTime));
```

Print **Week is 33**

## See also