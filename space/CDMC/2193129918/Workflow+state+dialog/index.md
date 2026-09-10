# Workflow state dialog

## Overview

The workflow state dialog helps you track and manage workflow applied to a page or blog post. All workflow actions are accessed and performed from this dialog.

- The dialog displays the workflow name and enables you to view state transitions, manage approvals and rejections, and update workflow parameters.
- You can also view current workflow details, document activity, and view the last approved version of the page.
- Space Administrators can bypass workflow rules and override the current document state.

To open the workflow state dialog on any Confluence page, click the **Document Management** status indicator in the page byline.

![Workflow state dialog showing the current workflow, state flow, reviewers, and actions.](/cms_trial/assets/ea2291d6-b976-4ce1-b2bc-4714687b0eb2.png)

## **Workflow details**

- The dialog displays the name of the active workflow, for example, *Basic Approval Workflow*. To view the workflow details, click the workflow name.

  ![Workflow state dialog with the Basic Approval Workflow link highlighted.](/cms_trial/assets/3c1ab099-ea85-4d9b-be05-4dc908b7ed33.png)
- This opens a full visual diagram of the entire workflow structure.

  ![Workflow diagram showing all workflow states and transitions.](/cms_trial/assets/ab84d47c-2e75-4e2b-8227-08554c70738f.png)

## Visual state flow

The visual state-flow diagram shows the current state and available transitions for the next state.

- Hover over **Next State** to view the available transition states, and hover over the state icon to view the tooltip.

  ![Workflow state diagram with available next-state transitions](/cms_trial/assets/cba5dff1-512e-4737-9034-bd814cfff8a7.png)

## **Reviewers and approvals**

1. To add reviewers for approval, in the workflow state dialog, click **Assign**.
2. The *Assign to* dialog opens. You can search for a user, add multiple reviewers, include a comment, and click **Save**.

   ![Add reviewers for approval](/cms_trial/assets/28b9186c-54af-48f4-83f2-9e4130235fb9.png)
3. The dialog displays the assigned reviewer. You can add multiple reviewers if required.

   ![Reviewer assigned](/cms_trial/assets/6084f6e2-7614-495f-b339-2da65bf89bf7.png)
4. To view the approval details, click any reviewer.
5. **Multi-stage approvals**: If a workflow requires multiple progressive approval stages, the dialog displays a carousel. You can add multiple reviewers for each approval stage.

   ![Multi-stage approval workflow showing multiple approval stages in the carousel.](/cms_trial/assets/ad68ef75-92a2-4ca9-ac07-6c3c0df7cb0c.gif)
6. Approvers can **Approve** or **Reject** and include comments. To add a comment, click **Comment** at the bottom left of the dialog.

   ![Basic Approval Workflow panel with Reject and Approve buttons.](/cms_trial/assets/3632e615-2ed8-483f-9516-761b1898bc5b.png)

## Actions menu

The workflow state dialog actions provide several options based on the workflow state and type. To view the options, click the **Actions** menu (**⋯**) in the top-right corner.

![Workflow state dialog Actions menu.](/cms_trial/assets/edbb839e-ba7c-406c-8707-ed064458124e.png)

- **Current Workflow**: Displays a visual diagram of the current workflow.
- **State Description**: Displays the current workflow state description. You can also view the state description by clicking the show state description icon (▢) in the dialog.
- **Document Activity**:Displays a summary of workflow-related actions on the page, including who approved, rejected, or changed states and when. Refer to the [document activity report](/cms_trial/space/CDMC/2193162907/Document+activity+(document-level)/).

  ![Document activity](/cms_trial/assets/ccacfc6d-1c0f-4954-90d1-c886047dada8.png)
- **View Approved Version**: Displays the latest approved version of the page.
- **Override State**:

  - This option is only available to Space Administrators who have page edit permissions. Otherwise, the option is disabled.
  - It bypasses all workflow rules and overrides the page's current state.
  - Every override is recorded in the **Document Activity** log.

    ![Override State dialog showing state change options with Approved selected.](/cms_trial/assets/1d646d24-7082-4d46-a3b5-bcee2c857107.png)

--

When a page-level workflow is applied, the **Actions** menu includes two additional options:

- **Page Parameters**: View and edit workflow parameter values for the page. See [Parameters](/cms_trial/space/CDMC/2192837939/Parameters/) for more details.

  ![Page Parameters dialog for viewing and editing workflow.](/cms_trial/assets/0c5245fc-49d5-4e01-8b18-e302db700ec5.png)

- **Remove Workflow**: Remove the workflow from the current page. Space-level workflows can’t be removed from individual pages.

  ![Remove Workflow confirmation dialog for a page-level workflow.](/cms_trial/assets/15eb3aa3-dd9d-42a7-bc73-60350fdf65b2.png)