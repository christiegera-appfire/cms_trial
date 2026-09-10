# bitwise_or

## Description

Takes two numbers as operands and does OR on every bit of two numbers. The result of OR is 1 if any of the two bits is 1.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | bitwise\_or(int1, int2) | **Package** | bitwise |
| **Alias** |  | **Pkg Usage** | b\_or(int1, int2) |

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
int result = b_or(int1, int2);
//------------or-----
//no package needed
int result = bitwise_or(int1, int2);
```

## See also