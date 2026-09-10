# lastIssueChanges

## Description

Returns the last changes details for all the fields touched by user (array of [Predefined structure types](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)) from the selected issue's history.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | lastIssueChanges(issueKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue key | String | Yes | Key of the selected issue. |

## Return Type

[**JFieldChange []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

The return value is an array of structures documenting what the user has changed on the issue.

## Example

```javascript
JFieldChange [] changes = lastIssueChanges("TEST-10");
for(number i = 0; i < size(changes); i++) {
    runnerLog("U:" + changes[i].user + " Field:" + changes[i].field + " Val:" + changes[i].oldVal + " -> " + changes[i].newVal);
}
```

## See also