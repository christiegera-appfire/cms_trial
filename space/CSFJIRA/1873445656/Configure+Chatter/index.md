# Configure Chatter

With Chatter, you can post Jira comments to Case Feed (Chatter) or to an associated Jira issue. This integration is currently only supported for the Case type of records.

When someone creates or edits a comment in Jira, a post will be made to the Case Feed of the corresponding associated Case record and vice versa.

The post is made if:

- The Chatter Feed setting is enabled in Salesforce, per the guide below.
- The Jira or Chatter comment satisfies comment privacy and hashtag filters set by the administrator.
- The associated Jira issue is not marked as **View-only**.

The Chatter post is posted by the administrator account configured for the connection. This behavior cannot be changed due to limitations in the Salesforce Chatter API. However, a remark is provided to indicate the user who left the comment in Jira.

To enable Chatter integration in Jira, visit [Configure connection settings](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/) in Jira.

## Enable Chatter Feed

1. Log in to your Salesforce and click **Settings** > **Setup**.  
   If you are using Salesforce Classic, click **Setup** located on the upper right pane.
2. In the sidebar, use **Quick Find** and type `Installed Packages,` then click the **Installed Packages** link that appears.
3. Look for *Jira for Salesforce* and click **Configure**.
4. In the **Comment Configuration** section, enable the toggle next to **Chatter Feed**.

   ![chatter feed.png](/cms_trial/assets/435252e2-605c-4c64-87fa-9b12728cd98d.png)

## Next steps

- [Configure Visualforce components](/cms_trial/space/CSFJIRA/1873740233/Configure+Lightning+Web+components/)

## Related information

- [View Salesforce comments in Jira](/cms_trial/space/CSFJIRA/1962443468/View+Salesforce+comments+in+Jira/)
- [View Jira comments in Salesforce](/cms_trial/space/CSFJIRA/1962607212/View+Jira+comments+in+Salesforce/)