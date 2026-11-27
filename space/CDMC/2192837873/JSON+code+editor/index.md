# JSON code editor

## Overview

Use the **JSON Code Editor** to create and customize workflows in Comala Document Management. Only the space administrator can edit the workflow template using the **code editor**.

The JSON Code Editor provides flexibility for power users who need more customization than the visual workflow builder allows. With the JSON code editor, you can,

- **Manually define and modify workflows** by editing the JSON structure directly.
- **Import and export workflows** across different spaces or instances by copying and pasting JSON code.
- **Refine workflow logic**, including triggers, conditions, transitions, and notifications.
- **Apply advanced configurations**, such as integrating external systems or automating document approvals with precise control.

## Steps to use the JSON code editor

You can edit an existing custom workflow or create a new one and edit it with the JSON code editor. In this example, let’s create a new workflow and build it with the code editor.

1. Log in to your Confluence space.
2. Choose **Comala document management** under *Space Apps*.
3. Click **Create New Workflow**.

   ![Create New Workflow button on the Comala Document Management workflows page.](/cms_trial/assets/0924a8cb-e04b-4248-894d-38326c3f146c.png)
4. The visual builder is displayed by default. Click the `{}` icon to open the JSON code editor.

   ![Visual workflow builder with the JSON code editor button indicated.](/cms_trial/assets/2ebadae6-3005-42bc-8c5c-745d66dc7258.png)
5. The workflow template JSON code is displayed in the workflow schema box and can be edited directly in the editor.

   ![JSON Code Editor displaying the workflow template JSON schema.](/cms_trial/assets/93a8a33f-dd12-481d-8283-13edc95339aa.png)
6. Click **Save** to save your code.

The JSON code editor includes the following:

- Color coding to distinguish property names, values, and different data types.
- Autocomplete feature for workflow properties and values.
- Dropdown selectors for available property names, including workflow triggers, workflow parameters, states, transitions, and approvals.
- A search tool accessed by the keyboard shortcut **CMD+F**.

The workflow builder also lets you toggle between the visual and code editors using the editor icon buttons in the right-hand navigator panel.

Changes applied in one editor are dynamically updated in the other editor.

If migrating from server to the cloud, each server workflow can be translated to a cloud-compatible JSON workflow template using the Workflow Translator for Cloud in data center and server apps. The cloud-compatible JSON for each workflow can be copied from the translator and pasted into the cloud app code editor.