# OKR module permissions

## Overview

The OKR module permissions are independent of BigPicture roles.

Permissions control what actions you or your teams can perform. If you do not have permission to carry out a certain action, it will be visible to you, but you will not be able to access it.

## Default permissions

By default, every user has full access to the OKR module (the default roles and settings can be changed on the [OKR module advanced permissions](/cms_trial/space/SPM/1918767695/OKR+module+advanced+permissions/) page).

## Change permissions

To change permissions to other users, you need to be either:

|  |  |
| --- | --- |
| **Jira Administrator** - Jira Admins can allow/restrict specific users from viewing and modifying OKRs by granting/revoking their access.  Jira Admins can also grant selected users or groups all the OKR permissions on the Jira level.  This allows selected users/groups to be independent of the in-module setup (basic and advanced) and enables organizations to address permission work items or other challenges outside the module's permissions configuration. | 1. Go to **Jira admin settings** > **System** > **Security** > **Global permissions**. 2. Find **View and Modify OKRs** permissions. 3. **Delete** the users/groups to remove that permission from them.  1. Go to **Jira admin settings** > **System** > **Security** > **Global permissions**. 2. Find the **Administer data of OKRs for Jira** permission. 3. Add users or groups who need unrestricted access to manage all aspects of the module, including:  - Accessing the module, - Creating and managing all data (OKRs, teams, labels, periods, etc.), - Adjusting settings, - Setting up permissions and OKR restrictions.   Alternatively:   1. Scroll to the bottom of the page to the **Grant Permission** section. 2. Select the **View and Modify OKRs** or **Administer data of OKRs for Jira** from the dropdown. 3. Add groups.  Gran Permissions section in Jira. |
| **In-module Adminstrator** (Box user granted “Full Access” permission/ Box user granted the “Change company settings” permission)- With these permissions, box users can control who can view and manage OKRs and the OKR module settings, and to what extent. | Individual OKR module permissions can be managed on the **Settings** > **Permissions** page in the OKR module. |

![Screenshot of the Permissions page in the OKR module.](/cms_trial/assets/a184850b-b0be-4684-916d-250f16f45c04.png)

## OKR basic permissions

OKR permissions are **global**—any changes you introduce also change the organization's settings.

OKR permissions are perfect for companies that want most of the users to have full access but need to restrict module setup or editing actions for some. Below, you can find a detailed description of all available options.

| **OKR module permissions** |
| --- |
| **Full Access** | This is the default permission setting, where everyone can perform all actions in the app, including changing all global settings on the **Settings** page, without any restrictions. |
| **Global settings control** | Selecting this option lets you control who can configure the app. It is ideal when a specific person or group is responsible for managing the OKR process, allowing others to focus on the OKRs without worrying about setup.  Users with this permission can edit all settings and rearrange OKRs. Users without it can view the settings tab but cannot make any changes. |
| **Editing control** | This option lets users view OKRs without limiting access to settings, but it prevents them from editing the OKRs.  Users without this permission will be able to just view the OKRs and add new ones. |
| **Global settings & editing control** | With this option, you can combine the two settings types.  If a person or group is not added to the **Global settings permissions** or **Editing permissions** group, they will be a viewer, meaning they can only view OKRs but cannot edit, create, or set up anything. If they are added to one of these lists, they will receive the corresponding permissions:   - **Global settings permissions** - All users with this permission will be able to edit all settings and rearrange OKRs. Users without this permission will be able to see the settings tab, but they will not be able to change anything. - **Editing permissions** - All users with this permission will be able to edit all OKRs. Users without this permission will be able to just view the OKRs and add new ones. |
| **Advanced setup** | This option lets you define permissions for specific users or groups, create custom roles, and use OKR ownership-based roles to ensure alignment with the OKR process.  Visit the <https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/1721337099/OKR+module+advanced+permissions?search_id=0222c41c-ffbc-40e6-915e-7eb533b01637&additional_analytics=queryHash---7ea87ef593d8bb0aeeb8d723221bc6ddf9803781dcfe066a4b25a620f35ffd1b> to learn more. |

## Individual OKRs restrictions

Use the OKR restrictionto hide from view or limit edit access to specific Objectives and Key Results. By restricting individual OKRs, you can conceal them from unprivileged users.

Visit the [OKR restrictions (per OKR)](/cms_trial/space/SPM/1918864985/OKR+restrictions+(per+OKR)/) page to learn more.

## Permissions precedence

- Only users who were explicitly set on Restricted OKRs can see and edit that OKR. The **Administer data of OKRs for Jira** global permission or in-module admin permission **does not grant** the ability to view or edit Restricted OKRs.
- Contextual permissions for Owners, Managers, and Collaborators do not override OKR restrictions.
- The **Administer data of OKRs for Jira** global permission overrides all in-module permissions, granting full module access (except for Restricted OKRs).
- If a user only has the **View and modify OKRs** global permission without any Restrictions configured, their available actions will depend on their in-module permissions.
- To use the OKR module, a user needs either the **View and modify OKRs** or the **Administer data of OKRs for Jira** global permission. Without either of these permissions, they cannot access the module.