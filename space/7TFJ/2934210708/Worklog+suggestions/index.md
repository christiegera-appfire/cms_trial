# Worklog suggestions

**Beta Notice:** This feature is currently in active development. We are iteratively refining the suggestion algorithms based on user interaction data. To provide feedback or report inconsistencies, please visit our [support portal](https://appfire.atlassian.net/servicedesk/customer/portal/11).

**Worklog Suggestions** simplifies time tracking by recommending the Jira tasks you have recently worked on. By analyzing your Jira activity and calendar events, the feature identifies relevant issues and pre-fills worklog details, reducing the manual effort of retracing your daily or weekly schedule.

## User interface and integration

Worklog Suggestions are currently accessible using two primary workflows:

### Add Time Dialog

![add-time-worklog-suggestions.png](/cms_trial/assets/e44cadf9-42b1-4695-bc4e-d36a041e09d0.png)

When the Add Time dialog is initialized, a dedicated suggestions panel appears on the left. This panel contains a list of Jira items the user has likely interacted with recently. Where data is available, the system also pre-populates:

- **Suggested Durations** (calculated from your 7pace history)
- **Custom Fields**
- **Worklog Comments**

After choosing a work item, Comments and Custom Field values are also suggested (if there are enough previous actions related to the item).

### Weekly view

This feature is being rolled out **gradually** (approximately 10% of users per day) to ensure stability. It will be available to all users soon. If you require immediate access, please **contact our** [**support team**](https://appfire.atlassian.net/servicedesk/customer/portal/11).

In the Weekly view, you can switch the Worklog Suggestions toggle to see suggestions:

![show-suggestions-toggle.png](/cms_trial/assets/58060e72-06cb-400a-ba0a-6836bb820ac4.png)

Once you do this, suggestions are displayed in the view:

![weekly-sugesstions.png](/cms_trial/assets/9a407563-d14a-473d-9e69-35dd8ba0c273.png)

You can:

![suggestions-options.png](/cms_trial/assets/96cb7eb1-8c7c-4974-a28c-60f99b9a979f.png)

- **Edit** suggestion. Clicking this option opens the Add worklog from suggestion form with date, time, duration, and comment fields filled in. You can save the worklog as it is, or edit details before selecting **Save**.

  ![edit-suggestions.png](/cms_trial/assets/53ccc334-fd85-4306-98b1-41f8cceb7835.png)
- **Dismiss** suggestion. Choosing this option removes the suggestion from the Weekly view
- **Accept** suggestion. After doing this, you can add a related work item (or leave it empty) and save the suggested worklog:

  ![add-missing-information.png](/cms_trial/assets/66299cc0-e390-4f7b-ba35-f9e13c275716.png)

### Work item workload suggestion

If a related Jira work item is In Progress, values for some fields in the 7pace Add Time panel are suggested based on workload suggestions.

![work-item-workload-suggestions.png](/cms_trial/assets/f27b4d7e-2288-4ec5-9798-c7cec7c5e4f0.png)

### Timesheet view

![worklog-suggestions-timesheet.png](/cms_trial/assets/75ba7ff5-be44-4a59-aaba-e58191ab927c.png)

When adding a worklog through Timesheet, the comment and custom field values are suggested based on the previously logged worklogs. The suggestions are marked with the Workload Suggestion icons and can be changed.

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

![worklog-suggestions.png](/cms_trial/assets/c0f6c8e4-434b-4865-85d5-b82caf8ce66b.png)

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