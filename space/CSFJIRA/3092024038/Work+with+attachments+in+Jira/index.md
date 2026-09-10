# Work with attachments in Jira

This page shows you how to handle attachments on the Jira side of the workflow when using Connector for Salesforce & Jira.

For an overview of how attachments work between Jira and Salesforce, view [Working with attachments](/cms_trial/space/CSFJIRA/1754432218/Work+with+attachments/).

## Before you start

An administrator must turn on the attachment synchronization feature through a [Connection setting](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/) called **Synchronize Attachments**.

## Push attachments from Jira to Salesforce

You can tell Jira when to push attachments to Salesforce:

- **Automatically** - when a file is attached to Jira, push it to Salesforce immediately. To achieve this, the association must be set to **Auto Push**.
- **Manually** - after attaching files to Jira, click the **Push** button available for the association.

When a push is triggered:

- All attachments in Jira will be pushed to Salesforce, regardless attached prior to or after the association.
- Attachments already existing in Salesforce (same name) will not be pushed to Salesforce again.
- The read-only association is not affected.

## Pull attachments from Salesforce to Jira

From inside Jira, you can retrieve attachments from Salesforce:

- **Automatically** - this is only configurable by administrators, as per [Configuring Automatic Pull from Salesforce](/cms_trial/space/CSFJIRA/1873446010/Configure+Automatic+Pull+from+Salesforce/).
- **Manually** - click the **Pull** button available for the association.

Similar to push:

- All attachments in Salesforce will be pulled to Jira, regardless of whether they are attached to Salesforce before or after the association.
- Attachment existing in Jira (same name) will not be pulled to Jira.
- The read-only association is not affected.

## Work with Salesforce Files

![Create Salesforce Attachment as Files.png](/cms_trial/assets/176fcaa9-0ba3-4478-9d89-dea8eb614a83.png)

Connector for Salesforce & Jira is compatible with the Salesforce Files feature.

To use the Connector with Salesforce Files, the **Create Salesforce Attachment as Files** setting must first be turned on by an admin through a [Connection setting](https://appfire.atlassian.net/wiki/spaces/470745117/pages/1463943741) called **Synchronize Attachments**.

Attachments attached to a Salesforce record using the Feed tab (Chatter) are supported as long as **Create Salesforce Attachment as Files** is enabled.

## Work with Synchronize Inline Attachments

![Synchronize inline attachments.png](/cms_trial/assets/3d99ea52-3dd4-442f-97ef-f7614d16c20c.png)

When **Synchronize Inline Attachments** is enabled, it ensures that once attachments/files are detected within a Jira comment, the connector synchronizes and creates a copy of the attachments in Salesforce.

When comments are rendered within the [Salesforce Jira Comment component (LWC)](https://appfire.atlassian.net/wiki/spaces/470745117/pages/1464402818), the links to the attachments/files point to the Salesforce attachment, not the Jira environment.

**Synchronize Inline Attachments** toggle is enabled automatically if the **Synchronize Attachment** toggle is enabled in [Connection settings](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/).

### Attachment size limits

### Bi-directional sync

The synchronization of attachments is affected if either limit is exceeded, whichever comes first.

- Maximum number of attachments per synchronization session: 50
- Maximum total size of attachments per synchronization session: 700MB

### Sync from Salesforce to Jira

- Attachment sync works for up to 350MB file size.

### Sync from Jira to Salesforce

- If **Create Salesforce Attachment as Files** in connection settings is **enabled**, attachment sync works for up to 350MB file size.
- If **Create Salesforce Attachment as Files** in connection settings is **disabled**, attachment sync works for up to 25MB file size.

  - When **Create Salesforce Attachment as Files** is disabled, files will be uploaded to the organization as **Salesforce Classic** which is limited to 25MB by Salesforce. See [File Size and Sharing Limits](https://help.salesforce.com/s/articleView?id=sf.collab_files_size_limits.htm&type=5) (Salesforce KB).
- Attachment size limits are also dependent on your Jira settings. As of May 2022, the default maximum attachment size is 1GB for Cloud and 10MB for Server/Data Center. This can be increased by the Jira admin. You should also be aware of total file storage limits if you are on the Standard plan.

  For more details, Jira admins can refer to these Atlassian KB pages:

  - [Configuring file attachments (Cloud)](https://support.atlassian.com/jira-cloud-administration/docs/configure-file-attachments/?__hstc=72543820.ab19c70c621fe76686456a1bcc7fc053.1645043228436.1651829678649.1652062197301.184&__hssc=72543820.9.1652062197301&__hsfp=370639710)