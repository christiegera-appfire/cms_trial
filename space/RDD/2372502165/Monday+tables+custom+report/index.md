# Monday tables custom report

The **Monday tables** custom report lists all the workspaces and boards from a monday.com instance. You can customize the JSON file to return the data you need. The example on this page is a sample only.

You need knowledge of monday.com’s [GraphQL](https://developer.monday.com/api-reference/docs/introduction-to-graphql) language to configure this report.

## **Prerequisites**

- **Dashboard Hub dashboard**: You need to have a dashboard set up to add Custom Report gadgets.
- **API token for monday.com**: Create this token in [monday.com](https://your-instance.monday.com/apps/manage/tokens) and store it to a secure location. You will need this token to set up your datasource in Dashboard Hub.
- **Datasource**: You need to add a datasource for a monday.com instance withGETandPOST access.

## How to set up the monday.com datasource

To connect monday.com data with relevant data in your Jira instance, you need to configure a REST API datasource.

1. In Dashboard Hub, select **More actions (…)** > **Add datasource**.
2. Select **Custom Reports**.
3. Configure the datasource:

   1. **Name**: Provide a name for the datasource to help you identify it when managing your datasources.
   2. **URL**: Enter the root URL of the latest [monday.com](http://Monday.com) version.
   3. **Token**: Paste the monday.com API token into the *Token* field. This token is a prerequisite. If you haven’t created it yet, follow the steps in the [monday.com documentation](https://developer.monday.com/api-reference/docs/authentication).
4. Click **Add**.

## How to use the monday.com tables report

1. Click **Edit** in your Dashboard Hub dashboard.
2. Click **Add Gadget**.
3. Select **Custom Reports** in the left sidebar, then select the **Monday tables** report gadget from the available reports.

   ![Dashboard Hub Monday tables custom report report preview](/cms_trial/assets/546855fd-6c97-4f1e-b715-5fc9bf9063f5.png)
4. On the gadget configuration page, the name is added by default.
5. Under *Datasources*, select the monday.com API datasource you created earlier. A preview of the report will appear similar to the following:

   ![Sample Monday tables report in Dashboard Hub.](/cms_trial/assets/38ca64ae-879c-41f3-a061-179ff8ea1437.png)
6. (optional)To customize the report, click **Open Editor**.

   1. In the *Report Descriptor Editor*, make the required changes to the JSON file. You can preview the changes in the editor. You can change the table layout and define the data to display in the columns. See [Custom report example](/cms_trial/space/RDD/2110030119/Custom+report+example/) to learn more about modifying report JSON files.

      ![Dashboard Hub monday.com tables custom report example](/cms_trial/assets/5b5fee6d-12bf-4d75-a696-4a0006ce970e.png)
7. (optional) To save the customized report as a template to reuse at any time, click **Save as Template**. Provide a title for the template, then click **Save Template**.
8. When the report is ready to use, click **Add**.