# substring

## Description

Returns substring is starting at index **start** and stop at index **stop**. The substring returned has length **stop** - **start**. First position of character expression str is 0. If index **start** is not initialized or -1, it will be set on 0. If index **stop** is not initialized or -1, it will be set on end of the string.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | substring(str, start, stop) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| str | String | Yes | Specifies a character expression the character string is returned from. |
| start | Number | Yes | Specifies the position in the character expression **str** the character string is returned from. |
| stop | Number | Yes | Specifies the position in the character expression **str** the character string is returned from. |

## Return Type

**String**

## Examples

### Example 1

```javascript
number start;
number stop;
substring("FooBar", start, stop);
// start will default to 0
// stop will default to 6
// substring() will return FooBar
// Result are the same if we initialize start and/or stop with -1
```

### Example 2

```javascript
number start;
number stop = 3;
substring("FooBar", start, stop);
// start will default to 0
// will return Foo
```

### Example 3

```javascript
string v = "ABCDEFGHIJKLMNOP...";
print(substring(v, 0, 3)); //"ABC" 
print (substring (v, 10, 100 )); //"KLMNOP..."
print(substring(v, 10, -1)); //"KLMNOP..." (same call)
```

If **stop** is equal **start** or **start** is greater than the maximum length of character expression **str**, **substring** returns an empty string.

## See also