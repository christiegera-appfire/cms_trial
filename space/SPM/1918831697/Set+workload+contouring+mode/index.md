# Set workload contouring mode

Workload contouring allows you to specify how an assignee's effort is distributed across a task period. On the box type configuration page, you can define the default workload contouring mode that will apply to all newly created boxes of that type.

An App Admin can establish a default workload contouring mode for new boxes of a specific type, which can be adjusted in individual boxes after they are created.

Altering the settings on the box type configuration page or on the individual box configuration page does not affect existing tasks; their workload contouring mode must be modified manually in the Resources module.

## Security and access

Keep in mind:

- A box type contains the default settings applicable to multiple boxes (all boxes of a given type). Those settings are adjusted in the BigPicture Administration.
- Box configuration refers to the settings of a single, individual box. They are dependent on the box type settings.

The table presents what you can configure at the box type and box levels.

| **Area** | **Security and access** | **What can be configured** |
| --- | --- | --- |
| Box type configuration | Only a user with the App admin security role can access and manage the box type configuration.  Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Tasks** > **Workload contouring**. Box type configuration page. | For a box type (all boxes of a given type), you can configure:   - Default workload contouring mode |
| Box configuration | Only a user with a minimum box admin security role can access and manage the box configuration.  Go to **box configuration** > **Tasks** > **Workload contouring**. image-20250327-084640.png | For a particular box, you can configure:   - Box workload contouring mode |

## Default workload contouring mode

You can set a workload contouring mode of a task to:

- Auto flat
- Auto back-loaded
- Auto front-loaded
- Manual

### Auto flat mode

The **flat mode** means that if a task duration lasts for five days and the original estimate to complete the work is 20 hours, the assignee's effort is distributed evenly. For example, 20 hours spread over five days results in 4 hours of work per day. This mode is shown on the Gantt chart in the Resources panel. If you adjust the task duration, the effort will be reallocated evenly.

![Flat mode shown in the resources module.](/cms_trial/assets/6ed88641-43e1-4a8f-bb42-5fe0be6d79a5.png)

### Auto front-loaded mode

In **front-loaded** mode, additional effort is progressively allocated from the start date of the task. The assignee is assigned as many hours per day as their capacity permits (for example, 8 hours per day) until the total effort is fully distributed.

![Front-loaded mode shown in the resourced module.](/cms_trial/assets/fcc24093-bc2c-41e8-9ef2-92763864b26a.png)

### Auto back-loaded mode

In the **back-loaded mode**, extra effort is gradually added, beginning at the task's end date. The assignee is assigned as many hours per day as their capacity allows (for example, 8 hours), going backward until the estimate is fully allocated.

![Back-loaded mode shown in the resources module.](/cms_trial/assets/9928e37a-b99d-49e2-b901-89fc42803a13.png)

### Manual Contouring Mode

Manual contouring mode cannot be enabled if the [effort mode](/cms_trial/space/SPM/1918764313/Effort+modes/) is set to story points.

You can manually adjust workload contour by switching to manual mode. Once activated, you can manually spread the workload directly on the task details dialog box.

As you modify the workload, the original estimate will be updated accordingly. The remaining capacity for each resource is displayed below each field, allowing you to see how much capacity is available on a given day.

This feature offers flexibility and helps ensure you can achieve the desired allocation. For example, if you want to assign someone 7 hours of work each day while leaving 1 hour for miscellaneous tasks, you can easily manage that, even if they have multiple commitments.

![Manual mode shown in the resources module.](/cms_trial/assets/c74fe98e-4f14-4844-a732-16b39f5279e3.mp4)