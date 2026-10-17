# Non-working days

## About non-working days

**The App can recognize non-working days and adjust the task period.** This means that if you plan a task or part of your task's period on a non-working day, it will be moved, extended, or shortened.

You can define the non-working days in the Administration section:

- [Absences](/cms_trial/space/SPM/1918764834/Absences/)
- [Holiday plans](/cms_trial/space/SPM/1918505164/Holiday+plans/)
- [Workload plans](/cms_trial/space/SPM/1918506352/Workload+plans/)

**Each non-working day reduces the capacity of your Resource.** The capacity is calculated by the App and does not sync with the Host platform (you will not be able to see the capacity of your Resource directly in Jira or Trello).

The Workload plan restriction will not be applied to parent tasks in [auto bottom-up modes](/cms_trial/space/SPM/1918831395/Scheduling+mode/). When the child task has a different assignee, and its start/end date influences the parent's duration, the parent's start/end date will be set according to the child's date, even if it's planned on a non-working day for the parent task's assignee. Simply put: parent always ignores schedules, i.e., You can set start and end date on non-working days if children's dates are set up on such days.

**If working days are changed (either globally or for a resource), it has no effect on the scheduling of existing tasks**. An action (such as a change of task duration) will trigger a new validation - the validation mechanism will take all non-working days into account and move tasks accordingly. Otherwise, some changes (e.g., adding a long absence or changing global working days) could have a massive unintended impact on the scheduling.

## Displaying non-working days on the timeline

The non-working days are displayed on the timeline of the Gantt and Resources modules as grey cells. By default, only the weekend is marked as non-working:

![contentId-1918504137](/cms_trial/assets/2613abca-1d81-4a91-9a2e-c8b772b20d93.png)

## Calculating tasks period based on assignee's working days

Go to [Calculate tasks automatically based on assignee's working days](/cms_trial/space/SPM/1918638098/Calculate+tasks+automatically+based+on+assignee%27s+working+days/) to learn more.