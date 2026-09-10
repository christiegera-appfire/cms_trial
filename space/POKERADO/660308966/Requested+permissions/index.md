# Requested permissions

When you install Planning Poker, Azure DevOps asks you to approve several permission scopes.

Planning Poker requests only the permissions it needs to provide its features. The table below explains why each permission is required and how the app uses it.

## Permission summary

| **Permission** | **Purpose** | **Details** |
| --- | --- | --- |
| **vso.work** | Read work items | Reads work items and related information, including user stories, tasks, bugs, and epics, so they can be displayed during estimation sessions. |
| **vso.work\_write** | Save estimates | Updates work items by writing estimation values back to Azure DevOps after an estimation session. |
| **vso.graph** | Verify administrator membership | Uses the Azure DevOps Graph API to determine whether a user belongs to the **Organization Administrators** group. |
| **vso.features** | Display the extension | Determines whether Planning Poker should appear in supported Azure DevOps locations, such as Boards and Work Item details. |
| **vso.features\_write** | Manage extension visibility | Controls where Planning Poker appears within supported Azure DevOps extension points when supported by the platform. |
| **vso.memberentitlementmanagement** | Manage licensed users | Retrieves user and license information so administrators can manage which users are authorized to use the extension. |
| **vso.identity** | Look up specific users | Retrieves information about individual users when needed, reducing the need to retrieve information for every user in the organization. |

For more information about Azure DevOps permission scopes, see the Microsoft documentation: <https://learn.microsoft.com/en-us/azure/devops/extend/develop/manifest?view=azure-devops#scopes>