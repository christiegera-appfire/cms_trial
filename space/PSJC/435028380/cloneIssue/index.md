# cloneIssue

## Description

Duplicates the issue and returns the key of the duplicated issue. If specified, it also creates a link to the duplicated issue.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | cloneIssue(issueKey, [issueLinkTypeName [, newParentKey]]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issuekey | String | Yes | Key of the issue that has to be cloned. |
| issueLinkTypeName | String | No | Link to the duplicated issue. |
| newParentKey | String | No | New parent, if subtask. |

## Return Type

**String**

The return value represents the key of the duplicated issue.

## Examples

### Example 1

```javascript
cloneIssue("PRJ-343");
//"PRJ-343" represents the key of the issue that will be duplicated.
```

Result: Issue **PRJ-343** is duplicated.

### Example 2

```javascript
cloneIssue("PRJ-267","Cloned Issue")
```

Result: Issue **PRJ-267** is duplicated and a link named **Cloned Issue** to the duplicated issue is created.

Using the "newParentKey" parameter can create subtasks in other projects and create infinite subtasks. This may render Jira unusable. Make sure the parent and the subtask will be in the same project. Make sure you do not create a subtask with another subtask as parent.

## See also