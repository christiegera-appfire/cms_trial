# getWorklogsForIssues

## Description

Returns an array with the worklogs for the specified list of issues, and if exists for given user also.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getWorklogsForIssues(startDate, endDate, issues[ , user] ) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| startDate | Date | Yes | Start date of the interval where the startDate of the worklog can be. |
| endDate | Date | Yes | End date of the interval where the startDate of the worklog can be. |
| issues | String[] | Yes | List of the issues the filter can be made from. |
| user | String | No | User from whom can be made the filter. |

## Return Type

[**JWorklog []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

### Example 2

```javascript
return getWorklogsForIssues("2014 -11 -26", "2014 -12 -03", {"DEMO -6","LFTP -1","TSTAG -4"});
```

Returns an array containing the JWorklog list structures of the issues that have the startDate between start date = "2014-11-26"(inclusive) and end date = "2014-12-03" (exclusive). The filter of the worklogs is made only by the issues.

## See also