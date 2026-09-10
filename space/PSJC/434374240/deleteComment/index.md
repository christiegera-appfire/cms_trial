# deleteComment

## Description

Deletes a comment with the specified id, deletes the latest comment or deletes all comments from a given issue.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | deleteComment(issue, commentId\_or\_mode) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue key | String | Yes | IssueKey. Should be used only if the mode is "DELETE\_LATEST" or "DELETE\_ALL" |
| commentId\_or\_mode | Number or String | Yes | Either the comment id (if we use the routine with only one parameter) or one of the next, otherwise:- "DELETE\_LATEST" to delete the latest comment for the given issue - "DELETE\_ALL" to delete all the comments for the given issue |

## Return Type

**Number**

The number of comments deleted.

## Examples

### Example 1

```javascript
return deleteComment("TEST-1", "DELETE_ALL");
```

Deletes all comments from "TEST-1" and returns the number of comments deleted.

### Example 2

```javascript
return deleteComment("TEST-2", "DELETE_LATEST");
```

Deletes the latest comment from "TEST-2" and returns "1" because only one comment was deleted. If the comment cannot be deleted it will return "0".

## See also