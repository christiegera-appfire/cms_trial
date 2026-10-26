# SLA Duration field

The **SLA Duration** custom field stores the calculated duration of selected Time to SLA metrics directly inside a Jira work item.

## How to create an SLA Duration field

1. Go to **Apps** > **Time to SLA** > **Administration** > **SLA Fields**.
2. Click the **SLA field** button.
3. Select **TTS -** **SLA Duration**.
4. Enter a name.
5. Optionally, provide a description.
6. **SLA sources –** Choose which SLAs this field should monitor.
7. Click **Create**.

## After creating the field

To make the SLA field visible in work items, ensure that:

- It is in scope for the correct project and work item type
- It is added to the relevant screens
- It is included in the work item layout

For detailed steps, refer to Atlassian’s documentation on [creating](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/) and [managing fields and screens](https://support.atlassian.com/jira-cloud-administration/docs/find-your-custom-fields/).

## Search SLA Duration fields using JQL

SLA Duration fields support Jira Query Language (JQL) searches using stored SLA values. Searchable values include SLA state, goal type, goal duration, remaining duration, start date, elapsed duration, elapsed duration percentage, target date, breached status, after-hours information, paused duration, finish date, and breached duration.

Use these values to filter work items by SLA progress and deadlines in Jira searches, saved filters, and dashboards. For example, you can build a filter for work items whose SLA has breached or whose remaining duration is within your team's escalation threshold.

The available query values depend on the field's indexing and search support. Use Jira's JQL suggestions to select the supported properties and operators for your SLA Duration field.

## How it appears in work items

After you create the SLA Duration field and configure Jira, it won’t automatically be applied to all existing work items. For the custom field to attach to a work item, calculate its SLA value, and become visible in the work item navigator, dashboards, queues, or gadgets, **the work item must be opened at least once**.

The field becomes populated **only** **after** the work item is viewed.

**Why does this happen?**

Jira custom fields are calculated and stored when a work item is accessed. They do not automatically recalculate in the background for all existing work items. Once the work item is opened:

- Time to SLA calculates the SLA value.
- The custom field is updated.

This behavior is expected and cannot be disabled.

Once properly configured and opened at least once, the SLA Duration field appears as a standard date field in the work item view.

- For each selected SLA, the field shows:

  - The SLA name
  - For each selected SLA, the field shows:

    - The SLA name
    - The duration value, depending on the SLA configuration and status

The value shown in the field follows these rules:

- Standard SLAs (with goals):

  - **Before breach:** Displays the remaining duration until the SLA target is reached. The duration is formatted as: `Xd Xh Xm Xs` (days, hours, minutes, seconds).
  - **After breach**: Displays the overdue duration as a negative value, indicating how much time has passed since the breach.
- SLAs without goals or with **No goal** target:

  - Displays a hyphen (-), because no target duration is defined.