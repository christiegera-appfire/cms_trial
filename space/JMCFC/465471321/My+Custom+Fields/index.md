# My Custom Fields

The **My custom fields** page (Figure 1, right) displays a paginated table listing all custom fields created using **JMCF for Jira Cloud**. The page includes, from top to bottom:

- **Page Toolbar** - The upper right corner of the page includes a menu with several commands:

  - **Documentation** - Open the JMCF for Jira Cloud documentation.
  - **Support request** - Open the Appfire Support portal to submit a support request.
  - **Feedback** - Open the Appfire Support portal to submit an enhancement or feature request.
  - **Atlassian Community** - Open the [Atlassian Community page for JMCF](https://community.atlassian.com/t5/tag/addon-com.innovalog.jmcf.jira-misc-custom-fields/tg-p/category-id/atlassian-marketplace).
- **Refresh** - Refresh the list of custom fields.
- **Search** - Search for custom fields by field name, field ID, description, or field type.
- **New custom field** - Click this button to add a new custom field and open the [Create Custom Field Wizard](/cms_trial/space/JMCFC/465405703/Create+Custom+Field/).
- **Custom Field Table** - The table listing all JMCF custom fields created in your instance.

  - **Pagination** - For instances with many custom fields, the table will be paginated with navigation controls under the table itself.

The table of fields includes the following:

**Note**: Column headers can be used to sort the Calculations table.

- **Enable/Disable** - Use this toggle to enable or disable a custom field entirely. Disabled custom fields will still be displayed on issue screens, but they will not be recalculated until they are enabled (including [scheduled recalculations](/cms_trial/space/JMCFC/1114997525/Scheduled+recalculations/)).
- **Field name** - The name of the custom field.   
  [note icon] **Note:** Newly created or edited custom fields will show at the top of the list of custom fields for a short time; after that, fields are listed alphabetically.
- **Description** - Description of field; this is entered during field creation and can be edited.
- **Field Type** - The type of custom field and its icon, such as Last Field Change Time, Parent Status, and Status Entered by User, among others. See [Custom Fields](/cms_trial/space/JMCFC/465471226/Custom+Fields/) for more information.
- **Formatter** - An icon [formatters icon] will display for any custom field that has been styled using [Formatters](/cms_trial/space/JMCFC/1559003309/Formatters/).
- **Screens** - The number of screens to which the custom field has been added. Click the link to open the **Edit custom field** window where screens can be added or removed. See [Screens and Contexts](#Screens-and-Contexts), below, for more information.
- **Context** - The number of projects in which the field is active, and the issue types for which the field is currently active. Click either badge to open the native Jira **Configure Custom Field** screen to edit the context(s) to which the custom field belongs. See [Screens and Contexts](#Screens-and-Contexts), below, for more information.
- **Schedule** - The recalculation schedule for the custom field (if any). See [Scheduled recalculations](/cms_trial/space/JMCFC/1114997525/Scheduled+recalculations/) for more information.
- **Errors** - A badge indicating the number of Errors for a custom field. Clicking the badge will open the [Error Logs](/cms_trial/space/JMCFC/465436864/Error+Logs/) page where you can view more details.
- **Calculations** - A badge indicating the calculation status of for the custom field (e.g. complete, in-progress, suspended, or the percent completed); click the calculation percentage to open the **Calculations** page. See [Calculations](/cms_trial/space/JMCFC/465633417/Calculations/) for more information.  
  [note icon] **Note**: Completed and inactive calculations will be automatically removed from the **Calculations** page after 24 hours.
- **Action Button** - A set of shortcut buttons to numerous actions related to the custom field. See **Working with custom fields**, below, for more information.

## Working with custom fields

Each custom field listed includes an **Action button** in the last column to the right; this menu includes options to perform standard actions for each field.

There are two ways to open a custom field for editing. In addition to the **Edit** action button ( [tts pencil icon] ) in the Action menu, you can click the **Screens** link to open the **Edit custom field** window!

- **Edit** ( [edit pencil icon] ) - Open the custom field editor to update the name and description; add or remove screens where the field will appear; or update the specific configuration for the field.
- **Duplicate** ( [copy paste icon] ) - Copy the custom field configuration to a new JMCF custom field; this opens the Create Custom Field Wizard where the current configuration of the custom field can be modified for the new copy.
- **Formatters**- Open the Formatters configuration dialog for the selected custom field. See [Formatters](/cms_trial/space/JMCFC/1559003309/Formatters/) for more information.
- **Recalculate** ( [action restart icon] ) - Start a recalculation of the custom field.
- **Schedule Recalculation** ( [addschedule icon] ) - Schedule the field for recalculation on an interval. See [Scheduled recalculations](/cms_trial/space/JMCFC/1114997525/Scheduled+recalculations/) for more information.
- **Delete** ( [delete icon] ) - Move the custom field to the Trash; the custom field will remain in the Trash for 60 days, after which it will be deleted. JMCF custom fields can be recovered the same as native custom fields - through the **Trash** tab in the Jira Custom fields screen.

## Edit a custom field

![Edit Custom Field Screen](/cms_trial/assets/0e7406aa-de60-42b5-9b42-569b1abf4255.png)

When you select **Edit**, the **Edit custom field** window (Figure 2, right) will open.

**Note**: The **Edit custom field** window has almost all of the same features as the [Create Custom Field Wizard](/cms_trial/space/JMCFC/465405703/Create+Custom+Field/), with one exception - you cannot change the custom field type!

This window includes two steps to update a custom field:

1. **Edit name and associate screens** - Update the name of the custom field, check the box next to a screen to add the field to that screen or, alternately, uncheck the box to remove the field from that screen. Use the **Search** box to find specific screens.   
   [circle icon] **Note**: Currently selected screens will display at the top of the list!
2. **Edit configuration** - Depending on the custom field type, the configuration screen will be different. Refer to each types specific documentation for details on its configuration options.

**Note**: if you recover a custom field from the Trash, you will need to manually trigger a recalculation by opening and saving the custom field context configuration using the native Jira configuration options.

See <https://support.atlassian.com/jira-cloud-administration/docs/edit-a-custom-fields-options/>.

## Screens and Contexts

A custom field is added to a screen by configuring the field, **not** by configuring the screen! The **My custom fields** page lists each of the JMCF-created custom fields along with details on the number of screens to which the field has been added. After a field has been added to a screen, its location on the screen can be updated by opening the [Jira screen editor](https://confluence.atlassian.com/adminjiraserver/defining-a-screen-938847288.html#Definingascreen-Configuringscreen'stabsandfields).

In addition to the details on screens, the table lists the **Contexts** to which the field has been added; the context, or [custom field configuration scheme](https://support.atlassian.com/jira-cloud-administration/docs/configure-custom-field-context/), is a set of general configurations that can be applied to custom fields. A context includes the localization and default value settings as well as the type of issues and specific projects in which the field is available.

If you create an additional context, or add a JMCF custom field to an existing context, it will trigger a backfill calculation for the custom field within the new context.

You are viewing the documentation for **Jira Cloud**.

| On This Page |
| --- |

![My Custom Fields page](/cms_trial/assets/18160755-9744-42a2-b262-3a0f2591f0d4.png)