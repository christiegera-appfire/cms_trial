# Set up a connection to Jira

This guide helps administrators configure the Jira Cloud for Salesforce package in Salesforce to connect to a Jira instance.

## **Before you start**

Make sure you have:

- Administrator rights in Salesforce - only administrators can set up the integration
- [Installed the Connector app in Jira](/cms_trial/space/CSFJIRA/1873412370/Install+the+Connector+in+Jira+Cloud/)
- [Set up your integration in Jira](/cms_trial/space/CSFJIRA/1873412559/Set+up+your+integration+in+Jira/)
- [Installed the Jira for Saleseforce package in Saleseforce](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/).
- [Added the remote site](/cms_trial/space/CSFJIRA/1873412619/Add+new+remote+site/)

## Configuration

1. In Salesforce, click **Settings** (▢)> **Setup**.  
   If you are using Salesforce Classic, click **Setup** in the upper-right pane.
2. In the **Quick Find** box, type *Package* and go to **Installed Packages**.
3. Look for the *Jira Cloud for Salesforce* package and click **Configure**.

   ![The Configure Installed Packages page in Salesforce](/cms_trial/assets/575a6eb0-e61b-4e59-99cc-f3891b79b2f6.png)
4. When you click **Add Connection,** you will be asked to generate an **Access Token** in Jira.   
   Keep this page open so you can return to it once you generate a Jira access token.
5. Open your Jira administrator page.
6. Navigate to **Jira** > **Apps** > **Salesforce**.
7. Choose your **Connection**, then click **Menu** (▢)> **API Access Token.**

   ![API Access Token option for Salesforce connections](/cms_trial/assets/dbe06401-c8ab-4040-a5d3-623c616d1dd9.png)
8. The *API Access Token*dialog window appears with the **Salesforce access token.**

   ![Salesforce access token shown in the API Access Token page.](/cms_trial/assets/f6a693f8-922d-4262-8eba-36fd97eb82f4.png)
9. Copy the **Salesforce Access Token** and go back to the *Jira Cloud for Salesforce* package configuration screen you kept open from *Step 4*.
10. Paste the Salesforce Access Token under **Access Token** in the *New Connection* window.

    ![Access token field for a new Salesforce connection](/cms_trial/assets/0d5dfcf4-7d7d-458d-bfb1-2cd6a5cf4121.png)

    If you receive an *Unauthorized Endpoint* error message at this point, refer to this [knowledge base](/cms_trial/space/CSFJIRA/3100410230/How+to+resolve+Unauthorized+Endpoint+or+The+session+has+expired.+Please+refresh+the+page+error./) article.
11. Click **Save.**
12. The Salesforce Package now has a connection to your Jira Cloud instance.

    ![The new Jira connections shown in the connections list.](/cms_trial/assets/7d60e601-0d86-4f84-aa6c-d4989d4fb51f.png)

## Next steps

- [Configure Lightning Experience components](/cms_trial/space/CSFJIRA/1873969162/Configure+Lightning+Experience+components/)
- [Configure settings in Salesforce](/cms_trial/space/CSFJIRA/1873740170/Configure+settings+in+Salesforce/)
- If you are using Salesforce Classic, see: [Configure Visualforce components](/cms_trial/space/CSFJIRA/1873445794/Configure+Visualforce+components/)