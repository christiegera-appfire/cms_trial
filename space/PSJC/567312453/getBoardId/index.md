# getBoardId

## Description

Used to obtain the unique identifier (ID) associated with a specific board. The ID is essential for performing various actions related to the board.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getBoardId(partial\_board\_name) or findBoard(partial\_board\_name) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| partial\_board\_name | String | Yes | partial board name to search for |

## Return Type

**Integer**

Returns the first board that matches. If return is null, it means no board was found

## Example

```javascript
return getBoardId("Sprint delta tiger force alpha");
```

## See also