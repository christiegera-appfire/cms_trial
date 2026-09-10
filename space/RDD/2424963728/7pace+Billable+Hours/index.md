# 7pace Billable Hours

This bar chartdisplays a monthly overview of total billable time.

![Dashboard Hub 7pace Billable Hours report table](/cms_trial/assets/78f8c42c-48a9-4714-9af6-87c5d6be3f58.png)

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
   2. **URL**: Enter the root URL of the latest 7pace API version. Refer to the [7pace API documentation](https://appfire.atlassian.net/wiki/spaces/7TFJ/pages/1987510406) for the latest version. In the following example, we’re using:

      ```text
      https://timehubjra.7pace.com/api/v1
      ```
   3. **Authentication type**: Select `Bearer token`.
   4. **Token**: Paste the 7pace API token into the *Token* field. This token is a prerequisite. If you haven’t created it yet, follow the steps in the [7pace API documentation](https://appfire.atlassian.net/wiki/x/hgB3dg).

      ![Dashboard Hub Custom Report datasource configuration for 7pace](/cms_trial/assets/7ab113cd-fc1a-4356-9477-124a23eb8354.png)
4. Click **Add**.

## How to use the 7pace Billable Hours report

1. Click **Edit** in your Dashboard Hub dashboard.
2. Click **Add Gadget**.
3. Search for `7pace` in the gadget search bar, then select the **7pace Billable Hours** report gadget from the matching results.
4. On the gadget configuration page, the name is added by default.
5. Under *Datasources*, select the 7pace API datasource you created earlier.
6. Click **Open Editor**. The report JSON file loads.
7. In the `path` parameter, update the custom field name to match the custom field name in 7pace.
8. Close the editor, then click **Add**.

![Dashboard Hub 7pace Billable Hours configuration fields](/cms_trial/assets/b79ecd27-b0af-4415-b34e-b298bc4288ad.png)

![Dashboard Hub 7pace Billable Hours chart preview](/cms_trial/assets/14f5686a-19b6-43a5-b0d7-90660c482fe4.png)

**Pro tip**: To populate the chart with a different 7pace custom toggle, replace `Billable hours` with the name of your selected 7pace custom toggle in the report configuration.

## Troubleshooting

### URL depth

If you receive a warning that an API call can’t be completed, compare the depth of URL paths defined in the report configuration and the datasource.

We recommend that your datasource setup uses the following URL format: `https://timehubjira.7pace.com/api/v1`, then the report configuration can be written with only the necessary endpoint.

![Dashboard Hub 7pace Billable Hours dashboard preview](/cms_trial/assets/d3ac8132-aa35-4d92-9e90-4bbde1e87661.png)