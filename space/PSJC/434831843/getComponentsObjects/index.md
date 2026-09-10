# getComponentsObjects

## Description

Returns all the project components as an array of JComponent structures.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getComponentsObjects(projectKey) | **Package** |  |
| **Alias** |  | **Pkg Usage** |  |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | Yes | Project key. |

## Return Type

[**JComponent []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example

```javascript
JComponent [] compObjs = getComponentsObjects("TP"); //projectKey as parameter
for(JComponent comp in comObjs) {
    runnerLog(comp.name);
    runnerLog(comp.lead);
}
```

Returns an array of JComponent structures containing all the project components.

## See also