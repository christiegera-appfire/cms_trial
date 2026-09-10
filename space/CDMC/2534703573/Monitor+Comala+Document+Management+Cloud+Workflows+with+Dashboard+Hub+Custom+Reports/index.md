# Monitor Comala Document Management Cloud Workflows with Dashboard Hub Custom Reports

## Overview

This document explains how you can integrate Dashboard Hub and Comala Document Management (CDM) cloud to view key metrics of your document workflows in Confluence.

This document is for the Comala Document Management **Cloud** version.

For the Comala Document Management **Data Center** version, see [Document Workflow Custom Charts](https://appfire.atlassian.net/wiki/spaces/RDD/pages/874905671).

## Custom Reports in Dashboard Hub

Dashboard Hub is a reporting app that enables the creation of centralized dashboards with data from various sources, including Confluence. Its Custom Reports gadget lets users create visuals based on Confluence Query Language (CQL) and integrate data from any product with a REST API.

For more details, see:

<https://appfire.atlassian.net/wiki/spaces/RDD/pages/146309347>

<https://appfire.atlassian.net/wiki/spaces/RDD/pages/1528825149>

<https://appfire.atlassian.net/wiki/spaces/RDD/pages/1568374878>

## Custom Reports templates

Use our curated and maintained catalog of [Custom Reports templates](https://appfire.atlassian.net/wiki/spaces/RDD/folder/1992261872?atlOrigin=eyJpIjoiODg3YmQwOGVlZjQ2NDE4MjkyMTc3Yjk0MWI3MjJjOTQiLCJwIjoiYyJ9). This catalog offers ready-to-use, easy-to-connect examples. Find links to the Comala Document Management templates here:

- <https://appfire.atlassian.net/wiki/spaces/RDD/pages/1955037214>
- <https://appfire.atlassian.net/wiki/spaces/RDD/pages/1955102741>
- <https://appfire.atlassian.net/wiki/spaces/RDD/pages/1955954748>

## Comala Document Management (CDM)

Comala Document Management provides workflow automation for pages and blog posts in Confluence spaces. Comala Document Management also offers in-app reporting tools, including the Document Report for tracking workflow activity across pages in a space and the Document Activity report for an individual page.

You can find Comala Document Management on the Atlassian Marketplace here: <https://marketplace.atlassian.com/apps/142/comala-document-management?hosting=cloud&tab=overview>

## Use cases

### Document stats report

This chart provides a visual breakdown of pages by Workflow State, offering a quick overview of content progress and status.

CQL:`cw_state`

![An example of a document stats report showing pages by Workflow state.](/cms_trial/assets/c4fd45f8-18f1-4324-bb3c-3143cfb68ffa.png)

### Pending approvals in Confluence

This dashboard provides a clear view of all Confluence pages with active approvals assigned to the current user. Each team member has a dedicated gadget displaying their assigned approvals, making it easy to track pending reviews.

CQL: `cw_approver = currentUser()`

![An example of a pending approvals dashboard.](/cms_trial/assets/bd3edd33-87fd-420a-950f-c3eb47cce81f.png)

### Upcoming expiring pages

This table helps identify Confluence pages that are set to expire within the next four weeks, ensuring timely reviews and updates across the instance.

CQL: `cw_expires < now("4w")`

![An example of an expiring pages table.](/cms_trial/assets/957c25ca-16fc-489f-b281-a096641c9580.png)

### Draft pages per space

This 1D pivot table displays the number of pages in the Draft state for each space, helping track unpublished content across Confluence.

CQL**:** `cw_state IN ("Draft")`

![An example of a table showing draft pages by space.](/cms_trial/assets/7f5e4d4a-358a-40a5-b186-6e1cf0054bf3.png)

## Set up

### Add a datasource

1. In the Custom Reports dashboard view, click [Blue elipse icon].
2. Click **Add datasource.** New to datasources? See [Learn about datasources](https://appfire.atlassian.net/wiki/spaces/RDD/pages/146309943) for more information.
3. Provide a meaningful name for your datasource.
4. Enter the API endpoint URL in the provided field. See the [Global catalog of templates](https://appfire.atlassian.net/wiki/spaces/RDD/pages/1568374878), a Comala Document Management example.
5. Set Authentication type: No Auth for this example. To understand each authentication type more thoroughly, refer to [Authentication types in Custom Reports datasources](https://appfire.atlassian.net/wiki/spaces/RDD/pages/1545601193).
6. Click **Add**.

### Add the Custom Reports gadget

1. Navigate to your Dashboard Hub app.
2. If you have not created a dashboard:

   1. Click the dashboard dropdown in the left corner or the [Blue elipse icon] action menu in the right corner, and select **Create Dashboard.**
   2. Name your dashboard, and click **Create**.
   3. Click **Add Gadget.**
3. If you already have a dashboard created, click **Edit.**
4. Click **Add Gadget**.
5. Type **Custom Reports** in the search bar in the gadget catalog or navigate to the Custom Reports section in the left-side navigation panel.
6. Locate the **Custom Reports** gadget, click **Add,** and click **Open Editor**.