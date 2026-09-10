# Working with Custom Fields

![TryItButton (2).png](/cms_trial/assets/26e3178d-3f5f-4bf6-946c-79a4179089a3.png)

Custom fields help you record more details with your time entries and can be easily created in 7pace Timetracker for Jira.

## Watch the video

In the following video, two custom fields are created:

1. A **Billable** toggle switch.
2. A dropdown field that helps you categorize work.

Note that custom fields can only be created by a Jira administrator and that a maximum of 10 custom fields can be created.

## Custom fields

In the following examples, two custom fields are created:

1. A **Billable** toggle switch.
2. A field that lets you categorize the type of work.

### Custom field - Billable toggle switch

Use the following steps to create a custom **Billable** toggle switch:

1. Click **Apps** > **Timetracker** > **Settings** > **Custom Fields**.
2. A preview of the *Add Time* dialog displays.
3. Click **Create new field**.
4. Select **Toggle**.
5. Enter a name for the new field, **Billable**, and a brief **Description**, if necessary.
6. Specify whether or not the field defaults to **On** or **Off**.

   - The *Add Time* dialog updates dynamically to reflect the new **Billable** field.
7. Click **Save changes**.

   ![A custom toggle field named Billable.](/cms_trial/assets/851047ee-1b70-4328-b231-f92021ff1e1b.png)

### Custom field - Categorize work type

In the next example, create an **Activity Type** dropdown field that captures how to categorize the time being entered.

1. Click **Create new field**.
2. Select **Dropdown**.
3. Enter a name for the new field, **Activity Type**, and enter a brief **Description,** if necessary.
4. Click **Add option.**

   1. Enter the first option name, **Design**.
   2. Click **Add option** to create the next **Activity Type**, **Requirements**. The color can be changed for each option, making it easy for users to distinguish between their choices.
5. Create a third **Activity Type**, **Documentation**.
6. Assume the activity types should be displayed alphabetically.
7. Simply drag Documentation into the second position.
8. Click **Save Changes**.

   ![image-20241108-221402.png](/cms_trial/assets/ba9ee687-4cb9-403a-b896-05f3bc899f04.png)

## Where do custom fields display?

The two custom fields now display in the *Add Time* dialog. Note that fields below the line in the left-hand pane are not mandatory. So, if we drag **Activity Type** below the line, users are not required to select an Activity Type when tracking time.

![Custom fields below the Not Required line do not have to be filled in by users.](/cms_trial/assets/63c368f6-c09c-4426-b3ba-3d6a67c0be91.png)

**Billable** and **Activity Type** are simply examples of custom fields. However, you have the flexibility to track any additional information required for your business.

Now, when tracking time, the custom fields display on the *Add Time* dialog. The custom fields also display when tracking time on the *Monthly* and *Weekly* pages.

![The Add Time dialog with both custom fields, Billable and Activity Type.](/cms_trial/assets/aff3f584-a1d8-48d3-9861-cbbc09974944.png)

Custom fields can also be added to the *Times Explorer*. Click **Settings** and then scroll down to add the **7pace Custom Fields** section.

![Custom fields can be added to the Times Explorer. Use the Customize Columns window to select fields.](/cms_trial/assets/bebe4ae1-5630-4892-998c-7fb2f6113f6f.png)

After selecting custom fields, they are visible and can be used in filtering.

## Custom fields by project

You can create a set of custom fields and assign it to a specific Jira project. To do this, select the plus icon. Define name of the set, select Jira project, and select Save.

![create-custom-fields.png](/cms_trial/assets/1a13917c-0044-4cb0-b8bd-2ec8b6c90e38.png)

Now you can define a set of fields for this specific project. You can also change the name of the set and choose another Jira project.

![custom-fields-set.png](/cms_trial/assets/e455df2f-294f-4ee4-b468-ecb584576088.png)

If a specific project does not have custom fields assigned, global settings apply.