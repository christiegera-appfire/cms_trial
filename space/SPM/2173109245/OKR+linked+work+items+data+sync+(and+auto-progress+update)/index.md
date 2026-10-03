# OKR linked work items data sync (and auto-progress update)

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

Auto-KRs rely on linked work items to keep their progress up to date. This means that any changes made to those work items in other modules need to be synchronized with the OKR module.

## Task data sync with the OKR module

To see linked work items under their respective KRs, make sure:

- The **Displaying connected work items in the OKR Overview** option is enabled in **Settings** > **General**.
- The **Connected Jira work items** option is checked under **Overview** > **View**.

When you mark a work item as **Done** in the Scope, Gantt, Board, Resources, or Calendar modules, the linked work item in the OKR module automatically reflects this progress.

If you move a work item back to **To Do**, OKR progress decreases. Work items marked **In Progress** don't affect OKR progress, but their status will still be updated in the OKR module.

Consequently, when the task is marked as **Done**, the progress of the Key Result and parent Objective increases proportionally as per their contribution toward a Key Result and Objective, respectively.

Linked work item status and progress usually update immediately when you switch back to the OKR module. However, in some cases, it can take up to 20 minutes.

The following video provides an overview of the task data sync between the Gantt and OKR modules.