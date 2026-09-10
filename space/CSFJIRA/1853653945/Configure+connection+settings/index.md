# Configure connection settings

This guide helps administrators configure all the settings available for a Connection with Salesforce.

## Before you start

Make sure you have:

- Administrator rights in Jira - only administrators can set up the integration
- [Set up your integration to Salesforce in Jira](/cms_trial/space/CSFJIRA/1873412559/Set+up+your+integration+in+Jira/)

## Access the configuration settings

1. Select **Apps** from the left sidebar in Jira.
2. Next to *Connector for Salesforce,* click **Menu** (▢) > **App settings**.

   ![Appsettings.png](/cms_trial/assets/01d3c642-d271-44b4-b808-f67febaa8cb2.png)
3. Under *Connector for Salesforce*, click **Connections**.
4. Select a connection, then click **Configure**.

   ![image-20260813-123526.png](/cms_trial/assets/5f95fd93-48a3-4162-b902-2baf771dc511.png)

## Available Salesforce objects

Only Salesforce object types and fields explicitly added here are available for entity and field mapping, enabling associations between Jira work items and Salesforce records. The objects and fields you configure will be visible to end users through Connector features in Jira.

1. Click **Add Salesforce Object**.

   ![add Salesforce object](/cms_trial/assets/b612995c-895c-417f-a982-f3ecc906337e.png)
2. In the *Add Salesforce Object* window, select the Salesforce object type you want to make available in Jira.
3. Optionally, select **Import Layout** to automatically import the object's compact layout from Salesforce. This pre-populates fields based on the layout defined in Salesforce, saving manual field selection.
4. Click **Next**.

   ![Salesforce object selection](/cms_trial/assets/5aca1072-65c5-4799-bbf1-31dbc3e00d16.png)
5. From the **Salesforce Field** dropdown, select a field you want to make visible in Jira.   
   Fields added here will appear to end users in record views and mapping screens.
6. Click **Add.** Repeat for each field you want to include.

   ![Add Salesforce fields](/cms_trial/assets/778a974e-8acf-4203-8c20-34a6da8a8ce9.png)

1. Click **Next**.
2. Repeat steps 1–7 for each additional Salesforce object type required by your integration.
3. Click **Appy Changes** at the top of the page to save your configuration.

**Note:** Salesforce object types not added here will be unavailable for record mapping and association configuration. Make sure to add all object types your team works with, including custom objects.

For more information, see [Configuring Field Displays and accessing the Details Display screen](/cms_trial/space/CSFJIRA/1873511110/Configure+field+displays+and+access+the+Details+screen/).

## Jira Notification Settings

![contentId-1853653945](/cms_trial/assets/6ee65969-6fc6-483d-bcfe-1c38a483e6b6.png)

These settings enable the configuration of notifications when a comment is added for Jira users in a Salesforce Case.

Enable or disable notifications for the following users:

- **All recipients of Issue Commented event**
- **Current Assignee**
- **Reporter**
- **All Watchers**
- **All Voters**
- **Groups**

For more information, see [Configuring email notifications to notify Jira users](/cms_trial/space/CSFJIRA/1873413074/Configure+email+notifications+to+notify+Jira+users/).

## Connection Settings

![contentId-1853653945](/cms_trial/assets/fd30c322-bfcc-4564-ad2f-6bff3cbd107a.png)

Enable or disable the **Connection Settings** options:

### Allow Modification

If disabled, the connection will be in read-only mode. This setting has the highest precedence and overrides other settings.

Disable this setting if you need to immediately stop any synchronization.

### Allow Automatic Push

If disabled, the auto push is not allowed to function in all current and new associations.

If enabled, the auto push is allowed to function in all current and new associations.

### Allow Automatic Pull

If disabled, the auto pull is not allowed to function in all current and new associations.

If enabled, the auto pull is allowed to function in all current and new associations. Apex trigger must be configured for the associated object type.

### Salesforce Auto Assign

If enabled, active [assignment rules](https://help.salesforce.com/articleView?id=creating_assignment_rules.htm&type=5) will be used when creating or updating Case and Lead objects.

## Attachment Settings

![contentId-1853653945](/cms_trial/assets/1296ecd6-a7fb-4508-a5b1-f7927f654f27.png)

For more information about file attachments, view [Working with attachments](/cms_trial/space/CSFJIRA/1754432218/Work+with+attachments/).

### Synchronize Attachments

If enabled, files attached to associated issues and Salesforce records will be synchronized.

### Create Salesforce Attachment as Files

If enabled, files will be uploaded as Salesforce files, not attachments. Requires **Synchronize Attachments** to be **Enabled**.

This setting is recommended if you use Salesforce Lightning.

## Comments and Chatter settings

### Comment Privacy

Select which Salesforce comments are visible in Jira based on their privacy.  
Available options: **All** **Comments, Public Comments Only, Private Comments Only**.

![Comment Privacy](/cms_trial/assets/4b095829-1a15-4656-a70a-a53ac182887b.png)

### Filter Comments by Tag

Only show comments that include specific tags. Set separately for Jira and Salesforce. The comments are rendered in the **Salesforce Comments** tab in Jira.

- The **Salesforce Comments** tags filter Salesforce comments and render them in the **Salesforce Comments** tab in the Jira work item.
- The **Jira Comments** tags filter Jira comments and render them in the **Salesforce Comments** tab in the Jira work item.

  ![Filter comments by tag](/cms_trial/assets/5a7b2117-8564-45bd-a39e-afbd9f33af94.png)

For more information, see [Filter Salesforce comments in Jira work items](/cms_trial/space/CSFJIRA/1873380322/Filter+Salesforce+comments+in+Jira+work+items/).

### Show Chatter feeds

Enables displaying the Salesforce Chatter feed in the **Salesforce Comments** tab, alongside synced comments.

For more information, see [Working with comments](/cms_trial/space/CSFJIRA/3091628846/Work+with+comments/).

With Lightning Experience, the way you can view Chatter feeds is different. For more information, see [Add comments in Salesforce (Chatter Feed and Case)](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=csfjira&title=Configure%20Jira%20comments%20%28NextGen%29%20with%20Lightning%20Experience&linkCreation=true&fromPageId=1853653945).

## Query Optimization

### Optimize the association JQL query

If enabled, this option can help improve performance by fine-tuning the JQL query that retrieves Salesforce and Jira associations, where it will be limited to projects with active binding. This option is disabled by default because the issue usually only affects projects with a very large number of Jira issues (around 5,000 or more).

![Query Optimization.png](/cms_trial/assets/236d3914-7e4c-48d8-948c-de0210a958dc.png)

## Default Presets

These settings allow admins to set defaults for what happens when a user creates or associates a Jira Issue/Salesforce Object.

![Default presets.png](/cms_trial/assets/90b8e082-b203-4058-b67c-9d628258b015.png)

### Limit the "Associate" feature to project / issue type with binding only

If enabled, you can’t associate unmapped Salesforce object types with Jira items.

### Force All Presets

Enabling this will allow admins to force all the presets that have been set below, both inside Jira and Salesforce. This will also completely hide the presets from being shown to users when they create or associate a JIRA Issue/Salesforce Object.

### View Only

If enabled, new associations will be set to **View Only** by default when users create or associate a Jira Issue/Salesforce record.

### Automatic Push

If enabled, new associations will be set to **Automatic Push** by default when users create or associate a Jira Issue/Salesforce record.

### Automatic Pull

If enabled, new associations will be set to **Automatic Pull** by default when users create or associate a Jira Issue/Salesforce record.

### After Associating

Admins can set the default action that happens immediately after an association.

Available Values:

- **Do nothing**
- **Push to Salesforce**
- **Pull from Salesforce**
- **Push to Salesforce then Pull from Salesforce**
- **Pull from Salesforce then Push to Salesforce**

### After Creating Jira Issue

Admins can set the default action that happens immediately after Jira Issue creation.

Available Values:

- **Do Nothing**
- **Push to Salesforce**

### After Creating Salesforce record

Admins can set the default action that happens immediately after Salesforce record creation.

Available Values:

- **Do Nothing**
- **Pull from Salesforce**

## Rich text setting

Before you start [creating Jira work items](/cms_trial/space/CSFJIRA/3091792703/Create+a+Jira+work+item+from+Salesforce/) from Salesforce, you can choose how to display the multiline fields editor in the **Create Jira issue** window. By default, all multiline fields use a rich text editor. If you prefer plain text formatting, you can disable the rich text editor, and the plain text setting will apply to all Jira work items you create from Salesforce.

![rich text setting.png](/cms_trial/assets/0378754e-393b-410d-91f5-79793f07bca7.png)

## Apply changes

When you’re ready with all your configuration, make sure you click the **Apply Changes** buttonto save all your settings.