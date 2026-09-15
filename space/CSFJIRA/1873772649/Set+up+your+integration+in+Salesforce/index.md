# Set up your integration in Salesforce

Follow this step-by-step guide to set up Connector for Salesforce & Jira on the Salesforce side. This page hosts all administrator guides for configuring the integration in Salesforce, from establishing a secure remote site connection to enabling automated synchronization.

**Before you start**

Make sure you have:

- Administrator rights in Salesforce - only administrators can set up the integration.
- [Installed the Connector app in Jira](/cms_trial/space/CSFJIRA/1873412370/Install+the+Connector+in+Jira+Cloud/).
- [Set up your integration in Jira](/cms_trial/space/CSFJIRA/1873412559/Set+up+your+integration+in+Jira/).
- [Installed the Jira for Saleseforce package in Saleseforce](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/).

Want a quick overview before diving in? The interactive walkthrough below covers the first four steps end-to-end:

<https://app.arcade.software/share/cqU23vvN1jaqfjoYxOTT>

### Follow the steps to set up your integration in Salesforce

1. [Add a remote site](/cms_trial/space/CSFJIRA/1873412619/Add+new+remote+site/) to provide a safe connection from Salesforce to your Jira.
2. [Set up a connection to Jira](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/).
3. [Configure the Salesforce record page to view Jira details directly in Salesforce](/cms_trial/space/CSFJIRA/3608707174/Configure+Salesforce+record+page+to+view+Jira+details+directly+in+Salesforce/)

1. Associate Salesforce records with Jira issues to see all related details in Salesforce and configure the synchronization behavior:

   - [For NextGen](/cms_trial/space/CSFJIRA/3092284698/Associate+a+Jira+work+item+from+Salesforce+with+Jira+Issues+(NextGen)/)

1. (Optional) Enable automatic synchronization with Jira with Flow Builder: [Automatically create Jira work items with Salesforce Flows](/cms_trial/space/CSFJIRA/3627581468/Automatically+create+Jira+work+items+with+Salesforce+Flows/)   
   Or with Apex triggers:

   - [Configure automated synchronization from Salesforce](/cms_trial/space/CSFJIRA/1873446010/Configure+Automatic+Pull+from+Salesforce/).
   - [Configure automated Jira issue creation from Salesforce](/cms_trial/space/CSFJIRA/1873413628/Configure+automatic+Jira+issue+creation+from+Salesforce/).
   - [Enable status synchronization from Salesforce to Jira](/cms_trial/space/CSFJIRA/1874002066/How+to+enable+status+transition+from+Salesforce+to+Jira+using+Automation+for+Jira/) to allow the pushing of status updates from Salesforce to Jira.