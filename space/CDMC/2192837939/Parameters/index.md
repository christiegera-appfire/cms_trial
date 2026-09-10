# Parameters

## Overview

In Comala Document Management, **workflow parameters** are placeholders that allow flexible values to be added to a workflow. They let you reuse the same workflow across different spaces without changing it.

The space administrator can set workflow parameter values for each space, allowing you to add and use those values without changing the workflow. This makes your workflow easier to manage and more adaptable across teams.

You cannot use a workflow parameter as a value for another workflow parameter.

## Where can you use workflow parameters

You can reference workflow parameters in the following areas:

- **Approvals**: Use parameters to dynamically define reviewers.
- **States**: Apply parameters to set values, such as state expiry dates.
- **Triggers**: Include parameters in trigger actions that support dynamic values.

## Parameter types

You can customize a workflow by adding one or more workflow parameters. When creating a parameter, you need to choose from several supported data types, depending on the kind of value you need. These parameters help make your workflows more flexible and reusable.

- **String**: A plain text value consisting of letters, numbers, or symbols.
- **User**: One or more Confluence usernames. Use this type to assign specific people to tasks or approvals.
- **Group**: One or more Confluence group names. Use this type to assign roles to teams or permission groups.
- **Duration**: A period or a specific date. Often used for setting state expiry or deadlines.
- **List**: A predefined set of values. Users can choose from this list when setting the parameter.

## Add a parameter

To add a parameter to your workflow:

1. Log in to your Confluence space.
2. Choose **Comala document management** under *Space Apps*.

   ![Comala Document Management listed under Space apps.](/cms_trial/assets/6d03a625-f376-462c-8f2c-81834e1dfb6b.png)
3. Click **Create new workflow** or edit an existing custom workflow. For example, when editing an existing workflow, click the **Edit** icon next to the workflow you want to edit.

   ![Workflow list with the Edit option for an existing workflow.](/cms_trial/assets/0d288b97-ac6f-45e2-b8d0-b429bdf523fe.png)

   This opens the [visual builder editor](/cms_trial/space/CDMC/2193162438/Visual+builder+editor/).
4. In the visual builder editor, click **Parameters** to add or edit a parameter.
5. You can click the existing parameter value and edit it, or click **+ Add Parameter** to create a new parameter.

   ![Parameters panel in the visual builder editor showing existing parameters.](/cms_trial/assets/31f66e44-7fc2-4f8d-9d6e-a5d4d376a68b.png)
6. In the **Add parameter** dialog, enter the following details.

   - **Name:** Enter a unique name for your parameter.
   - **Type:** Select a [parameter type](#Parameter-types).
   - **Label:** Enter a descriptive label for your parameter.
   - **Initial value:** Enter an initial value. When the workflow is first applied, this value is set by default.
   - **Description:** Enter a description for your parameter.
   - **Scope**: The `scope` attribute defines where a parameter’s value is accessible. This allows greater flexibility and control over how workflow parameters behave across a space or a specific page. See [scope options](#Scope-options) below for more details.

     ![Add parameter dialog showing the Name, Type, Label, Initial value, Description, and Scope fields.](/cms_trial/assets/d1a24afb-5121-405c-9fc6-4bfa11e4c840.png)

### **Scope options**

If **Scope** = **Workflow** (Default)

- The parameter is available **wherever the workflow is applied**.
- If the workflow is applied at the **space level**, the parameter is shared across all pages using that workflow in the space.
- If the workflow is applied at the **page level**, the parameter is available only to that page.

**Multiple workflows in the same space:**

Each workflow can use the same parameter name with **independent values**.

**Example:**

- `WorkflowA`: `Param1 = value1` → All pages using WorkflowA read `value1`
- `WorkflowB`: `Param1 = value2` → All pages using WorkflowB read `value2`

If **Scope = Page**

- The parameter value is **specific to each page**.
- You can view and edit these values directly in the [workflow dialog](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/) on the page.
- Useful when the same workflow needs to behave differently depending on the page context.

See [Manage workflow parameters](#Manage-workflow-parameters) for more details.

## Working with page parameters

### **Page parameters and space settings**

Page parameters with `scope=page` are not displayed in the **Workflow Parameters** form within **Space Settings**. You can only edit them at the individual page level.

![Workflow Parameters page in Space Settings displaying page-level parameter values.](/cms_trial/assets/3907c33a-f359-4652-94be-8ec3e935b572.png)

### **Initializing page parameters**

If page parameters have **not yet been configured** for a page, opening the **workflow dialog** displays a **Parameters initialization message**.  
This message includes:

- A brief prompt explaining that the parameters need to be set.
- A **Page Parameters** button to begin initialization.

  ![Workflow dialog with the Page Parameters button.](/cms_trial/assets/142b204a-b76b-4e5e-9c53-eb7244a74989.png)

### **Setting Page Parameters values**

After clicking the **Parameters** button:

- A form appears listing all **page-level parameter fields**.
- If initialization values are defined in the workflow, they will be pre-filled in the form.
- Users can review and customize these values before the workflow proceeds.

![Page Parameters dialog with Document Group Reviewers field and the Save Parameters button.](/cms_trial/assets/dfe6efd9-33f3-4868-9d1c-808a002c3760.png)

## Manage workflow parameters

Workflow parameters can be edited directly through the [workflow dialog](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/) on the page.

This option is displayed when:

- There is no active space workflow in the space.
- A page workflow that includes one or more workflow parameters is applied to the page

To manage workflow parameters on the page workflow

1. Add a workflow to a page as a page workflow
2. Once the workflow is added, you can edit its parameters in the *workflow dialog* on the page.   
   Click the **Workflow** **state byline > three-dot menu** (▢) >  **Page Parameters**

1. In the *Workflow Parameters* dialog box, the current parameters values are displayed. Edit the required values for the applied workflow.
2. Click **Save Parameters**.

   ![Page Parameters option selected from the Workflow dialog and the Page Parameters dialog underneath.](/cms_trial/assets/0f75fd20-7ac8-44a9-ae23-9b47e6dff6a9.png)

   **Related topics**

   - [Workflow builder visual editor](/cms_trial/space/CDMC/2193162438/Visual+builder+editor/)
   - [Workflow state dialog](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/)
   - [Approvals](/cms_trial/space/CDMC/2193195490/Approvals/)