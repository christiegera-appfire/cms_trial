# floor

## Description

Rounds number down, toward zero, to the nearest multiple of significance.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | floor(number, significance) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| number | Number | Yes | Numeric value you want to round to. |
| significance | Number | Yes | Multiple value you want to round to. |

## Return Type

**Number**

## Example

```javascript
number a = floor(4.5, 2);
print("a= " + a);
number b = floor(-2.5, -2);
print("b= " + b);
```

Prints:

a= 4;

b= -2;

If number is positive and significance is negative, FLOOR returns the NaN value.

## See also