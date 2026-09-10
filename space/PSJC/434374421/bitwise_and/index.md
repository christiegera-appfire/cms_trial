# bitwise_and

## Description

Takes two numbers as operands and does AND on every bit of two numbers. The result of AND is 1 only if both bits are 1.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | bitwise\_and(int1, int2) | **Package** | bitwise |
| **Alias** |  | **Pkg Usage** | b\_and(int1, int2) |

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
int result = b_and(int1, int2);
//------------or-----
//no package needed
int result = bitwise_and(int1, int2);
```

## See also