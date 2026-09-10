# Create calendars

Time to SLA offers advanced calendar customization, allowing you to create an unlimited number of calendars and time intervals.

With Time to SLA, you can:

- Define multiple business-hour intervals within a single workday
- Create separate calendars for teams working in different time zones
- Add holidays (recurring or one-time)
- Define exceptions for work outside standard business hours
- Share holidays and exceptions across calendars

## Calendar management

The *Calendars* page shows all calendars configured in your instance and lets you manage them.

![Calendars page showing configured calendars, time zones, calendar details, and action icons to view, edit, or delete.](/cms_trial/assets/baa16d36-cf87-414b-b4e1-019cfdd1b97c.png)

This section explains the key elements of the **Calendars** page:

1. **Name –** Displays the name of your calendar.
2. **Time Zone –** Displays the time zone selected for the calendar. Time to SLA uses Daylight Saving Time (DST) for calculations.
3. **Calendar Detail –** Provides a summary of the calendar’s settings.

Available actions:

1. **Add New Calendar –** Click to add a new calendar.
2. **Eye** **icon –** See the details of a calendar.
3. **Pencil icon –** Click to edit an existing calendar.
4. **Trash can icon –** Delete a calendar (irreversible). Calendars assigned to SLAs can’t be deleted.

## How to create a calendar

1. In Jira, open **Apps** > **Time to SLA**.
2. Go to **Calendars** > **Add New Calendar**.
3. Configure your calendar:

   - Name your calendar.
   - Select a **Time Zone**.
   - Define business hours, holidays, and exceptions.

### Business hours

In this tab, you can define your standard working time:

![Calendar configuration screen with Business hours tab, working days grid, working hours dropdown, and Break time option.](/cms_trial/assets/52f753df-e712-4d79-b60a-e70f6bf00a33.png)

1. **Set working days**

   - Use **Select working days** dropdown to choose which days are working days.
   - In the weekly grid, confirm the correct days are selected (checked).
2. **Set working hours**

   - Use **Select working hours** dropdown to select from pre-defined working hours.
   - The working-hour blocks appear in the grid under each day.
3. **Add break times (optional)**

   - Click **+ Break Time** to add the break period to the selected days.
   - You can add multiple break times (each break appears as a separate block in the grid).

### Holidays

In the **Holidays** tab, you can add holidays to the calendar:

1. Open the **Holidays** tab. You can add holidays as full-day events or specify custom hours. On the specified holidays, SLAs will stop counting.

   ![Add holiday dialog with date picker, custom hours option, and time range fields for defining holiday duration.](/cms_trial/assets/e556870e-cd31-41ef-980a-767b869ac930.png)
   - Tick the **Shared holiday** box to apply the holiday to all calendars. Changes will reflect across all shared calendars (for example, use it for New Year’s Day but not for region-specific holidays like Bastille Day).
   - Tick the **Recurring** box if you want the holiday to repeat within a certain timeframe (monthly or yearly).
2. Click **Add holiday.** After adding the holidays, the holidays that apply to the calendar will be displayed on the calendar as follows:

   ![Holidays tab listing shared and recurring holidays with start date, end date, and action options.](/cms_trial/assets/8de93c23-b404-4e97-8989-bfe342db4fd6.png)

   You can also use this section to delete holidays and change whether they are Shared and/or Recurring.

### Exceptions

Use the **Exceptions** tab to define additional working hours outside your regular business hours, such as planned overtime or special support coverage. Exceptions can be one-time or recurring and shared across calendars.

<https://app.arcade.software/share/CGivQ7jtrGKLGg9281IV>

1. Open the **Exceptions** tab.

   ![Exceptions tab with fields to define exception name, date, working hours, break times, and sharing options.](/cms_trial/assets/67bc8a3e-89b9-4a85-a829-3e933a34f0ee.png)
2. Enter an **Exception name**.
3. Select an **Exception date**, and define the working time for that day:

   - **From** – start time
   - **To** – end time
4. (Optional) Click **Break time** to add one or more non-working periods within the exception.

   - SLA calculation pauses during break times, even if the exception is active. You can add multiple break times.
5. (Optional) Configure sharing and recurrence:

   - **Apply exceptions to all calendars**  
     Shares the exception across all calendars.
   - **Repeat exceptions**  
     Repeats the exception monthly or yearly. When it’s enabled:

     - **Monthly exceptions**

       - If an exception is set on a date that doesn’t exist in a shorter month (for example, the 31st), it moves to the last day of that month.
     - **Yearly exceptions**

       - Repeats every 365 days.
6. Click **Add exception**.

This adds the exception to the **Exceptions within this calendar** list, where you can review and manage it.

Additionally, you can use the **SLA calculation behavior on exceptions** setting to control what happens when an exception and a holiday occur on the same date. This behavior is configured per calendar. To learn more about this feature and see example use cases, please refer to [this page](/cms_trial/space/TTSC/2824765517/I+want+to+track+SLAs+during+planned+work+outside+business+hours/).

- **Exceptions will override holidays**  
  SLAs will count during the exception hours.
- **Holidays will remain unchanged by exceptions**  
  SLAs will not count, even if an exception exists.

When an SLA is calculated during an exception, an indicator appears in the SLA panel to show that the SLA is running under an exception.

![SLA panel showing active SLA, elapsed and remaining time, and indicator that SLA is running under an exception.](/cms_trial/assets/a73bf1fc-2a02-4de1-a9b9-9e3b7b4afbbe.png)

This helps agents understand why an SLA is progressing outside normal business hours.

If your team uses exceptions, ensure agents are aware of this behavior to avoid confusion.

**How overlapping exceptions are handled**

You can add multiple exceptions on the same day. This can happen, for example, when a recurring exception overlaps with a one-time exception, or a shared exception overlaps with a calendar-specific exception.

When multiple exceptions exist on the same date, Time to SLA merges them automatically. The calculation follows this order:

1. **All exception working hours are merged**
2. **Break times are applied and subtracted from the merged working hours**

**Example**

Exceptions on the same day:

- **12:00–14:00**, no breaks
- **13:00–15:00**, with a break from **13:30–14:00**

**Resulting working time:**

- **12:00–13:30**
- **14:00–15:00**

In this case, the exception hours are merged first, and then the break time is removed from the combined interval. This ensures SLA calculations remain consistent, even when multiple exceptions overlap.

### Advanced

Under this tab, you can define the **Length of Business Day**. Keep in mind that this is an advanced feature. If you’re unsure about your use case, use the default format.

![Advanced tab showing Length of Business Day setting with default and custom duration options.](/cms_trial/assets/756dd81f-9bba-423b-a5f8-3317cf5d33a9.png)

By default, Time to SLA calculates the length of a business day from your calendar and uses this information to format SLA durations, such as remaining time and overdue. However, if you want the dedicated work time to differ from your actual working hours, you can define a custom duration. The new duration will be equivalent to 1 day. Refer to [this page](/cms_trial/space/TTSC/35881031/FAQ%3A+Calendars/) for an example.

Don’t forget to click **Save** to save your configuration.

## Next steps

[**Define SLAs**](/cms_trial/space/TTSC/35651691/Define+SLAs/)