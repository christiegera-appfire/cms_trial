# I need work item-specific SLA actions!

🤔 **Context:** A developer needs a deadline extension for a specific work item, but doesn’t want to change the SLA configuration, as that would affect all of their work items.

🌧️ **User Problem:** As a developer, I typically need 5 days to finish a work item, which is reflected in my SLA configurations. However, one of the latest work items I’ve been working on has proved itself to be a pain in the neck, and 5 days won't cut it. However, I don't want to change the Target Date from SLA configurations to extend the deadline, as this would affect all of my issues. I need to solve this problem on the issue level.

☔ **Solution:** Using the Time to SLA Issue Actions menu to Reset the SLA!

With Time to SLA, it’s possible to set work item-specific actions for your selected SLAs. With the Issue Actions dropdown menu, you can use the Reset an SLA, Undo Reset SLA, Where is my SLA?, and Recalculate SLA actions.

To solve the problem described above, let’s use the **Reset SLA** action.

## How to use the Reset SLA action

1. Go to the work item you want to reset on Jira Cloud.
2. Click the three-dots icon on top of the **Details** menu.

   ![Time to SLA work item actions page with SLA actions settings](/cms_trial/assets/9ccffc84-b65b-46ee-8867-66b5b11daed5.png)
3. Click **Time to SLA Issue Actions** > **Actions** > **Reset SLA**.
4. Select the SLA(s) you want to reset.

   ![Time to SLA work item actions dialog for SLA action configuration](/cms_trial/assets/e3dabc7b-f20b-4e77-8cd5-2ef671533ac9.png)
5. Select a reset date. If you leave this box blank, the SLA(s) will be reset immediately.
6. Click **Proceed**.

The resets you define here won't interfere with the ones you've defined in SLA configurations.

## Problem solved!