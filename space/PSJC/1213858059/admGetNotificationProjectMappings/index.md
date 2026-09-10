# admGetNotificationProjectMappings

## Description

Retrieves the mappings between notification schemes and projects.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetNotificationProjectMappings([notificationSchemeId, projectIds]) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | getNotificationProjectMappings([notificationSchemeId, projectIds]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| notificationSchemeId | integer [] | No | The ids of the notification schemes to be filtered. |
| projectIds | integer [] | No | The ids of the projects to be filtered. |

## Return Type

[**JIssueNotificationSchemeProjectMapping**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JIssueNotificationSchemeProjectMapping[] mappings = admGetNotificationProjectMappings();
int indexCC = 1;
for(JIssueNotificationSchemeProjectMapping mapping in mappings) {
    runnerLog("---mapping " + indexCC + "---");   
    runnerLog("notificationSchemeId = " + mapping.notificationSchemeId);
    runnerLog("projectId = " + mapping.projectId);
    indexCC++;
}
runnerLog("--------------");
```

## See also