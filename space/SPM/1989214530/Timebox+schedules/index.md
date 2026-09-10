# Timebox schedules

## About the timebox schedule

The timebox schedule (TS) feature helps standardize planning across teams working in recurring cycles, like sprints, program increments, or quarters. It's especially useful for organizations following Agile, SAFe, or similar frameworks, where consistent time-based structures are key. But it can also be utilized by organizations working in classic frameworks like Waterfall to visualize fiscal years or quarters on the timeline.

Instead of manually setting up [timeboxes](/cms_trial/space/SPM/1918766987/Timeboxes/) for each planning cycle, Admins can define a reusable timebox hierarchy (e.g., Year → Quarter → PI → Iteration) and apply it across multiple boxes. This reduces repetitive setup work and ensures alignment across teams.

Key capabilities:

- Define a timebox schedule with multiple levels and sequential dates.
- Apply schedules to multiple boxes.
- Ensure the same timebox structure across multiple projects, with a single place to manage those timeboxes.

## Security and access

Only a user with the App Admin security role can access the **Administration** page.

To access the timebox schedules page:

1. Open BigPicture.
2. Click the **wrench icon** at the top.
3. Select **Timebox schedules**.

![image-20250415-105440.png](/cms_trial/assets/80d58545-437a-4078-86d5-1052fe98def2.png)

## Timebox schedules overview

On the main *Timebox schedules* page, you can see a list of already created timebox schedules along with the following information:

- Name of the timebox schedule
- Boxes assigned to a timebox schedule
- Levels included
- Description

![timebox-schedule-general.png](/cms_trial/assets/73287d4e-eea1-439b-8f8f-95baf30baf02.png)

The table presents the available actions you can perform on the **Timebox schedules** page. The following actions:

- edit
- delete
- assign to boxes

can also be carried out on the TS details page (see: *Manage timebox schedule* section).

| **Action** | **Description** |
| --- | --- |
| Add new timebox schedule | To add a new timebox schedule:   1. Click **+Add new**. 2. Provide:     1. Name    2. Description (optional) 3. Define timebox levels. You can select up to four:     1. Year    2. Half Year    3. Program Increment    4. Iteration 4. Modify the start date if needed. 5. You can also choose to use existing Jira sprints to generate a timebox schedule. 6. Select global teams. 7. Click **Create** to finish the process.   Timebox schedules work only with [global teams](/cms_trial/space/SPM/1918798278/Teams+(Resource+management)/). create-new-timebox-schedule.png If no timebox schedule is listed on the *Timebox schedules* page, you can create a new TS by clicking the **Create Timebox schedule** tile on the splash screen. image-20250415-104932.png |
| Convert timeboxes into timebox schedule | You can turn your existing boxes into a reusable schedule.   1. Click **Convert timeboxes**.  convert-timeboxes-button.png  1. Set a timebox schedule name and choose a box as the origin for the schedule. convert-box-to-schedule.png The list contains only boxes that meet the following requirements:  - Only own scope boxes with sub-scope boxes are displayed on the list. If an own scope has a child of another own scope, it is not displayed. - Sub-scope boxes are sequential. Overlapping sub-boxes are not available for conversion. - There is only one box type on one level (e.g. if there is Iteration and Stage on the same level, boxes cannot be converted). - Only boxes with 1-4 levels of nesting of sub-boxes are available. If a box has more levels of sub-scope boxes, it is not available for conversion. - When you choose a box from the list, you are informed about the number of boxes available for conversion:  1. If any local team is associated with the box set for conversion, the following step is displayed: teams-to-schedule.png A local team with a unique code (no global team with the same code) can be converted to global and used in a timebox schedule. Be aware that teams converted to global are available in other boxes to be assigned to them. A local team with a code same as a global team cannot be converted. You can either convert or not all the related team - there is not option to choose just a few of them. 2. In the next step, set the box type mapping: convert-mapping.png  1. In the next step, you can see a schedule structure based on the chosen box. Click **Convert** or go back to change details: convert-boxes-list.png 2. Now, the box is being converted which is signaled by the loading icon ▢ in the box schedule list. During this time, the origin box is not deactivated in the box lists: conversion-in-progress.png 3. When the conversion is finished, the new option is available in the timebox schedule list: conversion-finished.png |
| Edit existing timebox schedule | When you click **More actions** (**…**)> **Edit**, you’ll be redirected to the details page of a selected timebox schedule. Alternatively, click the TS name to open its details page. edit-timebox-schedule.png |
| Assign timebox schedule to boxes | Click **More actions** (**…**)> **Assign to boxes** to assign a selected timebox schedule to boxes. image-20250415-115457.png |
| Delete timebox schedule | To delete a timebox schedule:  Deleting a timebox schedule deletes all timeboxes from all the assigned boxes. Tasks in scope will not be deleted, and the action can’t be reversed.   1. Click **More actions** (**…**)> **Delete**. 2. To confirm, click **Delete**.  image-20250415-115729.png |

### Global teams

The timebox schedule works only with [global teams](/cms_trial/space/SPM/1918798278/Teams+(Resource+management)/). Once connected, teams created in your box will no longer work. Only global teams (inherited from the root box) linked to the timebox schedule will be available.

![image-20250429-085357.png](/cms_trial/assets/572ba750-769a-4f95-a7b4-07e01fb6c3f7.png)

Swimlanes in the Board and Objectives modules will display global teams, allowing you to see which teams are assigned to which tasks within specific timeboxes. Tasks can be assigned to teams and timeboxes directly from the backlog or moved between teams and sprints using drag-and-drop in the Board module.

If global teams are **NOT** connected to the timebox schedule, they will **NOT** be visible in the swimlanes, even if you manually add them to a box.

![image-20250428-074726.png](/cms_trial/assets/d90658e5-ce92-4ea0-b626-1b37c660285d.png)

## Manage timebox schedules

You can open the *Timebox schedule details* page when:

- you finish creating a new timebox schedule, or
- click an existing timebox schedule on the **Administration** > **Timebox schedules** page.

![Timebox schedule details page.](/cms_trial/assets/9811c6a8-c7fd-4322-945f-3ab1974cf2e1.png)

### Edit timebox schedule details

On this page, you can edit the basic TS details you provided during the creation process:

- change the TS name
- add/ change a description
- add/remove global teams
- remove boxes associated with the selected TS

Timebox levels cannot be edited once the schedule is created.

### Edit timebox schedule structure

On the *Schedule structure* tab, you can see the timebox schedule structure that was created based on the number of levels in the timebox hierarchy you selected during the TS creation process.

You cannot change the number of those levels by deleting any level or adding extra sub-levels.

![Hierarchy cannot be edited once the timebox schedule is created.](/cms_trial/assets/e46f6d5b-7ddc-4628-aaf6-0576b9c148ed.png)

However, you can click the **pen** icon to edit the details of a timebox on each level, such as name, status, and start/end dates.

![Timebox level details.](/cms_trial/assets/1571d41b-9f8d-4d1c-8116-b55a805e3702.png)

In addition, you can add more timeboxes on each level, including the lowest (Iteration) and the highest one (Year).

When you are creating a new timebox on the TS hierarchy that consists of at least two levels, an arrow appears on the **Create timeboxes** screen. The **→** / **←** arrows let you move only only up, only down, or up only down, or up and down by one level (depending on where you clicked the **plus** icon on the hierarchy on the hierarchy). This way, you can add several timeboxes on two levels in one session.

1. Mouse over the line separating the levels until you see the **plus** (**+**) sign.
2. Click it to add another timebox.
3. On the **Create timeboxes** screen, add new timebox details. Optionally, click the **+Add more** to continue adding consecutive timeboxes on the selected level. Or move to another level to create more timeboxes (if applicable).
4. Click the **Create** button to finish the process.

If you happen to add a series of timeboxes whose dates overlap with boxes on another level, the app will prompt a warning.

![Hoe to create new timeboxes on individual levels.](/cms_trial/assets/46663da0-4dea-4988-9a12-f5b1c877fdb9.mp4)

Once you have at least two timeboxes on a sub-level, the **Delete** icon becomes active on that level.

### [Timeboxes field mapping](/cms_trial/space/SPM/1918766987/Timeboxes/)

In the *Timeboxes* [*field mapping*](/cms_trial/space/SPM/1918635376/Fields/) tab, you can map the fields for all the timeboxes in your TS structure. The process is the same as for regular timeboxes.

### Assign to boxes

You can assign a timebox schedule only to [**Own-scope**](/cms_trial/space/SPM/1918765868/Own-scope/) boxes that have no children (timeboxes) or to another Own-scope box as a child of the selected Own-scope box. You can also assign a TS to a box during box creation in the Overview module.

1. Click the **Assign to boxes button**.
2. On the **Assign timebox schedule to boxes** screen, check or uncheck the boxes you want to add the TS to.
3. Click **Save** to finish the process.

![How to assign a timebox schedule to boxes.](/cms_trial/assets/70bcca35-6536-47ba-b87b-27972ce641bb.png)

### Delete timebox schedule

The **Delete** button deletes the entire timebox schedule. Once you confirm, this action cannot be undone.

![How to delete a timebox schedule on the timebox schedule details page.](/cms_trial/assets/aa489566-2746-4096-89ca-7eb154627e43.png)

## Use timebox schedule during box creation

When [creating a new box](/cms_trial/space/SPM/1918406376/Create+box/), you can use one of the existing timebox schedules. If no timebox schedule was previously created yet, the **Use timebox schedule** toggle switch is unavailable (grayed out).

![image-20250415-124833.png](/cms_trial/assets/5471e32d-68cc-4eaf-98cc-2480759288d0.png)

## Timeboxes in modules

Boxes that are connected to a timebox schedule are marked with an icon in the **TS** column. Mouse over the icon to check the name of the timebox schedule.

![timeschedule-column.png](/cms_trial/assets/d12f6e89-bbe6-4905-a503-8924a6477583.png)

### Overview module

Timeboxes created manually can be chosen, and they display a list of lower-level timeboxes. You can choose one of the lower-level timeboxes and open it.

From this level an App Admin can also edit timebox schedule details.

### Gantt module

You can check the **Timeboxes** option to show timeboxes on the timeline.

![image-20250428-071913.png](/cms_trial/assets/0b74c069-3e87-4eb0-ab5b-0f16f2a43149.png)

### Board module

In the Board module, both manually created and created by timebox schedule boxes are displayed with their sub-boxes. From this level, you can also assign tasks to global teams.

From this level an App Admin can also edit timebox schedule details:

### Objectives module

In the Board module, boxes created manually and by timebox schedule are displayed along with their sub-boxes. From this level, you can also assign objectives to global teams. From this level an App Admin can also edit timebox schedule details.

The board displaying TS will show the swimlanes of only global teams assigned to the given timebox schedule. Local teams are not shown on such a board.

### Resources module

If you want to display timeboxes on the Resources grid, check the **Timeboxes** under the **View** dropdown. This will group tasks in a box by timeboxes. If you are currently viewing the parent-level box, like Home/root or portfolio box, switch to the **Projects** swimlane.

![timeboxes-resources.png](/cms_trial/assets/575fee72-58e7-4d02-8093-37c16810d9f8.png)

## Things to consider

- An App Admin manages everything. A user can no longer manage TS in a box.
- The timebox schedule works only with global teams.
- A user cannot open a timebox in the Overview and Gantt modules.