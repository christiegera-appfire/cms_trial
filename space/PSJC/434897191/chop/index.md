# chop

## Description

Returns a string, chopped at **nmb** characters, starting with the leftmost character. Cuts down the string (if length is greater than **nmb** characters) to a string of max **nmb** chars.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | chop(str, nmb) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| str | String | Yes | Specifies a character expression. |
| nmb | Number | Yes | Specifies the number of characters returned from the character expression str. |

## Return Type

**String**

## Examples

### Example 1

```javascript
wret = chop("Once upon a time", 6);
print(wret);
```

Print **Once u**

### Example 2

```javascript
wret = chop("Once upon a time", 30);
print (wret );
```

Print **Once upon a time**

### Example 3

```javascript
wret = chop(" Once upon a time", -1);
print (wret );
```

Print **Once upon a time**

## See also