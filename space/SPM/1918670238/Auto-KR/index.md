# Auto-KR

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

## Auto-KR (old navigation)

Click to expand the guide

## Overview

In the auto-KR mode, the progress of the Key Result is calculated based on the [linked work items](/cms_trial/space/SPM/1918507296/Link+work+items+to+Key+Results/) and/or the work items that belong to the scope of the [linked boxes](/cms_trial/space/SPM/2229665803/Link+boxes+to+Key+Results/). As your teams work toward their OKRs and update the status of the associated work items, the KR's progress automatically updates.

Visit the [OKR linked work items data sync](/cms_trial/space/SPM/2173109245/OKR+linked+work+items+data+sync+(and+auto-progress+update)/) page for more details on task data sync between the OKR module and other modules, and how it affects progress auto-update.

- When you mark a work item as **Done** in the Scope, Gantt, Board, Resources, or Calendar modules, the linked work item in the OKR module automatically reflects this progress.
- If you move a work item back to **To Do**, the OKR progress will decrease.
- Work items marked **In Progress** don't affect OKR progress, but their status will still be updated in the OKR module.

KRs in the auto mode require minimal user intervention to maintain accurate tracking. Auto KRs work particularly well for Jira tasks like bugs, new features, and test cases.

Note the “sync” icon for the auto-KR:

![Auto-KR.](/cms_trial/assets/f04bbbe7-a444-424b-9aec-4fc26cff69f6.png)

## Set the auto-KR mode

If you want your KR to be tracked automatically:

1. Select the **Linked items** under the **Progress** on the KR creation screen.

   ![Screenshot of setting the auto-KR mode.](/cms_trial/assets/ba82cb55-95a1-4242-b4a3-db0c3a6675b9.png)

1. You [can link work items](/cms_trial/space/SPM/1918507296/Link+work+items+to+Key+Results/) or [link boxes](/cms_trial/space/SPM/2229665803/Link+boxes+to+Key+Results/) when [creating a KR](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918538655) or later.

Note that it is possible to link work items and boxes to a manual KR. But unless you select the **Linked items** option during the KR creation, or [convert it to an auto-KR](/cms_trial/space/SPM/2223538218/Convert+OKR/), the linked items will not affect the KR’s progress.

## Update auto-KR progress

If you go to the [auto-KR update screen](/cms_trial/space/SPM/1918637972/Update+OKR/), you will notice that the **Last value** field is grayed out. That’s because the progress of the auto-KR is updated automatically, so you do not need to update it.

The auto-KR mode does not impact the [OKR status](/cms_trial/space/SPM/1918702011/OKR+status+and+progress/), meaning you must update it manually.

![Progress fields on the auto-kr update modal.](/cms_trial/assets/de9f3103-a542-4c6b-994f-849aba6522d6.png)

### KR auto update based on linked work items: Example

Say you have linked five Jira work items to an auto-KR. Three items are **In Progress**, and the other three are still in **To Do**. In such a case, the progress of the auto-KR is 0%.

![An auto-KR with five issues linked to it. KR has not progressed.](/cms_trial/assets/b17dce4a-2a3b-4f43-8796-bdc1dbe8d6c9.png)

At some point, as your team works on their tasks, two team members mark the task as **Done** in the Gantt module.

Both of these tasks are associated with the same Key Result, meaning that they will affect the KR’s progress.

`auto-KR progress = (linked work items in Done status / total number of linked work items) x 100%`

In our example:

`KR-18 progress = (2/5) x 100% = 0.4 x 100% = 40%`

The progress of the auto-KR based on the linked work items is now 40%.

![An auto-KR with five issues linked to it. KR has progressed.](/cms_trial/assets/95c07340-706e-4bc0-aa63-cec12345bdc2.png)

### KR auto update based on linked boxes: Example

Similar to the previous example, the progress of the auto-KR also depends on the linked work items. The only difference is that those items are in a box.

Let’s assume you linked an Iteration box with twelve tasks. The KR's progress is 0%.

![An iteration box linked to an auto-KR. The box has not progressed.](/cms_trial/assets/e2699681-0a27-452f-8d1f-ae9f82f5c911.png)

When you inspect the box in the Scope module, you can see that all tasks are in **To Do**.

![Iteration box in the scope module. All tasks are in to do.](/cms_trial/assets/d28a84a4-919c-4e2a-a728-34b239d0825c.png)

A few of your team members marked seven of the tasks in the Iteration box as **Done**.

![iteration box in the scope module. Seven tasks are marked as done, two are in progress, three are in to do.](/cms_trial/assets/96b9cf95-981e-4fcd-b60a-b4980f7ce19b.png)

`KR-14 progress = (7/12) x 100% ≈0.5833 x 100% ≈ 58.33% ≈ 58%`

The progress of the auto-KR based on the linked box is now 58%.

![An iteration box linked to an auto-KR. The box has progressed.](/cms_trial/assets/861732ea-1329-42ad-97e7-ffc8e6fbd11b.png)

## Auto-KR (new navigation)

Click to expand the guide

## Overview

In the auto-KR mode, the progress of the Key Result is calculated based on the [linked work items](/cms_trial/space/SPM/1918507296/Link+work+items+to+Key+Results/) and/or the work items that belong to the scope of the [linked boxes](/cms_trial/space/SPM/2229665803/Link+boxes+to+Key+Results/). As your teams work toward their OKRs and update the status of the associated work items, the KR's progress automatically updates.

Visit the [OKR linked work items data sync](/cms_trial/space/SPM/2173109245/OKR+linked+work+items+data+sync+(and+auto-progress+update)/) page for more details on task data sync between the OKR module and other modules, and how it affects progress auto-update.

- When you mark a work item as **Done** in the Scope, Gantt, Board, Resources, or Calendar modules, the linked work item in the OKR module automatically reflects this progress.
- If you move a work item back to **To Do**, OKR progress decreases.
- Work items marked **In Progress** don't affect OKR progress, but their status still updates in the OKR module.

KRs in auto mode require minimal user intervention to keep tracking accurate. Auto KRs work particularly well for Jira tasks like bugs, new features, and test cases.

Note the **KR icon** difference between an auto and manual KR.

| Auto KR icon. | Manual KR icon. |
| --- | --- |

## Set the auto-KR mode

If you want your KR to be tracked automatically:

1. Select the **Linked items** under **Progress** on the KR creation screen.

   ![Screenshot of setting the auto-KR mode.](/cms_trial/assets/ba82cb55-95a1-4242-b4a3-db0c3a6675b9.png)

1. You [can link work items](/cms_trial/space/SPM/1918507296/Link+work+items+to+Key+Results/) or [link boxes](/cms_trial/space/SPM/2229665803/Link+boxes+to+Key+Results/) when [creating a KR](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918538655) or later.

You can link work items and boxes to a manual KR. But unless you select the **Linked items** option during the KR creation, or [convert it to an auto-KR](/cms_trial/space/SPM/2223538218/Convert+OKR/), the linked items will not affect the KR’s progress.

## Update auto-KR progress

If you go to the [auto-KR update screen](/cms_trial/space/SPM/1918637972/Update+OKR/), you will notice that the **Last value** field is grayed out. That’s because the auto-KR progress updates automatically, so you don't need to update it.

Auto-KR mode does not affect [OKR status](/cms_trial/space/SPM/1918702011/OKR+status+and+progress/), so you must update it manually.

![Progress fields on the auto-kr update modal.](/cms_trial/assets/de9f3103-a542-4c6b-994f-849aba6522d6.png)

### KR auto-update based on linked work items: Example

Say you have linked five Jira work items to an auto-KR. Three items are **In Progress**, and the other three are still in **To Do**. In that case, the auto-KR progress is 0%.

![An auto-KR with five issues linked to it. KR has not progressed.](/cms_trial/assets/b17dce4a-2a3b-4f43-8796-bdc1dbe8d6c9.png)

At some point, as your team works on their tasks, two team members mark the task as **Done** in the Gantt module.

Both tasks are associated with the same Key Result, so they affect the KR’s progress.

`auto-KR progress = (linked work items in Done status / total number of linked work items) x 100%`

In our example:

`KR-18 progress = (2/5) x 100% = 0.4 x 100% = 40%`

The auto-KR progress based on the linked work items is now 40%.

![An auto-KR with five issues linked to it. KR has progressed.](/cms_trial/assets/95c07340-706e-4bc0-aa63-cec12345bdc2.png)

### KR auto-update based on linked boxes: Example

As to the previous example, the auto-KR progress also depends on the linked work items. The only difference is that those items are in a box.

Let’s assume you linked an Iteration box with twelve tasks. The KR's progress is 0%.

![An iteration box linked to an auto-KR. The box has not progressed.](/cms_trial/assets/e2699681-0a27-452f-8d1f-ae9f82f5c911.png)

When you inspect the box in the Scope module, you can see that all tasks are in **To Do**.

![Screenshot of the Scope module with the tasks in the To Do status.](/cms_trial/assets/4001f13a-be00-4b09-8f62-166cb5dbf15a.png)

A few of your team members marked seven of the tasks in the Iteration box as **Done**.

![image-20260415-120101.png](/cms_trial/assets/6bf1ca55-ef83-46e4-aefc-b62ba0d7647d.png)

`KR-14 progress = (7/12) x 100% ≈0.5833 x 100% ≈ 58.33% ≈ 58%`

The progress of the auto-KR based on the linked box is now 58%.

![An iteration box linked to an auto-KR. The box has progressed.](/cms_trial/assets/861732ea-1329-42ad-97e7-ffc8e6fbd11b.png)