# getWorklogAuthor

## Description

Returns the author of a worklog.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getWorklogAuthor(issue, worklog) | **Package** |  |
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
print(getWorklogAuthor(key, 11201))
```

Prints author's username of the worklog with id = 11201, on the current issue.

## See also