# Manage task templates

Basic tasks have been renamed to **BigPicture tasks** as part of the new navigation rollout.

Both names refer to the same functionality. You may see either term depending on whether you’re using the previous navigation or the new navigation that is currently being rolled out in BigPicture.

## Manage task templates (old navigation)

Click to expand the guide

With the task templates, you can predefine templates of [basic tasks](/cms_trial/space/SPM/1918405930/Basic+tasks+%2F+BigPicture+tasks/) (basic tasks can be viewed only in the app). This will arrange a group of tasks in an independent micro-structure, which can be reused as a template in the **Gantt, Scope, and Calendar modules** later on.

You can use basic task templates, create simple schedules to arrange your data into phases and stages or represent external providers' tasks.

To achieve a preconfigured arrangement of that sort, you need to use the relative dates column. It is relative because the numbers you put there are counted since the parent task (if there are any).

The template will appear in your task templates list in the **+Add task** menu, and you will be free to fit it into your structure in any desired way with pre-defined dependency rules.

## Security and access

Keep in mind:

- A box type contains the default settings applicable to multiple boxes (all boxes of a given type). Those settings are adjusted in the app Administration.
- Box configuration refers to the settings of a single, individual box. They are dependent on the box type settings.

The table presents what you can configure at the box type and box levels.

| **Area** | **Security and access** | **What can be configured** |
| --- | --- | --- |
| Box type configuration | Only a user with the App Admin security role can access and manage the box type configuration.  Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Tasks** > **Task templates**. Task templates settings in the box type configuration. | For a box type (all boxes of a given type), you can:   - Configure the inheritance mode - Add default task templates |
| Box configuration | Only a user with a minimum Box Admin security role can access and manage the box configuration.  Go to **box configuration** > **Tasks > Task templates**. Task templates settings in the box configuration. Alternatively, go to **+Add task** > **Manage templates** in the Gantt, Scope, or Calendar module. Screenshot of adding a new task from a template in the Gantt module. The box configuration page will not be visible if the module was deactivated or the inheritance mode is set to **inherited only**. | For a particular box, you can add:   - Task templates |

## Inheritance mode

The task templates can be inherited by the sub-level boxes when the inheritance mode is set to **Inherited only** or **Own with inherited** in the **Box type** configuration of the upper-level box. This way, every time you create new templates or edit the existing ones, all available views will also be updated in the sub-level boxes.

Inherited templates are marked with an **arrow pointing upward** and cannot be deleted.

Learn more about the inheritance mode on the [Inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/) page.

## Default task templates

Changes made to the default task templates don't impact existing Boxes - new settings apply only to Boxes created from that point on.

You can create default templates when the inheritance mode is set to either **Own** or **Own with inherited**:

![contentId-1918503892](/cms_trial/assets/a008a1ac-c09d-4876-92fd-c249c4df09dd.png)

The default templates are automatically set up when you create a new box. Afterward, Box Admins can edit and remove the default templates (if the Inheritance mode allows it). Click the '+' drop-down in the Gantt/ Scope/ Calendar module to select from the list of available templates:

![BigPicture-BigPicture-demo (62).png](/cms_trial/assets/bc176858-c19a-4147-86e8-fc0b80ec5d5f.png)

## Add new task templates

To add new templates:

1. Click A**dd new task template**.
2. Enter a template name.
3. Add **Description** (optional).
4. To confirm, click **Create**.

![Screenshot of adding a new task template.](/cms_trial/assets/bfb02e77-ab58-44ae-a21f-73d92969c904.png)

Once added:

1. Click the clickable name link.
2. Click **Create new task**.
3. Enter **Name**.
4. Provide **Start date lag time** and **End date lag time**.
5. To confirm, click **Create**.

![Screenshot of adding a new task to a template.](/cms_trial/assets/c9d12799-c32a-439d-b4d0-184e6fef8a7d.png)

Now, you can use the template by selecting it from the **+Add task** menu in the Gantt, Scope, or Calendar module.

![Screenshot of adding a new task from a template in the Gantt module.](/cms_trial/assets/a6b59f3d-4c87-4922-a68e-9437aae7ddab.png)

## Edit templates

To update the name and the description fields of the created template, click **Edit**.

![Screenshot of editing a task template in box configuration.](/cms_trial/assets/e1b4aa35-666e-4966-82cc-d3fec1234c8f.png)

## Delete templates

To remove a template, click **Delete**. You can’t recover deleted templates.

![Screenshot of deleting a task template in box configuration.](/cms_trial/assets/ef342aa4-c918-4fad-bc35-026a43641b4d.png)

## Manage task templates (new navigation)

Click to expand the guide

With the task templates, you can predefine templates of [BigPicture tasks](/cms_trial/space/SPM/1918405930/Basic+tasks+%2F+BigPicture+tasks/) (these tasks can be viewed only in the app). This will arrange a group of tasks into an independent micro-structure, which can be reused as a template in the **Gantt, Scope, and Calendar modules** later on.

You can use BigPicture task templates, create simple schedules to arrange your data into phases and stages, or represent external providers' tasks.

To achieve a preconfigured arrangement of that sort, you need to use the relative dates column. It is relative because the numbers you put there are counted from the parent task (if there is one).

The template will appear in your task templates list in the **Tasks > BigPicture task from template** menu, and you will be free to fit it into your structure in any desired way with pre-defined dependency rules.

![Screenshot of the BigPicture task from template option in the Gantt module.](/cms_trial/assets/50f32118-3294-4b1a-9583-b08ccb4e2ab0.png)

## Security and access

Keep in mind:

- A box type contains the default settings applicable to multiple boxes (all boxes of a given type). Those settings are adjusted in the app Administration.
- Box configuration refers to the settings of a single, individual box. They are dependent on the box type settings.

The table presents what you can configure at the box type and box levels.

| **Area** | **Security and access** | **What can be configured** |
| --- | --- | --- |
| Box type configuration | Only a user with the App Admin security role can access and manage the box type configuration.  Go to the **Administration** > **Box type** > **choose the box type you want to edit** > **Tasks** > **Task templates**. Task templates settings in the box type configuration. | For a box type (all boxes of a given type), you can:   - Configure the inheritance mode - Add default task templates |
| Box configuration | Only a user with a minimum Box Admin security role can access and manage the box configuration.  Go to **box configuration** > **Tasks > Task templates**. Task templates settings in the box configuration. Alternatively, go to **Tasks** > **BigPicture task from template** > **Manage templates** in the Gantt, Scope, or Calendar module. Screenshot of the Manage templates option in the BigPicture task from template menu.  The box configuration page will not be visible if the module was deactivated or the inheritance mode is set to **inherited only**. | For a particular box, you can add:   - Task templates |

## Inheritance mode

The task templates can be inherited by the sub-level boxes when the inheritance mode is set to **Inherited only** or **Own with inherited** in the **Box type** configuration of the upper-level box. This way, every time you create new templates or edit the existing ones, all available views will also be updated in the sub-level boxes.

Inherited templates are marked with an **arrow pointing upward** and cannot be deleted.

Learn more about the inheritance mode on the [Inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/) page.

## Default task templates

Changes made to the default task templates don't impact existing Boxes - new settings apply only to Boxes created from that point on.

You can create default templates when the inheritance mode is set to either **Own** or **Own with inherited**.

The default templates are automatically set up when you create a new box. Afterward, Box Admins can edit and remove the default templates (if the inheritance mode allows it).

![Screenshot of the Task templates page in the box type Administration.](/cms_trial/assets/d14e6140-8388-4acb-9ebc-08f81f1c8edb.png)

## Add new task templates

To add new templates:

1. Click A**dd new task template**.
2. Enter a template name.
3. Add **Description** (optional).
4. To confirm, click **Create**.

![Screenshot of adding a new task template.](/cms_trial/assets/bfb02e77-ab58-44ae-a21f-73d92969c904.png)

Once added:

1. Click the clickable name link.
2. Click **Create new task**.
3. Enter **Name**.
4. Provide **Start date lag time** and **End date lag time**.
5. To confirm, click **Create**.

![Screenshot of adding a new task to a template.](/cms_trial/assets/c9d12799-c32a-439d-b4d0-184e6fef8a7d.png)

Now, you can use the template by selecting it from the **Tasks > BigPicture task from template** menu in the Gantt, Scope, or Calendar module.

![Screenshot of the BigPicture task from template option in the Gantt module.](/cms_trial/assets/50f32118-3294-4b1a-9583-b08ccb4e2ab0.png)

## Edit templates

To update the name and the description fields of the created template, click **Edit**.

![Screenshot of the Edit button on the Task templates page in the box configuration.](/cms_trial/assets/fafb510e-8c0c-40c7-9658-1f59d8008a0b.png)

## Delete templates

To remove a template, click **Delete**. You can’t recover deleted templates.

![Screenshot of the Delete button available on the Task templates page in the box configuration.](/cms_trial/assets/3a9b3339-deac-4c4a-af4d-819065e86b94.png)