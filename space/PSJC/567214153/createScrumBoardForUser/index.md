# createScrumBoardForUser

## Description

Creates a Scrum board customized for a specific user, typically allowing users to set up their own Scrum boards tailored to their preferences and requirements.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | createScrumBoardForUser(name, filterId, user) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | String | Yes | Board name |
| filterId | Integer | Yes | Filter, make sure the JQL uses the Rank order otherwise you will not be able to rank the issues |
| user | String | Yes | account id of the user for which you are creating the board |

## Return Type

**Integer**

Gets the board id. Null if it cannot be created

## Example

Creates a new scrum board for the user "joeUser".

```javascript
int newBoard = createScrumBoardForUser("New board for Joe", 12345, "joeUser");
return newBoard;
```

## See also