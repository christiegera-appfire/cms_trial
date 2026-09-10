# Script Storage configuration

Power Scripts for Jira Cloud provides two storage methods for your scripts: disk storage (default) and database storage. The choice of a script storage option affects script execution speed, backup procedures, and system administration.

- Disk storage provides better performance and easier access to script files.
- Database storage simplifies migration between Jira instances.

Scripts can be transferred between storage methods as needed to accommodate changing requirements. Understanding the advantages and limitations of each storage option can help you make an informed decision for your environment.

**Limitations**

- Only SIL scripts are eligible for database storage. Other configuration files (such as mail templates) remain on the file system regardless of this setting.

## How to access the Script Storage configuration

Click **Power Scripts** > **Settings** > **SIL storage**.

![Power Scripts for Jira Cloud SIL Help panel interface](/cms_trial/assets/a03de52f-2a62-461c-bd4c-399d3cfcbf99.png)

Select your preferred script storage option from the **Default storage** drop-down menu, which contains the two options: **disk** and **database**.

Scripts created after changing the storage setting will use the newly selected storage option, while existing scripts remain in their original location.

## How to select the appropriate storage option

When selecting a storage option, consider the key differences between the database and disk storage options. This table outlines the major advantages and disadvantages of each storage option:

| **Script storage option** | **Advantages** | **Disadvantages** |
| --- | --- | --- |
| **Database** | - Simplified file management when migrating scripts between Jira instances. - Data protection through standard database backups. - Script files are not stored on the disk, keeping it clean. | - Slightly slower script access performance. - Limited access to scripts outside the SIL Manager. |
| **Disk** | - Scripts can be versioned and backed up by using a Git repo on the file system. - Faster script execution performance. - Scripts are easier to access. | - Additional security considerations for scripts can be required. - More complex migration between Jira instances. |

### General recommendations

Consider these recommendations when selecting between disk and database storage for your SIL scripts:

|  |  |
| --- | --- |
| **For most environments** | We recommend using disk storage. It's faster, easier to use, and provides additional benefits beyond script storage that advanced users can find valuable. |
| **Exception for multi-node setups** | If your file system isn't configured to 100% of Atlassian's guidelines, you might experience file sharing delays between nodes. While this usually goes unnoticed, editing scripts across nodes can take several seconds to propagate. In these specific scenarios, database storage can help alleviate these issues. |

## Other storage configuration settings

In addition to the two storage options, Power Scripts for Jira Cloud uses several key configuration settings to manage script storage and access.

### Virtual directory and script virtualization

Script virtualization in Power Scripts for Jira Cloud creates an abstraction layer between how scripts are referenced and where they're physically stored. This enables scripts to function consistently regardless of their storage location (disk or database).

The **Virtual Directory** option defines how the system references script locations. When a script is accessed, the system uses this virtual path to locate the correct script, whether it's physically stored in the database or in the specified disk location.

| **Virtual Directory** | **Virtual path** |
| --- | --- |
| `sil` | `/pscloud/silprograms` |

### SIL Home Directory

The **SIL Home Directory** indicates the path on the server that is used to store your SIL scripts. This directory is created when Power Scripts is first installed in the cloud environment. The directory path typically follows a pattern such as `/pscloud/silprograms`. Keep in mind that all references in your configuration are relative to this directory.

Changing your **SIL Home Directory**:

- If you move the SIL Home Directory after you've created scripts or established script references, you should manually copy all files involved in your specific configurations.
- When migrating between Jira instances, if the Jira home directory path changes, you'll need to update the SIL Home Directory setting. Otherwise, any automated processes or configurations that reference your scripts will point to incorrect locations, causing them to fail.

### Bulk storage change

A bulk migration utility is available to transfer scripts between storage locations. Note that this tool affects only SIL scripts, not supplementary files (HTML, JavaScript, CSV, text) that experienced scripters often use alongside their scripts.  
When switching between script storage options, the bulk storage change feature lets you migrate all your scripts between storage locations at once. To use this feature:

1. Navigate to the *Script Storage* configuration page.
2. Locate the *Bulk storage change* section at the bottom of the page and select one of the available options:

   - To transfer scripts for database to disk storage, click **Move all scripts to disk**.
   - To transfer scripts from disk to database storage, click **Move all scripts to DB**.

**Important considerations:**

- This operation only affects SIL files and their includes. Other file types (HTML, JavaScript, CSV, text) remain in their original location.
- Individual scripts can be migrated between storage locations through the SIL Manager if you prefer to move scripts selectively rather than all at once.
- Ensure you have adequate permissions and system resources before initiating a bulk migration, as the process may take time depending on the number of scripts.

After migration completes, verify that your scripts are functioning correctly in their new storage location.