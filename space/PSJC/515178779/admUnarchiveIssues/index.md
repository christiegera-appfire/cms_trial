# admUnarchiveIssues

## Description

Unarchives a issue or a list of issues (maximum 1000, that’s a limitation that Atlassian set).

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUnarchiveIssues(issueKeysOrIds) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | unarchiveIssues(issueKeysOrIds) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKeysOrIds | string [] | Yes | The issue key/s or id/s that will be unarchived |

## Return Type

**Number**

The number of unarchived issues

## Example

```javascript
return admUnarchiveIssues({"TEST-1", "TEST-2"});
```

Returns: 2

## See also