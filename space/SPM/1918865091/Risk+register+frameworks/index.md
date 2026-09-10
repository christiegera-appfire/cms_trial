# Risk register frameworks

## Risk register frameworks (old navigation)

Click to expand the guide

On the **Risk register frameworks** page, you can configure existing risk calculations or create new ones.

See an interactive video on how to access the **Risk register frameworks** page.

## Risk calculation attributes

The table presents all risk calculation attributes.

| **Risk calculation attribute** | **Screenshot** |
| --- | --- |
| Risk framework name | Risk framework name attribute. |
| Risk score | Risk score attribute. |
| Metrics | Metrics in the risk register. |
| Risk matrix | Risk matrix attribute. |
| Risk levels | Risk levels attribute. |

### Risk framework name

Typing a name in the field automatically updates the risk calculation row at the top.

![New risk calculation name entered and it's automatically updated in the risk calculation row above.](/cms_trial/assets/ae8e82d4-e223-4be8-a345-404d1f351b82.png)

### Risk score

If the scoring calculation needs improvement, you can tweak the score formula or create a completely new one. Simple math operators such as `* / - + ( )`, numbers, and metrics can be used.

You can customize score formulas using the metrics included in a template. Before making any changes to the formula, ensure all necessary metrics are added to the template.

#### Basic formula edit

To edit a score formula:

1. Click in the **Risk Score** field.
2. To add a new field to the formula, start typing to see available metrics.

   ![The risk score field, with the impact metric appearing after th](/cms_trial/assets/6716453a-3fd1-41ee-b5e5-9ad7adf032fc.png)
3. To change a math operator, click it and select a new one from the list.

   ![showing how to change the math operator in the Risk score field.](/cms_trial/assets/00b8675f-e552-412f-94ac-603b5f166d90.png)
4. To delete a metric from the formula, click the field and press **Delete**.

#### Advanced formula edit

If you want more flexibility when editing the scoring formula, then you can use **Advanced edit mode**.

1. Click **Switch to advanced edit** under Risk score.

   ![Risk score field showing the Switch to advanced edit button.](/cms_trial/assets/68cd017f-dde9-4486-80fa-de40356a1cdc.png)
2. You can edit metrics and operators.
3. Metrics in the advanced edit mode must be wrapped in the braces (curly brackets).   
   Example: `{{Impact}}`

   ![A metrics template showing the Add value button.](/cms_trial/assets/56605fe4-3fa7-42cc-bfdc-2a2ce034b7f7.png)![image-20250319-140250.png](/cms_trial/assets/8db81e65-8275-49bc-857e-4a6db9aeab2f.png)

### Metrics

When editing an existing template, you can update the attributes of existing metrics, such as the metric’s name, value names, colors, and values. You can also add new values to existing metrics.

Exception: [Metric attributes imported](/cms_trial/space/SPM/3558736271/Migrate+risks+to+Risk+Management+module/) from the Risk module via the Jira field cannot be edited. You cannot add new values, either.

![Risk metrics in the risk register. The risk probability values are imported.](/cms_trial/assets/44c435c8-a1f6-4b53-bb2f-330200fe05fc.png)

For new risk calculation templates, you can add two metric items.

![Two empty metric items called metric item 1 and metric item 2.](/cms_trial/assets/b554702c-5b7d-4fce-a8aa-288ccc92746e.png)

### Risk matrix and risk levels

You can modify default risk levels and add new ones. Define a new risk level, and assign a color and an icon. When ready, click **Create**.

![assigning a name, icon, and color to a risk level.](/cms_trial/assets/b02dc77f-38eb-4fe0-b77f-b9adac915e9a.png)

You can modify the risk matrix by selecting one of the available risk levels.

![Risk matrix with one of the risk levels being changed.](/cms_trial/assets/9ed43c20-4067-4822-83e5-53bb790c8d1d.png)

## Actions on risk calculations

You can perform the following actions on risk calculation templates:

- [Edit existing risk calculations](/cms_trial/space/SPM/1918865630/Edit+risk+calculation/)
- [Add new risk calculations](/cms_trial/space/SPM/1918670159/Create+new+risk+calculation/)
- [Delete existing risk calculations](/cms_trial/space/SPM/1918702869/Delete+risk+calculation/)

## Risk register frameworks (new navigation)

Click to expand the guide

On the **Risk register frameworks** page, you can configure existing risk calculations or create new ones.

## Access

### From the risk registers list

1. Click the **… More actions** menu > **Register settings**.

   ![Screenshot of the Register settings button in the More actions menu.](/cms_trial/assets/0eaaf5f6-c2a6-4088-bd14-621be92abf16.png)

### From the risks table

1. On the selected risk register screen, select **Configuration** from the drop-down menu.

   ![image-20260326-125530.png](/cms_trial/assets/5fb2cc14-6b1c-4067-a67a-248415a8a424.png)

## Risk calculation attributes

The table presents all risk calculation attributes.

| **Risk calculation attribute** | **Screenshot** |
| --- | --- |
| Risk framework name | Risk framework name attribute. |
| Risk score | Risk score attribute. |
| Metrics | Metrics attributes. |
| Risk matrix | Risk matrix attribute. |
| Risk levels | Risk levels attribute. |

### Risk framework name

Typing a name in the field automatically updates the risk calculation row at the top.

![New risk calculation name entered and it's automatically updated in the risk calculation row above.](/cms_trial/assets/ae8e82d4-e223-4be8-a345-404d1f351b82.png)

### Risk score

If the scoring calculation needs improvement, you can tweak the score formula or create a completely new one. Simple math operators such as `* / - + ( )`, numbers, and metrics can be used.

You can customize score formulas using the metrics included in a template. Before making any changes to the formula, ensure all necessary metrics are added to the template.

#### Basic formula edit

To edit a score formula:

1. Click in the **Risk Score** field.
2. To add a new field to the formula, start typing to see available metrics.

   ![The risk score field, with the impact metric appearing after th](/cms_trial/assets/6716453a-3fd1-41ee-b5e5-9ad7adf032fc.png)
3. To change a math operator, click it and select a new one from the list.

   ![showing how to change the math operator in the Risk score field.](/cms_trial/assets/00b8675f-e552-412f-94ac-603b5f166d90.png)
4. To delete a metric from the formula, click the field and press **Delete**.

#### Advanced formula edit

If you want more flexibility when editing the scoring formula, then you can use **Advanced edit mode**.

1. Click **Switch to advanced edit** under Risk score.

   ![Risk score field showing the Switch to advanced edit button.](/cms_trial/assets/68cd017f-dde9-4486-80fa-de40356a1cdc.png)
2. You can edit metrics and operators.
3. Metrics in the advanced edit mode must be wrapped in braces (curly brackets).   
   Example: `{{Impact}}`

   ![A metrics template showing the Add value button.](/cms_trial/assets/56605fe4-3fa7-42cc-bfdc-2a2ce034b7f7.png)![image-20250319-140250.png](/cms_trial/assets/8db81e65-8275-49bc-857e-4a6db9aeab2f.png)

### Metrics

When editing an existing template, you can update the attributes of existing metrics, such as the metric’s name, value names, colors, and values. You can also add new values to existing metrics.

Exception: [Metric attributes imported](/cms_trial/space/SPM/3558736271/Migrate+risks+to+Risk+Management+module/) from the Risk module via the Jira field cannot be edited. You cannot add new values, either.

![A metrics template in the risk register. Risk probability metrics are imported.](/cms_trial/assets/44c435c8-a1f6-4b53-bb2f-330200fe05fc.png)

For new risk calculation templates, you can add two metric items.

![Two empty metric items called metric item 1 and metric item 2.](/cms_trial/assets/b554702c-5b7d-4fce-a8aa-288ccc92746e.png)

### Risk matrix and risk levels

You can modify default risk levels and add new ones. Define a new risk level, and assign a color and an icon. When ready, click **Create**.

![assigning a name, icon, and color to a risk level.](/cms_trial/assets/b02dc77f-38eb-4fe0-b77f-b9adac915e9a.png)

You can modify the risk matrix by selecting one of the available risk levels.

![Risk matrix with one of the risk levels being changed.](/cms_trial/assets/9ed43c20-4067-4822-83e5-53bb790c8d1d.png)

## Actions on risk calculations

You can perform the following actions on risk calculation templates:

- [Edit existing risk calculations](/cms_trial/space/SPM/1918865630/Edit+risk+calculation/)
- [Add new risk calculations](/cms_trial/space/SPM/1918670159/Create+new+risk+calculation/)
- [Delete existing risk calculations](/cms_trial/space/SPM/1918702869/Delete+risk+calculation/)