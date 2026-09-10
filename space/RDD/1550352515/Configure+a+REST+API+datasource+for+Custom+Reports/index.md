# Configure a REST API datasource for Custom Reports

Adding a datasource through an API is a little different to the process you use for adding a datasource for our pre-configured connections. In this guide, we’ll walk you through creating your first Custom Report by connecting to an open REST API. You will need to follow this process for each API datasource that you want to add.

### How to add a Custom Report datasource

1. In Dashboard Hub, select **More actions** (**…**) > **Add Datasource**. The datasource selection window displays.
2. Select **Custom Report**. The *Custom Report* configuration form displays.

   1. Provide a descriptive name for the datasource.
   2. Enter the URL of the REST API you want to connect to for the product providing the content for your report.
   3. Select an authorization type and add the corresponding required detials. [Basic Auth](/cms_trial/space/RDD/1545601193/Authentication+types+in+Custom+Reports+datasources/) is recommended for this example. See [Authentication types in Custom Reports datasources](/cms_trial/space/RDD/1545601193/Authentication+types+in+Custom+Reports+datasources/) to learn more.
3. Click **Add** to create the datasource.

![Dashboard Hub REST API datasource configuration form](/cms_trial/assets/4cf84473-b049-4ab7-aa32-0705f90e5601.png)

### How to add a Custom Report gadget

1. Click **Edit** in the Dashboard Hub dashboard.
2. Click **Add Gadget**.
3. Select the *Custom Report* gadget.
4. In the configuration window, select **Templates** if you already have a saved report. In this example, we create one with the JSON file provided below to list issues from a Jira datasource.
5. Select the datasource added previously. In the provided example, you need to add a Jira datasource and a JQL query Jira in the provided example.
6. Click **Open Editor**. The JSON for the fields in the datasource displays and can be configured. See [How to configure the datasource](/cms_trial/space/RDD/1550352515/Configure+a+REST+API+datasource+for+Custom+Reports/), below.

Download the JSON descriptor here:

![contentId-1550352515](/cms_trial/assets/dcd3ee80-aa3d-48e5-921d-2b389abfe25a.json5)

Jira issues example. Descriptor to list Jira issues in a table:

```json
{
  "type": "rest",
  "uri": "datasource://jira/rest/api/3/search?jql={$initial.jql}&maxResults=5",
  "children": [
    {
      "type": "table",
      "path": "issues",
      "columns": [
        {
          "header": "Issue",
          "accessor": "key"
        },
        {
          "header": "Summary",
          "accessor": "fields.summary"
        },
        {
          "header": "Status",
          "accessor": "fields.status.name"
        }
      ]
    }
  ]
}
```

### How to configure the datasource

1. The uri section starts with *datasource://[YOUR\_DATASOURCE\_VARIABLE\_NAME]*, in our example, **jira**, and following, the rest of the URI **rest/api/3/search** . Select your previously created datasource from the dropdown. In our example **Jira Cloud datasource.**
2. Optionally, you can define variables to pass to your request. In the Jira example, the variable *{$initial.jql}* is used in the query as a parameter *jql={$initial.jql}*. Then, in the input field for our variable *jql* we are using **issuetype = Bug** as an example.
3. The response from the API will be mapped to a table.
4. Define the columns in the table by mapping attributes and fields returned by the API:

   - `key`: maps to the issue key.
   - `fields.summary`: maps to the issue summary field.
   - `fields.status.name`: maps to the issue status name.
5. Save the report configuration.

![Dashboard Hub Configure a REST API datasource for Custom Reports Jira list issues editor](/cms_trial/assets/b6824bdd-823a-43a6-8cf6-95d23008ed44.jpg)