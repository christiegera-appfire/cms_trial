# getWorklogUpdatedDate

## Description

Returns the last date when the worklog was updated.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getWorklogUpdatedDate(issue, worklog) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | String | Yes | The issue key. |
| worklog | Number | Yes | Id of the selected worklog. |

## Return Type

**Date**

## Example

```javascript
print(getWorklogUpdatedDate(key, 11201))
```

Prints the updated date of the worklog with id = 11201, on the current issue.

## See also