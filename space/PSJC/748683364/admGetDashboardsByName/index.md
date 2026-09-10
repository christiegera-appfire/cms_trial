# admGetDashboardsByName

## Description

Returns all dashboards the current user has access to containing that name.
Filtering is provided on Jira side

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetDashboardsByName(name) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | dashboardsByName(name) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | Yes | The value searched, as a string |

## Return Type

[**JDashboard []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

All the dashboard accessible to the user containing that name

## See also