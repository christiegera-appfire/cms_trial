# cos

## Description

Returns the cosine of the given angle. If the angle is in degrees, either multiply the angle by PI()/180 or use the **radians** function to convert the angle to radians.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | cos(number) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| number | Number | Yes | Angle in radians you want the cosine for. |

## Return Type

**Number**

## Example

```javascript
number a = cos(1.047);
print("a= " + a);
number b = cos(60*pi()/180);
print("b= " + b);
number c = cos(radians(30));
print("c= " + c);
```

Prints: a= 0.5001710745970701;

b= 0.5000000000000001;

c= 0.5000000000000001;

## See also