# Post migration

The **Post Migration** page is only visible on instances where JMWE has been migrated from **Jira Data Center/Server** to **Jira Cloud**.

The **Post Migration** page provides a way for you to view and address any issues that were encountered during the migration of workflows using JMWE Post-functions, Conditions, Validators, or any Actions (Shared, Scheduled, or Event-based) from **Jira Data Center/Server** to **Jira Cloud** using the Jira Cloud Migration Assistant (JCMA). These errors and warnings must be addressed in order for your transitions to function properly.

The Post Migration has four tabs - **JMWE extensions**, **Shared actions**, **Scheduled actions**, and **Event-based actions**.

## Migrated Extensions

**Note**: Only migrated Workflows that contain Extension errors and/or warnings are displayed in the Workflow dropdown menu.

![JMWE for Jira Cloud postmigration interface showing migration results and status](/cms_trial/assets/3acb31e3-38ad-435b-adb2-a96ec52dc60a.png)

The JMWE Extensions tab (Figure 1, right) lists all Conditions, Validators, or Post-functions that have been migrated to your Jira Cloud instance within Workflows. Select a **Workflow** to view the errors and warnings that must be addressed.

Once you have selected your workflow, you can group by:

- **Transition** - List extensions by their associated transition .
- **Extension type** - List each type of extension (Post function, Condition, Validator)*.*

Additionally, you can view either a **Summary** of the error, or **Details** giving a more descriptive reason for the error/warning.

From the list, you can drill down to individual extensions and view any errors or warnings that extension experienced during migration. Extensions can be updated using the **Edit** button in the far right column; see **Addressing errors and warnings**, below, for more information. Any issues detailed must be resolved before your workflows will function as designed.

## Migrated Actions

The other three tabs of the Post Migration page detail any Shared Actions, Scheduled Actions, or Event-based Actions that encountered issues during the migration. Similar to **Migrated Extensions**, above, each tab will list the action that encountered an issue; you can view either a **Summary**  of the error or the **Details** using the filter buttons at the top right of the table; you can update the action by using the **Edit** button (see below).

## Addressing errors and warnings

![JMWE for Jira Cloud detailed postmigration information with configuration status](/cms_trial/assets/b7877785-9cd7-4160-9944-5b42abb2177b.png)

To manually address each error:

1. Click the **Edit** button next to the error.
2. For individual extensions, a modal window (Figure 2, right) will open with a detailed description of the error or warning (or both) and the specific configuration field for the extension. For Shared Actions, Scheduled Actions, and Event-based Actions, the **Edit** button will open the action editor page.
3. You can update the configuration directly and once you have resolved all issues on the extension, click the **Save and resolve all problems** button. When you return to the Post Migration page, the error be removed from the list (you may need to refresh the page.)
4. For each item in the list you can also **Mark as resolved** (or **Mark all as resolved**) using the link in the upper right corner of the modal; this will retain the existing configuration and remove the item(s) from the list. Or you can click the **Save** button and return to this page later to finish any edits.
5. When all errors for a Workflow have been addressed, the Workflow will no longer appear in the **Workflow** dropdown. (This may require you to refresh the page.)

Repeat these steps for all Extensions or Actions listed in each of the tabs.

**Note**: Resolving all errors and/or warnings should result in your Workflows running correctly. However, as migration of JMWE is still considered a Beta process, it is **highly recommended** that you verify your Workflows before migrating your Production instance!