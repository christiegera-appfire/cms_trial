# Comala Document Management status report

## Overview

The Comala Document Management report provides an overview of Confluence pages matching a given CQL query and limit, including their workflow status.

To use this report, you should be familiar with Confluence REST API concepts, nested API calls, and Dashboard Hub Custom Reports.

---

## Prerequisites

- **Comala Document Management for Confluence:** Ensure the app is installed and active on your Confluence instance.
- **Datasource:** A Custom Reports datasource must be configured so the gadget can load data and access custom properties from Confluence.
- **Variables:** You must provide two variables when configuring the report:

  - **CQL**: The Confluence Query Language expression that defines which pages to display.
  - **Limit**: The maximum number of pages to return.

- **Dashboard Hub dashboard:** You need a Dashboard Hub dashboard where you can add Custom Reports gadgets.

---

## How to set up the datasource

To connect Confluence page data with Dashboard Hub you need to configure a REST API datasource in Dashboard Hub.

1. In Dashboard Hub, select **More actions (…)** > **Add datasource**.
2. Select **Custom Reports**.
3. Configure the datasource:

   - **Name:** Provide a clear name so you can easily identify this datasource later.
   - **URL:** Enter your Confluence Cloud REST API base URL (for example:  
     `https://your-domain.atlassian.net/wiki/rest/api`).
   - **Authentication type:** Select **Bearer token** or **Basic Auth**, depending on your Jira/Confluence configuration.
   - **Token / Credentials:** Enter the required authentication details.
4. Click **Add**.

---

## How to use the Comala Document Management status report

1. Click **Edit** on your Dashboard Hub dashboard.
2. Click **Add Gadget**.
3. Select **Custom Reports** in the left sidebar, then select the **Appfire Comala Document Management status report** gadget.
4. On the gadget configuration page:

   - The gadget name is pre-filled by default.
   - Under **Datasources**, select the datasource you created earlier.
5. Under **Variables**, enter:

   - **CQL** – the query defining the pages you want to display.
   - **Limit** – the maximum number of pages to include.
6. (Optional) To customize the report layout, fields, icons, or styling, click **Open Editor**.
7. Click **Add**.

![Dashboard Hub Comala Document Management status report example](/cms_trial/assets/fb69c986-f203-4340-8949-de36e304dc66.png)

See [Custom report example](/cms_trial/space/RDD/2110030119/Custom+report+example/) for a video walkthrough of how to configure your report.

## See also

- [Introduction to Custom Reports](/cms_trial/space/RDD/1529219266/Custom+Reports+-+REST+API+integration/)
- [Get started with Custom Reports](/cms_trial/space/RDD/1528825149/Get+started+with+Custom+Reports/)