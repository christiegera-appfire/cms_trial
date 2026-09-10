# 7pace Aggregations

This 7pace report provides a month-over-month overview of tracked time grouped by project and user.

![Dashboard Hub 7pace Aggregations custom report preview](/cms_trial/assets/f5964b2c-0d5e-4eec-97cb-6fae3f0a4882.png)

## Prerequisites

- **7pace for Jira Cloud:** You need to have 7pace Timetracker installed on your Jira Cloud instance. If you aren’t already using 7pace Timetracker, you can try it free from our [Atlassian Marketplace listing](https://marketplace.atlassian.com/apps/1235398/7pace-timetracker-for-jira?hosting=cloud&tab=overview).
- **7pace API Token**: Create this token in 7pace Timetracker and copy it to a safe place. You will need this token to set up your datasource in Dashboard Hub. Learn how to create this token in the [7pace API documentation](https://appfire.atlassian.net/wiki/x/hgB3dg).
- **Datasource**: You need a Custom Reports datasource configured through REST API so that the report can connect 7pace data with the relevant Jira data.
- **Dashboard Hub dashboard**: You need to have a dashboard set up to add Custom Report gadgets.

## How to set up the 7pace datasource

To connect 7pace data with relevant data in your Jira instance, you need to configure a REST API datasource.

1. In Dashboard Hub, select **More actions (…)** > **Add datasource**.
2. Select **Custom Reports**.
3. Configure the datasource:

   1. **Name**: Provide a name for the datasource to help you identify it when managing your datasources.
   2. **URL**: Enter the root URL of the latest 7pace API version. See [7pace API documentation](https://appfire.atlassian.net/wiki/spaces/7TFJ/pages/1987510406) for the latest version. In the following example, we’re using:

      ```text
      https://timehubjra.7pace.com/api/v1
      ```
   3. **Authentication type**: Select `Bearer token`.
   4. **Token**: Paste the 7pace API token into the *Token* field. This token is a prerequisite. If you haven’t created it yet, follow the steps in the [7pace API documentation](https://appfire.atlassian.net/wiki/x/hgB3dg).
4. Click **Add**.

   ![Dashboard Hub Custom Report datasource configuration for 7pace](/cms_trial/assets/4006df37-0c20-4ee1-8bd6-3fd6fbf69b75.png)

## How to use the 7pace Aggregations report

1. Click **Edit** in your Dashboard Hub dashboard.
2. Click **Add Gadget**.
3. Search for `7pace` in the gadget search bar, then select the 7pace Aggregations report gadget from the matching results.
4. On the gadget configuration page, the name is added by default.
5. Under *Datasources*, select the 7pace datasource for Jira and the 7pace API you created earlier.
6. Under *Variables*, enter the project key for the work item data that you want to display. This report can display data from a single project.
7. (optional) To customize the report, click **Open Editor**.
8. Click **Add**.