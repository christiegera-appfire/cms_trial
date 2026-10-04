# Workload contouring

## Workload distribution

You can change workload distribution for a given task. Workload contouring lets you specify how an assignee's effort is distributed across a task period.

App admins can set a default workload contouring mode for new box types, which can be overridden in a specific box.

Changing the box type or box configuration settings doesn't impact existing tasks - their workload contouring has to be manually changed in the Resources module.

### Workload contouring - box types

See the [Workload contouring](/cms_trial/space/SPM/1918831697/Set+workload+contouring+mode/) page to learn more about workload contouring in box type settings.

## Workload contouring modes

You can set a workload contouring mode of a task to:

- Flat
- Front-loaded
- Back-loaded
- Manual

### Auto flat mode

The **flat mode** means that if a task duration lasts for five days and the original estimate to complete the work is 20 hours, the assignee's effort is distributed evenly. For example, 20 hours spread over five days results in 4 hours of work per day. This mode is shown on the Gantt chart in the Resources panel. If you adjust the task duration, the effort will be reallocated evenly.

![nrg-flat-contouring-mode.png](/cms_trial/assets/bd930c12-2d97-4b67-a018-4c5daa4b7b62.png)

### Auto front-loaded mode

In **front-loaded** mode, additional effort is progressively allocated from the task's start date. The assignee is assigned as many hours per day as their capacity permits (for example, 8 hours per day) until the total effort is fully distributed.

![nrg-front-loaded-contouring-mode.png](/cms_trial/assets/a1f3f4e5-0bda-452c-ae48-e2684d2bda3d.png)

### Auto back-loaded mode

In the **back-loaded mode**, extra effort is gradually added, beginning at the task's end date. The assignee is assigned as many hours per day as their capacity allows (for example, 8 hours), going backward until the estimate is fully allocated.

![nrg-back-loaded-contouring-mode.png](/cms_trial/assets/a901af0b-0108-43bb-8b0a-00456ac9a7b0.png)

### Manual contouring mode

It can’t be enabled if the [effort mode](/cms_trial/space/SPM/1918764313/Effort+modes/) is set to story points.

You can manually adjust workload contouring by switching to manual mode. Once activated, you can manually spread the workload directly on the task details dialog box.

As you modify the workload, the original estimate will be updated accordingly. The remaining capacity for each resource is displayed below each field, allowing you to see how much capacity is available on a given day.

This feature offers flexibility and helps ensure you can achieve the desired allocation. For example, if you want to assign someone 7 hours of work each day while leaving 1 hour for miscellaneous tasks, you can easily manage that, even if they have multiple commitments.

See the video on how to manually adjust workload contour.

![Video of adding workload contour manually in the Resources module.](/cms_trial/assets/4be8cf82-9642-47b1-a0f7-52bbc62f57cd.mp4)

## Edit workload contouring

Workload contouring can be edited only in the **manual** workload mode. Otherwise, it is calculated **automatically**.

To change the workload contouring mode for an individual existing task:

1. Go to the Resources module.
2. Make sure tasks are displayed on the grid.

   ![Screenshot of the View menu in the Resources module.](/cms_trial/assets/fa572ae9-3f97-494a-beda-ebc4d5ff405a.png)
3. Click a task to see a context menu and make adjustments.

   ![Screenshot of editing the manual contouring mode in the Resources module.](/cms_trial/assets/bda15605-098d-479b-8619-22117e543c29.png)
4. To save changes, click outside of the dialog.

**Gantt module**

You can check and edit inline the workload inline in the Gantt module.

1. Go to the Gantt module.
2. Add the **Workload contouring mode** to the column view.

![Screenshot of adding the Workload contouring mode column in the Gantt module.](/cms_trial/assets/77084b17-66ef-4330-9ecb-185d098e23e7.png)

## Affected by

- When automatic workload contouring modes are selected, task effort distribution between specific days changes depending on the filters chosen in the Resource module. The algorithm is independent of filters.