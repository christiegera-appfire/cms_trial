# Last Field Changed by User

The **Last Field Changed by User** custom field is a calculated field that displays the user who performed the last change for the field it is configured to watch. It is a read-only field.

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

## Configure a new 'Last Field Changed by User' field

If you added a JMCF custom field through the native Jira custom fields screen, see **Edit a custom field**, below.

Follow the steps above to add a custom field to your Jira instance, then follow these steps:

1. In **Associate Screens** step of the wizard, check the boxes for the screens to which the field should be added.

   1. Use the search field above the list of screens to locate a specific screen.
   2. Check the box at the top of the column to add the field to all screens.  
      ⚠️ **Note**: some team management screens in Jira do not currently support custom fields!
2. Click **Next**.
3. Select a specific field from the **Field to watch** pulldown menu. To watch all fields, select `*ANY`.
4. Click **Save**.

**Note**: You cannot use a JMCF custom field to watch another JMCF custom field. JMCF fields are calculated fields and do not record updates in the Jira Changelog. Because ‘Last Field Change Time’ fields utilize the changelog to calculate their results, They cannot use other JMCF fields.

When selecting fields in **Fields to watch**, other JMCF fields will not be listed.

You are viewing the documentation for **Jira Cloud**.

![Last Field Changed by User Screen](/cms_trial/assets/150c6dbb-0b08-49e5-9099-e5e34913b94e.png)

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