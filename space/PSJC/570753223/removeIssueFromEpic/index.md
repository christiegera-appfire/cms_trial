# removeIssueFromEpic

## Description

Removes the association between an issue and an epic, indicating that the issue is no longer considered part of the larger project goal represented by the epic.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | removeIssueFromEpic(issue\_key) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue\_key | String | Yes | the issue key |

## Return Type

**Boolean**

True of operation succeeded

## Example

```javascript
return removeIssueFromEpic("TEST-123");
```

Returns true if successful, false if otherwise.

## See also