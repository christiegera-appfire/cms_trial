# getWorklogIds

## Description

Returns an array with the ids of the worklogs for the specified date and issue.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getWorklogIds(startDate, issueKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| startDate | Date | Yes | Start working date. |
| issueKey | String | Yes | Key of the selected issue. |

## Return Type

**Number []**

## Example

```javascript
getWorklogIds("2012-05-23 16:01:00",key)
```

Returns an array containing the ids of all the worklogs of the current issue who have the start date = "2012-05-23 16:01:00".

## See also