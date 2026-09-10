# Comala Document Management workflow and state chart

## Overview

The Comala Document Management workflow and state summary report lets you retrieve and visualize workflow and status information from Confluence content using a custom CQL (Confluence Query Language) expression.

The example shown on this page is for demonstration purposes only and can be adapted to fit your reporting needs.

To configure and customize this report, you should be familiar with Confluence CQL and REST API concepts.

## Prerequisistes

- **Comala Document Management for Confluence:** Ensure Comala Document Management is installed and active on your Confluence instance, as the report relies on workflow and status information provided by Comala.
- **Dashboard Hub dashboard**: You need to have a dashboard set up to add Custom Report gadgets.
- **API token for Confluence**: Create and save the API token. You will need it to set up your datasource in Dashboard Hub. You can create the API token from your [Atlassian account](https://id.atlassian.com/manage-profile/security/api-tokens). For more information on managing API tokens, see Atlassian’s [support documentation](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).
- **Datasource**: A Custom Reports datasource must be configured so the gadget can load data from Confluence and access custom properties.

## How to set up the Confluence datasource

To connect Confluence data to Dashboard Hub, you need to configure a REST API datasource.

1. In Dashboard Hub, select **More actions ( … )** > **Add datasource**.
2. Select **Custom Reports**.
3. Configure the datasource:

   1. **Name**: Provide a descriptive name to help identify the datasource later.
   2. **Authentication**: Use **Basic Authentication**.
   3. **Username**: Enter your Atlassian account email address.
   4. **Password**: Paste the Atlassian API token you generated earlier.
4. Click **Add**.

   ![The Custom Report configuration page as described on this page.](/cms_trial/assets/663cc470-0795-44ec-9af6-e77e78680f85.png)

## How to use the Workflows and state chart report

1. Click **Edit** on your Dashboard Hub dashboard.
2. Click **Add Gadget**.
3. Select **Custom Reports** in the left sidebar, then select the **CDM workflows and state chart** report gadget.
4. On the gadget configuration page, the gadget name is pre-filled by default.
5. Under **Datasources**, select the Confluence Custom Reports datasource you created earlier.
6. Under **Variables**, enter:

   1. **CQL** – the query defining which Confluence pages to include, for example, `type=page`.
   2. **Limit** – the maximum number of pages to retrieve. A preview of the report displays workflow and state statistics in a multi-pie chart.
7. (Optional) To customize the report layout, fields, chart type, or styling, click **Open Editor** then edit the parameters you want to change.
8. When the report is ready to use, click **Add**. The report appears similar to the example below.

   ![An example workflow and state chart.](/cms_trial/assets/3c195d4b-ad45-4bf1-a30f-ced9d0226452.png)

See [Custom report example](/cms_trial/space/RDD/2110030119/Custom+report+example/) for a video walkthrough of how to customize your report.

## See also

- [Introduction to Custom Reports](/cms_trial/space/RDD/1529219266/Custom+Reports+-+REST+API+integration/)
- [Get started with Custom Reports](/cms_trial/space/RDD/1528825149/Get+started+with+Custom+Reports/)