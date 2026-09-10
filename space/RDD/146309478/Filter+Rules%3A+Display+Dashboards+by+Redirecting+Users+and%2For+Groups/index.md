# Filter Rules: Display Dashboards by Redirecting Users and/or Groups

## Overview

Confluence is the hub for all the information in your teams, the single source of truth that your colleagues rely on. It’s the perfect location to create dynamic dashboards with live information from Jira projects, incidents from Opsgenie or custom charts with insights from Jira Service Management service desks.

And this power comes with the great responsibility of providing Confluence users the right dashboard when they access to it. Dashboard Hub for Confluence provides the ability to **define rules to filter which dashboard is shown** to either all users or a specific set of users and/or groups. These rules allow you to:

- **Replace the Confluence native dashboard** with a custom one defined on a wiki page or by one of the dashboards created in Dashboard Hub.
- **Display unique dashboards** for each team by defining filter rules for selected users and groups

And still have all the features of Dashboard Hub: +70 gadgets, custom charts, 10 integrations, dashboard restrictions, slideshow, external share…

![Dashboard Hub Filter Rules Display Dashboards by Redirecting Users andor Groups dashboard preview](/cms_trial/assets/5f80e6b2-51ef-4c43-b403-387bddd587de.jpg)

## Create a dashboard

You can:

- Use a regular wiki page to create your dashboard, using macros to insert gadgets and metrics (with the [Dashboard macro for Confluence](/cms_trial/space/RDD/146309561/Dashboard+macro+for+Confluence/), for example). With this option, you can use Confluence native mechanisms to create a specific layout and leverage the existing Confluence macros.
- Create a dashboard with the main functionality of Dashboard Hub (refer to [Get started](/cms_trial/space/RDD/146309347/Get+started/) for further information).

## Admin configuration

Only Confluence admins can create filter rules. Go to the Dashboard Hub configuration, in the global admin section: Go to **Browse** > **Confluence Admin** > **Dashboard Hub > Dashboard Filter Rules**

### Filter priority

The priority is used to determine the order the filter rules should be processed. The priority is only important if you define more than one filter rule. A lower value means a higher priority i.e., the rule with priority 1 has a higher priority than the rule with priority 2.

![Dashboard Hub Filter Rules Display Dashboards by Redirecting Users andor Groups filter configuration](/cms_trial/assets/1766bcc9-2846-44d6-b9ec-b3d1d0721fbd.png)

When you click + Add Rule you’ll access the rule creation dialog

![Dashboard Hub Filter Rules Display Dashboards by Redirecting Users andor Groups filter configuration](/cms_trial/assets/3ac07c45-5d6e-4fc2-aa16-e5cb209f578f.png)

### Show content from

Which content to show as your dashboard. Choose one of the following options:

|  |  |
| --- | --- |
| **Global Dashboard** | Select a dashboard to be the default global dashboard of Confluence. |
| **Site Homepage** | Either the global site homepage configured in the general configuration of Confluence or the personal site homepage, if the user has configured one in his user settings. Note: The user's personal settings will override the global setting. Use this option to allow personal dashboards. |
| **Wiki Page** | Any wiki page within your Confluence. Use this option to display a specific wiki page as dashboard instead of the default dashboard. |

### Show content as

Only available for Server and Data Center users, due to Confluence Cloud API limitations

Enable **Show content always as dashboard** to render wiki pages as dashboards as well, without edit buttons, comments, etc. Thus, if you enable this option, when you display a wiki page as a dashboard, you won’t see the interaction buttons (e.g., edit, star, watch, restrictions, share…) nor comments, removing all unnecessary elements to see a clean dashboard.

![Dashboard Hub Filter Rules Display Dashboards by Redirecting Users andor Groups dashboard preview](/cms_trial/assets/5e3b41cf-14b1-4104-b342-4244c3492ad5.jpg)

### Show content to

You can restrict **filter rules to all users or a specific set of users and/or groups**. Choose **All Users** if you want the rule to apply to all users, or choose to **Restrict to** and define the users and/or groups to which the rule should be applied.

![Dashboard Hub Filter Rules Display Dashboards by Redirecting Users andor Groups dashboard filter rules configuration](/cms_trial/assets/f9c34826-18d0-4e7d-acb7-edc0fc6b053a.png)

**Note:** A filter rule will be applied as long as the user meets at least one of the restrictions. If no filter rule matches or no filter rules are defined, the default dashboard of Confluence will be displayed.

## Differences of the *Data Center vs Cloud* edition

- In **Cloud**, the Wiki Homepage has to be configured manually by the admin, since it cannot be automatically retrieved
- “Show Content As” is **only available for Server and Data Center** users, due to Confluence Cloud API limitations
- In **Cloud**, the redirection is not as smooth as it is in Server and Data Center, due to Confluence Cloud API limitations

## See also