# getFieldChanges

## Description

Returns a list of tuples containing user||field|oldVal|newVal for the selected field from the selected issue's history.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getFieldChanges(key, history\_field\_name) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue key | String | Yes | Key of the selected issue. |
| field name | String | Yes | Name of the selected field. |

## Return Type

[**JFieldChanges []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

The return value is an array of JFieldChange. The strings come in pairs. The first value is a date representing the time when the value was modified and the second value is the content of the requested field at that date.

## Examples

### Example 1

```javascript
JFieldChange[] changes  = getFieldChanges("TEST-10", "My Text Field");
return changes;
```

Result:  
admin|2017-05-23 13:28:05|My Text Field||test|admin|2017-05-23 13:28:09|My Text Field|test|lalaa

### Example 2

Let's say we want to get the latest change for the given field:

```javascript
JFieldChange[] changes  = getFieldChanges("TEST -10", "customfield _10200");
JFieldChange latestChange = changes[0];
date newest = latestChange.changeDate;
for (JFieldChange change in changes) {
    if (change.changeDate> newest ) {
        latestChange = change;
    }
}
return latestChange;
```

Done. Program returned: admin|2017-05-23 13:28:09|Text Field|aaaaa|nnnnn

1. Besides the labels /ids of the custom fields, the name of the standard Jira fields (summary, assignee etc.) can be used as parameters.
2. If it returns an empty array, you must get the last value of the field from the issue.
3. The second parameter is the field name as it appears in history.

## See also