# Monitor Comala Document Management Cloud Workflows with Dashboard Hub Custom Reports

## Overview

This document explains how you can integrate Dashboard Hub and Comala Document Management (CDM) cloud to view key metrics of your document workflows in Confluence.

This document is for the Comala Document Management **Cloud** version.

For the Comala Document Management **Data Center** version, see [Document Workflow Custom Charts](/cms_trial/space/RDD/874905671/Document+Workflow+Custom+Charts/).

## Custom Reports in Dashboard Hub

Dashboard Hub is a reporting app for creating centralized dashboards with data from various sources, including Confluence. Our Custom Reports gadget connects through REST API and uses the search endpoint to filter pages by CQL(Confluence Query Language), expanding on Comala Document Management data to build a usable, visual report.

For more details, see:

[Get started with Custom Reports](/cms_trial/space/RDD/1528825149/Get+started+with+Custom+Reports/)

## Custom Reports templates

Use our curated and maintained catalog of [Custom Reports templates](https://appfire.atlassian.net/wiki/spaces/RDD/folder/1992261872?atlOrigin=eyJpIjoiODg3YmQwOGVlZjQ2NDE4MjkyMTc3Yjk0MWI3MjJjOTQiLCJwIjoiYyJ9). This catalog offers ready-to-use, easy-to-connect examples. Find links to the Comala Document Management templates here:

- [Comala Document Management status report](/cms_trial/space/RDD/1955037214/Comala+Document+Management+status+report/)
- [Comala Document Management workflow and state chart](/cms_trial/space/RDD/1955102741/Comala+Document+Management+workflow+and+state+chart/)
- [Comala Document Management Page Activity](/cms_trial/space/RDD/1955954748/Comala+Document+Management+Page+Activity/)

## Comala Document Management (CDM)

Comala Document Management provides workflow automation for pages and blog posts in Confluence spaces. Comala Document Management also offers in-app reporting tools, including the Document Report for tracking workflow activity across pages in a space and the Document Activity report for an individual page.

You can find Comala Document Management on the Atlassian Marketplace here: <https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview>

## Use cases

### Document stats report

This chart provides a visual breakdown of pages by Workflow State, offering a quick overview of content progress and status.

CQL:`cw_state`

![An example of a document stats report showing pages by Workflow state.](/cms_trial/assets/70bed254-bd6d-4020-a649-306acecd5ea1.png)

### Pending approvals in Confluence

This dashboard provides a clear view of all Confluence pages with active approvals assigned to the current user. Each team member has a dedicated gadget displaying their assigned approvals, making it easy to track pending reviews.

CQL: `cw_approver = currentUser()`

![An example of a pending approvals dashboard.](/cms_trial/assets/04ac4622-cf9e-4ed6-aec1-3d633249ad4b.png)

### Upcoming expiring pages

This table helps identify Confluence pages that are set to expire within the next four weeks, ensuring timely reviews and updates across the instance.

CQL: `cw_expires < now("4w")`

![An example of an expiring pages table.](/cms_trial/assets/34050c5e-a045-4a22-a7ad-95ce4f5be986.png)

### Draft pages per space

This 1D pivot table displays the number of pages in the Draft state for each space, helping track unpublished content across Confluence.

CQL**:** `cw_state IN ("Draft")`

![An example of a table showing draft pages by space.](/cms_trial/assets/884f579a-2b06-428d-9ad5-2af7ea56cb93.png)

## Set up

### Add a datasource

1. In your dashboard, click the **More actions** ellipses (…), then click **Add datasource.** If you are new to datasources, see [Learn about datasources](/cms_trial/space/RDD/146309943/Learn+about+datasources/) for more information.
2. Provide a meaningful name for your datasource.
3. Enter the API endpoint URL in the provided field. See [Custom Reports templates](/cms_trial/space/RDD/1568374878/Custom+Reports+templates/)for a Comala Document Management example.
4. Set Authentication type: **No Auth** for this example. To learn about authentication types see [Authentication types in Custom Reports datasources](/cms_trial/space/RDD/1545601193/Authentication+types+in+Custom+Reports+datasources/).
5. Click **Add**.

### Add the Custom Reports gadget

1. Navigate to your Dashboard Hub app.
2. If you have not created a dashboard:

   1. Click the dashboard dropdown in the left corner or in the **More actions** menu in the right corner, and select **Create dashboard.**
   2. Name your dashboard, and click **Create**.
   3. Click **Add Gadget.**
3. If you already have a dashboard created, click **Edit.**
4. Click **Add Gadget**.
5. Type **Custom Reports** in the search bar in the gadget catalog or navigate to the Custom Reports section in the left-side navigation panel.
6. Locate the **Custom Reports** gadget, click **Add,** and click **Open Editor**.

See also:

[CQL Search](/cms_trial/space/RDD/146310146/CQL+Search/)

[Add and configure gadgets](/cms_trial/space/RDD/146310019/Add+and+configure+gadgets/)