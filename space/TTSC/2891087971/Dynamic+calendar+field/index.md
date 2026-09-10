# Dynamic calendar field

The **TTS – Dynamic calendar** custom field lets you select a goal calendar directly from a Jira work item.

Instead of assigning a fixed calendar inside the SLA configuration, you can let users dynamically define which calendar should apply to a specific work item.

## Use cases

Use **Dynamic calendar** when:

- Your teams operate in different time zones
- Different customers require different working-hour definitions
- You want flexibility without duplicating SLA goals

By allowing calendar selection directly from the work item, you can manage complex SLA requirements with a cleaner and more scalable configuration.

## How it works

When the [**Select calendar via Jira issue**](/cms_trial/space/TTSC/35390901/SLA+goals/) [option](/cms_trial/space/TTSC/35390901/SLA+goals/) is enabled in an SLA goal:

- Time to SLA reads the calendar value from the **TTS – Dynamic Calendar** field.
- The selected calendar is used to calculate the SLA for that specific work item.
- Each work item can therefore follow a different working schedule.

## Step 1: Create a Dynamic Calendar field

1. Go to **Apps** > **Time to SLA** > **Administration** > **SLA Fields**.
2. Click the **SLA field** button.
3. Select **TTS -** **SLA Dynamic Calendar**.

   ![Time to SLA Dynamic calendar field setup panel](/cms_trial/assets/da931de6-f5d4-41f4-a9c1-74f6ebb89764.png)
4. Enter a name.
5. Optionally, provide a description.
6. Click **Create**.

## Step 2: Enable calendar selection in your SLA

After adding the field:

1. Open your SLA configuration.
2. In the goal settings, enable **Select calendar via Jira issue**.

For full goal configuration details, see the [SLA goals](/cms_trial/space/TTSC/35390901/SLA+goals/) documentation.

Time to SLA will then use the calendar selected in the work item field instead of the static calendar defined in the goal.

## How it appears in work items

After you create the SLA Dynamic calendar field and configure Jira, it won’t automatically be applied to all existing work items. For the custom field to attach to a work item, calculate its SLA value, and become visible in the work item navigator, dashboards, queues, or gadgets, **the work item must be opened at least once**.

The field becomes populated **only** **after** the work item is viewed.

**Why does this happen?**

Jira custom fields are calculated and stored when a work item is accessed. They do not automatically recalculate in the background for all existing work items. Once the work item is opened:

- Time to SLA calculates the SLA date.
- The custom field is updated.
- The update appears in the work item history (However, custom field value changes do not appear in the Jira work item history).

This behavior is expected and cannot be disabled.

Once properly configured and opened at least once, the SLA Dynamic calendar field appears as a standard date field in the work item view.

![Time to SLA Dynamic calendar field configuration with date options](/cms_trial/assets/2260e015-c57d-4bbe-8cba-a9dc20c400ea.png)