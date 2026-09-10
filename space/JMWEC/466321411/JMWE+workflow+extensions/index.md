# JMWE workflow extensions

![Administration page for all JMWE workflow extensions](/cms_trial/assets/a9d9f63d-e875-4720-ac0a-4fd3d39bf928.png)

The **JMWE workflow extensions** section of the JMWE Administration pages lists all of the workflow extensions that have been created in your Jira instance. From this administration page, you can perform multiple actions on the extensions, such as activate or deactivate them; view statistics including when it was last modified, its last run log, and any errors and/or warnings; and access a shortcut to edit the extension. The page consists of two primary sections - the **workflow selector** and the **extension list**. Additionally, new extensions can be created using the **Create new** button to the right of the workflow selector.

**Please note**: only extensions created with JMWE will be included on this page.

## Workflow selector

The primary filter for the Workflow Extensions page is the **workflow selector**. Selecting a workflow will display only the extensions that have been added to that workflow.

## Show obsolete only

As noted in [Deprecated post functions](/cms_trial/space/JMWEC/542803231/Deprecated+post+functions/), changes to Atlassian’s infrastructure require that deprecated JMWE post functions be **completely removed by the end of October 2025**. Please review the documentation on how this impacts your automations and how to update your workflows and Actions to the current versions of each deprecated post function.

Check this box to filter the display of extensions to only display obsolete post functions. The checkbox includes a number indicating how many deprecated post functions exist. This allows you to quickly switch between workflows using the selector and identify which workflows still include deprecated post functions.

## Create new

![Dialog for creating a new workflow extension from the Administration page](/cms_trial/assets/5710b301-1c57-4505-b47d-012740a99861.png)

The **Create new** button can be used to add a new extension to a workflow directly from the JMWE workflow extensions administration page. When you click the button, the **Create new extension** dialog will appear (Figure 2, right); select the **Project**, the **Workflow**, and the **Transition** to which you want to add the extension and click **Submit**.

You will be redirected to the transition editor screen for the selected transition where you can add the new extension.

## Extension list

The extension list contains the following columns:

- **Enabled** - Directly enable or disable the extension.
- **Name & Extension ID** - The name and ID of the extension. Click the name to open the extension in the Automation Rule Builder. The ID value can be used to filter the [JMWE logs](/cms_trial/space/JMWEC/466321741/JMWE+Logs/).
- **Transition** - The workflow transition to which the extension has been added.
- **Type** - Condition, Post-function, or Validator.
- **Executions** - Lists the number of errors or warnings within the last 24 hours.

## Filter and sort

Nearly every column in the table of actions includes tools for sorting the list (ascending or descending for the selected column) and filtering the list. The following tools are available:

- **Filter** - Filter the column based on the possible values. For example, you can filter the list for enabled or disabled actions using the **Enabled** column, filter the actions by the Projects in which they are included (**Project** column), or the post-functions they include (**Post-functions** column).
- **Sort** - Sort the column ascending or descending based on the column values.

**Note**: Due to restrictions on sorting by generic user names, the **By** column does not include the option to sort.