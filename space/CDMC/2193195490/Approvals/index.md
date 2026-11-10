# Approvals

## Overview

Approvals are added to a state in a workflow using the *Approval Editor* in the *Workflow Builder Visual Editor*. One or more approvals (content review) can be added to each workflow state in a custom workflow.

## Configure an approval

To add an approval for a custom workflow:

1. Log in to your Confluence space
2. Choose **Comala document management** under *Space* *Apps*.
3. A list of existing workflows is displayed. Click **Create New Workflow** or click the **Edit** icon to edit an existing workflow.

   ![Workflow management page showing the list of existing workflows and the option to create or edit a workflow.](/cms_trial/assets/1a775334-0121-4adc-821b-e187fb969113.png)
4. In the visual builder editor of an existing custom workflow, clickany **State** > **Approval** under *States.*
5. To add a new approval, click + **Add Approval**.

   ![Workflow state configuration showing the Add Approval option for a selected workflow state.](/cms_trial/assets/238d319b-f133-4e96-ac71-3ed752925a66.png)

The **Add approval** dialog opens. The dialog is organized into four sections:

- [General Settings](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/1685946594/Approvals#General-Settings)
- [Outcome criteria](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/1685946594/Approvals#Outcome-Criteria)
- [Reviewers](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/1685946594/Approvals#Reviewers)
- [Assigners](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/1685946594/Approvals#Assigners)

![image-20261106-125747.png](/cms_trial/assets/3b2ae0a6-3830-4994-9e1c-b0dab390dd52.png)

### **1. General Settings**

- **Approval Name:** Enter a unique, descriptive name for the approval (for example, `Legal Review`). The name must be unique within the workflow and must follow the supported naming rules. Special characters such as **? ! @ #** are not allowed.
- **Custom Action Labels:** Rename the default **Approve** and **Reject** buttons to fit your team’s vocabulary (for example, **Sign Off** or **Needs Changes**).
- **Authentication Method:** Optionally require reviewers to authenticate their decision, including via OTP. The default is *Not required*. See [E-signatures (credentials)](/cms_trial/space/CDMC/2192903044/E-signatures+(credentials)/) for details on setting up e-signature authentication.
- **Require a comment:** Require reviewers to add a comment when they approve or reject. When **Require a comment** is enabled, a reviewer cannot submit an approval or rejection without entering a comment explaining their decision. This is useful for audit trails and reviews that need a documented rationale, such as legal or compliance sign-off. This setting is off by default.

![General Settings section showing approval name, custom action labels, authentication method, and comment settings.](/cms_trial/assets/3313e550-c272-46b9-bf99-eaf89d072c66.png)

### **2. Outcome Criteria**

Define how many reviewers must participate and how the final decision is determined.

- **Required participation:** Choose how many assigned reviewers must decide before the approval can be finalized.

  - **All or default**: If reviewers are assigned, all of them must record a decision. If no reviewers are assigned, at least one reviewer must participate. For example, if 3 reviewers are assigned to an approval, all 3 must record a decision before the outcome is finalized. If no reviewers are assigned, at least 1 reviewer must participate.
  - **Minimum participants**: Set a **Minimum participation** number to specify how many reviewers must participate before a decision is finalized. This is useful when you have a large pool of reviewers but only need a subset to weigh in. For example, if 10 reviewers are assigned and the minimum participation is set to 3, the outcome is finalized once any 3 reviewers have recorded their decisions. The remaining reviewers don’t need to participate.

    ![Required participation settings showing the Minimum participants option and participation threshold field.](/cms_trial/assets/3b89edce-7893-4fd0-abe8-0499070ed414.png)
- **Decision type:** Choose how reviewer decisions are evaluated to determine the approval outcome.

  - **Unanimity**: All participating reviewers must agree (all approve or all reject) for the decision to pass.
  - **Majority**: The decision follows the majority vote among actively participating reviewers, not the total number assigned. For example, if 5 reviewers are assigned and 3 participate, the outcome is based on the 3 active participants. If 2 approve and 1 rejects, the content is approved.
  - **Minimum approvals/rejections**: Set explicit **Minimum approvals** and **Minimum rejections** thresholds for each outcome. The approval is finalized when either threshold is met.   
    When both thresholds are configured, evaluate them independently. The first threshold reached determines the outcome.

    If both thresholds are met at the same time:

    - The majority decision takes effect when one outcome has more votes than the other.
    - If votes are evenly split, the outcome defaults to rejection.

For example, if 4 participants are required, with a minimum of 3 approvals or 1 rejection, and the first 3 reviewers approve while the last rejects, the content is still approved.

![Approval outcome settings showing minimum approval and rejection thresholds used to determine the final decision.](/cms_trial/assets/7885d1ef-8bf2-496f-a22f-6e58a6d310fb.png)

### **3. Reviewers**

Control who can participate in the approval, how reviewers are assigned, and whether assignments persist across review cycles.

- **Allowed reviewers:** Choose who can approve or reject a page. The following options are available:

  - **Only assigned reviewers:** Only explicitly assigned reviewers, including pre-assigned and manually assigned reviewers, can approve or reject.
  - **Assigned reviewers and editors:** Assigned reviewers and users with permission to edit the page can approve or reject.
  - **Anyone:** Any user with permission to view the page can approve or reject.

    ![image-20261106-130112.png](/cms_trial/assets/cd153af5-2da6-4259-a6dd-16e476bfc221.png)

- **Manually assign reviewers:** Allow reviewers to be added or removed through the [workflow state dialog](/cms_trial/space/CDMC/2192968161/Assign+reviewers+through+the+workflow+state+dialog/) while an approval is active.
- **Allow self-assignment:** Allow users to assign or unassign themselves as reviewers through the workflow state dialog. When disabled, users cannot assign or unassign themselves, but they can manage other reviewer assignments if they have the required permissions. This setting applies only when **Manually assign reviewers** is enabled. It is enabled by default.
- **Remember reviewers:** When enabled, manually assigned reviewers are remembered for each workflow state and approval name and automatically reassigned the next time the page enters the same approval. Approval parameter: `rememberAssignees`. Default: `false`.

  - `true` – Manually assigned reviewers are remembered and automatically reassigned in subsequent rounds of the same approval.
  - `false` – Manually assigned reviewers are not remembered for subsequent approval rounds.

  If a remembered reviewer is manually unassigned, they are removed from the remembered list and are not automatically reassigned.

Remembered reviewers are restored only if they are not listed under **Excluded reviewers** and, when an **Eligible reviewers** list is configured, are included in that list.

- **Reset approvals after update:** When enabled, approval decisions are reset to pending after the page is updated, while the assigned reviewers are kept. Only applies when the state has no update transition. Each reset is logged once per approval in the Document Activity Report. Off by default.
- **Pre-assigned reviewers:** Select users, Confluence groups, and Confluence teams to be assigned when the workflow enters the state. Members of selected groups and teams are assigned for that round. This section remains editable in the workflow builder and is applied at runtime even when **Manually assign reviewers** is disabled. If none are selected, no reviewers are pre-assigned.

  - **Pre-assigned users:** Select individual users to be automatically assigned as reviewers when the workflow enters the approval state.
  - **Pre-assigned groups:** Select Confluence groups whose members should be assigned as reviewers when the workflow enters the approval state.
  - **Pre-assigned teams:** Select Confluence teams whose members are automatically assigned as reviewers when the workflow enters the approval state.

    ![image-20261106-130311.png](/cms_trial/assets/f7c0c33f-44e5-4ecf-9198-7d9f1fd722d9.png)
- **Eligible reviewers:** Specify who can be assigned as a reviewer and who can approve or reject a page. You can add users, Confluence groups, and Confluence teams. Members of a listed group or team are eligible unless an exclusion applies.

  When configured, this list applies to manually assigned, pre-assigned, and remembered reviewers, regardless of whether **Manually assign reviewers** is enabled. Reviewers who do not meet the eligibility requirements cannot approve or reject and are removed from reviewer assignments.

  If you leave this section empty or omit it, no additional eligibility restrictions apply.

- - **Eligible users:** Select users who may be assigned as reviewers and participate in approve/reject.
  - **Eligible groups:** Select groups whose members may be assigned as reviewers and participate in approve/reject.
  - **Eligible teams:** Select teams whose members may be assigned as reviewers and participate in approve/reject.

    ![image-20261106-131017.png](/cms_trial/assets/3cce48e1-526f-4047-b2bc-8d73bbc3a075.png)
- **Excluded reviewers:** Specify who cannot be assigned as a reviewer or approve or reject a page. You can exclude users, Confluence groups, and Confluence teams. Exclusions always take precedence over other reviewer settings, regardless of whether **Manually assign reviewers** is enabled. Excluded users cannot approve or reject and are removed from manually assigned, pre-assigned, or remembered reviewer assignments.

  If no users, groups, or teams are selected, no reviewers are excluded.

  - **Excluded users:** Select users who must not be assigned as reviewers or participate in approve/reject.
  - **Excluded groups:** Select Confluence groups whose members cannot be assigned as reviewers or approve or reject.
  - **Excluded teams:** Select Confluence teams whose members cannot be assigned as reviewers or approve or reject.

    ![image-20261106-131117.png](/cms_trial/assets/e239b0f8-3525-4cd8-9fd7-557077456e7e.png)

**Reviewer restrictions:**

- The **Allowed reviewers** setting determines who can approve or reject a page, subject to the **Eligible reviewers** and **Excluded reviewers** restrictions.
- **Excluded reviewers** always take precedence over other reviewer settings.
- When configured, the **Eligible reviewers** list determines who can approve or reject a page, including pre-assigned, remembered, and manually assigned reviewers.
- These restrictions apply regardless of whether **Manually assign reviewers** is enabled.
- Reviewers who do not meet the eligibility or exclusion rules are removed from reviewer assignments. No replacement reviewer is automatically assigned.

![image-20261106-131556.png](/cms_trial/assets/61d527f5-15cd-49cd-a7bb-bc32e06a54ad.png)

- When you add a reviewer who is excluded or not included in a configured **Eligible reviewers** list, the workflow state dialog marks that reviewer as ineligible for assignment. You cannot save the changes until you remove the ineligible reviewer. These eligibility and exclusion rules also apply when you approve or reject a page. Users who do not meet these requirements cannot approve or reject.
- If a configured user, Confluence group, or Confluence team **isn't found, the operation fails,** and an error message is displayed.

### 4. Assigners

Control who can assign or unassign reviewers in the workflow state dialog. This section applies only when **Manually assign reviewers** is enabled.

When **Manually assign reviewers** is disabled, the **Eligible assigners** and **Excluded assigners** sections remain visible but cannot be edited. A tooltip explains why these settings are unavailable. Any previously configured values are cleared when you save the workflow.

- **Eligible assigners:** Select users, groups, and teams who may manage reviewer assignments. If no users, groups, or teams are selected, any page editor may assign or unassign reviewers, subject to the assignment rules.

  - **Eligible users:** Select users who may manage reviewer assignments.
  - **Eligible groups:** Select groups whose members may manage reviewer assignments.
  - **Eligible teams:** Select teams whose members may manage reviewer assignments.

**Assignment permissions:** When assigning or unassigning reviewers, the following rules apply in order:

1. **Allow self-assignment:** When disabled, users cannot assign or unassign themselves.
2. **Excluded assigners:** Excluded users and members of excluded groups or teams cannot assign or unassign reviewers
3. **Eligible assigners:** When configured, only eligible users and members of eligible groups or teams can assign or unassign reviewers. If no users, groups, or teams are selected, no additional restrictions apply.
4. **Page permissions:** Users must have permission to edit the page, and **Manually assign reviewers** must be enabled.

- **Excluded assigners:** Select users, groups, and teams whose members cannot assign or unassign reviewers.

  - **Excluded users:** Select users who cannot manage reviewer assignments.
  - **Excluded groups:** Select groups whose members cannot assign or unassign reviewers.
  - **Excluded teams:** Select teams whose members cannot assign or unassign reviewers.

If no users, groups, or teams are selected, no assigners are excluded.

![image-20261106-074247.png](/cms_trial/assets/4d9a06e2-ec11-4d03-b80f-524f0d16012f.png)

If you do not have permission to assign or unassign reviewers, the **Assign** button remains visible but is disabled in the workflow state dialog.

Now click **Add** in the *Add approval* dialog. The new approval has now been added to your workflow.

![image-20261106-131929.png](/cms_trial/assets/bd8c8ce5-5fb6-4cc3-b2cb-493f40aab47d.png)

**Related topics**

- [E-signatures (credentials)](/cms_trial/space/CDMC/2192903044/E-signatures+(credentials)/)