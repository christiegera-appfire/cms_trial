# Create calendars

Calendars define when Time to SLA counts working time. You can configure working hours, holidays, and exceptions to match your team's schedule and ensure accurate SLA calculations.

With Time to SLA, you can:

- Define multiple working intervals within a single day.
- Create calendars for teams in different time zones.
- Add one-time or recurring holidays.
- Configure additional working hours outside regular business hours.
- Share holidays and exceptions across calendars.
- Control how exceptions affect SLA calculations on holidays.

## Calendar management

The *Calendars* page displays the calendars configured in your Jira instance. From this page, you can create, view, edit, and delete calendars.

The calendar list contains the following information:

- **Name:** Displays the calendar name.
- **Time Zone:** Displays the time zone configured for the calendar. Time to SLA accounts for daylight saving time when calculating working hours.
- **Calendar Detail:** Displays the calendar's working days and hours.
- **Holidays:** Lists the holidays configured for the calendar.
- **Exceptions:** Lists the exceptions associated with the calendar, including shared exceptions.

Available actions:

- **Add New Calendar:** Create a calendar.
- **View:** Open a calendar to review its configuration.
- **Edit:** Modify an existing calendar.
- **Delete:** Permanently delete a calendar. You can't delete calendars that are assigned to SLAs.

## How to create a calendar

1. In Jira, open **Apps** > **Time to SLA**.
2. Go to **Calendars** > **Add New Calendar**.
3. Select a **Time Zone**. Time to SLA uses this time zone to calculate working hours, holidays, and exceptions.
4. Configure the calendar using the **Business Hours**, **Holidays**, and **Exceptions** tabs.
5. Click **Save**.

### Business hours

Use the *Business Hours* tab to define the days and hours during which SLAs count working time.

![Calendar configuration screen with Business hours tab, working days grid, working hours dropdown, and Break time option.](/cms_trial/assets/52f753df-e712-4d79-b60a-e70f6bf00a33.png)

**Set working days**

1. Open the *Business Hours* tab.
2. Use **Select working days** to choose a working-day preset.
3. Review the weekly grid and adjust the selected days as needed.

**Set working hours**

1. Use **Select working hours** dropdown to select from pre-defined working hours.
2. The working-hour blocks appear in the grid under each day.

You can configure multiple working intervals within the same day.

**Add break times (optional)**

Break times define periods when SLA time doesn't count during an otherwise active working day.

1. Click **+ Break Time** to add the break period to the selected days.

   - You can add multiple break times (each break appears as a separate block in the grid).

For example, if your team works from 9:00 AM to 5:00 PM and takes a lunch break from 12:00 PM to 1:00 PM, you can exclude that hour from SLA calculations.

### Holidays

Use the *Holidays* tab to define dates or periods when regular working hours don't apply.

You can configure holidays as whole-day or partial-day events and set them to recur monthly or yearly.

1. Open the *Holidays* tab.
2. Enter a name for the holiday.
3. Select the holiday date or date range.

   ![Add holiday dialog with date picker, custom hours option, and time range fields for defining holiday duration.](/cms_trial/assets/e556870e-cd31-41ef-980a-767b869ac930.png)
4. Choose the holiday type:

   - **Whole day:** Excludes the entire day from working time.
   - **Half day:** Excludes the specified hours from working time.
5. Configure the following options as needed:

   - **Shared holiday:** Makes the holiday available across all calendars. For example, use shared holidays for company-wide closures and calendar-specific holidays for regional events.
   - **Recurring:** Repeats the holiday monthly or yearly.
6. Click **Add holiday**.

The holiday appears in the calendar's holiday list. You can review and manage existing holidays from this list. Shared holidays apply across calendars, so changes to shared holiday configurations can affect SLA calculations in multiple calendars.

![Holidays tab listing shared and recurring holidays with start date, end date, and action options.](/cms_trial/assets/8de93c23-b404-4e97-8989-bfe342db4fd6.png)

### Exceptions

Exceptions let you define additional working hours outside your calendar's regular business hours.

For example, if your support team normally works Monday through Friday, you can add an exception for planned Saturday coverage.

Exceptions can be one-time or recurring, and you can share them across calendars.

<https://app.arcade.software/share/CGivQ7jtrGKLGg9281IV>

1. Open the **Exceptions** tab.

   ![Exceptions tab with fields to define exception name, date, working hours, break times, and sharing options.](/cms_trial/assets/67bc8a3e-89b9-4a85-a829-3e933a34f0ee.png)
2. Enter an **Exception name**.
3. Define the exception's working hours:

   - **From:** The start of the exception interval.
   - **To:** The end of the exception interval.
4. (Optional) Click **Break time** to add periods when SLA time shouldn't count within the exception. You can add multiple breaks.
5. (Optional) Configure the following settings:

   - **Apply exceptions to all calendars:** Share the exception across all calendars.
   - **Repeat exceptions:** Repeat the exception monthly or yearly.
6. Click **Add exception**.

The exception appears in the **Exceptions within this calendar** list, where you can review and manage it.

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

### Configure advanced calendar settings

Expand the **Advanced** section to customize how Time to SLA interprets the length of a business day.

![Advanced tab showing Length of Business Day setting with default and custom duration options.](/cms_trial/assets/756dd81f-9bba-423b-a5f8-3317cf5d33a9.png)

By default, Time to SLA calculates the length of a business day from your calendar and uses this information to format SLA durations, such as remaining time and overdue. However, if you want the dedicated work time to differ from your actual working hours, you can define a custom duration. The new duration will be equivalent to 1 day. Refer to [this page](/cms_trial/space/TTSC/35881031/FAQ%3A+Calendars/) for an example.

Don’t forget to click **Save** to save your configuration.

## Next steps

After creating your calendar, you can assign it to an SLA to define when the SLA counts working time.

- [Define SLAs](/cms_trial/space/TTSC/35651691/Define+SLAs/)