# currentUser

## Description

Returns the key for the user that invoked the script containing **currentUser**.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | currentUser() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

**String**

The return value represents the key of the user that triggered the script. Usually transition is executed.

## Example

```javascript
customfield = currentUser();
```

Result: customfield = <key of the current user>.

## See also