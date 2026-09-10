# Global workflows

## Overview

Comala Document Management provides global workflows, which can be applied to multiple spaces in your Confluence.

- Once you install the app, three built-in global workflow templates are available by default in your Confluence.
- These global workflow templates are fully editable. You can customize or delete them to match your process.
- To access and manage Global Workflows, you must have **Confluence Site Administrator** permissions.

- The **Global Workflows** provide Administrators a centralized location for managing workflows, ensuring consistency and control globally.
- Administrators can:

  - Create, delete, enable, or disable workflows across multiple spaces.
  - Centrally manage workflow states, rules, and transitions to ensure consistent content review and approval processes across the organization.

### Watch this video to see how you can use Comala global workflows across different Confluence spaces for centralized document compliance

Video transcript

**Global Workflows in Comala Document Management: Financial Services QMS Walkthrough**

The financial services group runs its quality management system workflows across four Confluence spaces.

Keeping approval processes consistent across all of them used to mean managing workflows one space at a time — until it started using Comala Document Management Global Workflows.

To view Global Workflows, navigate to Comala Document Management under Apps. This gives Confluence Site Administrators a single place to create and manage workflow states, rules, and transitions — ensuring consistent review and approval across the organization.

The firm’s Compliance team manages Global Workflows.

For each workflow, the dashboard shows its Visibility toggle, Name, and description, any trigger Label, and how many spaces it's Linked to — with an Actions menu to manage it further.

Let's link the Quality Management System Workflow to the Risk space.

To do so, navigate to the Risk space, then click Comala Document Management under Space apps.

This is the Risk Space Workflows dashboard.

Click Link or Copy Workflow, select the Quality Management System Workflow, and choose Link.

Risk space now inherits this workflow automatically, scoped Global — active workflow in this space, but can't be edited at the space level.

Any future updates to the global version automatically apply to the space level.

Now let's copy the same workflow into the Internal Controls space instead.

Click Link or Copy Workflow — this time, choose Copy.

This creates an independent version scoped to the space that the Internal Controls team can customize without affecting the original global workflow.

Next, let's look at label-scoped workflows.

The Audit team wants to use a centralized workflow across all its pages, each tagged with the AUDIT label.

Navigate to the Comala Document Management space workflows

Click Link or Copy Workflow, select the Audit Management Workflow, and choose Link.

The Audit space now inherits this workflow, scoped as Global, with the AUDIT label shown.

Navigating to the space pages, you can see the workflow applied automatically wherever the label appears — no manual assignment needed.

Workflows and labels stay in sync in both directions, though the page can take a moment to reflect the applied state — refresh if it doesn't appear right away.

Now, let's get back to the Global Workflows dashboard.

The linked space count now updates to reflect the newly linked spaces.

The Actions menu lets us view workflow details, duplicate it, edit it in the visual builder or code editor, delete it, or check its version history.

Let's check the version history of the Audit Management Workflow.

Every edit is saved as a version — you can view the JSON behind any prior version, or click Revert to restore it instantly.

Reverting creates a new version so nothing is lost, and the change applies globally across every linked space right away.

That's Global Workflows — one dashboard, full control, applied consistently across the organization.

## Manage global workflows

- Log in to your Confluence instance and navigate to **Apps** > **Comala Document Management**.
- This opens the *Global Settings* page and displays the **Global Workflows** dashboard.

  ![Global Workflows dashboard showing the list of available global workflows and workflow controls.](/cms_trial/assets/62a35213-c92a-4342-af2e-879627870927.png)

To navigate to Global Workflows from the *Space Workflows* page, click **Global Workflows** in the workflows list.

![Navigate to the Global Workflows from the Space Workflows](/cms_trial/assets/9c3d3549-73dc-4720-a2fc-d1bc9d9e28a6.png)

### Global workflows dashboard

- The **Global Workflows** dashboard displays the list of built-in global workflows and their details.
- To create a new workflow, refer to the [create and edit workflows](/cms_trial/space/CDMC/2193162391/Create+and+edit+workflows/) page.

  ![Global workflows dashboard](/cms_trial/assets/2a16a76d-f8b2-448a-9d20-b5e49ae90c82.png)
- The dashboard displays the following details for each workflow:

  - **Visibility**: Toggle to enable or disable the workflow globally. Only the enabled workflows can be applied to a space.
  - **Name**: Displays the workflow title and a short description.
  - **Labels**: Shows the page label, if any, required to trigger the workflow. For example, the *Basic Approval Workflow* is configured to run only with the `SIMPLE` label.
  - **Linked**: Indicates how many Confluence spaces currently have this specific workflow applied. To view the space details, click **space count**. The dialog shows the linked spaces.

    ![Under Linked, click space count to view linked spaces](/cms_trial/assets/faf7d800-98ff-4886-ae24-655576b9fcc6.png)
  - **Actions** - Under *Actions*, you can view workflow details, duplicate the workflow, edit it using the visual builder or code editor, delete it, and view the version history.

    - **Version history**

      Each edit to a global workflow is saved as a new version.

      To view version history,

      - In the **Actions** column, click the **three-dot menu** (⋯) and select **View History**.

        ![To view the workflow version history, under Actions, navigate to the More actions](/cms_trial/assets/731c3f59-ac7f-48e1-91b0-a1f0ae4e7fc6.png)
      - The version history dialog displays all saved versions.

        - Click **View JSON** to view any previous version’s definition.
        - Click **Revert to this version** to restore a previous version.
      - Reverting creates a new version entry, and no history is lost. The reverted workflow applies globally to all pages and spaces using it.

        ![To revert to any previous version, click Revert to this version](/cms_trial/assets/9c18fdba-97ad-43e8-93e7-c9536c7e6cd7.png)
      - When the revert completes, a success message is displayed.

        ![Revert version_success message](/cms_trial/assets/f9cb7f27-3668-4a2c-ae3e-f868c7a1131f.png)

Deleting a workflow cannot be undone. Before you delete, consider the impact on any spaces using the workflow.

### Link/Copy Workflow

A global workflow can be linked or copied to a space.

To link or copy a global workflow:

1. Log in to your Confluence space and go to **Space apps** > **Comala Document Management**.
2. This opens the **Comala Document Management** configuration page for your space.
3. In the **Space Workflows** dashboard, click **Link/Copy Workflow**.

   ![In the Space Workflows dashboard, click Link or Copy Workflow](/cms_trial/assets/9b503efe-ed5c-48f4-ba1c-a6f3c4dc9e76.png)
4. The *Global workflows* dialog opens and displays a list of available workflows to link or copy.

   ![Global workflows dialog opens and displays a list of available workflows to link or copy](/cms_trial/assets/6c73fa0f-cc77-4388-b027-b5f737771a50.png)
   - **Link**: You can link a global workflow in space workflows.

     - A linked global workflow cannot be edited at the space level and automatically syncs future updates.
     - A global workflow can be linked to multiple spaces. Updates made to a global workflow are automatically applied to all linked spaces.

       ![Link a global workflow in space workflow](/cms_trial/assets/25d5d5dc-9237-4cf6-bebc-f1e1ce42b780.png)
   - **Copy**: Copy creates an independent version of the workflow in your space that you can edit without affecting the original global workflow.

     ![Workflow copied to space workflow ](/cms_trial/assets/f90b7951-98ee-4bd7-9fa3-a25dda726c53.png)

**Related topics**

- [Space workflows](/cms_trial/space/CDMC/2193033075/At+space+level/)
- [Visual builder editor](/cms_trial/space/CDMC/2193162438/Visual+builder+editor/)
- [Code editor](/cms_trial/space/CDMC/2192837873/JSON+code+editor/)
- [Workflow elements and concepts](/cms_trial/space/CDMC/2193066207/Workflow+elements+and+concepts/)