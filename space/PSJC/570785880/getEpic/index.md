# getEpic

## Description

Retrieves information about a specific epic, which is a larger work item that often encompasses multiple user stories or tasks, helping to organize and track complex projects.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getEpic(id) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| id | String | Yes | The epic id or key |

## Return Type

[**JEpic**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

The epic structure

## Example

```javascript
JEpic epic = getEpic("TEST-1");
runnerLog("Id: " + epic.id);
runnerLog("Name: " + epic.name);
runnerLog("Summary: " + epic.summary);
```

## See also