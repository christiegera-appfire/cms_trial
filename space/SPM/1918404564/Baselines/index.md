# Baselines

To assess the performance of your project over time, you can set Baselines and track deviations from your initial schedule.

The Baselines can be synchronized with Jira ([baseline fields](/cms_trial/space/SPM/1918702233/Baseline+start%2Fend+date+fields/) require Jira Admin permissions), and the synced fields can be added to Column views or as fields to the Task / Risk Cards.

You can create and delete Baselines for all the tasks in the box's scope or for selected tasks only. They are displayed as bold lines, showing the task's position at the time the Baseline is created.

## Baseline versioning

There can only be one current baseline for a specific task, but you can create up to 20 baseline history records per box to compare them with the current one or to restore them. A baseline history record is a snapshot of all the baselines set in a box: the start and end date of each baseline and the lack of a baseline for specific tasks. Keeping multiple baseline versions can be useful for comparing planning objectives that may have changed during a project: the first scheduled plan can be compared with the next accepted changes and the current plan.

You can create and delete Baselines for all the tasks in the box's scope or for selected tasks only.

![Baseline drop-down menu](/cms_trial/assets/1db8f648-3518-4152-9cd4-42228993b3dd.png)

## Viewing Baselines

To display Baselines on the timeline, go to **View** → **Show** → **Baselines**.

## Baseline fields in Column Views and Task/Risk Cards

You can store tasks' Baselines as a Date Picker or Date Time Picker field type. As you can connect with different tools, we recommend using the 'Baseline Start date' and 'Baseline End date' **built-in** fields to show the baselines from all connected platforms in a single column.

![Adding a Baseline column](/cms_trial/assets/7fb0c996-ab18-4a16-8773-5e44095c077c.png)

## Creating and Deleting Task Baselines

Baselines work for tasks with start and end dates; they CANNOT be created for tasks with only one date.

### Permissions

For information about the baseline related permissions, check the [Box-level permissions](/cms_trial/space/SPM/1918797447/Box-level+permissions/) page.

### Task Baseline Creation

Once your schedule is ready, you can create a Baseline schedule or, in other words, Baselines for all tasks shown in the issue list (WBS). Alternatively, you can create a Baseline by editing the synchronized fields directly.

To create Baselines, go to **Data** → **Baselines** → **Create** or **Delete**.

![Baseline drop-down-menu](/cms_trial/assets/bb90d3b8-8ec7-46fc-adc9-ebb72c54b3e6.png)

### All items

![Baselines drop-down menu, create option](/cms_trial/assets/bb90d3b8-8ec7-46fc-adc9-ebb72c54b3e6.png)

### Single item

To create or delete a Baseline for selected tasks only, right-click on the task or use the vertical menu that appears when you select the task. Remember to enable Baselines afterward.

![Baselines colors](/cms_trial/assets/6abd63d6-b6c7-4984-85cc-66cff42bc6b0.png)