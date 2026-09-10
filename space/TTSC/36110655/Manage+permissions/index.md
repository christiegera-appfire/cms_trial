# Manage permissions

Time to SLA permissions control access to app pages, settings, and work item actions. You can grant permissions to Jira groups and individual Jira users.

This page explains how to grant users permission to access Time to SLA menus and the purpose of each permission setting.

Jira administrators have full access to all Time to SLA features, even if they haven’t been explicitly granted permissions. This is due to their global administrative privileges in Jira.

Some Time to SLA features require **more than one permission** to work properly.  
Review the exceptions on this page when a user can open a feature but can't complete an action.

## How to manage user permissions

1. Navigate to **Administration** > **Permissions** in the app.
2. Find the permission you want to change and select **Edit**.
3. In the permission dialog, select one or more Jira groups under **Grant to Groups** and, if needed, individual users under **Grant to Users**.
4. Click **Save**.

Below is a detailed explanation of the different Time to SLA menus and their respective access permissions:

|  |  |
| --- | --- |
| **Get Started** | Grants access to the *Get started* page, which provides an overview of the app’s capabilities and serves as an introduction for new users. |
| **SLAs/Actions** | Access to the SLAs and Actions pages. Users can create and manage SLA configurations and SLA actions. This permission also allows access to the SLA information button on the SLA panel. |
| **Calendars** | Access to [**Calendars**](/cms_trial/space/TTSC/35750012/Create+calendars/) [page](/cms_trial/space/TTSC/35750012/Create+calendars/), including creating and managing calendars used by SLA calculations. |
| **SLA Panel** | Access to the [SLA panel](/cms_trial/space/TTSC/35815658/SLA+panel/)on the Jira work items and to **Administration >** [**SLA Panel**](/cms_trial/space/TTSC/35815658/SLA+panel/)[**settings**](/cms_trial/space/TTSC/35815658/SLA+panel/). |
| **SLA History** | Access to the [*SLA History*](/cms_trial/space/TTSC/35456368/SLA+History+tab/) [tab](/cms_trial/space/TTSC/35456368/SLA+History+tab/) on Jira work items, where users can review recorded SLA events such as start, pause, resume, reset, critical-zone, breach, extension, and stop events. |
| **Customer Portal SLAs** | Access to the **Space settings** > **Apps** > **Time to SLA** on [customer portal settings](/cms_trial/space/TTSC/36209105/Add+SLA+panel+to+the+customer+portal/), where you can configure the visibility of SLAs on the Jira Service Management customer portal. Time to SLA Manage permissions configuration for user access |
| **Permissions** | Grants access to: **Administration** > [**Permissions**](/cms_trial/space/TTSC/36110655/Manage+permissions/) [page](/cms_trial/space/TTSC/36110655/Manage+permissions/), where you can configure who has access to different menus and features in Time to SLA.  **Important: At least one group is required**  When configuring access to the **Permissions** page:   - You must select **at least one Jira group**. - You cannot grant access to only individual users. - Even if you want only one specific user to access the page, you must still assign at least one group.   If no group is selected, the configuration cannot be saved.  Jira administrators will always retain access due to their global administrative privileges. |
| **SLA Recalculation** | Access to the[**Recalculation**](/cms_trial/space/TTSC/35456416/Recalculation/) [page](/cms_trial/space/TTSC/35456416/Recalculation/), where you can run SLA recalculations for work items when necessary.  **Dependency in recalculation**  To properly recalculate and verify SLAs, users need:   - [SLAs page permission](/cms_trial/space/TTSC/36110655/Manage+permissions/) - [SLA panel permission](/cms_trial/space/TTSC/36110655/Manage+permissions/) - Recalculation permission |
| **Administration** | Grants access to the following sections under **Administration**:   - [General](/cms_trial/space/TTSC/37290034/Administration/) - [Advanced](/cms_trial/space/TTSC/37290034/Administration/) - [SLA Calculation Scope](/cms_trial/space/TTSC/48529969/SLA+calculation+scope/)   This permission does not automatically grant access to:   - [API token](/cms_trial/space/TTSC/36110655/Manage+permissions/) - [Import / Export](/cms_trial/space/TTSC/36110655/Manage+permissions/) - [Audit logs](/cms_trial/space/TTSC/36110655/Manage+permissions/)   These are controlled by separate permissions. |
| **SLA Reports** | Access to the[**Reports**](/cms_trial/space/TTSC/36012079/Reports/) [page](/cms_trial/space/TTSC/36012079/Reports/), where you can generate reports.  **Dependency in reports**  To see SLA data in reports, users must have:   - [SLAs page permission](/cms_trial/space/TTSC/36110655/Manage+permissions/) - Reports permission   Both are required. Without SLA access, reports will open, but SLA data will not be visible. |
| **Audit Logs** | Access to the **Administration** > [**Audit logs**](/cms_trial/space/TTSC/36110718/Audit+logs/), where you can track changes made to SLA configurations, permissions, and other settings. |
| **API Token** | Access to the **Administration** > [**API token**](/cms_trial/space/TTSC/36209134/REST+APIs/), where users can create and manage Time to SLA API tokens. |
| **Import Export** | Access to the **Administration** > [**Export/Import**](/cms_trial/space/TTSC/36110672/Import%2FExport/) screen, where you can export or import SLAs and calendars. |
| **SLA work item operations - Reset SLA** | Access to the [Reset SLA operation](/cms_trial/space/TTSC/36799257/TTS+work+item+actions/) in **Time to SLA Issue Actions**. |
| **SLA work item operations - Undo reset SLA** | Access to the [Undo Reset SLA operation](/cms_trial/space/TTSC/36799257/TTS+work+item+actions/) in **Time to SLA Issue Actions**. |
| **SLA work item operations - Where is my SLA?** | Access to the [Where Is My SLA? operation](/cms_trial/space/TTSC/36799257/TTS+work+item+actions/) in **Time to SLA Issue Actions**. |
| **SLA work item operations - Recalculate SLA** | Access to the [Recalculate SLA operation](/cms_trial/space/TTSC/36799257/TTS+work+item+actions/) in **Time to SLA Issue Actions**. |
| **SLA work items operations** - **Mute SLA notifications** | Access to the [Mute SLA operation](/cms_trial/space/TTSC/36799257/TTS+work+item+actions/) in **Time to SLA Issue Actions**. |
| **Contract Extension** | Permission to perform a [SLA contract extension](/cms_trial/space/TTSC/2001470255/SLA+contract+extension/). The user also needs **SLA Panel** access to use the extension control from the panel. |
| **SLA Fields** | Only Jira admins can create SLA fields or view the configuration page (**Administration** > [**SLA fields**](/cms_trial/space/TTSC/2875654192/Custom+fields/)). This matches Jira's standard permission logic for custom fields. |

Check out this cheatsheet to learn more about some types of Jira groups and what they mean:

| **Group name** | **Definition** |
| --- | --- |
| jira-admins | A Jira administrator is a user with the Administer Jira global permission. |
| jira-servicemanagement-users | Users in your service space are people who work on or send requests. |
| site-admins | Site admins administer the users and groups for the site's products. |
| system-administrators | Those with the Jira System Administrator permission can perform all administration functions in Jira, while those with only the Jira Administrator permission cannot perform functions that could affect the app environment or network. |

For further information, [refer to Atlassian’s documentation](https://community.atlassian.com/t5/Jira-articles/Default-Jira-Global-Permissions/ba-p/1623381).

If a user receives a 403 response, first confirm that they have the Time to SLA permission required for the page or action. Jira administrators retain access regardless of Time to SLA permission assignments. If the user has the required permissions and the error continues, contact Support.