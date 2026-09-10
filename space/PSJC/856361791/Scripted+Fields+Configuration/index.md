# Scripted Fields Configuration

## Manage Scripted Custom Fields

Go to **Administration > Manage Apps > Power Apps Config > Advanced > Scripted Fields** to manage Scripted Custom Fields.

![Power Scripts for Jira Cloud scripted field settings](/cms_trial/assets/148c4a61-4175-4b4d-82a0-df64e716220a.png)

### **Field Descriptions**

| Column | Description |
| --- | --- |
| Custom Field | The custom field that will receive an update when the script is triggered and run. |
| Script | The full path to the file. Click the path to access the file in the SIL Manager. |
| Filters | The project categories / projects / issue types that should be used to trigger the script. If the fields are left blank, the configuration will be global. |
| Operations | Sync, Edit and Delete buttons. |

## Add a Scripted Field

Each Scripted Field entry represents a script that runs for an event. When a Scripted Field is added, define the following properties:

- **Existing fields** - Use an existing custom field to receive the update from a script.
- **New field** - Create a new custom field to be updated from a script.

  - **Custom field name** - The name that should be used for the custom field that will be created.
  - **Custom field type** - The type of standard Jira custom field that will be created.
- **Trigger on** - Optional triggers that can be set to also trigger the script execution on related issues to make sure scripted fields on those issues stay up to date.

  - **Child update** - If 'Child update' is set to true, the child issue is updated and current issue(parent) has a Scripted Field that matches the project and issue type(s) filter, the scripted field will be recalculated for that (parent) issue.
  - **Parent update** - If 'Parent update' is set to true, the parent issue is updated and current issue(child) has a Scripted Field that matches the project and issue type(s) filter, the scripted field will be recalculated for that (child) issue.
  - **Linked issue update** - If 'Linked issue update' is set to true, the linked issue is updated and current issue has a Scripted Field that matches the project and issue type(s) filter, the scripted field will be recalculated for that issue.
- **Project category filter** - The project categories that should be used to trigger the script. Only selected project categories will trigger the script to update the field.
- **Project filter** - The projects that should be used to trigger the script. Only selected projects will trigger the script to update the field.
- **Issue type filter** - The issue types that should be used to trigger the script. Only selected issue types will trigger the script to update the field.

If you have a large number of issues (100,000+), it is strongly recommended to specify both project and issue type filters for each configuration. This breaks the synchronization process into smaller, more manageable batches, ensuring complete and successful field value calculation across your Jira instance.

- **SIL Script** - The existing SIL script that will be used to calculate the value for the custom field.
- **Synchronize issues after save** - The value of the script will be applied on the issues returned by the filters for the existing / just created custom field.

![Power Scripts for Jira Cloud script performance monitoring interface](/cms_trial/assets/80d16fe8-6556-4339-a11d-030d0078c3a3.png)

## Synchronize values of a Scripted Field

To synchronize the values, click the Synchronize icon in the **Operations** column on the **Scripted Custom Fields** page. The sync will start and all the other operation will be blocked. The status of the synchronization will be showed in a tool tip when the mouse is over the sync in progress.

![Power Scripts for Jira Cloud security configuration interface](/cms_trial/assets/b05529a8-d9d2-4d2f-a180-682c9826fe3b.png)

## Update a Scripted Field

To update a scripted custom field, click the Edit icon in the **Operations** column on the **Scripted Custom Fields** page and update the fields in the pop-up window.

## Delete a Scripted Field

To remove a scripted custom field, click the **Delete** icon in the **Operations** column on the **Scripted Custom Fields** page.