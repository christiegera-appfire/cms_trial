# admUpdateGadgetInDashboard

## Description

Updates a gadget in the specified dashboard. You must fill in the row, column, color,...

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admUpdateGadgetInDashboard(dashboardId, gadget) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | updateGadgetInDashboard(dashboardId, gadget) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| dashboardId | string | Yes | The dashboard ID |
| gadget | JGadget | Yes | The gadget |

## Return Type

[**JGadget**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

The updated gadget instance, null if update failed

## See also