# PowerBI Connector for Jira

The combination of Power BI Connector for Jira and Time to SLA presents a powerful opportunity to enhance your data analysis capabilities. This guide will walk you through the process of integrating Power BI with Time to SLA, enabling you to gain valuable insights into your organization's performance.

## Before you begin

- You must have [Power BI Connector for Jira](https://marketplace.atlassian.com/apps/1221150/power-bi-connector-for-jira?hosting=cloud&tab=overview) installed in your instance to carry out the instructions on this page.

## Step 1: Create a token

The configuration is done in two steps. First, you need to create a token on the Time to SLA app. Then, using the Power BI Connector app, you'll create a data source for it.

To learn how to create a token, [click here](/cms_trial/space/TTSC/36209134/REST+APIs/).

## Step 2: Add the token

1. Open the Power BI Connector plugin.
2. From the side menu, click **Tokens**.
3. Select the **Time to SLA** tab.
4. Enter the token.
5. Click **Validate & Save**.

   ![Time to SLA token configuration in Power BI Connector Tokens tab](/cms_trial/assets/16c6a470-ed37-45be-8894-266280c15c1b.png)

From now on, all users who were granted permission to work with the Connector can select Time to SLA fields for export.

## Step 3: Create a data source

1. From the side menu, click **Connectors**.
2. Click **Create a Data Source**.
3. Select the **Time to SLA** tab.
4. Give your connector a name, and optionally, a description.
5. Select all work items, or use filters or JQL to narrow down the work items.
6. Select the fields you want to see.

   ![Time to SLA data source configuration in Power BI Connector with field selection](/cms_trial/assets/f0736cf8-4e0c-4043-967e-8e4c4c7b5372.png)
7. Click **Save**.

After saving the data source, you can create various reports to fit all of your needs.