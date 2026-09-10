# admGetDashboardsByOwner

## Description

Returns all dashboards for the specified owner.
Filtering is provided on Jira side

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetDashboardsByOwner(userId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | dashboardsByOwner(userId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| userId | string | Yes | The owner account id |

## Return Type

[**JDashboard []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

All the dashboard which have as a owner the specified userId

## See also