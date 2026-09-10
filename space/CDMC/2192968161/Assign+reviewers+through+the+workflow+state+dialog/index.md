# Assign reviewers through the workflow state dialog

## Overview

The workflow state dialog lets you track the progress of the workflow applied to a page or blog post. It also enables editors and reviewers to interact with the workflow, such as by approving it or viewing its details.

The **+ Assign** button is added to the workflow state dialog if the content review is assignable.

![image-20260627-101320.png](/cms_trial/assets/daac61f3-dd45-4544-ab7b-04f8d675aa74.png)

- Assigned reviewers at least need **View** permission to approve or reject.
- To assign reviewers, you must have **View** and **Edit** permissions.
- Once assigned, a reviewer can assign or unassign others, even without the **Edit** permissions.

## Assign reviewers through the workflow state dialog

Assign reviewers directly from the workflow state dialog when a page enters a review state. This lets you select users responsible for approving or rejecting the content.

### Assign reviewers manually

To manually assign a reviewer through the workflow state dialog,

1. Click **+Assign** in the workflow state dialog.

   ![image-20260627-101403.png](/cms_trial/assets/2a311880-4819-49c1-b1cb-d39c665c663c.png)
2. Search for the required reviewers in the search bar and click **Add**.
3. Click **Save** after adding the reviewers.

   ![image-20260627-101754.png](/cms_trial/assets/d9f5233b-6251-416d-af61-57727dfc2b2c.png)

   The assignee avatars are added to the dialog.

   ![image-20260627-102255.png](/cms_trial/assets/15f17ccd-cd95-475e-b96c-52c368e8bafc.png)
4. An assigned reviewer sees an on-screen message notification when visiting the page.
5. Individual reviewer approval decisions are displayed in the workflow state dialog before all reviewers have recorded their decisions.

- Assigning a reviewer disables the **Approve** and **Reject** buttons for all other users, including space and Confluence admins. All assigned reviewers must record their decision before a state transition occurs. An assigned reviewer can be unassigned if they haven’t yet recorded a decision.

## Pre-assign a reviewer to an assignable content review

For a content review that is assignable, you can edit the approval to pre-assign one or more users as reviewers. Pre-assigned reviewers are added to the workflow state dialog in the content review state.

![image-20260627-103049.png](/cms_trial/assets/b5120509-4c37-4d67-ae71-05c294f91d13.png)

Additional users can be assigned as reviewers using the workflow state dialog.

Both pre-assigned and assigned reviewers can record their approval decisions with **View** permission or **View** and **Edit** permission for the content.

## Unassign reviewers

Administrators can't complete a content review assigned to another user; however, they can still **assign** additional reviewers and **unassign** existing ones.

To reassign or unassign reviewers,

1. Go to the search screen in the workflow state dialog.
2. Click the cross icon next to the user name to remove the reviewer. The user avatar is removed from the workflow state dialog.

![image-20260627-103347.png](/cms_trial/assets/1387240b-6268-4e27-9c41-56584cf15d17.png)

If all reviewers are unassigned from the content review, the approval can be completed by any user with **view** or **edit** permissions for the page or blog.

### **Related topics**

- [Approvals](/cms_trial/space/CDMC/2193195490/Approvals/)
- [Workflow state dialog](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/)