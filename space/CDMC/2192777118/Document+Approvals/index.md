# Document Approvals

## Overview

In **Comala Document Management**, one or more **Document approvals** macros can be added to a page to display workflow approval information. Each macro can be configured to display the approval information for a different state in the workflow.

The document approvals macro information for a workflow state is shown as a table, with one header row per approval and one row per reviewer of each approval.

![image-20260629-070930.png](/cms_trial/assets/783e6ec8-d808-4c45-b714-0fe1d25a3825.png)

The macro can be configured to display

- the approval(s) in a state
- The overall status of the **approval**
- The assignees for each approval
- Details of the assignee decision

Several separate **document approval** macros can be added to the content to display information for different approvals in different states.  If the named approval doesn’t exist (misspelled, renamed, or removed), the macro will ignore that approval.

When no workflow is applied to the page, the document approvals report macro displays the following message both when the page is being edited and on the published page.

![image-20260629-080037.png](/cms_trial/assets/7b4f624d-216e-483b-9c61-8d4aad5077b4.png)

## Add the macro to a page

To add the document approvals macro,

1. Edit the page and type /document approvals.
2. Choose **Document Approvals** to add the macro to the draft page.  
   By default, the macro displays the current workflow state name and the approvals in the state.

![image-20260629-063501.png](/cms_trial/assets/400e3bdc-b1e2-4633-a70c-b7fb8fd8c6b5.png)

1. Select the macro and click the edit icon to open the macro editor.

![image-20260629-071326.png](/cms_trial/assets/a32f1c02-f3fb-4b84-9252-fa80504622ce.png)

1. The **State** dialog box is empty by default, and the macro will display the approval information for the current workflow state.   
   With no checkboxes selected, the macro lists only the approval names for the state.

![image-20260629-071709.png](/cms_trial/assets/314ef682-2a15-4369-8f8a-2b5e333fdf42.png)

1. Select the **Show status** checkbox in the macro editor to display the overall approval status.

![image-20260629-071822.png](/cms_trial/assets/285f4cbc-4231-4e33-b35b-45d39982248a.png)

1. If a reviewer has been assigned, their information will be displayed in a separate row.  
   A separate column is added for each selected checkbox in the macro editor to display information for each approval.

![image-20260629-071953.png](/cms_trial/assets/32f77026-b0bc-42c6-968e-7f20235445a3.png)

When the approval is configured to require a minimum number of reviewers, a separate unassigned reviewer row is displayed for each required reviewer. These are populated when reviewers are assigned or when a review decision is recorded.

## Transition the content

The information displayed by the macro is dynamic.

### No state specified

If a state is not specified in the macro editor, transitioning the workflow to a different state will display the approval information for the new current state.

![image-20260629-174806.png](/cms_trial/assets/0bd1ed7f-a3bd-4836-8e33-a09d63fd6fac.png)

### No approval in state

If there is no approval in the current state, the document approvals macro will display the following message for the state.

![image-20260629-174225.png](/cms_trial/assets/9280f427-b6b5-4166-a198-78a692e7baad.png)

### State specified

Setting a state in the document approvals macro editor displays the approval information for that state, regardless of the current state.

![image-20260629-080541.png](/cms_trial/assets/0597e415-28eb-455e-b591-ec5434992897.png)

## Configure the macro

The macro can be configured to display approval information on the page.

### Display approvals in a named state

Approval information can be displayed for a single named state added to the macro editor.

![image-20260629-080640.png](/cms_trial/assets/590ebbcb-aa98-40d7-b741-d1b18ee3e526.png)

The macro will display the current approval information for this state, regardless of the content's current workflow state.

![image-20260629-082847.png](/cms_trial/assets/86a561c5-38ff-4a68-b6f0-e91b367dbc53.png)

Check the macro editor checkboxes to display one or more of the following

- The overall status for each approval in the state (***Pending****,* ***Rejected****,* ***Approved,*** *or* ***Approved and Signed***)- **Show status**
- The reviewers for each approval; check one or both

  - **Show reviewer avatar**
  - **Show reviewer name**
- The current status of each reviewer’s decision for the approval (*Pending, Rejected, Approved, Approved and Signed, Unassigned*) - **Show status**
- The date of each reviewer’s last action (if any) - **Show date**
- The page version at the time of each reviewer’s decision - **Show version**
- Any comments added by the reviewer on the last recorded action

If the **Show status** is checked, both the status of the overall approval and (if the reviewer avatar or the reviewer name is checked) the current decision for each reviewer are displayed.

### Display approvals, reviewers, and status information for the current workflow state

Leave the **State** dialog box empty to display approval information for the current workflow state.

![image-20260629-063324.png](/cms_trial/assets/61ac229e-0a2c-420d-a60b-f4da9d8c1fa0.png)

The approvals for the current workflow state are displayed.

![image-20260629-083456.png](/cms_trial/assets/e3d2289c-af23-424d-a7ff-c01d91bbe096.png)

If a workflow transition occurs, the approvals macro displays approval information for the new workflow state.

### Multiple approvals in a state

If there is more than one approval in a state, each approval is listed in a separate row.

![Comala Document Approvals macro displaying multiple approvals on a page](/cms_trial/assets/67934612-109f-4057-a787-c805fe69ebbd.png)

Approval information is displayed for multiple approvals in a state, in alphabetical order by approval names.

Each reviewer for an approval is displayed in a separate row.

To limit or set an order for the display of selected approvals in a state, add the name of each approval as a comma-separated list (with no spaces) in the **Approvals order** dialog box.

Approvals are displayed in the order that they are added in the comma-separated list.

![Comala Document Approvals macro with two approvals in review state](/cms_trial/assets/8a1251a6-8f37-4853-97b6-13dba7b6ce14.png)

## Use with other macros

The document approvals macro is compatible with the Confluence Page Properties macro and the Page Properties Report macro.

On the draft page, add one or more **document approvals** macros as table values in the **page properties** macro.

![Comala Document Approvals macro page properties view](/cms_trial/assets/5264fdc2-f09d-4ae9-bb67-f97e44d15f67.png)

The page properties report macro can then be added to a page to report on the added values.

![Comala Document Approvals macro page properties rendered on a page](/cms_trial/assets/c065b3fc-6228-4658-b7d3-af55c71f92d6.png)

## Exporting pages to PDF and Word

The approvals macro table of information is included when exporting to PDF or Word.

![Comala Document Approvals macro PDF export preview](/cms_trial/assets/2e3877a3-5591-48c2-a533-4b530edbf69c.png)

- The date (if included in the macro configuration) is in UTC format in the PDF and Word exports.
- Reviewer avatars are not included in the PDF or Word export.

**Related topics**

- [Approvals](/cms_trial/space/CDMC/2193195490/Approvals/)
- [Workflow state dialog](/cms_trial/space/CDMC/2193129918/Workflow+state+dialog/)