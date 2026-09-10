# issueInStartedSprint

## Description

Determines if a specific issue is associated with a sprint that is currently in progress, helping to identify tasks relevant to ongoing work.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | issueInStartedSprint(issueKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue key | String | Yes | The issue key |

## Return Type

**Boolean**

## Example

```javascript
boolean result = issueInStartedSprint("AGILE-3");
```

1. If there is no issue with that issue key, an exception will be raised.
2. The user must have enough permissions to perform this action

## See also