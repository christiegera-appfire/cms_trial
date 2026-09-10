# File upload storage management

To view the storage location where files uploaded through the Forms and Wizards feature are temporarily stored:

1. Open the **Apps** page from your Jira Administration Settings.
2. Navigate to **Power Scripts** > **Configurations** > **Automations** > **Forms and Wizards**.

The **File upload storage location**field in the *File Storage Configuration* section shows where files are temporarily stored when users upload them through Forms and Wizards. Files are uploaded immediately after selection before the action is executed.

No automatic cleanup is performed on the temporary upload directory. Scripts must use the [deleteFile](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15488990) function to remove files after processing. Note that if users upload files and then cancel the action execution, files will remain stored on the disk and might require regular manual cleanup.