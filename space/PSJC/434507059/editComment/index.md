# editComment

## Description

Edits a comment with the specified id and text. Optional, you can edit the security level for comment. Returns the comment representation after the edit.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | editComment(issueKey, commentId, comment[, securityLevel]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | String | Yes | Key of the selected issue. |
| commentId | Number | Yes | Id of the issue comment. |
| comment | String | Yes | Text that will be post on the selected comment. |
| securityLevel | String | No | Security level of comment. Can be a group or a project role. |

## Return Type

[**JComment**](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=Predefined%20Structure%20Types&linkCreation=true&fromPageId=434507059)

The comment representation with the following keys:

## Example

### Example 1

```javascript
string newComm = "This comment was edited.";
return editComment(key, 11801, newComm);
```

Edits the comment with id 11801 with the specified text.

## See also