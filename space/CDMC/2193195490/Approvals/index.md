# Approvals

## Overview

Approvals are added to a state in a workflow using the *Approval Editor* in the *Workflow Builder Visual Editor*. One or more approvals (content review) can be added to each workflow state in a custom workflow.

## Configure an approval

To add an approval for a custom workflow:

1. Log in to your Confluence space
2. Choose **Comala document management** under *Space* *Apps*.
3. A list of existing workflows is displayed. Click **Create New Workflow** or click the **Edit** icon to edit an existing workflow.

   ![Workflow management page showing the list of existing workflows and the option to create or edit a workflow.](/cms_trial/assets/66b4d444-5626-436f-9d8f-01f9269077b4.png)
4. In the visual builder editor of an existing custom workflow, clickany **State** > **Approval** under *States.*
5. To add a new approval, click + **Add Approval**.

   ![Workflow state configuration showing the Add Approval option for a selected workflow state.](/cms_trial/assets/473b69a6-fe03-4e66-b551-08280301ee3d.png)

The **Add approval** dialog opens.

![image-20260923-143811.png](/cms_trial/assets/86b88df7-9935-4cb7-90d4-e30f90a6cc1f.png)

The **Add approval** dialog is organized into three sections:

### **General Settings**

- **Approval Name:** Enter a descriptive name for your approval (for example, `Legal Review`). Special characters such as **? ! @ #** are not allowed in the name.
- **Custom Action Labels:** Rename the default **Approve** and **Reject** buttons to fit your team’s vocabulary (for example, **Sign Off** or **Needs Changes**).
- **Authentication Method:** Optionally require reviewers to authenticate their decision, including via OTP. The default is *Not required*. See [E-signatures (credentials)](/cms_trial/space/CDMC/2192903044/E-signatures+(credentials)/) for details on setting up e-signature authentication.
- **Require a comment:** Require reviewers to add a comment when they approve or reject. When **Require a comment** is enabled, a reviewer cannot submit an approval or rejection without entering a comment explaining their decision. This is useful for audit trails and reviews that need a documented rationale, such as legal or compliance sign-off. This setting is off by default.

![image-20260923-113207.png](/cms_trial/assets/c653fe20-d368-4c61-a505-8d660ee70ae4.png)

### **Outcome Criteria**

Define how many reviewers must participate and how the final decision is determined.

- **Required participation:** Choose how many assigned reviewers must decide before the approval can be finalized.

  - **All or default**: If reviewers are assigned, all of them must record a decision. If no reviewers are assigned, at least one reviewer must participate. For example, if 3 reviewers are assigned to an approval, all 3 must record a decision before the outcome is finalized. If no reviewers are assigned, at least 1 reviewer must participate.
  - **Minimum participants**: Set a **Minimum participation** number to specify how many reviewers must participate before a decision is finalized. This is useful when you have a large pool of reviewers but only need a subset to weigh in. For example, if 10 reviewers are assigned and the minimum participation is set to 3, the outcome is finalized once any 3 reviewers have recorded their decisions. The remaining reviewers don’t need to participate.

    ![Required participation settings showing the Minimum participants option and participation threshold field.](/cms_trial/assets/b739c2fa-b2b8-4799-a9ef-39dd95df5d75.png)
- **Decision type:** Choose how reviewer decisions are evaluated to determine the approval outcome.

  - **Unanimity**: All participating reviewers must agree (all approve or all reject) for the decision to pass.
  - **Majority**: The decision follows the majority vote among actively participating reviewers, not the total number assigned. For example, if 5 reviewers are assigned and 3 participate, the outcome is based on the 3 active participants. If 2 approve and 1 rejects, the content is approved.
  - **Minimum approvals/rejections**: Set explicit **Minimum approvals** and **Minimum rejections** thresholds for each outcome. The approval is finalized when either threshold is met.   
    When both thresholds are configured, evaluate them independently. The first threshold reached determines the outcome.

    If both thresholds are met at the same time:

    - The majority decision takes effect when one outcome has more votes than the other.
    - If votes are evenly split, the outcome defaults to rejection.

For example, if 4 participants are required, with a minimum of 3 approvals or 1 rejection, and the first 3 reviewers approve while the last rejects, the content is still approved.

![Approval outcome settings showing minimum approval and rejection thresholds used to determine the final decision.](/cms_trial/assets/c9605a71-7417-41c3-a522-8d147b2cdd61.png)

### **Reviewers**

Control who can participate in the approval, how reviewers are assigned, and whether assignments persist across review cycles.

- **Allowed reviewers:** Define whether any user can approve, or only assigned reviewers.
- **Manually assign reviewers:** Allow reviewers to be added or removed using the [workflow state dialog](/cms_trial/space/CDMC/2192968161/Assign+reviewers+through+the+workflow+state+dialog/) while an approval is active. You can add or remove reviewers at any point during the approval process.
- **Allow self-assignment:** Control whether users can add or remove themselves as reviewers on an active approval. Only applies when **Manually assign reviewers** is enabled. Enabled by default.
- **Pre-assign users:** Select individual users to be automatically assigned as reviewers when the approval starts.
- **Pre-assign groups:** Select entire Confluence groups to be automatically assigned as reviewers when the approval starts.
- **Remember reviewers:** When enabled, preassigned reviewers who were unassigned during a review cycle are automatically reassigned in future rounds of the same approval. Approval parameter: `rememberassignees`. Default: `false`.

  - `true` – any subsequent reviews in the workflow that have the same name as this review will automatically have the same reviewers assigned (“sticky assignees”).
  - `false` – don’t remember assignees.
- **Reset approvals after update:** When enabled, approval decisions are reset to pending after the page is updated, while the assigned reviewers are kept. Only applies when the state has no update transition. Each reset is logged once per approval in the Document Activity Report. Off by default.

![image-20260923-113346.png](/cms_trial/assets/b852d8ce-c2c9-4cd0-8b03-92d5e40206b7.png)

1. Click **Add** in the *Add approval* dialog. The new approval has now been added to your workflow.

**Related topics**

- [E-signatures (credentials)](/cms_trial/space/CDMC/2192903044/E-signatures+(credentials)/)