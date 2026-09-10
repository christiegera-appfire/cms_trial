# admGetPrioritySchemeObject

## Description

Returns the priority scheme (as a JPriorityScheme structure) for the given project key.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetPrioritySchemeObject(projectKey) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | getPrioritySchemeObject(projectKey) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | string | Yes | The project key. |

## Return Type

[**JPriorityScheme**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns the priority scheme name.

## Examples

### Example 1

Returns the priority scheme (full object) for project "TEST"

```javascript
return admGetPrioritySchemeObject("TEST");
```

prioSchemeObjForProject = 10143|New priority scheme|new desc updated at 2024-08-06 13:47:05|Highest|Medium|Low|DEMO|ITSD|TEST

### Example 2

Prints the priority scheme id and description for project "TEST"

```javascript
JPriorityScheme prioSchemeObjForProject = admGetPrioritySchemeObject("TEST");
runnerLog("The description of priority with id " + prioSchemeObjForProject.id + " is " + prioSchemeObjForProject.description);
```

The description of priority with id 10143 is new desc updated at 2024-08-06 13:47:05

## See also