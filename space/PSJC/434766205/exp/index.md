# exp

## Description

Returns e raised to the power of number. The constant e equals 2.71828182845904, the base of the natural logarithm.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | exp(number) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| number | Number | Yes | Exponent applied to the base e. |

## Return Type

**Number**

## Example

```javascript
number a = exp(1);
print("a= " + a);
number b = exp(2);
print("b= " + b);
number c = exp(-2);
print("c= " + c);
number d = exp(0); 
print("d= " + d);
```

Prints:

a= 2.71828182845904 ;

b= 7.38905609893065 ;

c= 0.1353352832366127;

d= 1;

## See also