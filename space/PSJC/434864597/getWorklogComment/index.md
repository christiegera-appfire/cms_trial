# getWorklogComment

## Description

Returns the comment associated with the worklog.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getWorklogComment(issue, worklog) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | String | Yes | Key of the selected issue. |
| worklog | Number | Yes | Id of the selected worklog. |

## Return Type

**String**

## Example

```javascript
print(getWorklogComment(key, 11201))
```

Prints the comment of the worklog with id = 11201, on the current issue.

## See also