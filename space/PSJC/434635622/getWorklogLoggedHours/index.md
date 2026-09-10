# getWorklogLoggedHours

## Description

Returns the logged hours for a worklog.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getWorklogLoggedHours(issue, worklog) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | String | Yes | The issue key. |
| worklog | Number | Yes | Id of the selected worklog. |

## Return Type

**Interval**

## Example

```javascript
print(getWorklogLoggedHours(key, 11201))
```

Prints the logged hours for the worklog with id = 11201, on the current issue.

## See also