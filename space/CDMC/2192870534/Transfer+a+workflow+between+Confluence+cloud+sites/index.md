# Transfer a workflow between Confluence cloud sites

## Scenario

I want to transfer my workflows from a test Confluence Cloud site to a production site. Is there a way to export workflows to a file and import them into the production environment, or do I need to recreate them manually?

## Solution

You don't need to use an import/export tool. To transfer your workflow from one Confluence Cloud site to another Confluence Cloud site is a manual procedure.

- Copy the JSON code of your Comala workflow from the code editor in the cloud test site space.
- Create a new workflow in the production space in your cloud production site.
- Paste the code you previously copied in place of the JSON code of the newly created workflow.

You need space administrator permission in the test space and the production space.

If you require the workflow in additional spaces in your production site, as above, copy and paste the workflow JSON code into the other space.

## Steps

**Copy the workflow template JSON code in the test space**

To open the code editor for the workflow in the test space document management dashboard,

1. Use the **Actions** menu option to edit with the code editor

![Comala custom workflow with code editor icon selected for transfer](/cms_trial/assets/32b9bd84-49d0-48d0-a1dd-26ecf5e934e5.png)

1. Highlight the workflow template JSON code in the code editor and copy the JSON code to the clipboard.

![Comala code editor with custom workflow JSON definition](/cms_trial/assets/4a749671-0ede-401e-b0e4-f3e7e55ec7c0.png)

To create a new workflow in the production space

1. Choose the **Create new workflow** option in the production space document management dashboard.
2. Click the **Code Editor** icon in the visual editor.

![Comala workflow builder create workflow with code editor toggle](/cms_trial/assets/910c8c5d-3776-4ad8-9d94-afd7ca4eb113.png)

In the code editor,

1. Paste the copied JSON code to replace the existing workflow code.
2. Click **Save** and then **Exit.**

![Comala code editor create new workflow with paste area highlighted](/cms_trial/assets/6094be7b-4fee-4a55-80e2-0f1f1a1e25e5.png)

The workflow is now added as a custom workflow in the production space document management dashboard.

This is a manual process for each workflow. It is also the same process when moving a workflow template from one space to another space in the same Confluence Cloud site.