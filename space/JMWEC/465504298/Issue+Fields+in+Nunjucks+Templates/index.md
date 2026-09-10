# Issue Fields in Nunjucks Templates

When building Nunjucks templates, the **Help** section includes shortcuts for adding common issue fields to the template. These shortcuts are listed under the **Issue Fields** tab (pictured right).

The shortcut buttons available update based on the settings in the top half of the section, reflecting the value that will be inserted into the template when the button is clicked.

To add a field to a Nunjucks template:

1. Open the **Select a field** pulldown menu and select the Jira field to be added to the template.
2. Select the issue from which the value should be selected using the **issue var** pulldown.
3. Use the toggle **Refer to the issue field by** to configure how fields are reference - either by Name or by ID. The shortcut button values will update to reflect this change.

After the desired field has been configured, several sets of shortcut buttons are available to insert fields into the template. These shortcuts are grouped into:

- **Accessing the field** - Insert a reference to the selected field.
- **Accessing sub-fields** - Insert references to fields from related objects of the selected field.
- **Testing the field’s value** - Insert common expressions used to test the value of the selected field (e.g. if the field value equals a specified value or if the field is null).

**Please note**: the shortcut button are only the *most common fields* used in templates. Other fields are available!

![JMWE for Jira Cloud Nunjucks template editor with issue field integration](/cms_trial/assets/1839034d-6d14-4826-90a6-b5fcd790a20e.png)