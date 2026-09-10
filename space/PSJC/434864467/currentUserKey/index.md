# currentUserKey

## Description

Returns the key for the user that invoked the script containing **currentUserKey**.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | currentUserKey() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

**String**

The return value represents the **key** of the user that triggered the script. Usually a transition is executed.

## Example

```javascript
customfield = currentUserKey();
```

Result: customfield = <key of the current user>.

## See also