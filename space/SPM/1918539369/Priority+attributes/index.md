# Priority attributes

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

## Priority attributes (old navigation)

Click to expand the guide

This page describes the available metric types and score formulas used to:

- [Customize existing prioritization templates](/cms_trial/space/SPM/1918506780/Customize+prioritization+templates/)
- [Create new prioritization templates](/cms_trial/space/SPM/1918506690/Create+new+prioritization+templates/)

Define metrics that align with your prioritization needs and configure formulas to calculate priority scores effectively.

## Available metric types

Metrics are set per the prioritization template. For example, if the Impact metric is added to multiple templates, you’ll need to update its values separately for each one, as metric values are not shared across templates.

![Screenshot of available metric types in the Priorities module.](/cms_trial/assets/e5220b53-6595-4b21-a89c-8b73e9832678.png)

The table presents a list of available metric types.

| **Metric type** | **Description** |
| --- | --- |
| Label | Creates a set of labels with custom names and colors.   1. Click **Add a new metric**. 2. Select **Label**. 3. Provide a name in the **Add metric name** field. 4. Add **Label names**. 5. Adjust colors and enter values. 6. Check the **Default value** option if you want default values to be automatically recorded for newly created work items in a project where a current template is selected for prioritization.  Screenshot of adding a Label metric type to the prioritization template in the Priorities module. |
| Number | Creates the field that accepts a number input (supports 4 decimal numbers).   1. Click **Add a new metric**. 2. Select **Number**. 3. Provide a name in the **Add metric name** field. 4. Select which number-based metric you want to link to Jira. Screenshot of adding a new Number metric type. 5. A confirmation box will appear. To confirm, click **Yes, link field**. Screenshot of confirming linking to a Jira field. 6. Once linked, you can’t edit the **Default value** field. 7. Once this connection is made, you can update the linked field in Jira. |
| Rating | Creates a 5-star rating.   1. Click **Add a new metric**. 2. Select **Rating**. 3. Provide a name in the **Add metric name** field. 4. Define values if needed. 5. Check the **Default value** option if you want default values to be automatically recorded for newly created work items in a project where a current template is selected for prioritization. Screenshot of adding a new Rating metric type to a template in the Priorities module. |
| Short text | Creates a drop-down with text values.   1. Click **Add a new metric**. 2. Select **Short text**. 3. Provide a name in the **Add metric name** field. 4. Add **Label names**. 5. Enter values. 6. Check the **Default value** option if you want default values to be automatically recorded for newly created work items in a project where a current template is selected for prioritization. Screenshot of the short text metric added to a template in the Priorities module. |
| Jira field | Allows for using App custom fields or Jira custom fields (only single select dropdown fields are available).   1. Click **Add a new metric**. 2. Select **Jira field**. 3. Provide a name in the **Add metric name** field. 4. Select a Jira field from the dropdown menu. 5. You can modify colors, label names, and values. Screenshot of adding a Jira field metric type to a template in the Priorities module. |

### Default prioritization values

You can use the **Default value** field to customize work item templates. This lets you pre-set metric values for all new work items.

When all template metrics have default values, the Priorities module automatically calculates the priority score and positions the work item accordingly within the priority table based on the score and chosen sorting method.

Key benefits:

- Streamlined workflow - pre-setting common values minimizes manual input and saves time.
- Establishing a baseline - set a default average priority score, allowing adjustments as needed.
- Prioritizing urgency - assign the lowest possible score upon work item creation to highlight critical tasks.

![Screenshot of the Default value field when customizing a prioritization template.](/cms_trial/assets/ba716164-7209-477b-b3be-429d22153e64.png)

## Score formula

If the scoring calculation needs improvement, you can tweak the score formula or create a completely new one. Simple math operators such as `* / - + ( )`, numbers, and metrics can be used.

You can customize score formulas using the metrics included in a template. Before making any changes to the formula, ensure all necessary metrics are added to the template.

### Basic formula edit

To edit a score formula:

1. In the Priorities module, click **Customize** in the top-right corner.
2. You can click metrics and operators to change them.
3. Click in the **Score formula** field:

   1. To add a new field to the formula, start typing to see available metrics.

      ![Screenshot of adding a new metric to the score formula in the Priorities module.](/cms_trial/assets/be006e0f-4bf5-41dc-87c9-0b34616cc0bc.png)
   2. To change a math operator, click it and select a new one from the list.

      ![Screenshot of the math operators available for score formulas in the Priorities module.](/cms_trial/assets/c93205db-68f5-4215-aef4-99ad00fdc366.png)
   3. To delete a metric from the formula, click the field and press **Delete**.
4. Click **Save changes** to save your new formula.

### Advanced formula edit

If you want more flexibility when editing the scoring formula, then you can use **Advanced edit mode**.

1. In the Priorities module, click **Customize** in the top-right corner.
2. Click **Switch to advanced edit** under Score formula.

   ![Screenshot of switching to the Advanced edit mode when modifying the score formula in the Priorities module.](/cms_trial/assets/3d5cabf7-1cbd-4854-a4fc-b1b686dc863c.png)
3. You can edit metrics and operators.
4. Metrics in the advanced edit mode need to be wrapped in the braces (curly brackets).   
   Example: `{{Reach}}`

   ![Screenshot of editing a score formula in advanced edit mode in the Priorities module.](/cms_trial/assets/809605b9-ac56-4c27-adf3-ce86ab20373a.png)
5. Click **Save changes** to save your new formula.

## Priority attributes (new navigation)

Click to expand the guide

This page describes the available metric types and score formulas used to:

- [Customize existing prioritization templates](/cms_trial/space/SPM/1918506780/Customize+prioritization+templates/)
- [Create new prioritization templates](/cms_trial/space/SPM/1918506690/Create+new+prioritization+templates/)

Define metrics that align with your prioritization needs and configure formulas to calculate priority scores effectively.

## Available metric types

Metrics are set per the prioritization template. For example, if the Impact metric is added to multiple templates, you’ll need to update its values separately for each one, as metric values are not shared across templates.

![image-20260427-094257.png](/cms_trial/assets/6e9c34c8-11a7-4161-bc92-42a0be86e157.png)

The table presents a list of available metric types.

| **Metric type** | **Description** |
| --- | --- |
| Label | Creates a set of labels with custom names and colors.   1. Click **Add a new metric**. 2. Select **Label**. 3. Provide a name in the **Add metric name** field. 4. Add **Label names**. 5. Adjust colors and enter values. 6. Check the **Default value** option if you want default values to be automatically recorded for newly created work items in a project where a current template is selected for prioritization.  Screenshot of adding a Label metric type to the prioritization template in the Priorities module. |
| Number | Creates the field that accepts a number input (supports 4 decimal numbers).   1. Click **Add a new metric**. 2. Select **Number**. 3. Provide a name in the **Add metric name** field. 4. Select which number-based metric you want to link to Jira. Screenshot of adding a new Number metric type. 5. A confirmation box will appear. To confirm, click **Yes, link field**. Screenshot of confirming linking to a Jira field. 6. Once linked, you can’t edit the **Default value** field. 7. Once this connection is made, you can update the linked field in Jira. |
| Rating | Creates a 5-star rating.   1. Click **Add a new metric**. 2. Select **Rating**. 3. Provide a name in the **Add metric name** field. 4. Define values if needed. 5. Check the **Default value** option if you want default values to be automatically recorded for newly created work items in a project where a current template is selected for prioritization. Screenshot of adding a new Rating metric type to a template in the Priorities module. |
| Short text | Creates a drop-down with text values.   1. Click **Add a new metric**. 2. Select **Short text**. 3. Provide a name in the **Add metric name** field. 4. Add **Label names**. 5. Enter values. 6. Check the **Default value** option if you want default values to be automatically recorded for newly created work items in a project where a current template is selected for prioritization. Screenshot of the short text metric added to a template in the Priorities module. |
| Jira field | Allows for using App custom fields or Jira custom fields (only single select dropdown fields are available).   1. Click **Add a new metric**. 2. Select **Jira field**. 3. Provide a name in the **Add metric name** field. 4. Select a Jira field from the dropdown menu. 5. You can modify colors, label names, and values. Screenshot of adding a Jira field metric type to a template in the Priorities module. |

### Default prioritization values

You can use the **Default value** field to customize work item templates. This lets you pre-set metric values for all new work items.

When all template metrics have default values, the Priorities module automatically calculates the priority score and positions the work item accordingly within the priority table based on the score and chosen sorting method.

Key benefits:

- Streamlined workflow - pre-setting common values minimizes manual input and saves time.
- Establishing a baseline - set a default average priority score, allowing adjustments as needed.
- Prioritizing urgency - assign the lowest possible score upon work item creation to highlight critical tasks.

![Screenshot of the Default value field when customizing a prioritization template.](/cms_trial/assets/ba716164-7209-477b-b3be-429d22153e64.png)

## Score formula

If the scoring calculation needs improvement, you can tweak the score formula or create a completely new one. Simple math operators such as `* / - + ( )`, numbers, and metrics can be used.

You can customize score formulas using the metrics included in a template. Before making any changes to the formula, ensure all necessary metrics are added to the template.

### Basic formula edit

To edit a score formula:

1. In the Priorities module, click **Configure** from the drop-down menu.

   ![image-20260427-094530.png](/cms_trial/assets/63e2ab94-ecf3-45cd-a29d-17d78aa4b79d.png)
2. You can click metrics and operators to change them.
3. Click in the **Score formula** field:

   1. To add a new field to the formula, start typing to see available metrics.

      ![Screenshot of adding a new metric to the score formula in the Priorities module.](/cms_trial/assets/be006e0f-4bf5-41dc-87c9-0b34616cc0bc.png)
   2. To change a math operator, click it and select a new one from the list.

      ![Screenshot of the math operators available for score formulas in the Priorities module.](/cms_trial/assets/c93205db-68f5-4215-aef4-99ad00fdc366.png)
   3. To delete a metric from the formula, click the field and press **Delete**.
4. Click **Save changes** to save your new formula.

### Advanced formula edit

If you want more flexibility when editing the scoring formula, then you can use **Advanced edit mode**.

1. In the Priorities module, click **Configure** from the drop-down menu.
2. Click **Switch to advanced edit** under Score formula.

   ![Screenshot of switching to the Advanced edit mode when modifying the score formula in the Priorities module.](/cms_trial/assets/3d5cabf7-1cbd-4854-a4fc-b1b686dc863c.png)
3. You can edit metrics and operators.
4. Metrics in the advanced edit mode need to be wrapped in the braces (curly brackets).   
   Example: `{{Reach}}`

   ![Screenshot of editing a score formula in advanced edit mode in the Priorities module.](/cms_trial/assets/809605b9-ac56-4c27-adf3-ce86ab20373a.png)
5. Click **Save changes** to save your new formula.