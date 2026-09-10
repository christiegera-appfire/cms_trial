# fact

## Description

Returns the factorial of a number. The factorial of a number **n** is equal to 1\*2\*3\*...\* n

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | fact(number) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| number | Number | Yes | Non-negative number you want the factorial for. If number is not an integer, it is truncated. |

## Return Type

**Number**

## Example

```javascript
number a = fact(5);
print("a= " + a);
number b = fact(3.7);
print("b= " + b);
number c = fact(-3);
print("c= " + c);
```

Prints:

a= 120 ;

b= 6;

c= NaN;

## See also