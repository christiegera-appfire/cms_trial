# Work with attachments in Salesforce

This page shows you how to handle attachments on the Salesforce side of the workflow when using Connector for Salesforce & Jira.

For an overview of how attachments work between Jira and Salesforce, visit [Work with attachments](/cms_trial/space/CSFJIRA/1754432218/Work+with+attachments/).

## Before you start

- The attachment synchronization feature must be turned on by an administrator through a [Connection setting](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/) called **Synchronize Attachments**.
- To prevent duplicate attachments and ensure proper file processing, follow these guidelines when naming files:  
  Do not use the following characters in filenames:

  - `/` (slash)
  - `?` (question mark)
  - `*` (asterisk)
  - `:` (colon)

## Push Salesforce attachments to Jira

You can tell Jira when to push attachments to Salesforce:

- **Automatically** - when a file is attached to Jira, push it to Salesforce immediately. To achieve this, the association must be set to **Auto Push**.
- **Manually** - after attaching files to Jira, click the **Push** button available for the association.

When a push is triggered:

- All attachments in Jira will be pushed to Salesforce, regardless attached prior to or after the association.
- Attachments already existing in Salesforce (same name) will not be pushed to Salesforce again.
- The read-only association is not affected.

## Pull Jira attachments from Salesforce

From inside Salesforce, you can retrieve attachments from Jira:

- **Automatically** - when the association is configured with **Auto Pull**.

  - Click **Configure** >**Auto Pull**.
- **Manually** - click **Pull** in the pull-down menu available for the association.

Similar to push:

- All attachments in Jira are pulled to Salesforce, regardless attached to Jira prior to or after the association.
- Attachment that already exists in Salesforce (same name) will not be pulled to Salesforce.
- The read-only association is not affected.

## Work with Salesforce Files

![Attachment Settings.png](/cms_trial/assets/ddfebadb-d4df-4e69-ad3f-a14781533857.png)

Connector for Salesforce & Jira is compatible with the Salesforce Files feature.

To use the Connector with Salesforce Files, the **Create Salesforce Attachment as Files** setting must first be turned on by an admin through a [Connection setting](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/) called **Synchronize Attachments**.

Attachments attached to a Salesforce record via the Feed tab (Chatter) are supported as long as **Create Salesforce Attachment as Files** is enabled.

## Work with Synchronize Inline Attachments

![Synchronize inline attachments.png](/cms_trial/assets/eaf32c7b-9590-4893-b72b-b08e80cd0edd.png)

When **Synchronize Inline Attachments** is enabled, it ensures that once attachments/files are detected within a Jira comment, the connector synchronizes and creates a copy of the attachments in Salesforce.

When comments are rendered within the [Salesforce Jira Comment component (LWC)](/cms_trial/space/CSFJIRA/1873478551/Work+with+Jira+comments+(NextGen)+with+Lightning+Experience/), the links to the attachments/files are pointing to the Salesforce attachment and not the Jira environment.

**Synchronize Inline Attachments** toggle is enabled automatically if the **Synchronize Attachment** toggle is enabled in [Connection settings](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/).

### Attachment size limits

### Bi-directional sync

The synchronization of attachments is affected if either limit is exceeded, whichever comes first:

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
  - [Configuring file attachments (Server and Data Center)](https://confluence.atlassian.com/adminjiraserver/configuring-file-attachments-938847851.html?__hstc=72543820.ab19c70c621fe76686456a1bcc7fc053.1645043228436.1651829678649.1652062197301.184&__hssc=72543820.9.1652062197301&__hsfp=370639710)