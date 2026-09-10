# Create Custom Field

The **Custom Field Creation Wizard** (Figure 1, right) walks you through the process of adding a new custom field. To create a new custom field, follow these steps:

You are viewing the documentation for **Jira Cloud**.

1. Log into your Jira instance as an Administrator.
2. In the upper right corner, click **Settings** ( ⚙️ ) and select **Apps**.
3. In the left-hand panel, click **Jira Misc Custom Fields**.
4. Click **My custom fields**.
5. In the upper right corner of the window, click **New custom field**. The Create Custom Field wizard will open.
6. Name the custom field and, optionally, enter a Description (**Point 1**, **Figure 1**, right). The Name and Description will appear in the [My custom fields](/cms_trial/space/JMCFC/465471321/My+Custom+Fields/) administration screen.
7. Select the type of custom field you want to create (**Point 2**, **Figure 1**, right). See [Custom Fields](/cms_trial/space/JMCFC/465471226/Custom+Fields/) for more information on the various types of fields that you can create.
8. Click **Next**.
9. Select the scope (or the context) for your custom field (**Point 3**, **Figure 2**, right); this includes selecting both the project(s) to which the custom field should be added and the issue types to which it should apply. See **Custom Field Contexts**, below, for more information.
10. Click **Next**.
11. Select the Jira screens to which the custom field should be added (**Point 4**, **Figure 3**, right). Screens can be added individually, or use the checkbox at the top of the column to select all screens. Additionally, the list of screens can be filtered using the search box at the top of the list. See **Filtering Screens**, below, for more information.
12. Click **Next**.
13. Set the configuration options for the field. Depending on the type of field chosen the options will vary; refer to the specific field type documentation for more information on its options.
14. Click **Save**.

A custom field can be added to additional screens and contexts after it has been created!

**Note**: custom fields are ***not*** currently supported on next-generation team management screens in Jira.

Your new custom field is now ready! When a custom field is first created, it is added to the Jira project and issue types you selected, as well as the screens selected in the Wizard

## Custom Field Contexts

**JMCF for Jira Cloud** uses Jira’s contexts to configure the projects and issue types to which a custom field will be available (but not screens, those are configured separately!). When **creating** a custom field, all company-managed projects and issue types should be available to select.

However, when creating **additional contexts** for a custom field, the list of projects for that context will show projects as unavailable if that project is already included in a different context for that custom field. See <https://support.atlassian.com/jira-cloud-administration/docs/configure-custom-field-context/> for more information.

## Filtering Screens

When working with a Jira instance that includes a large number of screens, selecting each screen manually can be difficult. When associating a custom field with Jira screens, you can use the search box at the top of the list to filter which screens are displayed. When a filter is active, the search box will include a badge containing the number of screens matching the search string.

**Note**: Using the **Select All/Deselect All** checkbox at the top of the list will only select or deselect *visible screens when a filter is applied.*

![admin-CreateCustomFieldWizard1.png](/cms_trial/assets/454a7e0d-ebc7-4077-9ede-7c4e8d636a33.png)![Create Custom Field Wizard select projects and issue types](/cms_trial/assets/9281a3ef-87a0-4726-83a4-df2b9d1a3092.png)

Image — asset pipeline pending  
Create Custom Field Wizard screen configuration