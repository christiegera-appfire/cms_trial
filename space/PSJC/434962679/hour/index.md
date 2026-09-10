# hour

## Description

Returns the hour of the provided date: 0-23.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | hour(date) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| date | Date | Yes | Specifies a DateTime expression. |

## Return Type

**Number**

## Examples

### Example 1

```javascript
print("Hour is " + hour(currentDate()));
```

### Example 2

```javascript
date varDateTime = "2011-08-17T18:30:55";
print("Hour is " + hour(varDateTime));
```

Print **Hour is 18**

## See also