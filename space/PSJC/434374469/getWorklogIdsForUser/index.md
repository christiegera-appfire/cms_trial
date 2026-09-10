# getWorklogIdsForUser

## Description

Returns an array with the ids of the worklogs for the specified user and issue.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getWorklogIdsForUser(author, issueKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| author | String | Yes | The username of the selected user. |
| issueKey | String | Yes | Key of the selected issue. |

## Return Type

**Number []**

## Example

```javascript
getWorklogIdsForUser("admin",key)
```

Returns an array containing the ids of all the worklogs of the current issue who were created by admin.

## See also