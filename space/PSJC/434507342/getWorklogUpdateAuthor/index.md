# getWorklogUpdateAuthor

## Description

Returns the author who last updated the worklog.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getWorklogUpdateAuthor(issue, worklog) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | String | Yes | The issue key. |
| worklog | Number | Yes | Id of the selected worklog. |

## Return Type

**String**

## Example

```javascript
print(getWorklogUpdateAuthor(key, 11201))
```

Prints the author who last updated the worklog with id = 11201, on the current issue.

## See also