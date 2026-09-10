# Filter Salesforce comments in Jira work items

Jira admins can filter Salesforce and Jira comments using hashtags (for example, #jira, #jira-servicedesk, #salesforce). You can set separate filters for Salesforce comments and Jira comments. This page shows you how to add hashtag filters and view filtered comments in the Salesforce Comments tab in Jira work items.

## Before you start

Make sure you have:

- Administrator rights in Jira - only administrators can set up the integration
- [Set up your integration to Salesforce in Jira](/cms_trial/space/CSFJIRA/1873412559/Set+up+your+integration+in+Jira/)

## Add hashtag filters in Jira

1. Select **Apps** from the left sidebar in Jira.
2. Next to *Connector for Salesforce,* click **Menu** (▢) > **App settings**.

   ![Appsettings.png](/cms_trial/assets/fd0ae13c-d058-42dc-adb5-2108efa56f19.png)
3. Under *Connector for Salesforce*, select **Connections**.
4. Select the connection you want to configure and click **Configure**.

   ![Connections.png](/cms_trial/assets/935cd506-f888-40a7-8cad-bfa3e6595c8a.png)
5. On the **Connection configuration** screen, scroll down to the **Filter Comments by Tag** section.

   ![Filter Comments by Tag section](/cms_trial/assets/9dd31c47-dba1-4599-a945-f0bb9848087e.png)
6. For **Comment Privacy** settings, select which Salesforce comments are visible in Jira based on their privacy:

   - All comments
   - Public comments only
   - Private comments only

The privacy setting is applied first and takes precedence over any hashtag filters below. A comment excluded based on privacy will never appear in Jira, regardless of its tags.

1. Enter hashtags in the relevant field:

- - The **Salesforce Comments** tags filter Salesforce comments and render them in the **Salesforce Comments** tab in the Jira work item.
  - The **Jira Comments** tags filter Jira comments and render them in the **Salesforce Comments** tab in the Jira work item.

Tags must be preceded by a *#* and separated by a space.

## View filtered comments in Jira

Filtered comments appear in a Jira work item based on the **Comment Privacy** settings and the hashtags configured by the administrator (see above).

![image-20260813-140659.png](/cms_trial/assets/492ea870-8c8a-4e35-850b-6b5877393979.png)

In Salesforce, to add a hashtag to a **Case Comment**, simply edit the comment and add the hashtag anywhere in the comment:

![connector-sf-casse-comment.png](/cms_trial/assets/4297d37a-c92f-450e-abfb-55496d0f80c7.png)

## Related articles

- [Viewing Salesforce comments in Jira](/cms_trial/space/CSFJIRA/1962443468/View+Salesforce+comments+in+Jira/)
- [Filter Jira comments in Salesforce Cases](/cms_trial/space/CSFJIRA/1873413366/Filter+Jira+comments+in+Salesforce+Cases/)