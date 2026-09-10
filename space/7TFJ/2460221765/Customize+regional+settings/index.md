# Customize regional settings

![TryItButton (2).png](/cms_trial/assets/fd4a733c-38c8-466d-a8da-086cb3530fc1.png)

7pace Timetracker is integrated with your Jira instance, so regional settings are inherited from Jira.

## Select the first day of the week

The first day of the week in 7pace Timetracker can be either Monday or Sunday, depending on the respective Jira settings. To change the first day of the week in 7pace, please update the corresponding settings in Jira.

### How to set the first day of the week in Jira?

Please follow the [official Jira instructions](https://support.atlassian.com/jira/kb/how-to-set-monday-as-first-day-of-week-in-date-picker-calendar/) (marked for Data Center, but applicable to Cloud as well).

Go to the System settings:

![image-20251016-161613.png](/cms_trial/assets/ea7563b0-33c0-4358-ab3a-80b93b29df47.png)

Navigate to the ‘Look and feel’ section and select the desired value in ‘Use ISO8601 standard in Date Picker’.

| **Value** | **First day of week** |
| --- | --- |
| Yes | Monday |
| No | Sunday |

![image-20251016-161752.png](/cms_trial/assets/81c8fbbe-fd45-43ba-8ae6-5640b5c00f7b.png)

### How is it reflected in 7pace?

After you change the setting in Jira, it is automatically reflected in 7pace. If you don’t see the first day of the week changed, please refresh the page.

The first day of the week is reflected in various views – Monthly, Weekly, Timesheet.

For example, with the ISO8601 setting set to ‘No’ in Jira, 7pace will display Sunday as the first day of the week.

![image-20251016-162207.png](/cms_trial/assets/371d2640-9dcc-4338-a68b-6e4dca4ad8bb.png)

The first day of the week is also reflected in the date pickers in 7pace, too. The example below shows the ‘Add time’ dialogue date picker when the Jira ISO8601 value is set to ‘Yes’ – Monday is used as the first day of the week in 7pace.

![image-20251016-162611.png](/cms_trial/assets/8257e2e7-94ad-4bbf-9883-47f1d51132f4.png)