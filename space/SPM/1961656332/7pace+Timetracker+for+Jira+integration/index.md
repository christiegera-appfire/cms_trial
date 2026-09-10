# 7pace Timetracker for Jira integration

## Integration overview

[7pace Timetracker for Jira](https://appfire.atlassian.net/wiki/spaces/7TFJ) is a streamlined, intuitive time-tracking app for recording, managing, and reporting time. Designed to support managers and individual contributors, it simplifies time-tracking tasks across the board. In BigPicture, you can define resource capacity based on workload plans and non-working days resulting from holiday plans and individual absences.

### Track time by custom fields or individuals

Add 7pace Timetracker columns to the Gantt and Scope column views. You can add the following fields:

- Custom fields from 7pace
- People

And then view the time spent on projects, categorized by either option.

Each column will display the time logged with a selected custom field value, for example, billable hours or time logged by a specific person. If two people worked on a task, you can add a column for each person to see how the logged time was distributed among them.

![image-20250415-065936.png](/cms_trial/assets/3e97788b-de14-4d3c-abcf-13551ecb46d7.png)

Once you click **7pace Timetracker columns**, you’ll see the window with the following elements:

- **List of added 7pace columns** - you can add one column multiple times, enabling different aggregations. To remove a column, click the **X** icon next to it.
- **Filter by custom fields** - use it to narrow down the list of available columns on the left.
- **List of columns available for selection** - the selected columns have a counter displaying how many times a column is added.
- **Seach box** - start typing to find a column by name.
- **Recently used** - click to see the recently used columns.

![image-20250416-085003.png](/cms_trial/assets/02c5c9d6-133b-40b5-acdc-96862640f012.png)

### Compare the time spent vs. person capacity

Compare the time spent vs. person capacity on the [7pace Timetracker’s Times Explorer](https://appfire.atlassian.net/wiki/spaces/7TFJ/pages/1924595956) and quickly understand if team members are below, at, or over capacity.

#### Access

The capacity badges are visible to users with BigPicture’s **Resource Administrator** or **App admin** role.

![With BigPicture integration active, you can view individual capacity in the Times Explorer.](/cms_trial/assets/18da2f45-3032-44f0-8103-c815fcb5cd81.png)

### Full integration

To get the most across both apps, enable the integration in 7pace Timetracker and BigPicture.

The process is described in detail in the *Step-by-step integration process* section below.

### Partial integration

When integration is enabled only in BigPicture and disabled in 7pace Timetracker, data flows one way, from 7pace Timetracker to BigPicture. You won’t be able to use BigPicture data in 7pace Timetracker.

Conversely, if integration is enabled in 7pace Timetracker but disabled in BigPicture, you can use BigPicture data in 7pace Timetracker, but you won’t be able to add 7pace Timetracker columns to the Gantt and Scope modules in BigPicture.

## Integration functionality

In *Times Explorer*, the icons at the top of the page indicate that 7pace Timetracker displays individual capacity from BigPicture.

You can quickly view cumulative time tracking data along with an individual’s capacity:

- on track (logged time in 7pace = capacity in BigPicture)
- above capacity (logged time in 7pace > capacity in BigPicture)
- below capacity (logged time in 7 pace < capacity in BigPicture)

![View individual capacity in the Times Explorer.](/cms_trial/assets/aa46cf6c-2086-4222-84aa-441d3eaf1b18.png)

### Person capacity view

#### Private views

Once the integration is enabled, a new **Person capacity** view will be available in *Times Explorer*.

![image-20250424-075851.png](/cms_trial/assets/76b44e34-6734-453b-a289-33f4b510d9a8.png)

This view can’t be removed. However, the view can be modified and saved as a new layout.

![image-20250424-080309.png](/cms_trial/assets/5e36ef0a-c111-4f75-ba6c-ad0f80d687fc.png)

#### Group by

Use the **Group by** feature to group data by person.

![image-20250424-080520.png](/cms_trial/assets/b611fbe5-407d-44d7-9906-7f7dbcb218ab.png)

## Step-by-step integration process

### I don’t have 7pace Timetracker for Jira installed

If you don’t have 7pace Timetracker for Jira installed, start with the instructions below from the beginning.

### I have 7pace Timetracker for Jira installed

If you already have 7pace Timetracker for Jira installed, skip to step 8 below.

1. Go to **BigPicture App Configuration** > **Integrations**  > **7pace Timetracker**.

   ![image-20250414-131326.png](/cms_trial/assets/98b50417-e13f-401f-8467-89257d55986f.png)
2. Click **Try 7pace for free**. You’ll be redirected to the Atlassian Marketplace page.

   ![image-20250414-131540.png](/cms_trial/assets/4187b16c-2f3e-4306-b9bc-1369997b04d0.png)
3. Click **Try it free** in the top-right corner.
4. Select a site where 7pace Timetracker for Jira will be installed.

   ![image-20250414-131843.png](/cms_trial/assets/db31493a-c99f-47af-993f-9e127d1b054e.png)
5. To confirm, click **Start free trial**. You’ll be moved to your Jira apps.
6. Confirm again by clicking **Start free trial**.

   ![image-20250414-132115.png](/cms_trial/assets/41999e29-2e8f-4ec7-a30d-b7f0622b71d6.png)
7. Once the app is added to your Jira, you’ll see the following message in the bottom-left corner.

   ![image-20250414-132332.png](/cms_trial/assets/ce381eb4-a73b-4f09-8d04-788cd96160a6.png)
8. When you open 7pace Timetracker, you’ll see the message that BigPicture is ready to integrate.

   ![image-20250414-132614.png](/cms_trial/assets/954fda7c-3943-4eb5-9d29-fa96dfba284c.png)
9. Click **Go to Integrations**.
10. To enable the BigPicture integration, click **Enable integration**.

    ![image-20250414-132914.png](/cms_trial/assets/7b2997b3-ef95-4091-b622-1505580aa07a.png)
11. If you want to view Time Spent in the Gantt, Scope, and Board modules, enable the integration on the BigPicture side as well.
12. Go to **BigPicture App Configuration** > **Integrations**  > **7pace Timetracker**.
13. Turn on the **Enable 7pace Timetracker integration** toggle switch and click **Save**.

By enabling this integration, you acknowledge and confirm that your 7pace Timetracker data will be stored in the EU.

![image-20250414-133947.png](/cms_trial/assets/b3fb27c2-5d1f-4b00-b90c-db463479c48c.png)

1. That’s all! The integration is now bi-directional.

## Disable integration

To disable the integration in 7pace Timetracker:

1. Go to **7pace Timetracker Settings** > **Integrations**.
2. Find BigPicture.
3. Click **Disable integration**.

   ![image-20250414-082125.png](/cms_trial/assets/791ab576-3e8a-417d-9738-383f4ecc640d.png)

To disable the integration in BigPicture:

1. Go to **BigPicture App Configuration** > **Integrations**  > **7pace Timetracker**.
2. Turn off the **Enable 7pace Timetracker integration** toggle switch and click **Save**.

   ![image-20250415-070732.png](/cms_trial/assets/7610c43b-bac4-49e0-80f8-5aba6516cb5a.png)