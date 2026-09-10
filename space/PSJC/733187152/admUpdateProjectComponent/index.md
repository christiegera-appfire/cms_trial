# admUpdateProjectComponent

## Description

Updates a project component.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUpdateProjectComponent(componentStructure) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | updateComponent(componentStructure) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| componentStructure | JComponent | Yes | Structure containing the component data to be updated. Component id is mandatory. The **componentStructure** parameter should have the **JComponent** type described [here](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/). |

## Return Type

**None**

Return value has no meaning.

## Example

```javascript
JComponent comp = getComponent("AP", "compName");
comp.name = "compName - updated";
comp.description = "compDesc";
comp.lead = "johnDoe";
comp.defaultAssignee = 2;
admUpdateProjectComponent(comp);
```

## See also