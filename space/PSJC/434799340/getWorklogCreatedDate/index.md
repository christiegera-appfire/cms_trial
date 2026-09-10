# getWorklogCreatedDate

## Description

Returns the created date of a worklog.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getWorklogCreatedDate(worklog) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| worklog | Number | Yes | Id of the selected worklog. |

## Return Type

**Date**

## Example

```javascript
print(getWorklogCreatedDate(key, 11201))
```

Prints the created date of the worklog with id = 11201, on the current issue.

## See also