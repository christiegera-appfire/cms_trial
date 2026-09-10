# Run an association report

You can produce a report of associations between Jira issues and Salesforce records.

This provides knowledge about the state of your associations, which you can use for various purposes.

- For developers, prioritize your escalated tickets by looking at the number of associated Cases per Jira issue.
- For product teams, get to know the popularity of feature requests you are tracking in Jira.
- For sales teams, let your development team know about the impact of the fixes they are delivering by looking at how many Leads and Opportunities will benefit from it.

## Access the report page

If you are using  Jira Cloud:

- Click the **Apps** menu at the top of the screen under *Connector for Salesforce*, and select **Reports**.
- From a Jira work item, look under the *Connector for Salesforce* section on the right side of the screen and click **Reports**.   
  This opens the Reports page with the work item's details pre-filled in the JQL search field and the first query already run, so you can immediately see its associated Salesforce records.

  ![image (4).png](/cms_trial/assets/fe2c7791-c45f-46d8-9994-4910f2d3cfd0.png)

If you are using*Jira DC*, click the *CONNECTOR FOR SALESFORCE* menu at the top of the screenand select **Reports**.

## Run a report

The report page can accept a standard JQL query. Click **Search** to run the report.

The results will return a list of:

- Jira work items
- Hyperlinked IDs of their associated Salesforce records

If you also filter results by Salesforce Object, additional columns appear, displaying the Salesforce fields based on what you [configured in the Connection Configuration screen](/cms_trial/space/CSFJIRA/1873511110/Configure+field+displays+and+access+the+Details+screen/).

In the following screen, the last two columns are populated by the "*Subject*" field (primary field) and "*Priority*" field (secondary field) respectively.

![csfjira-reports.png](/cms_trial/assets/7d809d63-f403-457e-9341-c0e70523a0f7.png)

You can’t run a report with an *ORDER BY* clause at this time.

## Filter reporting results by Connection

Specify a Salesforce Connection in this dropdown menu to filter the results by Connection.

![contentId-3091596677](/cms_trial/assets/31bada13-a75b-4cdc-b974-8fabb27ba987.png)

## Filter reporting results by Salesforce Object

To filter the results by Salesforce Object, use the **Salesforce Object** dropdown menu to choose an Object. This only works if you have specified a Connection in the **Connection** dropdown menu.

![contentId-3091596677](/cms_trial/assets/fa7aac13-2bf7-491f-9e38-4f3a45ed0414.png)

## Export reporting results to a CSV file

An **Export** button appears on the top right after a report has been generated. Click the button to show the CSV page options:

- **This page** - If the report generates many items and the results are paginated, the exported CSV will only contain results shown on the *current* page.
- **All results** - The exported CSV will contain all results.

  ![Screenshot of Export reporting results window](/cms_trial/assets/ff799667-f589-4d1f-8bf3-895f9d64f652.png)

Depending on the number of results, selecting **All results** can take a while to prepare and download the file.

The downloaded CSV file contains the following values for each result if Salesforce Object is not selected:

- Issue Key
- Summary
- Status
- Association Count
- Association

If the Salesforce Object is selected, the downloaded CSV file contains all the above values, plus all Salesforce fields set for the selected object in the *Connection* setting.