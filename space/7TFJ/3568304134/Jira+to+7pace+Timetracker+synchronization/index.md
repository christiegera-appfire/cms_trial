# Jira to 7pace Timetracker synchronization

Installing 7pace Timetracker initializes Jira worklog synchronization for the past 30 days. However, you can choose to sync up to 180 days back. You can choose any date in this range, allowing you to set the exact start date for synchronization.

## How to enable synchronization

1. Select **Jira synchronization** from the side navigation.
2. Locate the sync toggle in the **Jira to 7pace** section and switch it to **Active**.
3. Confirm the initial synchronization date when prompted.

   ![jira-to-7pace-sync.png](/cms_trial/assets/4f12d508-9877-4c15-af11-5a951ac43705.png)
4. Select **Confirm**.

## Key Information and Limitations

- **Sync Range:** By default, Jira worklogs from the last 30 days are synchronized into 7pace. You can use the Jira to 7pace sync option to choose a sync start date up to 180 days in the past. You can request a longer synchronization period by contacting support.
- **Sync Logic:** Synchronization is based on the *worklog creation date*, not the worklog date itself.
- **Data Safety:** Enabling sync imports Jira worklogs into 7pace without overwriting existing 7pace worklogs. If you need to start with a clean 7pace timesheet, turn off both Jira-to-7pace and 7pace-to-Jira synchronization, remove the relevant data from 7pace, and then restart synchronization using today's date.

## Requesting Extended Sync Range

If the default up-to-180-day synchronization window is not enough, administrators can request a longer range or ask support to disable synchronization so they can restart with a clean 7pace dataset. You can't extend the sync range directly in the user interface. Use the contact form available in the Jira synchronization settings page or submit a support ticket to request an extended range.