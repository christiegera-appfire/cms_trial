# Assign reviewers through the workflow state dialog

## Overview

The workflow state dialog lets you track the progress of the workflow applied to a page or blog post. It also enables editors and reviewers to interact with the workflow, such as by approving it or viewing its details.

The **+ Assign** button is added to the workflow state dialog if the content review is assignable.

![image-20260627-101320.png](/cms_trial/assets/ce58a1f7-34c8-4985-bade-e1d6f8e5a706.png)

- Assigned reviewers at least need **View** permission to approve or reject.
- To assign reviewers, you must have **View** and **Edit** permissions.
- Once assigned, a reviewer can assign or unassign others, even without the **Edit** permissions.

## Assign reviewers through the workflow state dialog

Assign reviewers directly from the workflow state dialog when a page enters a review state. This lets you select users responsible for approving or rejecting the content.

### Assign reviewers manually

To manually assign a reviewer through the workflow state dialog,

1. Click **+Assign** in the workflow state dialog.

   ![image-20260627-101403.png](/cms_trial/assets/039d011f-9c59-4919-a410-fb6aa9047211.png)
2. Search for the required reviewers in the search bar and click **Add**.
3. Click **Save** after adding the reviewers.

   ![image-20260627-101754.png](/cms_trial/assets/8c19d4c0-2409-4b5e-ac33-783545ea5be7.png)

   The assignee avatars are added to the dialog.

   ![image-20260627-102255.png](/cms_trial/assets/c195ddb1-afdb-4153-b915-5549e5b525b5.png)
4. Individual reviewer approval decisions are displayed in the workflow state dialog before all reviewers have recorded their decisions.

Assigning a reviewer disables the **Approve** and **Reject** buttons for all other users, including space and Confluence admins. All assigned reviewers must record their decision before a state transition occurs. You can unassign a reviewer if they haven’t recorded a decision yet.

## Pre-assign a reviewer to an assignable content review

For a content review that is assignable, you can edit the approval to pre-assign one or more users as reviewers. Pre-assigned reviewers are added to the workflow state dialog in the content review state.

![image-20260627-103049.png](/cms_trial/assets/3c94a8a2-1ee3-47e1-9245-d35006b3603e.png)

Additional users can be assigned as reviewers using the workflow state dialog.

Both pre-assigned and assigned reviewers can record their approval decisions with **View** permission or **View** and **Edit** permission for the content.

## Unassign reviewers

Administrators can't complete a content review assigned to another user; however, they can still **assign** additional reviewers and **unassign** existing ones.

To reassign or unassign reviewers,

1. Go to the search screen in the workflow state dialog.
2. Click the cross icon next to the user name to remove the reviewer. The user avatar is removed from the workflow state dialog.

![image-20260627-103347.png](/cms_trial/assets/2b1eac35-239e-437c-b7aa-3110f92faa6e.png)

If all reviewers are unassigned from the content review, the approval can be completed by any user with **view** or **edit** permissions for the page or blog.

### **Related topics**

- [Approvals](/cms_trial/space/CDMC/2193195490/Approvals/)
- [Workflow state dialog](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/)