# Scripted Field

The **Scripted** custom field types are a set of calculated fields that utilize JavaScript to calculate a return value, usually based on other field values. They are read-only fields. Within **JMCF for Jira Cloud**, there are several types of scripted fields, each corresponding to the type of value the script returns (the script **must** return the data type of the field).

The scripts for Scripted Fields will be executed with App-level permissions.

**Note**: If a scripted field encounters an error during calculation or recalculation, the calculation of that field will pause. Other custom fields in your instance will continue to (re)calculate.

Errors with a scripted field will be displayed in the [Error Logs](/cms_trial/space/JMCFC/465436864/Error+Logs/) page; errors **will not** be indicated on issue screens. The only indication of an error in a field recalculation will be:

- If the field is new and has never been calculated, the value will remain `None`.
- If the field’s script returns a value of `undefined`, the value will display `None`.
- If the error occurred during recalculation, the field value will fail to update.

## Field types

The following scripted field types are currently available:

- **Scripted string** - Returns a string value.
- **Scripted date** - Returns a date value.
- **Scripted datetime** - Returns a datetime value.
- **Scripted number** - Returns a number value.
- **Scripted user** - Returns an Atlassian account ID or a user object.
- **Scripted group** - Returns a group ID or a Group object.
- **Scripted string collection** - Returns a collection of string values.
- **Scripted user collection** - Returns a collection of user IDs or user objects.
- **Scripted group collection** - Returns a collection of Group IDs or Group objects.

**Note**: Scripted collection fields are limited to collections with 100 entries. Longer collections will be truncated, and an error will be added to the JMCF [Error Logs](/cms_trial/space/JMCFC/731676729/Scripted+Field/).

## Add a custom field

There are two paths for adding a JMCF custom field - through the [My Custom Fields](/cms_trial/space/JMCFC/465471321/My+Custom+Fields/) page or through the native Jira **Custom fields** page.

To create a new field through **My custom fields**:

1. Log into your Jira instance as an Administrator.
2. Click **Settings** ⚙️ in the upper right corner.
3. Select **Apps**.
4. In the left-hand panel, click **Jira Misc Custom Fields**.
5. Select **My custom fields**.
6. Click **New custom field** in the upper right corner.
7. Give the custom field a name and, optionally, a description. **Note:** the maximum length of both the name and description fields is 255 characters.
8. Select the **JMCF** field type and click **Next**.
9. Select the Projects and Work Item types to which the custom field should be added. Click **Next**.
10. Follow the steps in the next section to configure your custom field.

To create a new JMCF custom field through the Jira custom fields page:

1. Log into your Jira instance as an Administrator.
2. Click **Settings** ⚙️ in the upper right corner.
3. Select **Work Items**.
4. In the left-hand panel, click **Custom fields**.
5. Click **Create custom field** in the upper right corner.
6. In the **Select a Field Type** window, click **Advanced**.
7. Select the **JMCF** field type you want to add and click **Next**.
8. Give the custom field a name and, optionally, a description.
9. Click **Create**.
10. Follow the steps in the next section to configure your custom field.

**Note**: If you create a **JMCF** custom field using the native Jira custom field process, the new custom field *will not calculate until its* ***Contexts have been updated****;* this limitation applies even when the custom field is configured for the Default context.

## Edit a custom field

There are two ways you can access a custom field to edit its configuration after it has been created:

1. From the **My custom fields** page of JMCF Administration, click **Action** [menu button icon] and select **Edit**. Update the name and description, add or remove projects and issue types, add or remove screens, and update the JMCF configurations described below.
2. From the Jira **Custom fields** administration page, click **Action** [menu button icon] and select an option:

   1. **Edit details** - Update the **Field Name**, **Description**, and **Search Template** for the field.
   2. **Contexts and default value** - Add or remove contexts for the field. Additionally, configure the **Default Value** and access the **Custom field config** to set the JMCF configurations described below.
   3. **Translation and options** - Set the language in **Choose Language**, then enter the **Field Name** and **Description** for that language.
   4. **Associate to Screens** - Add or remove Jira screens on which the field will appear.
   5. **Move to Trash** - Remove the custom field from all screens and move it to the Trash.

Custom fields can be recovered from the Trash for 60 days. After 60 days, the field will be **deleted permanently** and cannot be recovered!

## Configure a new ‘Scripted’ field

If you added a JMCF custom field through the native Jira custom fields screen, see **Edit a custom field**, above.

Follow the steps above to add a custom field to your Jira instance, then follow these steps:

1. In the **Select Scope** step of the wizard, select the projects and issue types to which the custom field should be available.
2. Click **Next**.
3. In the **Associate Screens** step of the wizard, check the boxes for the screens to which the field should be added.

   1. Use the search field above the list of screens to locate a specific screen.
   2. Check the box at the top of the column to add the field to all listed screens.  
      ⚠️ **Note**: some team management screens in Jira do not currently support custom fields!
4. Click **Next**.
5. The **Configure Field** screen will open; from here you can enter the script for the field, configure its dependencies, and test it before saving. See **Script Configuration**, below, for more information.
6. Click **Save**.

You are viewing the documentation for **Jira Cloud**.

| On This Page |
| --- |

![Jira Misc Custom Fields (JMCF) Cloud scripted field type selection](/cms_trial/assets/6e607da5-5d8f-4582-bec4-d7a078f0c8d1.png)

## Script configuration

JMCF Scripted fields use JavaScript to calculate an output. The output of your script must match the field type you selected when creating the custom field (e.g. a string or a user object); see **Field Types**, above, for a list of all supported output types.

When a new custom field is first configured, the script editor (Figure 2, right) will be populated by an example script; replace this with your own script. The script editor window includes standard code editing features, including syntax colorization, error highlighting, code formatting, and code completion.

The editor also includes three shortcut buttons to the right side of the window:

- [contract icon] **Expand/Contract** - Expand the editor to full height, or shrink it back to its original height.
- [templates icon] **Templates** - Pre-written script examples. See the [list of templates available](/cms_trial/space/JMCFC/1741815975/Scripted+Field+Snippets/).
- [help icon] **Help** - Links to JMCF for Jira Cloud documentation, scripted field documentation, and the Appfire support portal.

### API access

JMCF Scripted fields have access to a limited set of data through the Jira API. Currently, access is limited to the current issue’s fields including:

- **All issue fields** - `api.issue.getField` and `api.issue.getFields`
- **Issue properties** - `api.issue.getProperty` and `api.issue.getProperties`
- **Parent and Child issues** - api.issue.getParent and api.issue.getChild
- **Linked issues** - `api.issue.getLinkedIssues`
- **Users** - `api.jira.getUser`
- **Groups** - `api.jira.getGroup` and `api.jira.getGroupUsers`
- **Projects** - `api.jira.getProject`

### Dependencies

**Note**: The release of JMCF for Jira Cloud 3.0 introduced the ability to access data from other issues through the [getParentIssue](/cms_trial/space/JMCFC/1326022692/getParentIssue/), [getChildIssues](/cms_trial/space/JMCFC/1325072483/getChildIssues/), and [getLinkedIssues](/cms_trial/space/JMCFC/1798209737/getLinkedIssues/) APIs. While access to fields on related issues is now possible, updates to any related issue fields will **not** trigger a recalculation as described below!

When writing your script, JMCF scans the script for dependencies in the form of references to other fields or properties. When dependencies are detected, they are automatically saved as a part of the scripted field configuration, and the field value will be recalculated whenever necessary.

**Note**: there is a difference in behaviors between field dependencies and property dependencies:

- **Field dependencies** will trigger a recalculation of the Scripted Field when their value changes.
- **Property dependencies** will not trigger a recalculation; these dependencies are used to prefetch values before a recalculation.

**Note**: automatic recalculation of scripted fields using dependencies requires that Jira triggers a system event when the dependency is updated. This is generally true, but may not work with all fields. In scenarios where a system event is not triggered, you can [schedule a recalculation of the scripted field](/cms_trial/space/JMCFC/1114997525/Scheduled+recalculations/).

![Jira Misc Custom Fields (JMCF) Cloud scripted field editor interface](/cms_trial/assets/8b67a5bc-8412-4e20-bd33-e109ab6aea2a.png)

## Testing your script

The testing features built into Scripted field configuration can greatly assist in building your script and verifying its output before you save it. You can test your script against a specific issue and JMCF will:

- Verify that the script output type matches the return type for the custom field (**Point 1**, **Figure 3**, right)
- Indicate whether the script executed successfully or encountered an error (**Point 1**, **Figure 3**, right)
- Display the outcome of the script (**Point 2**, **Figure 3**, right)
- Display the contents of the console (if any) (**Point 3**, **Figure 3**, right)

Much like testing other JavaScript, using the console can greatly assist in testing. However, instead of needing to use the browser’s console, you can use the **Console output** window. Anywhere you include `console.log()` in the custom field script, the results of that command will be added to the Console output window. Adding logs to the console is an effective way of testing intermediate values and troubleshooting script components.

To test your script:

1. Enter the ID of the issue against which your script should be run (e.g. ‘TEST-19’). **Note:** currently, searching by Jira ID is not supported.
2. Click **Test**.
3. The result of your script will be displayed below the issue selection (Figure 3, right):

   1. If your script runs successfully, a Success badge will show, and the results of the script and any console logs will be displayed.
   2. If your script encounters any issues, error will be displayed and the **Test result** window will show the specific error message, and any console logs will be shown up to the point of the error.

## Search templates

Currently, there are no specific search templates for custom fields created with JMCF; currently the only search template available is **Forge custom field searcher**, the default search template for Jira Forge apps. Because JMCF uses native data types, the fields are generally searchable using JQL and basic search. However, there are some differences between search in Jira Data Center and Jira Cloud:

- **Time in Status** values are stored in seconds, but can be searched using a variety of representations, including by number of days (days or d), hours (hours or h), minutes (minutes or m), and seconds (seconds or s). This includes combinations of these units. Some examples include:

  - `2days3hours42minutes17seconds`
  - `2d3h42m17s` - 2 days, 3 hours, 42 minutes, 17 seconds
  - `7h15m`- 7 hours, 15 minutes
  - `485903` - 485,903 seconds

For example, the JQL query `TimeInCurrentStatus > 9h30m` will search for all issues with a value greater than 9 hours 30 minutes (34200 seconds) in the field **TimeInCurrentStatus**.

- **Time in Status Table** values are stored in seconds, and total time is stored for both individual status values (Sub-Status Times), and for the work item as a whole (Total Time). These values can be accessed using the following syntax (where *myTime* is the custom field name):

  - `myTime.Total` - Access the total time for all statuses included in the field.
  - `myTime.ToDo` or `myTime.Blocked` - Access the total time for status values of *ToDo* or *Blocked*.
- Additionally, both **Time in Status** fields and **Time in Status Table** fields can be searched using a custom JQL function - `jmcfDuration`. This JQL function accepts an argument of a time value in narrow format (w,d,h,m,s). For example:

  - `myTime.Total > jmcfDuration('5h')` checks that the total time (all status values cumulative) is greater than 5 hours.
  - `myTime.ToDo < jmcfDuration('3d')` checks that the issue has been in the **To Do** status for less than 3 days.
  - `myTime.InProgress >= jmcfDuration('2w 3d 30s')` checks that the issue has been in the **In Progress** greater than or equal to 2 weeks, 3 days, and 30 seconds.

Search template flexibility will be expanded in later versions of **JMCF for Jira Cloud** as the Forge team introduces more capabilities for search.

![Jira Misc Custom Fields (JMCF) Cloud scripted field test results.](/cms_trial/assets/523d41d0-0017-45f5-bf82-823a7034a898.png)