# admGetFavouriteDashboards

## Description

Returns all dashboards favorited by the the specified user.
User does not necessarily is the owner!. Filtering is provided on Jira side

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | admGetFavouriteDashboards(userId) | **Package** | adm |
| **Alias** |  | **Pkg Usage** | favouriteDashboards(userId) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| userId | string | Yes | The account id |

## Return Type

[**JDashboard []**](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

All the dashboard starred by the specified user

## See also