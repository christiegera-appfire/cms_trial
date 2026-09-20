# Risk register frameworks

## Risk register frameworks (old navigation)

Click to expand the guide

On the **Risk register frameworks** page, you can configure existing risk calculations or create new ones.

See an interactive video on how to access the **Risk register frameworks** page.

## Risk calculation attributes

The table presents all risk calculation attributes.

| **Risk calculation attribute** | **Screenshot** |
| --- | --- |
| Risk framework name | Image — asset pipeline pending Risk framework name attribute. |
| Risk score | Image — asset pipeline pending Risk score attribute. |
| Metrics | Image — asset pipeline pending Metrics in the risk register. |
| Risk matrix | Image — asset pipeline pending Risk matrix attribute. |
| Risk levels | Image — asset pipeline pending Risk levels attribute. |

### Risk framework name

Typing a name in the field automatically updates the risk calculation row at the top.

Image — asset pipeline pending  
New risk calculation name entered and it's automatically updated in the risk calculation row above.

### Risk score

If the scoring calculation needs improvement, you can tweak the score formula or create a completely new one. Simple math operators such as `* / - + ( )`, numbers, and metrics can be used.

You can customize score formulas using the metrics included in a template. Before making any changes to the formula, ensure all necessary metrics are added to the template.

#### Basic formula edit

To edit a score formula:

1. Click in the **Risk Score** field.
2. To add a new field to the formula, start typing to see available metrics.

   Image — asset pipeline pending  
   The risk score field, with the impact metric appearing after th
3. To change a math operator, click it and select a new one from the list.

   Image — asset pipeline pending  
   showing how to change the math operator in the Risk score field.
4. To delete a metric from the formula, click the field and press **Delete**.

#### Advanced formula edit

If you want more flexibility when editing the scoring formula, then you can use **Advanced edit mode**.

1. Click **Switch to advanced edit** under Risk score.

   Image — asset pipeline pending  
   Risk score field showing the Switch to advanced edit button.
2. You can edit metrics and operators.
3. Metrics in the advanced edit mode must be wrapped in the braces (curly brackets).   
   Example: `{{Impact}}`

   Image — asset pipeline pending  
   A metrics template showing the Add value button.

   Image — asset pipeline pending  
   image-20250319-140250.png

### Metrics

When editing an existing template, you can update the attributes of existing metrics, such as the metric’s name, value names, colors, and values. You can also add new values to existing metrics.

Exception: [Metric attributes imported](/cms_trial/space/SPM/3558736271/Migrate+risks+to+Risk+Management+module/) from the Risk module via the Jira field cannot be edited. You cannot add new values, either.

Image — asset pipeline pending  
Risk metrics in the risk register. The risk probability values are imported.

For new risk calculation templates, you can add two metric items.

Image — asset pipeline pending  
Two empty metric items called metric item 1 and metric item 2.

### Risk matrix and risk levels

You can modify default risk levels and add new ones. Define a new risk level, and assign a color and an icon. When ready, click **Create**.

Image — asset pipeline pending  
assigning a name, icon, and color to a risk level.

You can modify the risk matrix by selecting one of the available risk levels.

Image — asset pipeline pending  
Risk matrix with one of the risk levels being changed.

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

   Image — asset pipeline pending  
   Screenshot of the Register settings button in the More actions menu.

### From the risks table

1. On the selected risk register screen, select **Configuration** from the drop-down menu.

   Image — asset pipeline pending  
   image-20260326-125530.png

## Risk calculation attributes

The table presents all risk calculation attributes.

| **Risk calculation attribute** | **Screenshot** |
| --- | --- |
| Risk framework name | Image — asset pipeline pending Risk framework name attribute. |
| Risk score | Image — asset pipeline pending Risk score attribute. |
| Metrics | Image — asset pipeline pending Metrics attributes. |
| Risk matrix | Image — asset pipeline pending Risk matrix attribute. |
| Risk levels | Image — asset pipeline pending Risk levels attribute. |

### Risk framework name

Typing a name in the field automatically updates the risk calculation row at the top.

Image — asset pipeline pending  
New risk calculation name entered and it's automatically updated in the risk calculation row above.

### Risk score

If the scoring calculation needs improvement, you can tweak the score formula or create a completely new one. Simple math operators such as `* / - + ( )`, numbers, and metrics can be used.

You can customize score formulas using the metrics included in a template. Before making any changes to the formula, ensure all necessary metrics are added to the template.

#### Basic formula edit

To edit a score formula:

1. Click in the **Risk Score** field.
2. To add a new field to the formula, start typing to see available metrics.

   Image — asset pipeline pending  
   The risk score field, with the impact metric appearing after th
3. To change a math operator, click it and select a new one from the list.

   Image — asset pipeline pending  
   showing how to change the math operator in the Risk score field.
4. To delete a metric from the formula, click the field and press **Delete**.

#### Advanced formula edit

If you want more flexibility when editing the scoring formula, then you can use **Advanced edit mode**.

1. Click **Switch to advanced edit** under Risk score.

   Image — asset pipeline pending  
   Risk score field showing the Switch to advanced edit button.
2. You can edit metrics and operators.
3. Metrics in the advanced edit mode must be wrapped in braces (curly brackets).   
   Example: `{{Impact}}`

   Image — asset pipeline pending  
   A metrics template showing the Add value button.

   Image — asset pipeline pending  
   image-20250319-140250.png

### Metrics

When editing an existing template, you can update the attributes of existing metrics, such as the metric’s name, value names, colors, and values. You can also add new values to existing metrics.

Exception: [Metric attributes imported](/cms_trial/space/SPM/3558736271/Migrate+risks+to+Risk+Management+module/) from the Risk module via the Jira field cannot be edited. You cannot add new values, either.

Image — asset pipeline pending  
A metrics template in the risk register. Risk probability metrics are imported.

For new risk calculation templates, you can add two metric items.

Image — asset pipeline pending  
Two empty metric items called metric item 1 and metric item 2.

### Risk matrix and risk levels

You can modify default risk levels and add new ones. Define a new risk level, and assign a color and an icon. When ready, click **Create**.

Image — asset pipeline pending  
assigning a name, icon, and color to a risk level.

You can modify the risk matrix by selecting one of the available risk levels.

Image — asset pipeline pending  
Risk matrix with one of the risk levels being changed.

## Actions on risk calculations

You can perform the following actions on risk calculation templates:

- [Edit existing risk calculations](/cms_trial/space/SPM/1918865630/Edit+risk+calculation/)
- [Add new risk calculations](/cms_trial/space/SPM/1918670159/Create+new+risk+calculation/)
- [Delete existing risk calculations](/cms_trial/space/SPM/1918702869/Delete+risk+calculation/)