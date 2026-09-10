# ceiling

## Description

Returns number rounded up, away from zero, to the nearest multiple of significance.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | ceiling(number, significance) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| number | Number | Yes | Numeric value you want to round. |
| significance | Number | Yes | Multiple you want to round to. |

## Return Type

**Number**

## Example

Prints:

```javascript
number a = ceiling(2.5, 1);
print("a= " + a);
number b = ceiling(-2.5, -2);
print("b= " + b);
```

Prints:   
 a= 3;  
 b= -4;

If number is positive and significance is negative, ceiling returns the NaN value.

## See also