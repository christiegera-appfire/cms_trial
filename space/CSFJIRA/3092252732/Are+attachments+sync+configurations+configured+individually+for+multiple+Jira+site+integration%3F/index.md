# Are attachments sync configurations configured individually for multiple Jira site integration?

Yes, only Jira sites that have the **Synchronize Attachments** toggle enabled on the **Connections** page will have the attachment synced from the associated issues and Salesforce objects.

If there are two sites connected in the Salesforce environment, Jira Site A has turned on the **Synchronize Attachments** and Jira Site B turned it off, then Salesforce will only push/pull attachments from Jira Site A and not Jira Site B.

For more information on how to configure the attachment syncs, read [Working with attachments in Salesforce](/cms_trial/space/CSFJIRA/3091695099/Work+with+attachments+in+Salesforce/).

![contentId-3092252732](/cms_trial/assets/8b81306e-68c1-411e-8c32-c3518f64c168.png)

## Related content

- [Is there any difference in setting up the integration in Jira for the multi-site feature?](/cms_trial/space/CSFJIRA/3091597518/Is+there+any+difference+in+setting+up+the+integration+in+Jira+for+the+multi-site+feature%3F/)
- [How do I connect more than one Jira connection in my Salesforce environment?](/cms_trial/space/CSFJIRA/3091827403/How+do+I+connect+more+than+one+Jira+connection+in+my+Salesforce+environment%3F/)
- [How to view, create and associate Jira Issues from Salesforce by switching the Jira connection?](/cms_trial/space/CSFJIRA/2258010468/How+to+view%2C+create+and+associate+Jira+Issues+from+Salesforce+by+switching+the+Jira+connection%3F/)
- [Why can't I switch or view the Jira connection dropdown for the Lightning Aura and Visualforce components?](/cms_trial/space/CSFJIRA/3091335936/Why+can%27t+I+switch+or+view+the+Jira+connection+dropdown+for+the+Lightning+Aura+and+Visualforce+components%3F/)
- [What are the limitations of the multiple Jira site integration?](/cms_trial/space/CSFJIRA/3091925030/What+are+the+limitations+of+the+multiple+Jira+site+integration%3F/)