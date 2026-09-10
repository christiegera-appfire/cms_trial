# Analyze Native Table Enhancer [Beta] macro data with Atlassian Rovo

## Overview

The Advanced Tables for Confluence app by Appfire integrates with Atlassian Rovo through the **Advanced Tables Data Analyst** agent. It lets you quickly run AI-driven analysis on your Native Table Enhancer macro data.

You can use custom prompts, generate summaries, find trends, make comparisons, and run calculations on your table data without leaving your Confluence page.

- **Dataset limit**: The total size of the shared table data cannot exceed 1.5 MB. You must filter large data files before analysis.
- **Analysis scope**: Rovo only analyzes the data within the specific macro that triggered it. You can perform Rovo analysis for only one macro at a time.

The Native Table Enhancer macro is currently in beta. [Learn more](https://support.appfire.com/space/TBL/3520037211).

## Prerequisites

Configure the following to use the Rovo capability within the Native Table Enhancer macro:

- **Atlassian Rovo**: Ensure **Atlassian Rovo** is active for your organization. If it is not, contact your Atlassian Organization administrator. See [Manage Rovo access](https://support.atlassian.com/organization-administration/docs/manage-rovo-access/) for more information.
- **Global configuration**: The **Enable Ask Rovo** toggle must be **ON** under the app's [**Global configuration**](/cms_trial/space/TBL/74812041/Configuration+-+Cloud/) settings. If not enabled, contact your Confluence Administrator.

## How it works

### Import your data

Configure the Native Table Enhancer macro for your native Confluence table. For more information, refer to [Insert and configure the macro](/cms_trial/space/TBL/3520037211/Native+Table+Enhancer+%5BBeta%5D+macro/).

### Launch Rovo

Once you import the data, the **Ask Rovo** button appears embedded in the macro. If you do not see it, ensure that the [prerequisites](#Prerequisites) are configured for Rovo.

If the **Enable Ask Rovo** toggle is disabled in Global configuration, the **Ask Rovo** button is disabled in the macro. Hovering over the button displays a tooltip prompting you to contact your Confluence Administrator.

![When Ask Rovo button is disabled in Advanced Table Viewer macro, contact your administrator](/cms_trial/assets/bc6fd17a-e7b5-424c-b9f5-f459d1d8e8bd.png)

You can access **Ask Rovo** in the Confluence page view mode to analyze your Native Table Enhancer data.

1. To open the **Advanced Table Data Analyst** agent chatwindow for the required macro, click the **Ask Rovo** ( ▢ ) button embedded in the macro interface. This shares the current table dataset context with Rovo for analysis.

   ![Click Ask Rovo to share the current table dataset with Rovo for analysis](/cms_trial/assets/f5aa5e44-8b06-426b-ba92-2285a8ab6d47.png)

If the shared dataset exceeds 1.5 MB, the **Ask Rovo** button is disabled and displays a tooltip prompting you to reduce or filter the dataset.

![Ask Rovo button disabled because the dataset exceeds 1.5 MB](/cms_trial/assets/3b6b2ad7-0ac6-4a9d-967f-8df3904b4c5e.png)

### Analyze the data

- The **Advanced Table Data Analyst** chat window opens in the right panel, preloaded with the table data context and prompts, and ready to process your requests.

  ![The Advanced Tables Data Analyst chat window opens in right panel](/cms_trial/assets/8b1d1ae4-ceb4-4b29-9ac5-7dd9366b106f.png)
- Type custom prompts into the chat to analyze your shared data and get quick insights from Rovo.

  ![Type custom prompts into the chat to analyze your shared data](/cms_trial/assets/b2ae0b06-7fc6-4cb0-8a64-f0dd85202dcd.png)