# Timeboxes

## Timeboxes (old navigation)

## About timeboxes

Timeboxes define consecutive timeframes used for work planning. In BigPicture, they represent sprints, iterations, increments, and stages.

There are two types of timeboxes:

- Automatic (timeboxes synchronized with Jira sprints)
- Manual (timeboxes added manually. The timeboxes you can add depend on the [box type settings](/cms_trial/space/SPM/1918766536/Scope+types/))

App admins can configure timebox schedules to define a reusable timebox hierarchy (e.g., Year → Quarter → PI → Iteration) and apply it across multiple boxes. See more on the [Timebox schedules](/cms_trial/space/SPM/1989214530/Timebox+schedules/) page.

![Timeboxes configuration on the box scope definition page.](/cms_trial/assets/036bef13-2aab-4df5-b7c5-de0b8ea94b0d.png)

## Set box type sequentiality

To prevent the period of consecutive timeboxes from overlapping, the box type's sequentiality should be set to **Sequential**. See the [Period mode and sequentiality](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/) page for more information.

[Unmapped block: nestedExpand]

## Automatic timeboxes (synced with Jira sprints)

Before you start working with the Board module, you must configure timeboxes first. Here’s a short video showing you the process.

To create timeboxes based on Jira sprints from a selected Jira board:

[Unmapped block: nestedExpand]

### Add missing sprint dates in Jira

When Jira sprints do not have dates, timeboxes **cannot** be created. In this case, you will see the message in the screenshot below.

You can fix it by adding the dates for the first Jira sprint and running the synchronization again.

![BigPicture warning that pop up when the Jira sprint dates are missing.](/cms_trial/assets/73030ac4-8dcc-415b-8e2e-fe9ef6467ee2.png)

### Use Jira boards to create automatic timeboxes

You can choose a Jira board to create timeboxes automatically. The board you choose will be then automatically added to the scope of the box.

Thanks to this, you can be sure that all the tasks from the Jira board are in the box. This approach is especially helpful if your Jira boards are connected to different projects, and, for that reason, they have complex task structures.

## Switch from automatically to manually added timeboxes

If you set synchronization of timeboxes based on Jira sprints, timeboxes are created automatically.

You **cannot** create the next timeboxes manually unless you change the settings (Box configuration > Tasks > Scope definition > Timeboxes).

![image-20240214-112947.png](/cms_trial/assets/99dc7b7e-27e2-42a9-99fc-7cce3f2f4b64.png)

To switch from automatically to manually added timeboxes:

**IMPORTANT:** This action will **turn off** the synchronization of newly created Jira sprints to BigPicture, and enable the creation of iterations in the Board module.   
You can adjust synchronization settings based on the field mapping, including specific team rules. After the change, existing timeboxes will **remain unaffected** - sprints changes won't result in timebox creation/deletion.

1. Go to **Box configuration > Tasks > Scope definition > Timeboxes**.
2. Select **Manually created timeboxes**.
3. Click **Save**.

After switching from automatically to manually added timeboxes, you can create timeboxes manually from the **Scope definition** page or directly in the **Board module**. Learn more in the Manually added timeboxes section.

![image-20240214-113825.png](/cms_trial/assets/3c49cc22-4c89-4f07-86bd-0983a5949ccd.png)

## Manually added timeboxes

To start working with the Board module, you need to configure timeboxes.

### **Create first timeboxes**

To create first timeboxes manually:

[Unmapped block: nestedExpand]

### Create next timeboxes

If you already have timeboxes and want to create next timeboxes, you can:

- Create next timeboxes on the Scope definition page
- Create next timeboxes directly in the Board module

**Method 1 (Scope definition page):**

[Unmapped block: nestedExpand]

**Method 2 (the Board module):**

[Unmapped block: nestedExpand]

### Next timebox template

If you want a new subsequent timebox to have its scope definition set based on the selected timebox:

1. Enable the **Next timebox template toggle** switch.
2. Click on the **cog button** and define if the **value name convention** will be based on:

   1. **Values of this timebox** - sprint names will be generated based on the setup of this timebox
   2. **New box name** - sprint names will be generated based on the newly created box

![image-20240214-131017.png](/cms_trial/assets/782e4e7d-ead6-4e56-bd52-1fd802df0bb0.png)

## Project teams with separate sprints

If project teams have separate sprints:

1. Go to the **Scope definition** page.
2. Tick **Each team has a different mapping with value**.
3. Enter the sprint name and data for each team.
4. Click **Save.**

![image-20240214-142428.png](/cms_trial/assets/99a0d461-3c56-43a7-8b6e-89db4668c56e.png)

## Actions on timeboxes

You can perform the following actions on timeboxes (available on the **Scope definition** page and in the **Board module**):

| **Action** | **Screenshot** |
| --- | --- |
| Navigate the timeline | Use the arrows to navigate the timeline: image-20240216-083754.png |
| Zoom in/out | image-20240216-084011.png |
| Go to today’s date | image-20240216-084138.png |
| More actions   - Edit - Create timeboxes inside - Delete - Change status | Click on the **More actions** menu to:   - Edit - Create timeboxes inside (divide a selected timebox into smaller chunks, for example, if a timebox works as a program increment, you may add iterations) - Delete - Change status (Not started, In progress, Closed)  image-20240216-084257.png |

## Timeboxes (new navigation)

## About timeboxes

Timeboxes define consecutive timeframes used for work planning. In BigPicture, they represent sprints, iterations, increments, and stages.

There are two types of timeboxes:

- Automatic (timeboxes synchronized with Jira sprints)
- Manual (timeboxes added manually. The timeboxes you can add depend on the [box type settings](/cms_trial/space/SPM/1918766536/Scope+types/))

App admins can configure timebox schedules to define a reusable timebox hierarchy (e.g., Year → Quarter → PI → Iteration) and apply it across multiple boxes. See more on the [Timebox schedules](/cms_trial/space/SPM/1989214530/Timebox+schedules/) page.

![timeboxes-new-navigation.png](/cms_trial/assets/091ab20d-5e56-4817-a512-cf25a5b0817a.png)

## Set box type sequentiality

To prevent the period of consecutive timeboxes from overlapping, the box type's sequentiality should be set to **Sequential**. See the [Period mode and sequentiality](/cms_trial/space/SPM/1918669073/Period+mode+and+sequentiality/) page for more information.

[Unmapped block: nestedExpand]

## Automatic timeboxes (synced with Jira sprints)

Before you start working with the Board module, you must configure timeboxes first. Here’s a short video showing you the process.

To create timeboxes based on Jira sprints from a selected Jira board:

[Unmapped block: nestedExpand]

### Add missing sprint dates in Jira

When Jira sprints do not have dates, timeboxes **cannot** be created. In this case, you will see the message in the screenshot below.

You can fix it by adding the dates for the first Jira sprint and running the synchronization again.

![BigPicture warning that pop up when the Jira sprint dates are missing.](/cms_trial/assets/73030ac4-8dcc-415b-8e2e-fe9ef6467ee2.png)

### Use Jira boards to create automatic timeboxes

You can choose a Jira board to create timeboxes automatically. The board you choose will be then automatically added to the scope of the box.

Thanks to this, you can be sure that all the tasks from the Jira board are in the box. This approach is especially helpful if your Jira boards are connected to different projects, and, for that reason, they have complex task structures.

## Switch from automatically to manually added timeboxes

If you set synchronization of timeboxes based on Jira sprints, timeboxes are created automatically.

You **cannot** create the next timeboxes manually unless you change the settings (Box configuration > Tasks > Work items from Jira > Timeboxes).

![image-20240214-112947.png](/cms_trial/assets/99dc7b7e-27e2-42a9-99fc-7cce3f2f4b64.png)

To switch from automatically to manually added timeboxes:

**IMPORTANT:** This action will **turn off** the synchronization of newly created Jira sprints to BigPicture, and enable the creation of iterations in the Board module.   
You can adjust synchronization settings based on the field mapping, including specific team rules. After the change, existing timeboxes will **remain unaffected** - sprints changes won't result in timebox creation/deletion.

1. Go to **Box configuration > Tasks > Work items from Jira > Timeboxes**.
2. Select **Manually created timeboxes**.
3. Click **Save**.

After switching from automatically to manually added timeboxes, you can create timeboxes manually from the **Work items from Jira** page or directly in the **Board module**. Learn more in the Manually added timeboxes section.

## Manually added timeboxes

To start working with the Board module, you need to configure timeboxes.

### **Create first timeboxes**

To create first timeboxes manually:

[Unmapped block: nestedExpand]

### Create next timeboxes

If you already have timeboxes and want to create next timeboxes, you can:

- Create next timeboxes on the Work items from Jira page
- Create next timeboxes directly in the Board module

**Method 1 (Work items from Jira page):**

[Unmapped block: nestedExpand]

**Method 2 (the Board module):**

[Unmapped block: nestedExpand]

### Next timebox template

If you want a new subsequent timebox to have its scope definition set based on the selected timebox:

1. Enable the **Next timebox template toggle** switch.
2. Click on the **cog button** and define if the **value name convention** will be based on:

   1. **Values of this timebox** - sprint names will be generated based on the setup of this timebox
   2. **New box name** - sprint names will be generated based on the newly created box

![image-20240214-131017.png](/cms_trial/assets/782e4e7d-ead6-4e56-bd52-1fd802df0bb0.png)

## Project teams with separate sprints

If project teams have separate sprints:

1. Go to the **Work items from Jira** page.
2. Tick **Each team has a different mapping with value**.
3. Enter the sprint name and data for each team.
4. Click **Save.**

![image-20240214-142428.png](/cms_trial/assets/99a0d461-3c56-43a7-8b6e-89db4668c56e.png)

## Actions on timeboxes

You can perform the following actions on timeboxes (available on the **Work items from Jira** page and in the **Board module**):

| **Action** | **Screenshot** |
| --- | --- |
| Navigate the timeline | Use the arrows to navigate the timeline: image-20240216-083754.png |
| Zoom in/out | image-20240216-084011.png |
| Go to today’s date | image-20240216-084138.png |
| More actions   - Edit - Create timeboxes inside - Delete - Change status | Click on the **More actions** menu to:   - Edit - Create timeboxes inside (divide a selected timebox into smaller chunks, for example, if a timebox works as a program increment, you may add iterations) - Delete - Change status (Not started, In progress, Closed)  image-20240216-084257.png |