# countIssues

## Description

Returns the number of issues that matched the search query.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | countIssues(jql) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| search query | String | Yes | Searches query containing the details of the returned issues. |

## Return Type

**Number**

Returns the number of **issue keys** that match the specified jql.

## Example

```javascript
string jql;
jql = "project = PRJ AND reporter in membersOf('Employees') AND status in (Open, 'In Progress', Reopened, Resolved, 'On hold', Assigned, 'Internal QA', 'Results rejected', 'Tested and not delivered', 'Tested and delivred')";
countIssues(jql);
```

Result: The number of issues that are in the project **PRJ**, with the reporter included in **Employees** group and the status being one of the above.

For the search query use apostrophe(') instead of quotes(") and double backslashes(\\)for escaping characters (instead of a single backslash).

## See also