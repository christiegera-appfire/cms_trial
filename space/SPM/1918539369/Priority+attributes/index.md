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

![Screenshot of the Configure page in the Priorities module. ](/cms_trial/assets/fabef4da-df81-4fc8-9651-2528e407c082.png)

The table presents a list of available metric types.

| **Metric type** | **Description** |
| --- | --- |
| Label | Creates a set of labels with custom names and colors.   1. Click **Add a new metric**. 2. Select **Label**. 3. Provide a name in the **Add metric name** field. 4. Add **Label names**. 5. Adjust colors and enter values.  Screenshot of the Label metric type. |
| Number | Creates the field that accepts a number input (supports 4 decimal numbers).   1. Click **Add a new metric**. 2. Select **Number**. 3. Provide a name in the **Add metric name** field. 4. Select which number-based metric you want to link to Jira. Screenshot of the Number metric type. 5. Once this connection is made, you can update the linked field in Jira. |
| Rating | Creates a 5-star rating.   1. Click **Add a new metric**. 2. Select **Rating**. 3. Provide a name in the **Add metric name** field. 4. Define values if needed.  Screenshot of the Rating metric type. |
| Short text | Creates a drop-down with text values.   1. Click **Add a new metric**. 2. Select **Short text**. 3. Provide a name in the **Add metric name** field. 4. Add **Label names**. 5. Enter values.  Screenshot of the Short text metric type. |
| Jira field | Allows for using App custom fields or Jira custom fields (only single select dropdown fields are available).   1. Click **Add a new metric**. 2. Select **Jira field**. 3. Provide a name in the **Add metric name** field. 4. Select a Jira field from the dropdown menu. 5. You can modify colors, label names, and values.  Screenshot of the Jira field metric type. |

## Score formula

If the scoring calculation needs improvement, you can tweak the score formula or create a completely new one. Simple math operators such as `* / - + ( )`, numbers, and metrics can be used.

You can customize score formulas using the metrics included in a template. Before making any changes to the formula, ensure all necessary metrics are added to the template.

### Basic formula edit

To edit a score formula:

1. In the Priorities module, click **Customize** in the top-right corner.
2. You can click metrics and operators to change them.
3. Click in the **Score formula** field:

   1. To add a new field to the formula, start typing to see available metrics.

      ![Screenshot of adding a new metric to the score formula in the Priorities module.](/cms_trial/assets/0a6a8c9d-1ad8-40e7-b54d-ab94fdf8a0d7.png)
   2. To change a math operator, click it and select a new one from the list.

      ![Screenshot of the math operators available for score formulas in the Priorities module.](/cms_trial/assets/7f703837-9fe4-4fe5-b9e0-245530a714f8.png)
   3. To delete a metric from the formula, click the field and press **Delete**.
4. Click **Save changes** to save your new formula.

### Advanced formula edit

If you want more flexibility when editing the scoring formula, then you can use **Advanced edit mode**.

1. In the Priorities module, click **Customize** in the top-right corner.
2. Click **Switch to advanced edit** under Score formula.

   ![Screenshot of switching to the Advanced edit mode when modifying the score formula in the Priorities module.](/cms_trial/assets/117c38e6-9916-4e3c-a49a-ce790fe533c8.png)
3. You can edit metrics and operators.
4. Metrics in the advanced edit mode need to be wrapped in the braces (curly brackets).   
   Example: `{{Reach}}`

   ![Screenshot of editing a score formula in advanced edit mode in the Priorities module.](/cms_trial/assets/34341af7-37fb-46ad-b458-4bff485340f3.png)
5. Click **Save changes** to save your new formula.

## Priority attributes (new navigation)

Click to expand the guide

This page describes the available metric types and score formulas used to:

- [Customize existing prioritization templates](/cms_trial/space/SPM/1918506780/Customize+prioritization+templates/)
- [Create new prioritization templates](/cms_trial/space/SPM/1918506690/Create+new+prioritization+templates/)

Define metrics that align with your prioritization needs and configure formulas to calculate priority scores effectively.

## Available metric types

Metrics are set per the prioritization template. For example, if the Impact metric is added to multiple templates, you’ll need to update its values separately for each one, as metric values are not shared across templates.

![Screenshot of the Configure page in the Priorities module. ](/cms_trial/assets/fabef4da-df81-4fc8-9651-2528e407c082.png)

The table presents a list of available metric types.

| **Metric type** | **Description** |
| --- | --- |
| Label | Creates a set of labels with custom names and colors.   1. Click **Add a new metric**. 2. Select **Label**. 3. Provide a name in the **Add metric name** field. 4. Add **Label names**. 5. Adjust colors and enter values.  Screenshot of the Label metric type. |
| Number | Creates the field that accepts a number input (supports 4 decimal numbers).   1. Click **Add a new metric**. 2. Select **Number**. 3. Provide a name in the **Add metric name** field. 4. Select which number-based metric you want to link to Jira. Screenshot of the Number metric type. 5. Once this connection is made, you can update the linked field in Jira. |
| Rating | Creates a 5-star rating.   1. Click **Add a new metric**. 2. Select **Rating**. 3. Provide a name in the **Add metric name** field. 4. Define values if needed.  Screenshot of the Rating metric type. |
| Short text | Creates a drop-down with text values.   1. Click **Add a new metric**. 2. Select **Short text**. 3. Provide a name in the **Add metric name** field. 4. Add **Label names**. 5. Enter values.  Screenshot of the Short text metric type. |
| Jira field | Allows for using App custom fields or Jira custom fields (only single select dropdown fields are available).   1. Click **Add a new metric**. 2. Select **Jira field**. 3. Provide a name in the **Add metric name** field. 4. Select a Jira field from the dropdown menu. 5. You can modify colors, label names, and values.  Screenshot of the Jira field metric type. |

## Score formula

If the scoring calculation needs improvement, you can tweak the score formula or create a completely new one. Simple math operators such as `* / - + ( )`, numbers, and metrics can be used.

You can customize score formulas using the metrics included in a template. Before making any changes to the formula, ensure all necessary metrics are added to the template.

### Basic formula edit

To edit a score formula:

1. In the Priorities module, click **Configure** from the drop-down menu.

   ![image-20260427-094530.png](/cms_trial/assets/f322b649-8455-4c76-aa96-6f161d37c76d.png)
2. You can click metrics and operators to change them.
3. Click in the **Score formula** field:

   1. To add a new field to the formula, start typing to see available metrics.

      ![Screenshot of adding a new metric to the score formula in the Priorities module.](/cms_trial/assets/0a6a8c9d-1ad8-40e7-b54d-ab94fdf8a0d7.png)
   2. To change a math operator, click it and select a new one from the list.

      ![Screenshot of the math operators available for score formulas in the Priorities module.](/cms_trial/assets/7f703837-9fe4-4fe5-b9e0-245530a714f8.png)
   3. To delete a metric from the formula, click the field and press **Delete**.
4. Click **Save changes** to save your new formula.

### Advanced formula edit

If you want more flexibility when editing the scoring formula, then you can use **Advanced edit mode**.

1. In the Priorities module, click **Configure** from the drop-down menu.
2. Click **Switch to advanced edit** under Score formula.

   ![Screenshot of switching to the Advanced edit mode when modifying the score formula in the Priorities module.](/cms_trial/assets/117c38e6-9916-4e3c-a49a-ce790fe533c8.png)
3. You can edit metrics and operators.
4. Metrics in the advanced edit mode need to be wrapped in the braces (curly brackets).   
   Example: `{{Reach}}`

   ![Screenshot of editing a score formula in advanced edit mode in the Priorities module.](/cms_trial/assets/34341af7-37fb-46ad-b458-4bff485340f3.png)
5. Click **Save changes** to save your new formula.