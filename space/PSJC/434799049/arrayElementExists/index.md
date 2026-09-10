# arrayElementExists

## Description

Returns "true" if the element exists in the array and "false" otherwise.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | arrayElementExists(array, elem) | **Package** | array |
| **Alias** | elementExists (array, elem) | **Pkg Usage** | elementExists(array, elem) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| array | Array | Yes | Array where the element existence is checked. |
| element | Any | Yes | Element the existence is checked for. |

## Return Type

**Boolean**

## Example

```javascript
if( elementExists(watchers, currentUser()) ){
    print("You are watching this issue.");
}
```

The function returns "true" if **currentUser** is in the **watchers** array and if the result is "true" a message is printed.

If **elem** is not the same type as declared in the array definition, the function returns "error".

## See also