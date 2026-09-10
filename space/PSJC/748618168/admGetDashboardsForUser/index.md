# admGetDashboardsForUser

## Description

Returns all dashboards accessible by the the specified user.
User does not necessarily is the owner!. Filtering is provided on Jira side

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetDashboardsForUser(userId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | dashboardsForUser(userId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| userId | string | Yes | The account id |

## Return Type

[**JDashboard []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

All the dashboard accessible by the specified userId

## See also