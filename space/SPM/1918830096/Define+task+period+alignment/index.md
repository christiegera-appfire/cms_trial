# Define task period alignment

The scheduling mechanism can align or adjust the start/end dates of tasks assigned to a box with the box's own start/end dates. Switching to **Precise alignment** or **Smart adjustment** will reschedule all the tasks already assigned to those boxes.

## Enable the alignment

Go to **Box Configuration > Tasks > Scheduling**. Use the drop-down to select the desired **Task period alignment**.

![contentId-1918830096](/cms_trial/assets/350233f3-522c-4289-b91b-4d6454370cf7.png)![contentId-1918830096](/cms_trial/assets/2b4be9b0-e570-49e3-ae95-eaebec764b22.png)

Alternatively, to enable this feature click the "Info" button found on the Box header in the Board module and select one of the options:

![contentId-1918830096](/cms_trial/assets/948b3158-c1e2-4c09-82c1-897c54524dac.png)

## Configuration

When creating a new box, you can set the default period mode by configuring a box type in **App** **Administration** > **box types**. You need an App Admin security role to access the box type configuration.

You can set the period mode for each box in **box bonfiguration** > **Tasks** > **Scheduling**. To access this page, you need the Box Administrator security role.

The period mode can synchronize with Jira using a custom field - Select List (single choice) type, created during the installation. You can add this field to issue screens and change the period mode by editing the issue without opening the app.

## Scheduling mode

Default scheduling mode is applied to new tasks (added to the scope of the Box for the first time). If a task is already within the scope of any other box, its scheduling mode will not be overwritten.

There are different ways to add tasks that will be treated as new. These include:

- using the '+' (add task) button in different modules,
- changing the Box scope - for example, adding a new filter to the automatic rules,
- updating the task to fit within the Box scope definition - for example, moving the task to a project added to the box scope.
- you can also change the task period alignment directly on the box details dialog.

![A dropdown menu on the box details dialog where you can select the task period alignment.](/cms_trial/assets/307fe135-e080-43df-88cf-9f9d82e6883f.png)

We recommend using the 'Manual' period mode to ensure that your task will not be automatically rescheduled based on the configuration of structure builders and dependencies. You can always enable automation at any time, but you might not be able to revert changes quickly.

For example, All tasks are in the auto bottom-up period mode, and the manual mode is set for newly added tasks - OA-135:

![BigPicture-BigPicture-demo.png](/cms_trial/assets/276ea6ae-0575-4c45-800a-08c2fcad904f.png)

## Synchronization mechanism

Please note the synchronization mechanism is:

- Unidirectional - planning tasks using Boxes (Program Increments or Iteration) updates the tasks to fit within the Boxes' duration. However, changing the tasks' start/end date fields doesn’t automatically add a task to the Box.
- A one-time operation - when a task is placed in a Box (e.g., using the Board module), the task period is updated only once; if you adjust the task period after it has been placed in a Box (e.g., making changes using the Gantt module) the app will not validate the adjustment even if the new period doesn’t fit within the Box time frame (i.e., smart alignment will be overridden by a manual change).

The update of the task period mentioned above will be appropriately executed only if all task scheduling rules (parent-child relation, period mode, inward dependency, etc.) allow the operation to be executed. For example, if a Story has a parent task in the task structure with a "lock" mode set, the app may not update the Story period if it exceeds the parent period after the update.

- Rescheduling a task period may trigger changes in related tasks (linked tasks or parent/children in the task structure). To learn more about task scheduling rules, go to [Automations](/cms_trial/space/SPM/1918535176/Automations/).
- There are different ways to assign a task to a box. For example, you can drag and drop a task using the Board module or edit the task and update the synchronized field value.

## Set alignment on lower levels

The task alignment applies to the box configured and not to its sub-boxes. If you want to align tasks only on, for example, the Iteration level, use the option **Set alignment on lower levels**.

This configuration applies to the sub-boxes, and you can set the alignment for two levels of sub-boxes. For example, the PI Planning Program box consists of Program increment sub-boxes, which, in turn, consist of Iteration sub-boxes.

## Task scheduling options

Use the Precise alignment or Smart adjustment to update the date estimates at the task level.

### No alignement

The task's period will not align with the box's period. When a task is planned in one of the Timeboxes, the fields mapped as start and end dates will not get updated.

### Precise alignment

The task's period will align precisely with the box's period. A task can be aligned with a Timebox created using the **Overview** module > **Views** > **Hierarchy** (a timebox is a sub-box such as Iteration or Project Increment that doesn't have its own scope, as it's used to organize tasks within the parent).

Fields mapped as start and end dates are affected by a task placed in one of the boxes and starting/finishing on the same date.

When you enable the Precise alignment and change the start/end dates of a box, the scheduling mechanism will update all tasks accordingly.

The **precise alignment** option can be enabled only for sequential boxes with sub-scope.

#### After the adjustment

The initial position of the task is irrelevant as the outcome is always the same. All tasks were assigned to the iteration named "Iteration 2.1":

![contentId-1918830096](/cms_trial/assets/3435cd9f-ba9c-4937-8782-396322b0f62a.png)

### Smart adjustment

The task's timeframe aligns with the start and/or end date of a Box. The task's length remains unchanged (whenever possible). Fields mapped as start and end date are affected by a task being placed in one of the Boxes as follows - a task starts on the start date of the Box (when moved to a future Box relative to the Task) or ends on the end date of the Box (when moved to a previous Box relative to the Task).

When you enable the Smart adjustment and change the start/end dates of your Boxes, the scheduling mechanism will update all tasks accordingly.

#### Before vs. after the adjustment

The below image showcases the initial positions of tasks (on the left) and the adjustment outcome (on the right).

All tasks were assigned to iIteration named "Sprint".

![contentId-1918830096](/cms_trial/assets/a6930410-bfaa-4875-92ca-487303cd78a6.png)

- Purple task - the entire task is already contained within the Iteration →  no changes applied.
- Navy blue task - the entire task precedes the Iteration period with no overlap (task length doesn’t exceed the Iteration duration) → task is moved - start dates of the task and Iteration are aligned; task length remains unchanged.
- Red task - the entire task follows the Iteration period with no overlap (task length doesn’t exceed the Iteration duration) → task is moved - end dates of the task and Iteration are aligned; task length remains unchanged.
- Orange task - the entire task precedes the Iteration period with no overlap (task length exceeds the Iteration duration) → task is moved - both start and end dates of the task are aligned with the Iteration; task length altered to fit within the Iteration.
- Light green task - the entire task follows the Iteration period with no overlap (task length exceeds the Iteration duration) → task is moved - both start and end dates of the task are aligned with the Iteration; task length altered to fit within the Iteration.
- Grey task - the entire task overlaps with the Iteration period (task length exceeds the Iteration duration) → task start and end dates are aligned with the Iteration; task length altered to fit within the Iteration.
- Dark green - the task partially overlaps with the beginning of the Iteration period (task length doesn’t exceed the Iteration duration) → task is moved - start dates of the task and Iteration are aligned; task length remains unchanged.
- Brown task - the task partially overlaps with the end of the Iteration period (task length doesn’t exceed the Iteration duration) → task is moved - end dates of the task and Iteration are aligned; task length remains unchanged.
- Turquoise task - the task partially overlaps with the beginning of the Iteration period (task length exceeds the Iteration duration) → task is moved - the start and end dates aligned with the Iteration; task length altered to fit within the Iteration.
- Black task - the task partially overlaps with the end of the Iteration period (task length exceeds the Iteration duration) → task is moved - the start and end dates aligned with the Iteration; task length altered to fit within the Iteration.