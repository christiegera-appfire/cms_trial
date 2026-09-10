# Monday formula cards custom report

The **Monday formula cards** custom report lets you build formula cards based on data from your monday.com boards. You can customize the JSON file to return the data you need. The example on this page is a sample use case only.

You need knowledge of monday.com’s [GraphQL](https://developer.monday.com/api-reference/docs/introduction-to-graphql) language to configure this report.

## **Prerequisites**

- **Dashboard Hub dashboard**: You need to have a dashboard set up to add Custom Report gadgets.
- **API token for monday.com**: Create this token in [monday.com](https://your-instance.monday.com/apps/manage/tokens) and store it to a secure location. You will need this token to set up your datasource in Dashboard Hub.
- **Datasource**: You need to add a datasource for a monday.com instance withGETandPOST access.
- **Board ID**: You need the board ID for the relevant board in your monday.com instance.

## How to set up the monday.com datasource

To connect monday.com data with relevant data in your Jira instance, you need to configure a REST API datasource.

1. In Dashboard Hub, select **More actions (…)** > **Add datasource**.
2. Select **Custom Reports**.
3. Configure the datasource:

   1. **Name**: Provide a name for the datasource to help you identify it when managing your datasources.
   2. **URL**: Enter the root URL of the latest [monday.com](http://monday.com/) version.
   3. **Token**: Paste the monday.com API token into the *Token* field. This token is a prerequisite. If you haven’t created it yet, follow the steps in the [monday.com documentation](https://developer.monday.com/api-reference/docs/authentication).
4. Click **Add**.

## How to use the Monday formula cards report

1. Click **Edit** in your Dashboard Hub dashboard.
2. Click **Add Gadget**.
3. Select **Custom Reports** in the left sidebar, then select the **Monday formula cards** gadget from the available reports.

   ![Dashboard Hub Dashboard Hub Monday formula cards CR](/cms_trial/assets/f1bd12e9-0187-48ba-bd73-52c90c86000e.png)
4. On the gadget configuration page, the name is added by default.
5. Under **Datasources**, select the monday.com API datasource you created earlier.
6. Under **Variables**, enter the monday.com board ID for the data you want to display. A preview of the report appears similar to the following:

   ![Dashboard Hub Dashboard Hub monday formula cards example CR](/cms_trial/assets/d9b9a220-b7ba-4318-bcab-62fba5408b2d.png)
7. (optional)To customize the report, click **Open Editor**.

   1. In the *Report Descriptor Editor*, make the required changes to the JSON file. Use the JSONpath aggregate data to render custom values, for example, count items, calculate averages, or display different values. You can preview the changes in the editor. See [Custom report example](/cms_trial/space/RDD/2110030119/Custom+report+example/) to learn more about modifying report JSON files.

      ![Dashboard Hub monday.com formula cards custom report example](/cms_trial/assets/cfc2dc4f-cd56-455c-97a1-8b9ded902102.png)
8. (optional) To save the customized report as a template to reuse at any time, click **Save as Template**. Provide a title for the template, then click **Save Template**.
9. When the report is ready to use, click **Add**.