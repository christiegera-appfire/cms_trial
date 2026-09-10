# SLA contract extension

You can extend the SLA deadline for a specific work item without affecting the SLA configuration or other work items.

This feature is useful in exceptional cases such as service disruptions or customer-approved delays where additional time is required to meet the SLA. Once extended, the SLA report reflects the new deadline, and the work item is not marked as failed if it is resolved within the extended timeframe.

## When to use it

You can extend an SLA whether it is running, paused, or breached. Use this feature in exceptional cases, such as:

- Service outages
- Customer-approved deadline shifts
- Escalations requiring more time

This action only affects the SLA on the current work item. It does **not** alter your global SLA configuration.

## How to extend the SLA for a work item

Once SLA tracking has started for a work item, you'll see an **Extend SLA** icon in the SLA panel.

1. Click the **Extend SLA** icon.

   ![Time to SLA SLA contract extension configuration page](/cms_trial/assets/5d46cd45-1b74-4dce-a008-cd93ac2e5966.png)
2. The **Extend SLA** modal will appear. Fill out the form:

   - **Extend SLA by:**

     ![Time to SLA SLA contract extension rule dialog](/cms_trial/assets/b087d213-15e4-4ba3-abf7-b296bcf2a921.png)

     Enter how much more time is needed (for example, `2d 5h`).
   - **Extension starts –** Depending on your selection and the extension duration you’ve entered, you’ll see the target date in the New SLA Target Date section.

     ![Time to SLA SLA contract extension duration field](/cms_trial/assets/f0a7d25a-f126-46f9-a37d-9fc565dc3ea1.png)
     - **After original SLA target date (default):** Adds the entered time to the previous SLA target.  
       *Example: SLA was due at 3 PM; adding 1h moves the deadline to 4 PM.*
     - **From now:** Adds the time from the current moment.  
       *Use this if the SLA has already breached.*
   - **Extension reason:**  
     Enter the reason for the extension (for example, `Customer approved extension due to server outage`).  
     Depending on your app settings, this field may be required. When an admin requires an extension reason, you must enter a reason before you can extend the SLA.
   - **Attach file (Optional):**  
     Upload evidence of the approval (like an email screenshot) to avoid miscommunication.

Admins can require users to provide a reason whenever they extend an SLA. To make extension reasons required:

1. Go to **Time to SLA** > **Settings** >[**General Settings**](/cms_trial/space/TTSC/37290034/Administration/).
2. Enable the option to require an extension reason.
3. Save your changes.

When this setting is enabled, users cannot extend an SLA without entering a reason in the **Extend SLA** dialog. The setting is disabled by default, so extension reasons remain optional unless an admin enables it.

1. Click **Extend**.

The SLA panel will update to show:

- The new target date

  ![Time to SLA SLA contract extension settings with date range](/cms_trial/assets/ce9f208d-dc4a-42fd-95b6-b348ab0c1ccc.png)
- Extended status label
- Remaining time under *Extended Remaining*

### Example

Before extension:

- SLA Target Date: `9/May/22 12:30 AM`
- Breached: SLA shown as failed

After extension:

- SLA Target Date: `10/May/22 12:30 AM`
- Status: **Extended**
- SLA report will now reflect success if resolved within the extended period.

A tooltip in the SLA panel will show the target date before the extension happened, the reason for the extension, and any attached files.

![Time to SLA SLA contract extension confirmation message](/cms_trial/assets/a3919c05-6882-4554-b001-632e175b098f.png)

## Undoing an SLA extension

You can revert an SLA extension if needed.

1. Click the **Extend SLA** button on the SLA panel again.
2. Confirm your choice in the **Undo Extend SLA** dialog.

   ![Time to SLA SLA contract extension configuration with trigger details](/cms_trial/assets/eaf8c87a-fa42-4365-8b33-aae25c95ad5e.png)

The SLA will revert to its original configuration and timeline.

## Tracking extensions

All SLA extension activity is recorded in the **SLA History** tab:

- You’ll see when the SLA was started, entered critical zone, breached, extended, and by whom.

  ![Time to SLA SLA contract extension final settings review](/cms_trial/assets/b47c1bea-742a-4982-b8a5-8dbc59e9ce6a.png)