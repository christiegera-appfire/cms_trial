# Quality management system workflow

## Overview

The **Quality Management System (QMS) Workflow** is a four-state, compliance-review-focused workflow. Reviewers are managed in the app space settings and automatically assigned to each approval.

![Comala QMS workflow state diagram](/cms_trial/assets/dfa7a657-df6e-41d2-a77c-69b6daaa3fbd.png)

## Workflow states

This workflow is ideal for teams that need to demonstrate compliance with guidelines, rules, or standards, including ISO standards, FDA regulations, or internal corporate standards.

### Draft

- If no reviewers are assigned to a page, any user can approve or reject the content. In this case, only one approval decision is required to advance the workflow from the Draft state.
- If a user has assigned reviewers, only those users can approve or reject.
- All reviewers must authenticate their identity using an [e-signature](/cms_trial/space/CDMC/2192903044/E-signatures+(credentials)/) before approving or rejecting content.

![Draft workflow state showing the approval controls and reviewer actions.](/cms_trial/assets/a9ac0e19-be3c-4a7a-809d-945a890cb6dd.png)

All reviewers must have **edit** permissions on the Confluence page.

### In Approval

- If all reviewers approve in the Draft state, the content transitions to the **In Approval** state.
- Space admins set the reviewers required to approve content in this state by configuring [workflow parameters](/cms_trial/space/CDMC/2192837939/Parameters/) in the space document management dashboard. These reviewers can also be [assigned through the workflow state dialog](/cms_trial/space/CDMC/2192968161/Assign+reviewers+through+the+workflow+state+dialog/).
- Assigned reviewers are notified by email when the state changes to **In Approval**. See [Notifications](/cms_trial/space/CDMC/2193001238/Notifications/) for more details on how custom email notifications work.

These custom email notifications are created by a [JSON trigger in the workflow](/cms_trial/space/CDMC/2192837873/JSON+code+editor/).

### Published

- When a page transitions to this state, it becomes the final approved version.
- The workflow automatically moves the page back to the **Draft** state when it is edited.

### Obsolete

- The page’s content is considered **Obsolete**.
- Any update transitions it back to the **Draft** state.

Adding or removing a label or attachment does not activate the **updated** transition when the content is in the *In Approval*, *Obsolete*, or *Published* state. This transition occurs only when the content is edited and published (by changing the Confluence page version).

**Related topics**

- [E-signatures](/cms_trial/space/CDMC/2192903044/E-signatures+(credentials)/)
- [Assign reviewers](/cms_trial/space/CDMC/2192968161/Assign+reviewers+through+the+workflow+state+dialog/)
- [Notifications](/cms_trial/space/CDMC/2193001238/Notifications/)