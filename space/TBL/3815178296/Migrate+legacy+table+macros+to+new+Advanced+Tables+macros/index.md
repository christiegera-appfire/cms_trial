# Migrate legacy table macros to new Advanced Tables macros

## Overview

The Advanced Tables for Confluence app is deprecating the CSV, JSON Table, and Table Plus legacy macros. You can migrate these macros to Advanced Table Viewer and Native Table Enhancer, which receive ongoing updates and new features.

This page guides Administrators on how to migrate legacy macros - CSV, JSON Table, and Table Plus macros to the new macros. Administrators can scan a space for legacy macros, review the expected changes, and migrate the selected macros in bulk.

### **Legacy macro mapping**

The following table shows which macro replaces each legacy macro.

| **Legacy macro** | **New macro** |
| --- | --- |
| CSV | Advanced Table Viewer |
| JSON Table | Advanced Table Viewer |
| Table Plus | Native Table Enhancer |

### Limitations

- Migration does not support the Attachment Table macro.
- Migration skips Table Plus macros that contain no content, Jira content, or only text.
- Migration skips JSON Table macros that contain nested table structures or load data from an attachment, profile, or URL.
- Migration skips CSV macros that contain no content.
- If a CSV macro uses a data profile, the profile must remain available after migration. Otherwise, the migrated macro displays an error message.
- Migration does not include blog posts and draft pages.
- Migration fails for macros that use files larger than 10 MB because the Advanced Table Viewer macro supports file sizes of up to 10 MB.
- You can migrate macros in one Confluence space at a time.
- You can't roll back an entire bulk migration. However, you can restore an earlier version of an individual page from its Confluence version history to reverse its migration changes.

## Migrate legacy macros

You need Confluence administrator permissions to migrate legacy macros.

### Navigate to the Migration page

1. Log in as a Confluence administrator and click **Settings**(▢).
2. In the left navigation, under **Apps**, click **Advanced Tables Configuration**.
3. The **Advanced Tables** **Configuration** page opens.

   ![AT_configuration page.png](/cms_trial/assets/6f26101e-105f-4a25-8311-74d6738e3017.png)
4. To open the Migration page, click **Migration**.
5. To start the migration process, click **Set up migration**.

   ![Legacy macro_migration page.png](/cms_trial/assets/58c10660-5a05-4953-be37-8eb194d1f104.png)

### Set up migration

The Set up migration page shows the steps to migrate legacy macros.

The migration process has three steps:

1. [Select space](#Select-space)
2. [Select macros](#Select-macros)
3. [Review and Run migration](#Review-and-Run-migration)

![Legacy macros_Set up migration.png](/cms_trial/assets/f378573d-b3f8-408d-adc8-535598b436fc.png)

#### Select space

Select the Confluence space containing the legacy macros you want to migrate. You can migrate a single space at a time.

1. In this step, define the scope of migration:

- **Space**: Select a space to scan pages with legacy macros.
- **Label**: This is optional, and you can enter only one label.

  - Enter a label to scan only pages with that label. The pages matching the specified label are scanned for legacy macros.
  - Leave the field empty to scan all pages in the selected space that contain legacy macros.

1. To start the scan, click **Scan space**.

![Set up migration_select space and label.png](/cms_trial/assets/b6b2bba7-520f-4249-adbe-c82d848a0dbb.png)

#### Select macros

After the scan completes, the page displays a list of legacy macros found on each page and live docs, along with their impact and expected changes during migration.

![Legacy migration_step2_select macros.png](/cms_trial/assets/2f00b8ef-c89f-4169-b1eb-8366620355ff.png)

- Pages already migrated completely do not appear again in a later scan.
- If no macros are found, it displays a message.

![No macros found.png](/cms_trial/assets/f07d2e2b-b784-4672-9e99-0e46ec2be7b0.png)

- To view pages and macros with specific impact, navigate to the **All**, **No data loss**, **With changes**, and **Blocked** tabs. Each displays a table listing pages, macros, and details about the specific impact and expected changes.

| **Tab** | **Description** |
| --- | --- |
| All | Displays all legacy macros found during the scan. Legacy migration_step2_select macros.png |
| No data loss | Displays macros that can be migrated without data loss. Step 2_No data loss.png |
| With changes | Displays macros that can have visual or functional changes after migration. Step 2_with changes.png |
| Blocked | Displays macros that can’t be migrated. These macros are automatically excluded from bulk migration. Step 2_migration blocked.png |

- Each tab contains the following columns.

  - - **Page/Macro**: Displays the page name and the number of macros with expected changes. Expand a page to see the macros.
    - **Impact**: Impact shows the type of changes you will see after migration, such as visual differences, functionality changes, or no data loss. If a macro cannot be migrated, the impact is *Migration blocked*.
    - **Expected changes**: This column provides details on the visual changes you will see after migration and any post-migration checks needed. For macros with blocked migration, it explains why migration is not possible.
- To continue:

1. 1. Select the macros you want to migrate.
   2. Clear the selection for any macros you want to exclude.
   3. Click **Review migration**.

![Legacy migration_review migration.png](/cms_trial/assets/4823c296-2029-4480-b522-bcce8552c90a.png)

- To navigate to the previous screen, click **Back**.
- To navigate back to the main **Migration** screen, click **Back to migration**.
- To find specific pages or macros, use the **search bar**.

#### **Review and Run migration**

The **Review and Run migration** screen shows the final migration details. It displays the number of pages and macros selected for migration, with full details in the table.

You cannot roll back a bulk migration. To reverse the migration changes on an individual page, restore an earlier version of that page from its Confluence version history.

- Review the selected pages, macros, and migration impact.
- To change your selection, click **Edit selection** or **Back**.
- Read the bulk migration acknowledgment and select the checkbox.
- Click **Run migration**.

  ![Legacy migration_review and run migration.png](/cms_trial/assets/0f068660-3a8d-4fdb-b47c-99e2678c2363.png)

- If you delete a selected page after scanning but before running the migration, migration fails for that page.
- If any of the pages selected for migration is edited and published just before running the migration, the migration uses the latest edited version of macros on that page.

#### Migration results

After the migration completes, the results page displays the migration status and details for each macro.

The migration result can be:

| **Migration result** | **Description** |
| --- | --- |
| Migration completed successfully | All selected macros are migrated successfully. |
| Migration completed with errors | Some macros were migrated, and some failed. |
| Migration failed | None of the macros were migrated. |

- The results table includes the list of pages and macros migrated:

  - **Result**: Shows the migration result for each macro.
  - **Changes or error column**: Describes any visual or functional changes, recommended post-migration checks, or errors encountered during migration.
- To view the list of pages and macros with specific impact, navigate to the **All**, **No data loss,** **With changes, and Failed** tabs. Each displays a table listing migrated macros and impact details.
- Click **Done** to return to the Migration page.

  ![Legacy migration_migration results.png](/cms_trial/assets/3242fd9d-f1f2-4e9f-add0-7c53aa53a9c9.png)

#### View pages after migration

To open a migrated page from the migration results, click the page name.

![Legacy_view page after migration.png](/cms_trial/assets/c7ea58bd-b503-4889-a461-99ff833f3e60.png)

If a legacy macro is not configured correctly or its format is not supported, the page shows the error: *The macro is not configured correctly*.

## Migration history

Advanced Tables records each migration, including migrations that are completed, failed, and completed with errors. You can review previous migrations in the Migration history section.

The **Migration history** section displays the details for each migration, such as Date, Space, Scope, Status, Created by, and Actions.

![AT_Migration history.png](/cms_trial/assets/3c48057d-0b10-4e99-817c-65131868ef42.png)

- **Date:** The date when the migration ran.
- **Space:** The Confluence space included in the migration.
- **Scope:** The migration scope.
- **Status:** The migration status - Completed, Failed, or Completed with errors.
- **Created by:** Who initiated the migration.
- **Actions:** This column displays the actions based on the migration result status.

  - **View**: A migration record with **Completed** and **Completed with errors** status shows the **View** action.

    - Click **View** to review the complete details of the Migration result.

      - For migrations with **Completed with errors** status, you have an option to retry the migration for the failed macros.
      - To re-run the migration only for the failed macros, click ▢ > **Retry failed macros**.

        ![Completed with errors_retry.png](/cms_trial/assets/37b09cee-1772-4b25-a891-1030d5f67a2d.png)
  - **Retry**: A migration record with **Failed** status shows the **Retry** action.

    - Click **Retry** to re-run a failed migration.
    - You can remove a failed migration from the Migration history; click ▢ > **Remove migration**.

      ![Legacy macro_Remove migration.png](/cms_trial/assets/0d0180dd-271e-4916-83e3-80ca08aed9a7.png)
    - The *Remove migration* warning dialog opens.
    - To confirm, click **Remove migration**. This removes this record from the migration history.

      ![image-20261102-121035.png](/cms_trial/assets/b97d9193-2df4-4390-97b2-7926715a3988.png)