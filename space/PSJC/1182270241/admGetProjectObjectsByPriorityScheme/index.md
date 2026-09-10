# admGetProjectObjectsByPriorityScheme

## Description

Returns a list of projects (as JProject structures) by the given priority scheme name.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetProjectObjectsByPriorityScheme(prioritySchemeName) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | getProjectObjectsByPriorityScheme(prioritySchemeName) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| prioritySchemeName | string | Yes | The priority scheme name. |

## Return Type

[**JProject []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

Returns a list of projects.

## Examples

### Example 1

Returns projects from the priority scheme "New priority scheme"

```javascript
return admGetProjectObjectsByPriorityScheme("New priority scheme");
```

10002|DEMO|DEMOPRJ||service\_desk|||false||10001|ITSD|IT service desk||service\_desk|||false||10000|TEST|TEST||software|||false|

### Example 2

Prints the ids and names of the projects from the priority scheme "New priority scheme"

```javascript
JProject[] prjObjects = admGetProjectObjectsByPriorityScheme("New priority scheme");
for (JProject proj in prjObjects) {
    runnerLog("Name for project with id " + proj.id + " is " + proj.name);
}
```

Name for project with id 10002 is DEMOPRJ
Name for project with id 10001 is IT service desk
Name for project with id 10000 is TEST

## See also