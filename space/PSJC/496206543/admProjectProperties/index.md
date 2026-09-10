# admProjectProperties

## Description

Returns the project properties.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admProjectProperties(pkey) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | projectProps(pkey) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| pkey | String | Yes | Project key. |

## Return Type

[**JProject**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

The properties of the project.

## Example

```javascript
JProject prj = admProjectProperties("TP");
runnerLog("Project id is:" + prj["id"]);
runnerLog("Project key is:"  + prj["key"]);
runnerLog("Project name is:"  + prj["name"]);
runnerLog("Project description is:"  + prj["description"]);
runnerLog("Project lead is:"  + prj["lead"]);
runnerLog("Project url is:"  + prj["url"]);
runnerLog("Project unassigned by default:"  + prj["unassignedByDefault"]);
runnerLog("Project category is:" + prj["category"]);
runnerLog("Project type is:" + prj["projecttype"]);
```

## See also