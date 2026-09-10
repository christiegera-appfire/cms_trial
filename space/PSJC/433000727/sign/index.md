# sign

## Description

Determines the sign of a number (signum). Returns 1 if the number is positive, zero (0) if the number is 0, and -1 if the number is negative.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | sign(number) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| number | Number | Yes | Any real number. |

## Return Type

**Number**

## Example

```javascript
number a = sign(3);
print("a= " + a);
number b = sign(-4);
print("b= " + b);
number c = sign(3-3);
print("b= " + c);
```

Prints:

a= 1;

b= -1;

c= 0;

## See also