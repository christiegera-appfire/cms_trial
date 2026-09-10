# allLinkedIssues

## Description

Returns an array with the issue names linked with the specified issue, including the system links (subtask, issue in epic).

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | allLinkedIssues(issueKey, [[linkTypeName], [direction]]); | **Package** |  |
| **Alias** | getAllLinkedIssues (issueKey, [[linkTypeName], [direction]]) | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKey | String | Yes | Specifies a string representing the key of the issue. |
| linkTypeName | String | No | Specifies the link type. |
| direction | number | No | -1, 0, 1 : Negative means inward links. Positive means outward links. Use zero to get both outward and inward links. |

## Return Type

**String []**

The return value represents a list with all issues (issue keys) that are linked with the argument.

## Example

```javascript
return allLinkedIssues("TEST-53");
```

## See also