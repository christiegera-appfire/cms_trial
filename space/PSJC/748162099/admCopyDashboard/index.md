# admCopyDashboard

## Description

Copies the the dashboard. The name becomes 'Copy of <original name>'. Optionally changes the owner for the copy.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admCopyDashboard(dashboardId[, newOwnerId]) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | copyDashboard(dashboardId[, newOwnerId]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| dashboardId | string | Yes | The dashboard to be copied |

### Or

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| dashboardId | string | Yes | The dashboard to be copied |
| newOwnerId | string | Yes | The owner of the copy |

## Return Type

[**JDashboard**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

The dashboard, copied, optionally with some other user as owner

## See also