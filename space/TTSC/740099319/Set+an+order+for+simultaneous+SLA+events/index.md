# Set an order for simultaneous SLA events

This feature lets you control the order in which simultaneous SLA events are handled, applying to scenarios where multiple SLA conditions are met simultaneously. Previously, these events were handled randomly. Now, you can define the order of execution using the **Default Event Order** feature.

This feature significantly impacts the calculation logic of your SLA, so it's crucial to understand your business requirements before making changes.

You must use recalculation for this to take effect on your old SLAs.

## How to configure the default event order

1. Navigate to **Settings** > **Advanced**.
2. Locate the **Default Event Order** option.
3. Use the drag-and-drop functionality to arrange the events in the order you want.

   ![Time to SLA Advanced Settings page with Default Event Order drag-and-drop list](/cms_trial/assets/2fd9fd80-bbad-4221-bcbf-804c91ea0411.png)
4. Click **Save** to apply the changes.

This default order will be applied to all SLAs in your environment unless overridden.

## How to override the default order for specific SLAs

If you'd like to set a different order to the simultaneous events per SLA, follow these steps:

1. Go to the configuration of the specific SLA you want to modify.
2. Click **Edit**.
3. Scroll down and click **Event Order**.
4. Enable the **Override Default Event Order** option.

   ![Time to SLA SLA configuration with Override Default Event Order toggle enabled](/cms_trial/assets/1f779713-6462-459d-a4e2-da5bd079811c.png)
5. Use the drag-and-drop functionality to reorder the events for this specific SLA.
6. Click **Save** to apply the changes.

### Example

Let's look at an example to illustrate how this feature works. Consider an SLA with the following configuration:

| **Condition** | **Value** |
| --- | --- |
| Start | Status **is changed to** TO DO |
| End | Status **is changed to** DONE |
| Reset | Status **is changed from** IN PROGRESS |

In a scenario where the `Status is changed to DONE` and `Status is changed from IN PROGRESS` conditions occur simultaneously, the default order might be `Start > Resume > Pause > Stop > Reset`. This default order would prioritize the `Stop` condition over the `Reset` condition.

To modify this behavior, you can edit the SLA and reorder the events. For example, changing the order to `Start > Resume > Pause > Reset > Stop` would prioritize the `Reset` condition over the `Stop` condition.

![Time to SLA event order showing Start, Resume, Pause, Stop, Reset sequence](/cms_trial/assets/fbb5aab9-2989-4f8c-b76b-8acf41552076.png)

![Time to SLA event order showing Start, Resume, Pause, Reset, Stop sequence](/cms_trial/assets/dade5692-12c7-4bf2-82a1-8b5863039ffb.png)