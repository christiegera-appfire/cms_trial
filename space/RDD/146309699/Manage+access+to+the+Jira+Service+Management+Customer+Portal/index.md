# Manage access to the Jira Service Management Customer Portal

## Overview

When an organization provides premium support services through Jira Service Management (JSM), customers need a mechanism to access the reports so they can see if SLAs are being met or breached, for example. Organizations resort to manual approaches like exporting JSM reports to documents, creating PDFs, and sending these by email (read our success stories about [Unifly](https://appfire.com/resource/business-intelligence-reporting/how-unifly-improved-reporting-efficiency-and-transparency-on-jsm-with-jira-charts-dashboards/) and [Success Solutions](https://appfire.com/resources/resource-library/customer-stories/success-solutions-saves-150-hours-jsm)).

Dashboard Hub lets your administrator share your JSM portal's specific reporting dashboards with customers and organizations.

## Global settings - global access restrictions

Go to **Admin configuration** > **Dashboard Hub** > **Global Settings**. In the *Global Access Restriction* section. Turn on the toggle for **Restrict Access in the Customer Portal**.

![The Restrict Access in the Customer Portal options in Dashboard Hub Global Settings.](/cms_trial/assets/3d5f630c-20e7-441a-97e6-a016a15421ad.png)

Customers and organizations can be added to view dashboards through the JSM Customer Portal. Customer portal users can’t be granted Edit permissions. In the [next section](/cms_trial/space/RDD/146309699/Manage+access+to+the+Jira+Service+Management+Customer+Portal/), we’ll explain how to grant access to dashboards to users of the JSM Customer Portal.

### Issue Link Policy

You can control how links behave in the dashboards shared through the JSM Customer Portal:

- **Redirected to the issues in Jira:** When a user clicks a link or chart section, the user is redirected to the list of issues in Jira.

Only users with access to the Jira instance will be able to see this list. If the user doesn’t have the right permissions in Jira, the list won’t be displayed.

- **Users are redirected to the list of requests in their service desk:** When a user clicks a link or chart section, they are redirected to the list of requests they have raised in the Customer Portal.
- **Not presented with the option to click through issue keys, charts, and graphs**: Users cannot click links or chart sections.

## Permissions for customers and organizations at the dashboard level

Customers and organizations can be granted access to view dashboards. Customers and organizations can be selected in the Customer Portal section of the dashboard settings.

You can create a single dashboard for all your organizations (for example, to showcase your public roadmap or work in progress) and use **Allow any organization**.

![The Allow any organization option selected in the Customer Portal panel in dashboard settings.](/cms_trial/assets/97e9ed2b-6169-40b8-9336-84bbd975a86f.png)

Jira users won’t appear here, just users of your Customer Portal and organizations. Select the ones you’d like to provide access to.

![The organization and user selection list for the customer portal.](/cms_trial/assets/4b5978e4-a8b2-4efb-bb4d-495a939c3426.jpg)

## Content filtering of shared dashboards

If selected, this filter limits the dashboard's content to the viewer's specific organization. Even if the viewer has access to this dashboard, the content displayed will be limited to issues/tickets belonging to their organization. In the screenshot above, you can see Maria’s organization is Appfire, so Maria will see all the issues where she is the reporter and all the issues with Appfire as an organization.

**Security enhancement**: Issues/tickets without an organization won’t be available when filtering content. If an issue has an empty organization field, it won’t be shown.

### Available gadgets

This filterapplies only to data from the local Jira instance (all Jira Service Management gadgets, but also the JQL Custom Charts, Formula Cards, Cycle Time, and Lead Time gadgets); data from other gadgets or external instances won’t be displayed.

If the user sees a gadget with the following message:

> You cannot view the content of this gadget. The person sharing the dashboard has activated the “Content filtering” functionality.  
> Contact the person sharing this dashboard for further information.

It means that the content has been filtered for one of the aforementioned reasons.

## Customer Portal

When the customer accesses to the portal, a new **Dashboard Hub** option appears in the menu.

![The Dashboard Hub option in the user menu of a customer portal.](/cms_trial/assets/8afb73c0-d5f9-47f1-bcf8-ad86424bbede.png)

This option redirects the customer to a window with all the dashboards to which this customer has been granted access.

![Example dashboards available to a customer in the customer portal.](/cms_trial/assets/0ac748f8-9641-4079-9714-ef270660bf68.png)

## See also

- [Manage Feature Management](/cms_trial/space/RDD/2141683713/Manage+Feature+Management/)
- [Manage Datasource Restrictions](/cms_trial/space/RDD/1900118024/Manage+Datasource+Restrictions/)
- [Manage Permissions on Datasources](/cms_trial/space/RDD/1899429890/Manage+permissions+on+datasources/)
- [Manage Restrictions on Datasource Creation](/cms_trial/space/RDD/1798045983/Manage+Restrictions+on+Datasource+Creation/)
- [Dashboard permissions](/cms_trial/space/RDD/146309693/Dashboard+permissions/)
- [Manage Global Access Restrictions](/cms_trial/space/RDD/146309685/Manage+Global+Access+Restrictions/)