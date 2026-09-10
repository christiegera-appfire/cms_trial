# SLA custom field

You can view the target date of your SLA on the **SLA panel**, but you might also want to display this information in a field for better visibility. To do this, you can assign a **Date Time Picker** field (which you must create beforehand) as the SLA target date.

This will display the target date in the **Details** > **More Fields** category in the work item view, like this:

![Time to SLA SLA custom field configuration panel](/cms_trial/assets/b91909b5-e02b-4040-b3fc-24046e85d6bb.png)

This page explains how to set a field as the SLA Target Date field.

## Step 1: Create the field

You can use an existing field as an SLA target date, but as a best practice, we recommend creating a Date time picker type field specifically for this purpose.

1. Follow the [Atlassian documentation](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/) to create a Date time picker type field.

We don't recommend using a target date for more than one SLA because the field may display inaccurate data as a result.

If you have two different SLAs that will appear on the same work item, you shouldn't use a single field for both. Create two separate fields to avoid any mishaps.

## Step 2: Set the field as the SLA target date field

1. Go to **SLAs** in Time to SLA**.**
2. Click the settings button in the row of the SLA you want to update and select **Edit**.
3. Scroll down to the *SLA Custom Field* section and tick the **Update date field in issue** checkbox.

   ![Time to SLA SLA custom field display in Jira issue fields](/cms_trial/assets/7c1b065c-b23b-4def-94b5-49c043cd7980.png)
4. Select the field you want to set as the SLA target date field.
5. Click **Save**.

That’s it! Now, all you need to do is recalculate your SLA data so that you can see the SLA target date field on your existing work items. If you don't know how, [read this article](/cms_trial/space/TTSC/35456416/Recalculation/) to find out.

The SLA target date field will be added automatically for work items updated after this configuration.

**Not seeing the field on your work item?** You may not have added the field to the correct screens. Ensure that you have added the field that you've set as the SLA target date field to the appropriate screens.

The SLA Target Date field reflects the current SLA deadline. If the SLA is paused after it has already breached, the deadline will remain unchanged, and the field will not update further.

Pauses only affect the target date before the breach. After a breach occurs, the SLA remains marked as breached, and the target date is locked.

This is by design to ensure accurate and auditable SLA tracking.

---

## Target date refresh interval

You can enter a refresh interval (for example, 30 minutes) to determine how often you'd like the SLA Target Date field to update the target date on an SLA.

When an SLA is paused before a breach, the Target Date field stores information about how long it has been paused. This information is then used to recalculate the SLA target date, which is updated regularly during the pause. This gives you a more accurate estimate of how long it will take to complete a task.

If the SLA is already breached when the pause starts, the target date will no longer be recalculated. The SLA remains marked as breached, and the target date stays fixed.

If the target date does not change, Time to SLA will not update this value regardless of the Target Date Refresh Interval.

For example, let's imagine an SLA with a goal of 2 hours. As it continues to count, the target date remains unchanged. When the SLA stops (due to a pause before breach), the target date is pushed forward every minute. This is where the value you picked comes into play: this information is updated as often as the Target Date Refresh Interval value.

This information also appears in the work item history section.

To set the target date refresh interval, follow these steps:

1. Open Time to SLA and click **Settings** > **Advanced**.
2. Adjust the **Target Date Refresh Interval** **(****In Minutes****)** according to how often you want the information in your field to be updated. (Minimum: **2m**, Maximum: **1,440**m.)

   ![Time to SLA SLA custom field settings page](/cms_trial/assets/393d2fb4-912d-42bf-9d71-9e95d8acb574.png)
3. Click **Save**.

If your history is flooded with update notifications, you can try setting a higher target date refresh interval number to solve that problem.