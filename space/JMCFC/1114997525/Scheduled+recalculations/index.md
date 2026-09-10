# Scheduled recalculations

In general, JMCF custom fields will recalculate when you open an issue view that includes the custom field; additionally, a [Scripted Field](https://appfire.atlassian.net/wiki/spaces/MCFCS/pages/713588743) will recalculate when its dependent fields are updated. In some circumstances, however, it may be advisable to schedule a custom field to recalculate on an interval. These scenarios can include (but are not limited to):

- Jira instances with a very large number of issues, where recalculation of fields can take longer
- “Mission critical” fields that are required for workflow and need to be as fresh as possible
- Custom fields that need to be updated when a triggering event is not available, or
- When multiple events must complete prior to the recalculation

In all of the above scenarios, scheduling a recalculation of JMCF custom fields can supplement automatic recalculations or can be scheduled to suit your organizations processes and procedures. For example, running the recalculation of a custom field on a very large number of issues can be done overnight (during off-hours) so that the custom field values are ready for the following day.

## Scheduling a recalculation

You need to create a custom field before it can be scheduled for recalculation. Once you have your custom field configured and have verified that it returns the expected data, follow these steps:

1. In the upper right corner of Jira, click **Settings** ( ⚙️ ) and select **Apps**.
2. In the left-hand sidebar, click **Jira Misc Custom Fields**.
3. Click **My custom fields**.
4. Click the **Action button** ( [png icon] ) to the right of the custom field you want to schedule. Select **Schedule Recalculation**.
5. The **Schedule calculation** window will open (Figure 1, right).
6. From the pulldown menu, select the primary interval (e.g. **hour**, **day**, or **week**).
7. Configure any other options for your schedule. See **Interval options**, below, for more information.
8. Click **Confirm**.

**Note**: If you select a specific hour for your recalculation, it may not start exactly at the time selected; it will begin within an hour of the scheduled time.

Full recalculation times will vary, depending on the number of issues that need to be updated and the level of activity, both on your Jira instance and on the JMCF servers.

## Interval options

Calculations can not be scheduled to start at an exact time; rather, they are scheduled to start within an hour of the selected time. Further, it is highly recommended to test your recalculation schedules to verify that they complete before the next scheduled interval (e.g. the recalculation completes within an hour when **Every day at every hour** is the scheduled interval). If a recalculation is still running when its next scheduled recalculation is set to start, that scheduled recalculation will be skipped.

When setting your schedules, hold Ctrl (PC)/Command (Mac) and click to select multiple values within a menu (e.g. hold Ctrl/Command and click **monday**, **wednesday**, **friday** to set your schedule to run on those three days).

The interval options are:

- **Every hour** - The recalculation will run every 60 minutes (approximately) of every day of the week.
- **Every day** - The recalculation will run every day at the selected interval:

  - **every hour** - The recalculation will run every 60 minutes (approximately).
  - a selected **hour or hours** - The recalculation will run within 60 minutes of the selected hour(s).
  - in the selected **time zone** - By default, all schedules are set using UTC. You can select an offset to schedule using your time zone.
- **Every week** - The recalculation will run every week at the selected interval:

  - **every day of the week** or
  - a selected **day or days**
  - at the selected **hour or hours**
  - in the selected **time zone**

You are viewing the documentation for **Jira Cloud**.

| On This Page |
| --- |

![Jira Misc Custom Fields (JMCF) Cloud schedule calculation button](/cms_trial/assets/641b4f81-4324-4685-b865-4a9123b2c494.png)