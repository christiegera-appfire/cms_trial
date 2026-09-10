# Timer

![7pace in Jira opened, the timer option highlighted.](/cms_trial/assets/f4682e94-c259-475a-8b90-8db5c02490a9.png)

The **Start/Stop Timer** feature lets you track your work hours in real time directly from within a Jira work item. Instead of manually logging hours after completing a task, you can simply start the timer when you begin working and stop it when you are finished, which automatically creates a corresponding worklog. This real-time approach removes the need to remember and reconstruct your work hours later, making your time tracking significantly more accurate and far less disruptive to your daily workflow.

## How to Use the Timer

### Quick Reference: Timer Controls

![7pace-timer-ui.png](/cms_trial/assets/ab8e7318-54c5-480c-b9fa-ea462ff48873.png)

|  |  |  |
| --- | --- | --- |
| **Action / Control** | **Description** | **System Outcome** |
| **Track time** | Click to start tracking work in real time. | Displays an active timer measuring passing time. |
| **Stop Icon** | Click to save your currently recorded time. | Opens the Add Time Dialog with the duration pre-filled and rounded up to full minutes. |
| **Bin Icon** | Click to delete the current tracking session. | Discards the active timer without automatically creating a worklog. |

### Step-by-Step Workflow

#### Starting a Session

- Navigate to the relevant Jira work item and click the **Track time** option.
- The system will instantly switch to display an **Active timer**, which actively measures your passing work time.

  ![7pace-timer.png](/cms_trial/assets/f4682e94-c259-475a-8b90-8db5c02490a9.png)

#### Stopping and Saving Time

- When your task is complete, click the **stop icon** to save your hours.
- This action launches the **Add Time Dialog**, automatically populating your measured time into the **Duration** field.
- **Note on Rounding:** The recorded tracking time is automatically rounded up to full minutes upon saving.

![tracked-time-rounded.png](/cms_trial/assets/303d8a52-f6c8-4ff8-a4fc-852db8770d81.png)

#### Discarding a Session

- If you need to cancel a tracking session without logging any hours, click the **bin icon**.
- This action deletes the active timer immediately.

## Tracking Limitations & Admin Settings

### Single Tracker Restriction

To keep data clean, you can only track one work item at a time. If you attempt to start a new timer while a tracker is already active on a different work item, the system will prevent it and display the following message:

> "You can only track one item at a time. Save the worklog from the active timer to track time here, or add time manually."

Along with this warning notification, a direct link to the currently active timer is provided so you can easily navigate back to your running session and manage it:

![7pace-active-tracker-warning.png](/cms_trial/assets/ef1c154a-2dc9-4bca-9ea8-78db3910d87c.png)

### Administrative Maximum Limits

Administrators have the ability to configure a maximum time limit that can be recorded using the timer feature to prevent run-away logging sessions.