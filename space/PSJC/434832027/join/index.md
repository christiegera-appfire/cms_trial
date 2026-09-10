# join

## Description

Returns the string obtained by concatenating all the strings from the array using the provided delimiter.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | join(string\_arr, delimiter) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| string\_arr | string [] | Yes | Specifies the strings to be concatenated. |
| delimiter | String | Yes | Delimiting string. |

## Return Type

**String**

## Example

```javascript
string [] arr = {"boo", "and", "foo"};
return join(arr, ":");
```

Returns "**boo:and:foo**"

## See also