# bitwise_xor

## Description

Takes two numbers as operands and does XOR on every bit of two numbers. The result of XOR is 1 if the two bits are different.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | bitwise\_xor(int1, int2) | **Package** | bitwise |
| **Alias** |  | **Pkg Usage** | b\_xor(int1, int2) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| int1 | Integer | Yes | First operand. |
| int2 | Integer | Yes | Second operand. |

## Return Type

**Integer**

The result of the bitwise operation.

## Example

```javascript
use "bitwise";
int result = b_xor(int1, int2);
//------------or-----
//no package needed
int result = bitwise_xor(int1, int2);
```

## See also