# removeIssuesFromEpic

## Description

Dissociates multiple issues from a specific epic, indicating that these issues are no longer part of the epic's scope or objectives.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | removeIssuesFromEpic(array\_of\_issue\_keys) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| array\_of\_issue\_keys | String [] | Yes | The board id |

## Return Type

**Boolean**

True of operation succeeded

## Example

```javascript
string [] issues = "TEST-1|TEST-2|TEST-3";/nreturn removeIssuesFromEpic(issues);
```

Returns true if successful, false if otherwise.

## See also