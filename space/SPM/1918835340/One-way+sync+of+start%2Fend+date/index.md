# One-way sync of start/end date

Refer to the [Task dates based on estimates](/cms_trial/space/SPM/1918539473/Task+dates+based+on+estimates/) page for more information.

The start and end date fields can be mapped and uni-directionally synchronized with an additional Jira field. This will result in a one-way data sync from BigPicture to Jira.

## Access the one-way sync fields

To see a one-way sync field, change the start/end date field mapping to a time tracking field and save the changes. A corresponding one-way sync field will appear.

The **one-way sync start date field** is visible only when:

- start date field is synchronized with the **Original Estimate** field.

The **one-way sync end date field** is visible only when:

- end date field is synchronized with the **Original Estimate** field.
- or, the end date field is synchronized with the  **Time Spent + Remaining Estimate** fields.

![Field mapping settings in BigPicture for one-way sync.](/cms_trial/assets/ae4878e3-d1dd-4198-9d2d-7ee9db5f8bde.png)

## Configure the Start/End date one-way sync

The one-way sync from BigPicture to Jira does not disrupt the functioning of the Start/End date fields.

First, configure the standard field mapping for the Start/End date. For example, you can map the BigPicture Start date to the Jira Start date and the BigPicture End date to Jira Time Spent + Remaining Estimate.

Then, map the BigPicture one-way sync end date field with another Jira field, such as the Jira Due date.

- The one-way sync mapping follows the same rules as the standard (bi-directional) field mapping, meaning you **cannot select the same field** for both the End Date and the one-way sync End Date.
- Only simple date and time fields can be selected for the one-way sync mapping. Fields such as Time Spent and Remaining Estimate are not available.

![Once way sync example.](/cms_trial/assets/033b7489-ef2e-437e-9144-013ea985eea2.png)

This will result in the following:

- The tasks' end dates in BigPicture are based on Jira’s Time Spent + Remaining Estimate.
- BigPicture updates the tasks' end dates and visualizes them on the timeline based on those settings.
- BigPicture updates the Due date field value in Jira based on the End date field value.

Such synchronization is uni-directional, so changing the Due date in Jira does not change the end date in BigPicture.