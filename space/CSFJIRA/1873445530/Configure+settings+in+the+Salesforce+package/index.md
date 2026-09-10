# Configure settings in the Salesforce package

This guide helps Salesforce administrators configure all the settings available for the Jira Cloud for Salesforce package to control data synchronization, Jira work item creation, comment synchronization, and feature access behavior for your Salesforce users.

## Access configuration settings of the Salesforce package

To find the settings:

1. In Salesforce, click **Settings** > **Setup**.
2. In the sidebar, use **Quick Find,** type *Package,* and go to **Installed Packages**.
3. Look for *Jira Cloud for Salesforce* (for Jira Cloud) and click **Configure**.

   ![2025-10-15_12-23-49.png](/cms_trial/assets/9ca0eb3d-b610-475a-93ce-6df5586cfa3d.png)

## Feature Toggles

**Feature Toggles** allow the administrator to disable product features that are available to users.

![Feature Toggles page on Salesforce](/cms_trial/assets/e40ffcb0-5ad9-4a9a-a42b-674624c7b616.png)

The following features can be toggled on or off:

- **Create Jira Issue**
- **Associate Jira Issue**
- **Push changes to Jira**
- **Pull changes from Jira**
- **Unlink issues**
- **Configure associations**
- **Sync email attachments**

Attachments can still sync even if you disable this feature because of Salesforce’s Email-to-Case Settings. For more information, refer to this [knowledge base](/cms_trial/space/CSFJIRA/3100541911/Why+do+email+attachments+still+sync+even+though+they+have+been+disabled+in+settings%3F/) article.

## Available Fields

This allows the administrator to specify which Jira fields should appear in the Jira issues Visualforce pages.

![Available Fields section on Salesforce](/cms_trial/assets/379b2d45-4f2e-4eb6-a440-14bf26457e8d.png)

Click **+ Add Jira Fields** to add more Jira fields.

## Issue Creation

This allows the administrator to configure the **Project Filter**.

![Issue Creation section on Salesforce](/cms_trial/assets/db9362cf-6fb7-4c5c-8ed6-b3dbb7a96dc2.png)

Use the **Project Filter** to filter which Jira projects are shown in the **Create Jira Issue** dialog box. However, only projects with a binding in Jira can be selected.

For more information, see [Filtering Projects in the Create Jira Issue dialog box](/cms_trial/space/CSFJIRA/1873511284/Filter+projects+in+the+Create+Jira+Issue+dialog+box/).

## Comment configuration

This section controls how synchronized Jira comments and Salesforce native comments are handled and displayed in Salesforce.

![Comment configuration](/cms_trial/assets/42ccf6ce-9c82-4d09-bcd8-483b0433e79b.png)

### Comment privacy

Determines which Jira comments are synchronized to Salesforce based on their visibility setting. Only comments that meet the configured privacy level are displayed in Salesforce. Comments restricted to a Jira project role are excluded entirely, ensuring that role-restricted content is not disclosed to unauthorized users.

The following options are available under **Visibility**:

- The **Show all** option synchronizes both internal and external comments to Salesforce.
- The **Show only unrestricted comments** option synchronizes only external comments.

Comments restricted to a Jira project role are excluded from synchronization, ensuring that role-restricted content is not disclosed to unauthorized users in Salesforce.

### Filter comments by tag

Jira comments shown in Salesforce can be filtered using hashtags (e.g. `#jira`, `#support`, `#customer_desk`), so Salesforce users only see the comments that matter to them instead of the full comment history.

Filters are configured separately for each platform:

- **Jira comments** tags control which Jira comments are shown in Salesforce in the **Jira Comments** component.
- **Salesforce comments** tags control which Salesforce comments are shown in the **Jira Comments** component.

For more information, see [Filtering Jira Comments in Salesforce Cases](/cms_trial/space/CSFJIRA/1873413366/Filter+Jira+comments+in+Salesforce+Cases/).

### Chatter feed

If enabled, Jira comments satisfying privacy and hashtag filters will be posted as Chatter Feeds for associated Cases (excluding view-only associations).

For more information, see [Configuring Chatter](/cms_trial/space/CSFJIRA/1873445656/Configure+Chatter/).