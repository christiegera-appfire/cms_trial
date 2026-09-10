# selectIssues

## Description

Returns an array with the keys of the issues that matched the search query.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | selectIssues(jql [,maxResults [, reconcileIssues]]) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| jql | String | Yes | Search query containing the details of the returned issues. |
| maxResults | number | No | The maximum number of returned issues. |
| reconcileIssues | number [] | No | Strong consistency issue ids to be reconciled with search results. Accepts max 50 ids |

## Return Type

**String []**

Returns a list of issue keys that match the specified jql.

## Example

```javascript
string jql;
jql = "project = PRJ AND reporter in membersOf('Employees') AND status in (Open, 'In Progress', Reopened, Resolved, 'On hold', Assigned, 'Internal QA', 'Results rejected', 'Tested and not delivered', 'Tested and delivred')";
selectIssues(jql);
```

Result: An array of strings containing the keys of all the issues that are in the PRJ project, with the reporter included in Employees group and the status being one of the above.

For the search query, please use apostrophe(') instead of quotes(") and double backslashes(\) instead of a single backslash for escaping characters.

## See also