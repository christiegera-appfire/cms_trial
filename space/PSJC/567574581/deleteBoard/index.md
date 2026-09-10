# deleteBoard

## Description

Allows for the removal of a specific board from the system. Deleting a board typically involves permanently removing all associated data and configurations.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | deleteBoard(boardId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| boardId | Integer | Yes | Board id |

## Return Type

**bool**

true if the delete occurred

## Example

```javascript
return deleteBoard(12345);
```

## See also