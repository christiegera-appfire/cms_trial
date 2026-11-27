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

![Workflow view showing workflow properties, triggers, states, and parameters.](/cms_trial/assets/f66112a9-a5fb-4a1d-8e84-eb63883e29df.png)

For a custom workflow, you can:

- Click the workflow name to edit the name and description.
- Add one or more workflow triggers.
- Add, edit, and delete a state.
- Add and edit workflow parameters.
- Add and edit workflow triggers.

### State view

![State view showing the selected workflow state's properties, transitions, approvals, and parameters.](/cms_trial/assets/f983fe2b-4b24-4780-9e2b-3c90d6124e7a.png)

In the state panel, for a custom workflow, you can:

- Access the state editor to edit the state name, state description, state parameters, and expiry due date for the state.
- Add or edit state transitions in the transitions editor.
- Add or edit approvals and the approval reviewers in the approvals editor.

![Visual builder editor displaying configuration options for a workflow state.](/cms_trial/assets/28ad3a98-1054-42f5-b480-87eca1013b89.png)

See [Workflow elements and concepts](/cms_trial/space/CDMC/2193066207/Workflow+elements+and+concepts/) for more information.

## **Workflow Navigator**

You can use the navigator panel to view the workflow visually, toggle to the [code editor](/cms_trial/space/CDMC/2192837873/JSON+code+editor/), save changes to the workflow, and exit the app space settings. It also includes shortcuts to edit or add new workflow components, using the buttons or clicking on the workflow state lozenges.

![Workflow navigator showing the workflow diagram and editor controls.](/cms_trial/assets/22d0fe03-21bb-43e0-8f65-9bf49d52a599.png)

The Visual Builder Editor fully adapts to Confluence’s dark mode theme.

![Visual builder editor displayed in Confluence dark mode.](/cms_trial/assets/90e06248-ca4c-4c78-b5a0-0e49cdfeef66.png)

## Steps to use the Visual Builder Editor

You can edit an existing workflow or create a new one and edit it with the **Visual Builder Editor.**

To create a new workflow:

1. Log in to your Confluence space.
2. Choose **Comala document management** under *Space Apps*.
3. Click **Create New Workflow.** 

   ![Comala Document Management page with the Create New Workflow button.](/cms_trial/assets/d54e5953-f7d5-40ea-b9a7-685d09f2e8c4.png)

This opens the Visual Builder Editor.

1. In the *workflow panel* of the Visual Builder Editor, enter the details of your new workflow:

   1. Add a name and a workflow description.
   2. Add one or more content labels to filter the workflow's app to the document content label. When one or more labels are added, the active workflow can only be applied to documents that have at least one of the specified labels. Select the **Exclude labels** checkbox to apply the workflow only to documents that don’t have any of the specified labels.
   3. Click **Apply** tosave the changes in the workflow panel.

![Create Workflow panel showing fields for the workflow name, description, and label settings.](/cms_trial/assets/797ade0e-c6e6-47c6-ab21-a47a6bc2c1ad.png)

1. Select **Save** in the*navigator panel*to update the workflowand the *app space settings*.

![Navigator panel with the Save button indicated.](/cms_trial/assets/752918c5-4ab8-4f36-ace9-8baf1df53cad.png)

1. Click **Exit** to view the workflow in the app space settings.

![Navigator panel with the Exit control used to leave the visual builder editor.](/cms_trial/assets/5cc6432f-e37b-46dd-b979-dd4c89f30f23.png)

### Related topics

- [JSON code editor](/cms_trial/space/CDMC/2192837873/JSON+code+editor/)
- [Workflow elements and concepts](/cms_trial/space/CDMC/2193066207/Workflow+elements+and+concepts/)