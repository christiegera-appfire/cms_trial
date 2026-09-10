# Worklog suggestions

**Beta Notice:** This feature is currently in active development. We are iteratively refining the suggestion algorithms based on user interaction data. To provide feedback or report inconsistencies, please visit our [support portal](https://appfire.atlassian.net/servicedesk/customer/portal/11).

**Worklog Suggestions** simplifies time tracking by recommending the Jira tasks you have recently worked on. By analyzing your Jira activity and calendar events, the feature identifies relevant issues and pre-fills worklog details, reducing the manual effort of retracing your daily or weekly schedule.

## User interface and integration

Worklog Suggestions are currently accessible using two primary workflows:

### Add Time Dialog

![image (7).png](/cms_trial/assets/c4bfce9f-c932-4d03-8b0f-7c110b2bb509.png)

When the Add Time dialog is initialized, a dedicated suggestions panel appears on the left. This panel populates a list of Jira items the user has likely interacted with recently. Where data is available, the system will also pre-populate:

- **Suggested Durations** (calculated from your 7pace history)
- **Custom Fields**
- **Worklog Comments**

### The Weekly view

This feature is being rolled out **gradually** (approximately 10% of users per day) to ensure stability. It will be available to all users soon. If you require immediate access, please **contact our** [**support team**](https://appfire.atlassian.net/servicedesk/customer/portal/11).

In the Weekly view, you can switch the Worklog Suggestions toggle to see suggestions:

![show-suggestions-toggle.png](/cms_trial/assets/88a3e8c3-7da6-4eba-9918-f88ad1974cce.png)

Once you do this, suggestions are displayed in the view:

![weekly-sugesstions.png](/cms_trial/assets/fec86d82-1685-4f9d-b4a2-bb74bb1f5b9e.png)

You can:

![suggestions-options.png](/cms_trial/assets/8ee3d0f2-0ac6-4e56-babe-05b8faba2368.png)

- **Edit** suggestion. Clicking this option opens the Add worklog from suggestion form with date, time, duration, and comment fields filled in. You can save the worklog as it is, or edit details before selecting **Save**.

  ![edit-suggestions.png](/cms_trial/assets/cff9dca5-5615-4a05-a11f-52676a32b41d.png)
- **Dismiss** suggestion. Choosing this option removes the suggestion from the Weekly view
- **Accept** suggestion. After doing this, you can add a related work item (or leave it empty) and save the suggested worklog:

  ![add-missing-information.png](/cms_trial/assets/78966c94-79d0-4584-8ba6-651188e17504.png)

### Work item workload suggestion

If a related Jira work item is In Progress, values for some fields in the 7pace Add Time panel are suggested based on workload suggestions.

![work-item-workload-suggestions.png](/cms_trial/assets/00b5971d-e48c-4868-9b12-fd87ad4ce6e4.png)

## Calculation logic and data sources

To ensure relevance, the suggestion engine utilizes a weighted scoring system based on activity within a rolling **3-day window**. The following data sources are utilized:

|  |  |
| --- | --- |
| **Data Category** | **Specific Logic & Fields Tracked** |
| **Jira System Activity** | The engine monitors the Jira "Changelog" for modifications made by the user. Monitored fields include: `Status`, `Summary`, `Assignee`, `Due Date`, `Resolution`, `Attachment`, `Description`, `Labels`, and `Time Spent`. |
| **Comment History** | The system identifies issues where the user has recently added or edited comments, specifically for issues already identified via the system activity logic above. |
| **Historical 7pace Data** | 7pace analyzes the user’s worklog history to predict the likely issue and calculate suggested durations based on previous logging patterns. |
| **Integrated Calendars** | The system performs text-matching searches between calendar event titles/descriptions and Jira issues. For **recurring events**, the engine prioritizes the Jira issue previously associated with that event series. |

To ensure accurate results, the timezone settings in Jira must be configured correctly. The timezone should match the current location and be set to **Visible for all users**. Additional details can be found in the [Jira documentation](https://confluence.atlassian.com/jirakb/changing-user-profile-preferred-timezone-1518962968.html).

## Settings

![worklog-suggestions.png](/cms_trial/assets/0cd2b96c-6761-4ac8-9fa5-e0daeaed6821.png)

Go to **Settings > Worklog suggestions** to choose preferred worklog suggestion calculation method.

- **Percentage-based allocation**: splits your capacity proportionally across the work items you worked on.
- **Transition-time allocation**: uses Jira status changes and assignments to estimate time spent.

In the **Other settings that shape your suggestions section**, you can access other settings that can influence worklog suggestions:

- [Work preferences](/cms_trial/space/7TFJ/3572597090/Work+preferences/)
- [Calendar integration](/cms_trial/space/7TFJ/3572924445/Calendar+integration/)
- [BigPicture integration](/cms_trial/space/7TFJ/2106556524/BigPicture+integration/)

## Privacy and permissions

Worklog Suggestions strictly adheres to your existing Jira security architecture:

- **User isolation:** Suggestions are generated individually. No user can see suggestions based on another user’s private calendar events or restricted Jira activity.
- **Permission:** If a user does not have the View permissions for a specific Jira issue, the suggestion engine will never surface that issue to them.
- **Data scope:** The system only processes specific, non-configurable system fields (Status, Summary, Assignee, Due Date, Resolution, Attachment, Description, Labels, and Time Spent) to identify relevant work.

## Troubleshooting

If no suggestions are appearing, please verify:

1. **Activity:** You have performed trackable activity (status changes, comments) within the last 72 hours.
2. **Sync:** Your calendar integration is active (for Calendar-specific suggestions).
3. **Permissions:** You have the appropriate Jira permissions to view the issues they are working on.