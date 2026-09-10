# year

## Description

Returns the year of the provided date.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | year(date) | **Package** |  |
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
print("Year is " + year(currentDate()));
```

### Example 2

```javascript
date varDateTime = "2011-08-17T18:30:55";
print("Year is " + year(varDateTime));
```

Print **Year is 2011**.

## See also