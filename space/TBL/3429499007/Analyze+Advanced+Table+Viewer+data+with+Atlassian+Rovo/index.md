# Analyze Advanced Table Viewer data with Atlassian Rovo

## Overview

The Advanced Tables for Confluence app by Appfire integrates with Atlassian Rovo through the **ATV Data Analyst** agent. It lets you quickly run AI-driven analysis on your Advanced Table Viewer macro data.

You can use custom prompts, generate summaries, find trends, make comparisons, and run calculations on data imported from CSV, Excel, or JSON data sources without leaving your Confluence page.

- **Dataset limit**: The total size of the shared table data cannot exceed 1.5 MB. You must filter large data files before analysis.
- **Analysis scope**: Rovo only analyzes the data within the specific macro that triggered it. You can perform Rovo analysis for only one macro at a time.

## **Watch the video to quickly analyze the Advanced Table Viewer macro data with Atlassian Rovo**

## Prerequisites

Configure the following to use the Rovo capability within the Advanced Table Viewer macro:

- **Atlassian Rovo**: Ensure **Atlassian Rovo** is active for your organization. If it is not, contact your Atlassian Organization administrator. See [Manage Rovo access](https://support.atlassian.com/organization-administration/docs/manage-rovo-access/) for more information.
- **Global configuration**: The **Enable Ask Rovo** toggle must be **ON** under the app's [**Global configuration**](/cms_trial/space/TBL/74812041/Configuration+-+Cloud/) settings. If not enabled, contact your Confluence Administrator.

## How it works

### Import your data

Configure the Advanced Table Viewer macro to import data from the required data source (CSV, Excel, or JSON). For more information, refer to [Insert and configure the macro](/cms_trial/space/TBL/1531117698/Advanced+Table+Viewer+macro/).

### Launch Rovo

Once you import the data, the **Ask Rovo** button appears embedded in the macro. If you do not see it, ensure you have the [prerequisites](#Prerequisites) configured for Rovo.

If the **Enable Ask Rovo** toggle is disabled in Global configuration, the **Ask Rovo** button is disabled in the macro. Hovering over the button displays a tooltip prompting you to contact your Confluence Administrator.

![Ask Rovo button disabled in Advanced Table Viewer macro](/cms_trial/assets/089bd831-327c-479f-a568-4509270e57ae.png)

You can access **Ask Rovo** in the Confluence page view and edit modes to analyze your Advanced Table Viewer data.

1. To open the **ATV Data Analyst** agent chatwindow for the required macro, click the **Ask Rovo** ( ▢ ) button embedded in the macro interface. This shares the current table dataset context with Rovo for analysis.

   ![ATV_Ask Rovo icon enabled](/cms_trial/assets/0a91b96c-c4c1-4d4a-81dc-630bede35d2a.png)

If the shared dataset exceeds 1.5 MB, the **Ask Rovo** button is disabled and displays a tooltip prompting you to reduce or filter the dataset.

![Ask Rovo button disabled because the dataset exceeds 1.5 MB](/cms_trial/assets/2a2965c9-462d-466c-8ae1-0f4f24cacd45.png)

### Analyze the data

- The **ATV Data Analyst** chat window opens on the right panel, preloaded with the table data context and prompts, and ready to process your requests.

  ![ATV_Data Analyst chat](/cms_trial/assets/27afa5ec-0f71-4972-b4be-1c06371cc668.png)
- Type your custom prompts into the chat to quickly analyze the shared data.

  ![ATV_Rovo chat with prompts](/cms_trial/assets/ad135119-a539-468d-bfa4-d7d584950a26.png)