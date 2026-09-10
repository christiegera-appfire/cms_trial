# sin

## Description

Returns the sine of the given angle. If the angle is in degrees, either multiply the angle by PI()/180 or use the radians function to convert the angle to **radians.**

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | sin(number) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| number | Number | Yes | Angle in radians you want the sine for. |

## Return Type

**Number**

## Example

```javascript
number a = sin(1.047);
print("a= " + a);
number b = sin(60*pi()/180);
print("b= " + b);
```

Prints:

a= 0.8659266112878228;

b= 0.8660254037844386;

## See also