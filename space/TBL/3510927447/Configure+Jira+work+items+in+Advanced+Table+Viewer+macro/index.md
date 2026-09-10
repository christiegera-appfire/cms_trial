# Configure Jira work items in Advanced Table Viewer macro

The Advanced Table Viewer macro supports importing Jira work items from the Jira instance linked to the current Confluence site. The macro can display up to 2,000 Jira work items. If a JQL query returns more than 2,000 work items, only the first 2,000 are shown.

**Prerequisites**

- Your organization or site administrator has established the app connection between the Advanced Tables for Confluence app and the Jira instance.
- Both Confluence Cloud and Jira Cloud must be active on the same Atlassian site.
- For more information, refer to [How to connect the Advanced Tables for Confluence app to the Jira application](/cms_trial/space/TBL/3510698190/How+to+connect+the+Advanced+Tables+for+Confluence+app+to+the+Jira+application/).

**Permission boundaries**: Jira data visibility in Confluence is strictly bound by Jira permissions, including project and work item security-level permissions, so end users see only the Jira data they already have permission to view.

This page details how to configure the Advanced Table Viewer macro to import Jira work items.

## Configure the Jira work items

[Unmapped macro: refined-tab — no content to fall back on]

- Insert the macro in a Confluence page using the macro browser or the macro shortcut (/).

  ![Advanced Tables macro shortcut for inserting Advanced Table Viewer](/cms_trial/assets/c2107f79-268d-4c5d-8af6-5143c48b4a49.jpg)
- On the initial setup screen, click **Connect Data Source**.

  ![connect datasource](/cms_trial/assets/20d75936-3cfa-44ed-a39c-5bc81bb290a0.jpg)
- The *Select* *data source* dialog opens.
- To configure the Jira data source, select **Jira work items** from the *Select data connector* dropdown. By default, the CSV data connector is selected.

  ![Advanced Table Viewer_select Jira work items](/cms_trial/assets/6f85b47c-ca48-4dc8-9c3e-f11223c8f728.png)

- If the Jira site is not connected, the macro displays a message to connect to the Jira site.

  ![If Jira site not connected, the Advanced Table Viewer macro displays a message to connect to the Jira site](/cms_trial/assets/c462beb7-288f-4614-b0dc-f3b54fe43ffb.png)

- Once you choose Jira work items, the dialog displays the following fields and details.

  ![The Advanced Table Viewer macro Jira data source dialog displays the JQL query and details](/cms_trial/assets/2994e09a-e6d4-41bf-90c8-c3a166068316.png)
  - **Jira site**: Displays the Jira site the Advanced Tables for Confluence app is connected to. You can import Jira work items from this site.
  - **View Jira projects**: This navigates you to the Jira site projects page, displaying the projects list.
  - **JQL query**: Displays a default Jira query to import data.

    - To import the required Jira work items, enter a JQL query.

      - As you enter the query, the JQL query editor displays a real-time syntax autocomplete dropdown to quickly complete your query.
      - To validate the query and import Jira work items, click **Search** (▢ ).

        ![Validate JQL query in Jira work items dialog](/cms_trial/assets/82a8c90e-e1e9-472c-b89f-38b847484644.png)
    - The macro validates the **JQL query**. If valid, it returns the count of work items found; if invalid, it displays an error message.

      ![The JQL query is validated and macro returns the count of work items](/cms_trial/assets/4be3d567-f804-4f26-9a03-685491bcf878.png)

- To expand the JQL query editor, click Expand editor (▢ ).
- If you need help with JQL syntax, click [Syntax help](https://support.atlassian.com/jira-service-management-cloud/docs/use-advanced-search-with-jira-query-language-jql/) (▢ ).

- **Columns**: In the Columns field, you can specify the list of Jira fields to be imported. By default, a few Jira fields such as Issue key, Summary, Status, Assignee, Priority, and Updated are preselected. You can remove fields, select more fields, and reorder them. For further configuration, proceed to the **Select and order columns** section on this page.

[Unmapped macro: refined-tab — no content to fall back on]

The **Columns** field displays a few default Jira fields as column names to import. You can remove, select, and reorder the column names as needed.

- Clear all selected columns

  - To remove all column selections at once, click **clear all** ([cross circle icon] ). After clearing, click the field and re-select column names in the required order.

    ![Remove all column names](/cms_trial/assets/48448e75-0c03-41b4-a4f8-057a6468a17e.png)
- Remove a specific column

  - Next to the column name, click **clear** ([cross circle icon]) to remove it from the selection.

    ![remove specific column names](/cms_trial/assets/cb9c13de-84a6-4f46-a0c8-439c3b67eb74.png)
- Select columns

  - Click the **Columns** field and choose the column names from the list.

    ![Click columns field and choose the required Jira fields](/cms_trial/assets/6c82e1a5-6a6b-4409-9aab-7fd611307560.png)

The order in which you select the column names determines the column order displayed in the Confluence table.

Once you have selected the required columns, proceed to the **Save and publish** section on this page.

[Unmapped macro: refined-tab — no content to fall back on]

- In the *Select data source* dialog, click **Save**.

  ![Select data source_click Save](/cms_trial/assets/bca3aae6-470a-4b75-9ab2-e3f3a5893ef5.png)
- The macro opens in setup mode, displaying the table with the selected column names and Jira data.
- In setup mode, you can configure various available features, such as column filtering, grouping, row styling, search, row numbering, sorting, download, and sum-up. Refer to [Set up the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/).

  ![Setup mode displays the Jira work items](/cms_trial/assets/41e11149-277d-4615-a74b-addc3e8f689b.png)
- To apply the configurations, click **Save**.
- The configured table appears in the Confluence page edit mode.

  ![Advanced Table Viewer macro displaying Jira work items in page edit mode](/cms_trial/assets/d73de072-c24d-4280-aa00-5106f13222a6.png)
- **Publish** the page to view the table in the Confluence page view mode.

  ![Advanced Table Viewer macro  displaying Jira work items in page view mode](/cms_trial/assets/ce581d13-c859-4ac7-9c5e-8ec9576b52ab.png)
- Your Jira work items are now ready to view and analyze directly within Confluence.

- To refresh the imported Jira work items for any changes from the Jira instance, click **Refresh** (▢ ).
- You can refresh the Jira work items in setup mode, page edit mode, and page view mode.