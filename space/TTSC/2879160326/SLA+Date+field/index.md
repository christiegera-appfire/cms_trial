# SLA Date field

The SLA Date field stores a selected SLA date inside a Jira custom field.

You can configure it to store:

- SLA target date
- SLA start date
- SLA end date

The field behaves like a standard Jira date field and can be used in JQL, dashboards, reports, and automations.

## Use cases

Because the SLA Date field is a Jira custom field, you can use it anywhere Jira date fields are supported.

For example, you can:

- Add it as a column in the work item navigator.
- Filter work items using JQL (for example, overdue target dates).
- Display it in dashboards and gadgets.
- Use it in queues and reports.
- Trigger automation rules based on SLA deadlines.

This allows teams to track SLA milestones without opening individual work items.

For example, you configure the field to store the **SLA target date** and choose **Earliest date** (explained below) as the selection logic. Then, you:

- Add the field as a column in your queue, and
- Sort the queue by that field.

This lets you prioritize work items with the closest upcoming SLA deadlines. Selection logic directly affects how this prioritization works.

---

## How to create an SLA Date field

1. Go to **Apps** > **Time to SLA** > **Administration** > **SLA Fields**.
2. Click the **SLA field** button.
3. Select **TTS -** **SLA Date**.

   ![Create an SLA field dialog showing SLA field type with TTS - SLA Date selected, Name, Description, SLA sources, Display value, and Selection logic.](/cms_trial/assets/fdbea2d4-9fb7-47e5-b826-c69c85d6656e.png)
4. Enter a name.
5. Optionally, provide a description.
6. **SLA sources** **–** Choose which SLAs this field should monitor. You can select:

   - **ALL SLAs**, or
   - Individual SLAs available in your instance (select them one by one)

   If no SLA is assigned, the field will not calculate or display any values.
7. **Display** **value –** Choose which date should be stored in the field:

   - SLA target date
   - SLA start date
   - SLA end date

These dates in the SLA panel will appear in the SLA field:

![SLA panel displaying time to resolution with the start date, target date, and end date indicated..](/cms_trial/assets/1ae50aad-7557-4b78-87e9-8148b73218dc.png)

**1 - Start date**

**2 - Target date**

**3 - End date**

1. **Selection logic –** If multiple SLAs apply to the same work item, select whether the field should store:

   - The earliest date
   - The latest date

   This determines which value is written to the custom field.

**Example:**

A work item matches two SLAs with different target dates:

- SLA A → Target date: March 10
- SLA B → Target date: March 15

If you select:

- **Earliest date** → The field stores March 10
- **Latest date** → The field stores March 15

If you use this field in a queue and sort by it, the selection logic directly affects which work items appear first.

1. Click **Create**.

## After creating the field

To make the SLA field visible in work items, ensure that:

- It is in scope for the correct project and work item type.
- It is added to the relevant screens.
- It is included in the work item layout.

For detailed steps, refer to Atlassian’s documentation on [creating](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/) and [managing fields and screens](https://support.atlassian.com/jira-cloud-administration/docs/find-your-custom-fields/).

## How it appears in work items

After you create the SLA Date field and configure Jira, it won’t automatically be applied to all existing work items. For the custom field to attach to a work item, calculate its SLA value, and become visible in the work item navigator, dashboards, queues, or gadgets, **the work item must be opened at least once**.

The field becomes populated **only** **after** the work item is viewed.

**Why does this happen?**

Jira custom fields are calculated and stored when a work item is accessed. They do not automatically recalculate in the background for all existing work items. Once the work item is opened:

- Time to SLA calculates the SLA date.
- The custom field is updated.
- Custom field value changes do not appear in the Jira work item history even if it's updated.

This behavior is expected and cannot be disabled.

Once properly configured and opened at least once, the SLA Date field appears as a standard date field in the work item view.

In the work item view, you see:

- The SLA name, and
- The related date (start, target, or end).

  ![Work item view showing QA target latest and QA target earliest fields shown in the Details section.](/cms_trial/assets/a764ba4f-89c4-4851-a77d-4c6c27e1ffa8.png)

However, in other Jira views, such as work item navigator, queues, or gadgets, you only see the stored date value. The SLA name is not displayed, because the SLA Date field is a standard Jira date field and only stores the selected date value.

This means that outside the work item view, the field displays only the time data, not which SLA it belongs to.

If you need to distinguish between multiple SLAs, consider creating separate SLA Date fields for each SLA.

## Using the SLA Date field in JQL search

SLA Date fields can be used in Jira Query Language (JQL) to filter work items based on SLA timing values, such as:

- Start date/time
- Target date/time
- End date/time

This enables time-based reporting, tracking, and filtering directly from the work item navigator, boards, dashboards, and saved filters.

### Example: Filtering by SLA start date

You can filter work items where an SLA timer started on or after a specific date. For example:

```text
tts-start >= 2026-02-12
```

The work item navigator shows results like in the screenshot below, where `tts-start` is displayed as a column, and the filter returns all work items with an SLA start after the given date:

![Work item navigator displaying JQL search results for tts-start after date entry and the filtered list of work items.](/cms_trial/assets/f28e28dc-ab3e-4301-b5f3-7e09f2cdb7bf.png)

## Troubleshooting

### Why is my SLA Date field empty?

The field may appear empty if:

- You’ve created the custom field through the Jira fields settings and haven’t completed the SLA field configuration.
- The SLA hasn’t started running for the work item.

### Why can’t I see the SLA field even though I created it?

If the field does not appear, use Jira’s **Find your field** option from the work item view to identify the missing configuration.

### I see a spinner for a long time when opening the SLA Fields page. Why?

This is due to Atlassian Cloud platform limitations. The more custom fields your Jira instance has, the longer it may take to load the **SLA Fields** page. This happens because Time to SLA retrieves and displays up-to-date custom field data every time the page is opened.