# Task dates

## Task dates (old navigation)

Click to expand the guide

## Introduction

To start working in BigPicture, you need to create a box and add tasks to this box.

It is not required for tasks to have the start and end dates defined:

- Tasks have dates if the **Start Date** and **End Date** fields are set in Jira and the field mapping is configured. For more information, refer to the [Start/end date fields](/cms_trial/space/SPM/1918834667/Start%2Fend+date+of+newly+created+tasks/) article.
- Tasks without dates (the **Start Date** and **End Date** fields are not set in Jira) can also be added to a box in BigPicture (from the 8.19 version of BigPicture).

## Add dates to tasks without dates in BigPicture

There are multiple ways to add dates to tasks without dates. You can add both dates (start date and end date) or only one. A task with one date is semi-transparent, as presented below:

- No start date:

  ![Screenshot of a task with no start date.](/cms_trial/assets/24c9fffa-ae14-404c-90d3-48406d452cff.png)
- No end date:

  ![Screenshot of a task with no end date.](/cms_trial/assets/964e4776-856d-407e-ad41-fafab2d739fc.png)

### Gantt module

To add dates to a task in the [Gantt module](/cms_trial/space/SPM/1918797129/Gantt+module/):

1. Hover the mouse cursor over a task on the timeline.
2. Click the **+** icon.

   ![Screenshot of the Gantt timeline with a task without dates.](/cms_trial/assets/39d5059c-ec42-4e53-9b88-0c0facac8917.png)
3. Edit the **Start Date** and **End Date** fields (make sure that these columns are added to the current [column view](/cms_trial/space/SPM/1918404907/Column+views/)).

   ![Screenshot of the Gantt timeline when adding dates to a task.](/cms_trial/assets/22742176-04bf-4958-867b-af5aa083e59f.png)

### Scope module

To add dates to a task in the [Scope module](/cms_trial/space/SPM/1918666763/Scope+module/):

1. Find a task.
2. Edit the **Start Date** and **End Date** fields (make sure that these columns are added to the current [column view](/cms_trial/space/SPM/1918404907/Column+views/)).

![Screenshot of Scope module when adding dates to a task.](/cms_trial/assets/56a4887e-b26f-461b-a446-631b1a786e23.png)

### Board module

To add dates to a task in the [Board module](/cms_trial/space/SPM/1918796888/Board+module/):

1. Right-click on a task and select **Edit**.
2. Complete the dates.
3. For iterations with precise alignment:

   1. Move a task to such an iteration (dates to a task are added automatically based on dates for an iteration).

      ![Screenshot of Board module when editing a task.](/cms_trial/assets/ff8c2622-19e4-431f-8043-9543a4516b90.png)

### Resources module

Unscheduled tasks are visible in the sidebar on the right.

To add dates to a task in the [Resources module](/cms_trial/space/SPM/1918535629/Resources+module/):

1. Expand the **Unscheduled tasks** panel.
2. Drag tasks onto the grid, or double-click to edit the dates.

![Screenshot of Resources module when editing a task in the Unscheduled tasks panel.](/cms_trial/assets/f3d2cf52-5872-4635-ae49-ba202af831a6.png)

### Risks module

To add dates to a task in the [Risks module](/cms_trial/space/SPM/1918666681/Risks+module/):

1. Right-click on a task and select **Edit**.
2. Complete the dates.

   ![Screenshot of Risks module when editing a task.](/cms_trial/assets/def09843-8e5f-4fda-9bba-1f78efae7bb4.png)

## Delete task dates in BigPicture

You can delete dates from tasks. As a result, such tasks (without dates) disappear from:

- [Gantt timeline](/cms_trial/space/SPM/1918797129/Gantt+module/)
- [Resources module](/cms_trial/space/SPM/1918535629/Resources+module/)
- [Calendar module](/cms_trial/space/SPM/1918699000/Calendar+module/)

## Edit task dates in BigPicture

Apart from modifying the **Start Date** and **End Date** fields of a task in Jira, you can change dates by the following actions in BigPicture:

- Edit dates:

  - in the column view
  - in the card view (Board and Risks modules)
- Move a task:

  - on the Gantt timeline
  - in the Resources module
  - in the Calendar module
- Inline edit dates:

  - in the Gantt module
  - in the Resources module

## Changes in dates caused by other mechanisms

### Scheduling

- Tasks without dates and tasks where dates have been deleted **are excluded** from the scheduling mechanism (are considered locked tasks). Refer to the [Scheduling mode (previously period mode)](/cms_trial/space/SPM/1918831395/Scheduling+mode/) article.
- Tasks with one date (start date or end date) are included in the scheduling mechanism.

#### **Auto bottom-up mode**

- A task without dates in the scheduling mode set to **auto bottom-up** can get dates when dates for children tasks are added.
- A task with dates in the scheduling mode set to **auto bottom-up** can lose dates when dates for children tasks are deleted.

Refer to the [Scheduling mode (previously period mode)](/cms_trial/space/SPM/1918831395/Scheduling+mode/) article.

#### Start date or end date set to estimate

If dates are calculated based on an estimate:

- Setting a task's start or end date results in calculating the other date automatically.
- Deleting a task's start or end date results in deleting the other date automatically.

Refer to the [One-way sync of Start/End date](/cms_trial/space/SPM/1918537987/Sync+rules/) article.

#### **Auto top-down and Locked modes**

- Tasks in the scheduling mode set to **auto top-down or locked** can modify the dates of their children.

#### Task period alignment

- When the task period alignment of a sub-scope is set to **precise alignment**, after adding a task to such a sub-box, the dates of a sub-box are assigned to a task automatically.

Refer to the [Task period alignment](/cms_trial/space/SPM/1918830096/Define+task+period+alignment/) article.

### Conversion to milestones

Find out more on [the Milestones page](/cms_trial/space/SPM/1918537479/Milestones/)

## Constraints

### [Overdue tasks](/cms_trial/space/SPM/1918537803/Overdue+tasks/)

The overdue tasks feature **works** for:

- Tasks that have start and end dates
- Tasks that have only an end date (the task is semi-transparent)
- The overdue tasks feature **does NOT work** for:

  - Tasks without start and end dates
  - Tasks with a start date, but no end date

### [Critical path](/cms_trial/space/SPM/1918405060/Critical+path/)

The critical path is drawn for:

- tasks with start and end dates
- tasks with one date (either start or end date)

When many tasks are linked by dependencies on the critical path, and one of the tasks loses start and end dates, the critical path may be disrupted. Once the task has dates assigned again, the critical path will appear.

### [Dependencies](/cms_trial/space/SPM/1918538718/Display+dependencies/)

When many tasks are linked by dependencies, and one of the tasks loses both dates (start and end dates), **dependencies are saved**. The arrow between tasks will temporarily disappear, but you can still check the dependency by switching to the **Collapsed** display and clicking on a number in a dot next to the task.

![Screenshot of an example for a collapsed dependency on the Gantt chart.](/cms_trial/assets/2401e0a8-8a95-4869-a5cc-1d2278b384f2.png)

The arrow between tasks will appear once you assign at least one date to the task.

![Screenshot of an example for a collapsed dependency with no end date on the Gantt chart.](/cms_trial/assets/5e5b0a93-bc3f-42ef-984a-52a14671ba75.png)

### Period warnings

See more on the [Period warnings / Parent task conflicts](/cms_trial/space/SPM/1918832897/Period+warnings+%2F+Parent+task+conflicts/) page.

### [Baselines](/cms_trial/space/SPM/1918404564/Baselines/)

Baselines work for tasks with start and end dates. They can’t be created for tasks with only one date.

## Task dates (new navigation)

Click to expand the guide

## Introduction

To start working in BigPicture, you need to create a box and add tasks to this box.

It is not required for tasks to have start and end dates defined:

- Tasks have dates if the **Start Date** and **End Date** fields are set in Jira and the field mapping is configured. For more information, refer to the [Start/end date fields](/cms_trial/space/SPM/1918834667/Start%2Fend+date+of+newly+created+tasks/) article.
- Tasks without dates (the **Start Date** and **End Date** fields are not set in Jira) can also be added to a box in BigPicture.

## Add dates to tasks without dates in BigPicture

There are multiple ways to add dates to tasks without dates. You can add either both dates (start and end) or only one. A task with one date is semi-transparent, as presented below:

- No start date:

  ![Screenshot of a task with no start date.](/cms_trial/assets/24c9fffa-ae14-404c-90d3-48406d452cff.png)
- No end date:

  ![Screenshot of a task with no end date.](/cms_trial/assets/964e4776-856d-407e-ad41-fafab2d739fc.png)

### Gantt module

To add dates to a task in the [Gantt module](/cms_trial/space/SPM/1918797129/Gantt+module/):

1. Hover the mouse cursor over a task on the timeline.
2. Click the **+** icon.

   ![Screenshot of clicking the plus icon on the Gantt timeline to add task dates.](/cms_trial/assets/90361a45-b049-4b74-8e9d-73511e3230d8.png)
3. Edit the **Start Date** and **End Date** fields (make sure that these columns are added to the current [column view](/cms_trial/space/SPM/1918404907/Column+views/)).

   ![Screenshot of changing the start date for a task in the Gantt module.](/cms_trial/assets/740c856e-7fd0-41e6-847c-20410d2b5671.png)

### Scope module

To add dates to a task in the [Scope module](/cms_trial/space/SPM/1918666763/Scope+module/):

1. Find a task.
2. Edit the **Start Date** and **End Date** fields (make sure that these columns are added to the current [column view](/cms_trial/space/SPM/1918404907/Column+views/)).

### Board module

To add dates to a task in the [Board module](/cms_trial/space/SPM/1918796888/Board+module/):

1. Go to **Infobar** > **Backlog**.
2. Edit the **Start Date** and **End Date** fields (make sure that these columns are added to the current [column view](/cms_trial/space/SPM/1918404907/Column+views/)).

For iterations with precise alignment:

1. Move a task to such an iteration (dates to a task are added automatically based on dates for an iteration).

   ![Screenshot of Board module when editing a task.](/cms_trial/assets/ff8c2622-19e4-431f-8043-9543a4516b90.png)

### Resources module

Unscheduled tasks are visible in the sidebar on the right.

To add dates to a task in the [Resources module](/cms_trial/space/SPM/1918535629/Resources+module/):

1. Expand the **Backlog** panel.
2. Drag tasks onto the grid, or double-click to edit the dates.

## Delete task dates in BigPicture

You can delete dates from tasks. As a result, such tasks (without dates) disappear from:

- [Gantt timeline](/cms_trial/space/SPM/1918797129/Gantt+module/)
- [Resources module](/cms_trial/space/SPM/1918535629/Resources+module/)
- [Calendar module](/cms_trial/space/SPM/1918699000/Calendar+module/)

## Edit task dates in BigPicture

Apart from modifying the **Start Date** and **End Date** fields of a work item in Jira, you can change dates by the following actions in BigPicture:

- Edit dates:

  - in the column view
- Move a task:

  - on the Gantt timeline
  - in the Resources module
  - in the Calendar module
- Inline edit dates:

  - in the Gantt module
  - in the Resources module

## Changes in dates caused by other mechanisms

### Scheduling

- Tasks without dates and tasks where dates have been deleted **are excluded** from the scheduling mechanism (are considered locked tasks). Refer to the [Scheduling mode (previously period mode)](/cms_trial/space/SPM/1918831395/Scheduling+mode/) article.
- Tasks with one date (start date or end date) are included in the scheduling mechanism.

#### **Auto bottom-up mode**

- A task without dates in the scheduling mode set to **auto bottom-up** can get dates when dates for child tasks are added.
- A task with dates in the scheduling mode set to **auto bottom-up** can lose dates when dates for child tasks are deleted.

Refer to the [Scheduling mode (previously period mode)](/cms_trial/space/SPM/1918831395/Scheduling+mode/) article.

#### Start date or end date set to estimate

If dates are calculated based on an estimate:

- Setting a task's start or end date automatically calculates the other date.
- Deleting a task's start or end date automatically deletes the other date.

Refer to the [One-way sync of Start/End date](/cms_trial/space/SPM/1918537987/Sync+rules/) article.

#### **Auto top-down and Locked modes**

- Tasks in the scheduling mode set to **auto top-down or locked** can modify the dates of their children.

#### Task period alignment

- When the task period alignment of a sub-scope is set to **precise alignment**, after adding a task to such a sub-box, the dates of a sub-box are assigned to a task automatically.

Refer to the [Task period alignment](/cms_trial/space/SPM/1918830096/Define+task+period+alignment/) article.

### Conversion to milestones

Find out more on the [Milestones](/cms_trial/space/SPM/1918537479/Milestones/) page.

## Constraints

### [Overdue tasks](/cms_trial/space/SPM/1918537803/Overdue+tasks/)

The overdue tasks feature **works** for:

- Tasks that have start and end dates
- Tasks that have only an end date (the task is semi-transparent)
- The overdue tasks feature **does NOT work** for:

  - Tasks without start and end dates
  - Tasks with a start date, but no end date

### [Critical path](/cms_trial/space/SPM/1918405060/Critical+path/)

The critical path is drawn for:

- Tasks with start and end dates
- Tasks with one date (either start or end date)

When many tasks are linked by dependencies on the critical path, and one of the tasks loses its start and end dates, the critical path may be disrupted. Once the task has dates assigned again, the critical path will appear.

### [Dependencies](/cms_trial/space/SPM/1918538718/Display+dependencies/)

When many tasks are linked by dependencies, and one of the tasks loses both dates (start and end dates), **dependencies are saved**. The arrow between tasks will temporarily disappear, but you can still check the dependency by switching to the **Collapsed** display and clicking on a number in a dot next to the task.

![Screenshot of an example for a collapsed dependency on the Gantt chart.](/cms_trial/assets/2401e0a8-8a95-4869-a5cc-1d2278b384f2.png)

The arrow between tasks will appear once you assign at least one date to the task.

![Screenshot of an example for a collapsed dependency with no end date on the Gantt chart.](/cms_trial/assets/5e5b0a93-bc3f-42ef-984a-52a14671ba75.png)

### Parent task conflicts

See more on the [Parent task conflicts](/cms_trial/space/SPM/1918832897/Period+warnings+%2F+Parent+task+conflicts/) page.

### [Baselines](/cms_trial/space/SPM/1918404564/Baselines/)

Baselines work for tasks with start and end dates. They can’t be created for tasks with only one date.