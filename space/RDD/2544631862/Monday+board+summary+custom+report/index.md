# Monday board summary custom report

The **Monday board summary** custom report lets you fetch, calculate, and summarize the values of all the columns in a board through REST API. You can customize the JSON file to return the data you need. You can decide which columns to display and how to calculate the corresponding summary. See the monday.com [documentation](https://support.monday.com/hc/en-us/articles/115005310285-Available-column-types-on-monday-com) for more information on available columns. The example on this page is a sample only.

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

## How to use the Monday board summary custom report

1. Click **Edit** in your Dashboard Hub dashboard.
2. Click **Add Gadget**.
3. Select **Custom Reports** in the left sidebar, then select the **Monday board summary** gadget from the available reports.

   ![Dashboard Hub Dashboard Hub Monday Board summary CR](/cms_trial/assets/85fa5d5a-87c8-4a43-90d4-af82242c35f3.png)
4. On the gadget configuration page, the name is added by default.
5. Under **Datasources**, select the monday.com API datasource you created earlier.
6. Under **Variables**, enter the monday.com board ID for the data you want to display. A preview of the report appears similar to the following:

   ![Dashboard Hub Dashboard Hub Monday Board summary CR example](/cms_trial/assets/7676d826-9883-4494-a6b3-61f821d5f5c8.png)
7. (optional)To customize the report, click **Open Editor**.

   1. In the *Report Descriptor Editor*, make the required changes to the JSON file. You can customize any parameter to suit your needs, for example, use conditional nodes for different content types, or retrieve icons and colours from your monday.com boards. You can preview the changes in the editor. See [Custom report example](/cms_trial/space/RDD/2110030119/Custom+report+example/) to learn more about modifying report JSON files.

      ![Dashboard Hub Monday board summary custom report Dashboard Hub Monday board summary editor](/cms_trial/assets/ae65fc9a-c2b6-43af-be87-48ec459e7edd.png)
8. (optional) To save the customized report as a template to reuse at any time, click **Save as Template**. Provide a title for the template, then click **Save Template**.
9. When the report is ready to use, click **Add**.