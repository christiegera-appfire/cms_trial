# Comala Document Management Page Activity

## Overview

The Comala Document Management (CDM)PageActivity report lets you retrieve and visualize workflow activity information for a specific Confluence page using Comala Document Management data and the Confluence REST API. The example shown on this page is for demonstration purposes only and can be adapted to suit your reporting and visualization requirements.

To use this report, you should be familiar with Confluence REST API concepts, nested API calls, and Dashboard Hub Custom Reports.

---

## Prerequisites

- **Comala Document Management for Confluence:** Ensure Comala Document Management is installed and active on your Confluence instance. The page you query must have a valid workflow configured.
- **Dashboard Hub dashboard:** You must have a Dashboard Hub dashboard where you can add Custom Report gadgets.
- **API token for Confluence:** Create and save an Atlassian API token. This token is required to authenticate requests to the Confluence REST API. You can generate a token from your Atlassian account security settings. For more information, see Atlassian’s API token documentation. You can generate one from the [Atlassian API tokens](https://id.atlassian.com/manage-profile/security/api-tokens) page. For more details, see <https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/>.
- **Datasource:** A Custom Reports datasource is required so the gadget can load data from Confluence. See, [Configure a REST API datasource for Custom Reports](/cms_trial/space/RDD/1550352515/Configure+a+REST+API+datasource+for+Custom+Reports/) to learn more.

## How to set up the Confluence datasource

To connect Confluence data to Dashboard Hub, you need to configure a REST API datasource.

1. In Dashboard Hub, select **More actions ( … )** > **Add datasource**.
2. Select **Custom Reports**.
3. Configure the datasource:

   - **Name**: Enter a descriptive name to identify the datasource.
   - **Authentication**: Select **Basic Authentication**.
   - **Username**: Enter your Atlassian account email address.
   - **Password**: Paste the Atlassian API token you generated earlier.
4. Click **Add**.

   ![Dashboard Hub Custom Report page for Comala Document Management activity](/cms_trial/assets/943e176c-7434-485d-8c65-f18a1cb0f2d8.png)

After the datasource is created, configure the report to use this datasource.

---

## How to configure the Comala workflow activity report

1. Click **Edit** on your Dashboard Hub dashboard.
2. Click **Add Gadget**.
3. Select **Custom Reports** from the left sidebar, then choose the **Comala Document Management page activity** report.
4. On the gadget configuration page:

   - The gadget name is pre-filled by default.
   - Under **Datasources**, select the Confluence Custom Reports datasource you created earlier.
5. Under **Variables**, enter the contentId of the Confluence page you want to display workflow activity for. The page must have a valid Comala workflow configured. A report preview displays.

   ![An example CDM Page Activity report.](/cms_trial/assets/1a303f55-9533-43bb-8de4-b827cab24ac1.png)
6. (Optional) To customize the layout, fields, SVG styling, or data processing logic, click **Open Editor** and adjust the report configuration as needed. You can load nested API calls to gather complex information
7. When the report is ready, click **Add**.

See [Custom report example](/cms_trial/space/RDD/2110030119/Custom+report+example/) for a video walkthrough of how to customize your report.

## See also

- [Introduction to Custom Reports](/cms_trial/space/RDD/1529219266/Custom+Reports+-+REST+API+integration/)
- [Get started with Custom Reports](/cms_trial/space/RDD/1528825149/Get+started+with+Custom+Reports/)