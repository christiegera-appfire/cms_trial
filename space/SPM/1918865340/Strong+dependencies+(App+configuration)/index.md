# Strong dependencies (App configuration)

Strong dependencies are dependencies with a scheduling impact. For example, when in auto mode, moving one linked task might update the position of the other linked tasks.

## Security and access

Only Jira administrators can access this page.

1. Click the **wrench** icon at the top right and select**General** from the drop-down list.
2. Next, go to **Dependencies** > **Strong dependencies**.

   ![image-20250211-131519.png](/cms_trial/assets/e4cd8d40-52df-4418-b4d0-ffa7669c0784.png)

## Default dependency configuration

The app creates custom dependencies that are most suitable for working with Gantt tasks:

| **Dependency** | **Outward description** | **Inward description** |
| --- | --- | --- |
| Gantt: **End to End** dependency | has to be finished together with → | has to be finished together with |
| Gantt: **End to Start** dependency | has to be done before → | has to be done after |
| Gantt: **Start to End** dependency | the start is the earliest end of → | the earliest end is the start of |
| Gantt: **Start to Start** dependency | has to be started together with → | has to be started together with |

## ASAP mode

The ASAP **mode** is a scheduling mechanism that minimizes the gap between dependent tasks. It applies to strong dependencies only. In such case, the scheduling mechanism will try to reduce the gap between dependent tasks to a minimum. When you set this switch to active, the app remembers the settings, and all future dependencies will be created with the ASAP mode.

The ASAP mode is disabled by default on the App Configuration page. It means that all the strong dependencies you create will have the ASAP mode turned off.

The Source task date rules the Target task date. It's a uni-directional relationship.

### Activate ASAP mode

To activate the ASAP mode:

1. Go to **App Configuration > General**
2. Go to **Dependencies**
3. Set the **'Default ASAP mode'** toggle to active

![contentId-1918865340](/cms_trial/assets/b97a17a7-5585-4a07-afc3-8587780a258b.png)

If you leave the ASAP mode disabled by default, you can still enable this mode for the individual dependencies. In the Gantt or Board module, click on the dependency you want to edit. On the Dependency details screen, toggle on the ASAP mode.

There are four possible ways to connect tasks:

- end to start - the end date of a task dictates the ASAP start of a target task.

See the example![contentId-1918865340](/cms_trial/assets/ffe7d9da-a919-4a91-9cfd-f2aac93fd8c6.png)![contentId-1918865340](/cms_trial/assets/8fc8dd8e-dd73-4b0c-a6a8-726e979b4150.png)

- start to end - the start date of a task dictates the ASAP end of another task.

See the example![contentId-1918865340](/cms_trial/assets/502b3fca-2c1f-49b5-ae02-9be461ad89f4.png)![contentId-1918865340](/cms_trial/assets/5de45c32-2b2b-405a-a4a7-83a2db154358.png)

- end to end - the end date of a task dictates the ASAP end date of a target task.

See the example![contentId-1918865340](/cms_trial/assets/12a07707-3034-40a3-9ac8-ad013a122273.png)![contentId-1918865340](/cms_trial/assets/f113756a-305d-4122-ae78-344996f8dd39.png)

- start to start - the start date of a task dictates the ASAP start date of a target task.

See the example![contentId-1918865340](/cms_trial/assets/ede1b783-b8b8-410f-ba5a-0a039c4ec718.png)![contentId-1918865340](/cms_trial/assets/48f8abc6-65e1-4c0e-b244-e4699379f037.png)

The direction of the dependency is based on how you create a dependency (the direction of an arrow when connecting tasks).

In other words, dependency in ASAP mode always schedules the target task as soon as possible based on dependency type. There are no restrictions on how many dependencies are created for each source or target task as long as they are not creating circular relationships. If a task is moved to a prohibited position (based on dependency type and mode), **it is moved back/forward to the appropriate position.**

To enable the ASAP mode, click on one of the dependencies:

![contentId-1918865340](/cms_trial/assets/4ff5ee5f-a64d-4dfd-a754-a65aa522a81c.png)

Creating a dependency can re-adjust the task period, but deleting a dependency will not move tasks on the timeline.

### Dependency Color

The dependencies with ASAP mode enabled are colored dark grey.

### Dependency Lag Time

It is possible to add lag time to an ASAP mode dependency. The system will add a delay equal to the specified number of days.

Non-working days are included in the calculation.

![contentId-1918865340](/cms_trial/assets/e3491509-c50b-466e-93f6-e9c256d23b26.png)![contentId-1918865340](/cms_trial/assets/eb4a931c-5d9b-495f-b5a1-558c15562bfb.png)

The Lag time is the minimum time between the tasks, but if you set a 3 day lag time and a task ends on Wednesday, effectively, the gap will last 4 days (Saturday is counted as the 3rd day, but it is not possible for the next task to start on Sunday).

![contentId-1918865340](/cms_trial/assets/eb47526d-f785-4fba-b430-03722e277e63.png)

## ASAP "on" vs "off"

### ASAP mode on

With ASAP mode **on,** there is only one position where a dependency can place a task. The lag time is respected. With ASAP mode **on**, the date of the target task should be the same as the date of the source task.

In the example below (no lag time), end date of PP-326 dictates the start date of PP-332. The target start date can't be manually overridden - it will always be the next possible day after the source end date.

![contentId-1918865340](/cms_trial/assets/7c2bead2-e5f2-40d3-bb72-673a73ede43b.png)

### ASAP mode off

When ASAP mode is **"off"**, there is more than one way to position a task. The lag time is respected.

With ASAP mode is **"off"**, the date of the target task should be the same or later than the date of the source task.

There is more than one possible start date for the PP-332 task (any date after August 6th will work).

![contentId-1918865340](/cms_trial/assets/f405a01e-8176-4505-868d-ab70f9d67f54.png)