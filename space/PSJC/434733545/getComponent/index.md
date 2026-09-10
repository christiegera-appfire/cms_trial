# getComponent

[Unmapped macro: button-handy — no content to fall back on]

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getComponent(projectKey, componentName) | **Package** | adm |
| **Alias** | admGetProjectComponent(projectKey, componentName) //deprecated | **Pkg Usage** | getComponent(projectKey, componentName) |

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | getComponent(componentId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | getComponent(componentId) |

## Description

Returns a JComponent for either a component id or a specified project and component name.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| projectKey | String | No | Project key. |
| componentName | String | No | Name of the component. |
| componentId | Integer | No | Component id. |

## Return Type

[**JComponent**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Example 1

```javascript
getComponent("TEST", "sil");
```

Returns a JComponent structure for the "sil" component in the "TEST" project.

## Example 2

```text
getComponent(10000);
```

Returns a JComponent structure for the **10000** component ID.

## See also

[Unmapped macro: fc909b09-b512-4c31-a844-dd855b0e6aae/db1c8759-c7e5-4e80-9022-d19e47b0e2b0/static/macro — no content to fall back on]