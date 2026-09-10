# second

## Description

Returns the seconds of the provided date: 0-59.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | second(date) | **Package** |  |
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
print("Second is " + second(currentDate()));
```

### Example 2

```javascript
date varDateTime = "2011-08-17T18:30:55";
print("Second is " + second(varDateTime));
```

Print **Second is 55**

## See also