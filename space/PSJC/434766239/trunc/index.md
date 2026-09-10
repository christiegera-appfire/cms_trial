# trunc

## Description

Truncates a number to a specified precision.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | trunc(number, digits) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| number | Number | Yes | Number to truncate. |
| digits | Number | Yes | Precision. |

## Return Type

**Number**

## Example

```javascript
number a = trunc(1.1578212823495777, 3);
print("a= " + a);
```

Prints: a= 1.157;

## See also