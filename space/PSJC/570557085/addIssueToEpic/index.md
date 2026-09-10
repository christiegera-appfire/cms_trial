# addIssueToEpic

## Description

Associates an issue or task with a specific epic, indicating that the issue is part of a larger project goal or initiative represented by the epic.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | addIssueToEpic(issue\_key, epicId) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue\_key | String | Yes | the issue key |
| epicId | Integer | Yes | The epic id |

## Return Type

**Boolean**

True of operation succeeded

## Example

```javascript
return addIssueToEpic("TEST-5", "TEST-123");
```

Returns true if successful, false if otherwise.

## See also