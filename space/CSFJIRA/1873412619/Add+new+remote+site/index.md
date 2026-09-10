# Add new remote site

Add a Remote Site to allow a safe connection from Salesforce to your Jira.  
If you're using Jira Cloud, Salesforce must connect to an intermediary server we host.

### **Before you start**

Make sure you have:

- Administrator rights in Salesforce - only administrators can set up the integration
- [Installed the Connector app in Jira](/cms_trial/space/CSFJIRA/1873412370/Install+the+Connector+in+Jira+Cloud/)
- [Set up your integration in Jira](/cms_trial/space/CSFJIRA/1873412559/Set+up+your+integration+in+Jira/)
- [Installed the Jira for Salesforce package in Salesforce](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/)

### Configuration

1. In Salesforce, in the upper right corner, click the gear icon (▢) and select **Setup**.
2. In the **Quick Find** box, type `Remote Site Settings`.

   ![Remote Site Settings](/cms_trial/assets/5e2fb0e9-476e-46b6-aeed-eb14a75e2725.png)
3. From the results, click **Remote Site Settings**.
4. Click **New Remote Site** on the *All Remote Sites* screen.

   ![2025-10-15_09-07-51.png](/cms_trial/assets/0dc6a000-c5da-466c-9bce-eed676fa5b22.png)
5. On the **Remote Site Edit** screen, enter the following details:  
   To ensure connectivity regardless of your data residency location, we recommend adding two remote sites for Jira Cloud:

   - **Remote Site Name:** `Global`  
     **Remote Site URL:** `https://sfjc.integration.appfire.app` (Global)

     ![image-20250430-083628.png](/cms_trial/assets/0ec5ce0e-7d90-4a32-a90e-0a7210694466.png)
   - **Remote Site Name:** `Europe`  
     **Remote Site URL:**  `https://eu-sfjc.integration.appfire.app` (Europe location)

     ![2025-11-07_09-43-16.png](/cms_trial/assets/86448596-1542-4351-a8db-1ca2da23db6b.png)

1. Click **Save**

## Next steps

- [Set up a connection to Jira](/cms_trial/space/CSFJIRA/1873379599/Set+up+a+connection+to+Salesforce+(Jira+Cloud)/)
- [Use Jira Issues NextGen with Lightning Experience](/cms_trial/space/CSFJIRA/1873543771/Use+Jira+Issues+(NextGen)+with+Lightning+Experience/)