# currentUsername

## Description

Returns the username for the user that invoked the script containing **currentUsername**.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | currentUsername() | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Return Type

**String**

The return value represents the **username** of the user that triggered the script. Usually a transition is executed.

## Example

```javascript
customfield = currentUsername();
```

Result: customfield = <username of the current user>.

## See also