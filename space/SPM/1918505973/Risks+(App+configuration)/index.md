# Risks (App configuration)

## Security and access

Only Jira/App Admins can manage the app on the global (app) configuration level.

To access the global settings for the Risks module:

1. Click the **wrench icon** in the top right corner.
2. Select **Modules** from the dropdown.
3. Go to the **Risks** page.

## Risks configuration

On the **Risks** page, you can set up a risk heat map. It displays the risk level based on the likelihood and severity of the risk assessment.

You can also modify the axis labels and sync Jira fields.

![Risks configuration page.](/cms_trial/assets/4445fa1f-d342-4527-9d6f-2e479e445c68.png)

### Task sources

By default, two "select list (single choice)" custom fields are created during app installation with predefined options. The default values are listed below:

| **Custom field** | **Select options** |
| --- | --- |
| Risk probability | - Almost none - Low - Medium - High - Very high |
| Risk consequence | - Trivial - Low - Medium - High - Severe |

The fields are selected per integration instance.

Fields can be:

- **Not synchronized** → The value is stored in the app only and is not synchronized with any Jira field.
- **Mapped to a Jira field** → The risk field value in the app corresponds to the field value in Jira.

### Risk value definition

The same field cannot be used to map both axes. You can use each field only once.

#### Probability setting

Add and remove positions to determine what values should be visible on the risk matrix.

If you want the values to be synchronized with a task source (Jira), make sure that the value you add exists as a value for the mapped field.

How can you tell if the axis value can be synchronized?

- A red **cross** (❌) mark means the value exists in BigPicture only and **cannot** be synchronized with a task source.
- A green (✅) checkmark means the value exists for a mapped field and **can** be synchronized.

![Risk value fefinition on the risks global configuration page.](/cms_trial/assets/406b216c-b886-4134-8a5a-7ba375f7a247.png)

The reason is that the field you have used for mapping can have many values, but only the selected ones will be used on the risk matrix.

For example, you could remove all values except "High" and "Very high" to create a custom risk matrix focused only on visualizing high-risk tasks.

## Customize the risk matrix

### Add a value to the axis

To add a new risk value:

1. Click the **plus icon** below the respective axis (named “Probability” and “Consequence” by default). Alternatively, you can add a new risk “Probability”/“Consequence” value inline.

![Adding new risk value.](/cms_trial/assets/bdc0fd0c-03b4-4da2-97ce-0f92e80d268a.png)

1. Name the new value.

You can either type the value name manually (when the toggle switch is "off") or select it from a list (when the toggle switch is "on"). The list is based on the values of the mapped fields.

![Naming new risk value.](/cms_trial/assets/d6b545aa-5915-4b09-9188-bb691d6c3d94.png)

1. **Save** changes to add new values labeled “To be added.”

![Saving changes.](/cms_trial/assets/3080dcca-0ec3-4b8a-9e19-572f38c99c28.png)

### Remove a value from an axis

Consequence and probability values set for a risk need to be consistent with the configuration of both axes. If you delete a consequence or probability value from the axis configuration, a risk that has such a value set is removed from both the matrix and table view.

Click the trash icon on the right:

![contentId-1918505973](/cms_trial/assets/61eb8716-e1e4-4a03-bf02-1766b733838e.png)

Until you hit "Save", changes are indicated with the "To be added" label:

![contentId-1918505973](/cms_trial/assets/e1ca1f4d-e031-47c2-bf15-8f4e7604f223.png)

#### Change axis name

You can also change the name of either axis → this is the name you will see in the Matrix of the Risk module.

![contentId-1918505973](/cms_trial/assets/c02ab4ef-f436-4393-890a-d43706c446d2.png)

### Order risk values

Use the drag-and-drop mechanism to change the order of items.

Remember to save the changes:

![save-changes.png](/cms_trial/assets/c544cadb-ea28-4267-a70d-df1c18c07b5e.png)

### Saving the changes - changelog

New settings have to be saved.

The changelog can be found at the bottom of the page. Review the changelog and confirm by clicking the **Save** button.

![contentId-1918505973](/cms_trial/assets/7009194f-3446-48f3-b7cc-f9a0111dfffe.png)

## Matrix dimensions

The dimensions of the matrix depend on the number of selected options. The default dimension is 5x5, the recommended size due to the coloring of the risk levels when the heat map mode is enabled.

If you want to adjust the matrix to resemble ROAM, use ROAM as one of the axes and leave only a single option for the second one. Alternatively, you can add a risk score or severity.

To use the matrix i.e. show Jira issues on the matrix, you need to add both fields to your Jira issue screens and select one of the values.