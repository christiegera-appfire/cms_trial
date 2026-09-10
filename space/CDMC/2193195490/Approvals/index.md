# Approvals

## Overview

Approvals are added to a state in a workflow using the *Approval Editor* in the *Workflow Builder Visual Editor*. One or more approvals (content review) can be added to each workflow state in a custom workflow.

## Configure an approval

To add an approval for a custom workflow:

1. Log in to your Confluence space
2. Choose **Comala document management** under *Space* *Apps*.
3. A list of existing workflows is displayed. Click **Create New Workflow** or click the **Edit** icon to edit an existing workflow.

   ![Workflow management page showing the list of existing workflows and the option to create or edit a workflow.](/cms_trial/assets/12cab341-f029-4761-a7b7-93b45150a02e.png)
4. In the visual builder editor of an existing custom workflow, clickany **State** > **Approval** under *States.*
5. To add a new approval, click + **Add Approval**.

   ![Workflow state configuration showing the Add Approval option for a selected workflow state.](/cms_trial/assets/f5a5f8a2-f191-4ce3-ad18-f4951fac2319.png)

The **Add Approval** dialog opens.

![Add Approval dialog displaying configuration options for approval settings, outcome criteria, and reviewers.](/cms_trial/assets/852ac5fa-9505-46ce-83ab-c0037449883b.png)

The **Add Approval** dialog is organized into three sections:

### **General Settings**

- **Approval Name:** Enter a descriptive name for your approval (for example, `Legal Review`). Special characters such as **? ! @ #** are not allowed in the name.
- **Custom Action Labels:** Rename the default **Approve** and **Reject** buttons to fit your team’s vocabulary (for example, **Sign Off** or **Needs Changes**).
- **Authentication Method:** Optionally require reviewers to authenticate their decision, including via OTP. The default is *Not required*. See [E-signatures (credentials)](/cms_trial/space/CDMC/2192903044/E-signatures+(credentials)/) for details on setting up e-signature authentication.

  ![Authentication Method setting showing available approval authentication options, including OTP verification.](/cms_trial/assets/268485bc-05f9-458f-9895-9878bbec267e.png)

### **Outcome Criteria**

Define how many reviewers must participate and how the final decision is determined.

- **Required participation:** Choose how many assigned reviewers must make a decision before the approval can be finalized.

  - **All or default**: If reviewers are assigned, all of them must record a decision. If no reviewers are assigned, at least one reviewer must participate. For example, if 3 reviewers are assigned to an approval, all 3 must record a decision before the outcome is finalized. If no reviewers are assigned, at least 1 reviewer must participate.
  - **Minimum participants**: Set a **Minimum participation** number to specify how many reviewers must participate before a decision is finalized. This is useful when you have a large pool of reviewers but only need a subset to weigh in. For example, if 10 reviewers are assigned and the minimum participation is set to 3, the outcome is finalized once any 3 reviewers have recorded their decisions. The remaining reviewers don’t need to participate.

    ![Required participation settings showing the Minimum participants option and participation threshold field.](/cms_trial/assets/d9b30d50-77f1-4243-b4fe-d14cd6bb19f0.png)
- **Decision type:** Choose how reviewer decisions are evaluated to determine the approval outcome.

  - **Unanimity**: All participating reviewers must agree (all approve or all reject) for the decision to pass.
  - **Majority**: The decision follows the majority vote among actively participating reviewers, not the total number assigned. For example, if 5 reviewers are assigned and 3 participate, the outcome is based on the 3 active participants. If 2 approve and 1 rejects, the content is approved.
  - **Minimum approvals/rejections**: Set explicit **Minimum approvals** and **Minimum rejections** thresholds for each outcome. The approval is finalized when either threshold is met.   
    When both thresholds are configured, they are evaluated independently. The first threshold reached determines the outcome.

    If both thresholds are met at the same time:

    - The majority decision takes effect when one outcome has more votes than the other.
    - If votes are evenly split, the outcome defaults to rejection.

For example, if 4 participants are required, with a minimum of 3 approvals or 1 rejection, and the first 3 reviewers approve while the last rejects, the content is still approved.

![Approval outcome settings showing minimum approval and rejection thresholds used to determine the final decision.](/cms_trial/assets/e2b2b863-9396-40a7-a3f7-b937aaa1f1ef.png)

### **Reviewers**

Control who can participate in the approval, how reviewers are assigned, and whether assignments persist across review cycles.

- **Allowed reviewers:** Define whether any user can approve, or only assigned reviewers.
- **Manually assign reviewers:** Allow reviewers to be added or removed using the [workflow state dialog](/cms_trial/space/CDMC/2192968161/Assign+reviewers+through+the+workflow+state+dialog/) while an approval is active. You can add or remove reviewers at any point during the approval process.
- **Pre-assign users:** Select individual users to be automatically assigned as reviewers when the approval starts.
- **Pre-assign groups:** Select entire Confluence groups to be automatically assigned as reviewers when the approval starts.
- **Remember reviewers:** When enabled, preassigned reviewers who were unassigned during a review cycle are automatically reassigned in future rounds of the same approval. Approval parameter: `rememberassignees`. Default: `false`.

  - `true` – any subsequent reviews in the workflow that have the same name as this review will automatically have the same reviewers assigned (“sticky assignees”).
  - `false` – don’t remember assignees.

![Reviewer assignment settings showing options to assign users, groups, and approval participants.](/cms_trial/assets/8a5358d8-343f-4243-b772-a349d9d8e0c3.png)

1. Click **Add** in the *Add approval* dialog. The new approval has now been added to your workflow.

**Related topics**

- [E-signatures (credentials)](/cms_trial/space/CDMC/2192903044/E-signatures+(credentials)/)