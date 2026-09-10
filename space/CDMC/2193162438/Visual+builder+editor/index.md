# Visual builder editor

## Overview

The visual builder editor in Comala Document Management provides a graphical interface to edit an existing workflow or create a new one without writing code.

Here is a short demo on how to use the **visual builder editor** in Comala Document Management for Cloud.

The visual editor has two main sections: the Workflow panel and the workflow navigator.

## Workflow panel

You can use the workflow panel to add new workflow components and edit options for the workflow, each workflow state, workflow parameters, and workflow triggers.

The workflow panel is contextual. The options change according to the current task, such as adding or editing a state, editing an approval, and editing the workflow.

It has two views:

### **Workflow view**

![Workflow view showing workflow properties, triggers, states, and parameters.](/cms_trial/assets/e0536343-4909-40db-bb86-a259fc14b92b.png)

For a custom workflow, you can:

- Click the workflow name to edit the name and description.
- Add one or more workflow triggers.
- Add, edit, and delete a state.
- Add and edit workflow parameters.
- Add and edit workflow triggers.

### State view

![State view showing the selected workflow state's properties, transitions, approvals, and parameters.](/cms_trial/assets/c7b6efaf-f320-42cf-896d-757a5cfaae5c.png)

In the state panel, for a custom workflow, you can:

- Access the state editor to edit the state name, state description, state parameters, and expiry due date for the state.
- Add or edit state transitions in the transitions editor.
- Add or edit approvals and the approval reviewers in the approvals editor.

![Visual builder editor displaying configuration options for a workflow state.](/cms_trial/assets/78481a71-fdfa-49c8-9550-0e10748dfb7b.png)

See [Workflow elements and concepts](/cms_trial/space/CDMC/2193066207/Workflow+elements+and+concepts/) for more information.

## **Workflow Navigator**

You can use the navigator panel to view the workflow visually, toggle to the [code editor](/cms_trial/space/CDMC/2192837873/JSON+code+editor/), save changes to the workflow, and exit the app space settings. It also includes shortcuts to edit or add new workflow components, using the buttons or clicking on the workflow state lozenges.

![Workflow navigator showing the workflow diagram and editor controls.](/cms_trial/assets/f08b440c-115a-4b5a-b1ce-d2b369218ab5.png)

The Visual Builder Editor fully adapts to Confluence’s dark mode theme.

![Visual builder editor displayed in Confluence dark mode.](/cms_trial/assets/8ea598b0-620b-45e2-9f5f-9fc4a65d429d.png)

## Steps to use the Visual Builder Editor

You can edit an existing workflow or create a new one and edit it with the **Visual Builder Editor.**

To create a new workflow:

1. Log in to your Confluence space.
2. Choose **Comala document management** under *Space Apps*.
3. Click **Create New Workflow.** 

   ![Comala Document Management page with the Create New Workflow button.](/cms_trial/assets/415480a2-5983-46cc-9b9b-7321a5fc9910.png)

This opens the Visual Builder Editor.

1. In the *workflow panel* of the Visual Builder Editor, enter the details of your new workflow:

   1. Add a name and a workflow description.
   2. Add one or more content labels to filter the workflow's app to the document content label. When one or more labels are added, the active workflow can only be applied to documents that have at least one of the specified labels. Select the **Exclude labels** checkbox to apply the workflow only to documents that don’t have any of the specified labels.
   3. Click **Apply** tosave the changes in the workflow panel.

![Create Workflow panel showing fields for the workflow name, description, and label settings.](/cms_trial/assets/c7155b47-deec-4a8f-a52f-132ccf40109b.png)

1. Select **Save** in the*navigator panel*to update the workflowand the *app space settings*.

![Navigator panel with the Save button indicated.](/cms_trial/assets/0c9d926b-439d-4966-821e-0da3ffe2c66e.png)

1. Click **Exit** to view the workflow in the app space settings.

![Navigator panel with the Exit control used to leave the visual builder editor.](/cms_trial/assets/d6a376af-4fff-4480-90b6-e641c218accf.png)

### Related topics

- [JSON code editor](/cms_trial/space/CDMC/2192837873/JSON+code+editor/)
- [Workflow elements and concepts](/cms_trial/space/CDMC/2193066207/Workflow+elements+and+concepts/)