# admArchiveIssues

## Description

Archives a issue or a list of issues (maximum 1000, that’s a limitation that Atlassian set).

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admArchiveIssues(issueKeysOrIds) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | archiveIssues(issueKeysOrIds) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issueKeysOrIds | string [] | Yes | The issue key/s or id/s that will be archived |

## Return Type

**Number**

The number of archived issues

## Example

```javascript
return admArchiveIssues({"TEST-1", "TEST-2"});
```

Returns: 2

## See also