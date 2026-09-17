# getEventIssueFieldChange

## Description

Retrieves a structure containing information about the changes made for a specific field on the specific event.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getEventIssueFieldChange(field) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| field | String | Yes | Field name. |

## Return Type

[**JFieldChange**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JFieldChange [] changes = getEventIssueFieldChange("description");
logPrint("ERROR", "Event Changes: " + changes);
```

## See also