# bitwise_lshift

## Description

Takes two numbers, left shifts the bits of the first operand, the second operand decides the number of places to shift.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | bitwise\_lshift(int1, int2) | **Package** | bitwise |
| **Alias** |  | **Pkg Usage** | b\_lshift(int1, int2) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| int1 | Integer | Yes | First operand. |
| int2 | Integer | Yes | Second operand. Number of bits to shift. |

## Return Type

**Integer**

The result of the bitwise operation (signed left shift).

## Example

```javascript
use "bitwise";
int result = b_lshift(int1, int2);
//------------or-----
//no package needed
int result = bitwise_lshift(int1, int2);
```

## See also