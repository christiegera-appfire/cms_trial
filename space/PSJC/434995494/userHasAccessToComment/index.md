# userHasAccessToComment

## Description

Verifies if a comment is visible for an user.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | userHasAccessToComment(accountId, issueKey, comment\_id) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| accountId | String | Yes | The account id of the user. |
| issueKey | String | Yes | The issue key. |
| comment\_id | Number | Yes | Id of the comment. |

## Return Type

**Boolean**

A "true" return value means that the user can see the comment.

## Example

```javascript
userHasAccessToComment(key, "admin","10000");
```

Returns "true" if the user "admin" can see the comment with id "10000" from the current issue and "false" if the user cannot see the comment.

## See also