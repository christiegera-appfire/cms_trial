# How do I connect more than one Jira connection in my Salesforce environment?

## Answer

1. In Salesforce, click ⚙️ **> Setup**.  
   If you are using Salesforce Classic, click **Setup** on the upper right pane.
2. Search for "*Package*" and go to **Installed Packages**.
3. Look for "*Jira for Salesforce*" and click **Configure**.
4. Select **Add Connection** on the top right and a pop-up will appear.
5. ![image-20241213-091308.png](/cms_trial/assets/e9af3041-de0c-411d-a0d6-1fd8d7eacf1f.png)

   Enter the **Connection Name** and **Access Token**:

   1. For the **Access Token**, switch over to your first Jira instance to generate a Jira access token.
   2. Navigate to **Apps** > **Salesforce** > **Connections**.
   3. Choose your **Connection**, then click

      [Unmapped macro: inline-media-image — no content to fall back on]

      **> API Access Token.**
   4. Copy the **API Access Token** and paste it into the Salesforce screen from Step 4 and click **Save**.
6. The first connection created is marked as *default*. Repeat Step 4 - Step 5 to add additional Jira connections from different sites.

   ![contentId-3091827403](/cms_trial/assets/f40e899a-2098-48d6-8542-b871a331faa9.png)
7. For each Jira connection added to this page, you will be able to perform the following operations:

   1. **Configure** - To configure the settings of the configuration made. For more information, read [Configuring settings in the Salesforce Package](/cms_trial/space/CSFJIRA/1873445530/Configure+settings+in+the+Salesforce+package/).
   2. **Revoke Access** - To revoke the connection made using the API Access Token from Jira.
   3. **Make Default** - Marking a connection default will make this connection be selected in the Jira components by default. The Jira Comments component will only be able to display issues from the default connection.

## Related content

- [Is there any difference in setting up the integration in Jira for the multi-site feature?](/cms_trial/space/CSFJIRA/3091597518/Is+there+any+difference+in+setting+up+the+integration+in+Jira+for+the+multi-site+feature%3F/)
- [How to view, create and associate Jira Issues from Salesforce by switching the Jira connection?](/cms_trial/space/CSFJIRA/2258010468/How+to+view%2C+create+and+associate+Jira+Issues+from+Salesforce+by+switching+the+Jira+connection%3F/)
- [Why can't I switch or view the Jira connection dropdown for the Lightning Aura and Visualforce components?](/cms_trial/space/CSFJIRA/3091335936/Why+can%27t+I+switch+or+view+the+Jira+connection+dropdown+for+the+Lightning+Aura+and+Visualforce+components%3F/)
- [Are attachments sync configurations configured individually with multiple Jira site integration?](/cms_trial/space/CSFJIRA/3092252732/Are+attachments+sync+configurations+configured+individually+for+multiple+Jira+site+integration%3F/)
- [What are the limitations of the multiple Jira site integration?](/cms_trial/space/CSFJIRA/3091925030/What+are+the+limitations+of+the+multiple+Jira+site+integration%3F/)