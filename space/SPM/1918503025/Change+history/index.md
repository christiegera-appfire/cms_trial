# Change history

## Introduction

The **change history**tab displays the **history of scheduling changes for that task.** Changes that affect the start date, end date, and duration of the task are logged. It does not matter if the change was made in the Gantt module, elsewhere in BitPicture, or in Jira/Trello.

![contentId-1918503025](/cms_trial/assets/c0111445-8ff5-431e-bfe5-bcd0a57a6fce.png)

---

## Task details view

You can also open the panel directly from the task details view.

1. Click on a task on the Gantt timeline.
2. Click "**See changes**".

   ![image-20250314-121707.png](/cms_trial/assets/c0db992c-1c8f-4800-a4ac-b2d91377b842.png)

## Recorded information

- The date the change occurred
- The reason for the change
- The author of the change

| **Item** | **Description** |
| --- | --- |
| Expand arrow | contentId-1918503025 In the expanded state you can see the **archival data of the task** contentId-1918503025 |
| Change reason | The following changes are recorded:   - New start/end date was set - Task was moved - Task was converted to a milestone - Task structure was changed - Dependency was added - Scheduling mode was changed  contentId-1918503025 |
| Change Author | contentId-1918503025 |
| Date of change | When the modification took place contentId-1918503025 |
| Number of changes | contentId-1918503025 When you move a parent task, all its children are also moved. All changes are logged: contentId-1918503025 **Changes affecting other Boxes -** a task can be in multiple Boxes. When you move a task, it is moved in all Boxes it is in. The change log reflects that. contentId-1918503025 |

## Filters

Narrow down the list by using the **search** function or the **date range** filter.

### Search

Only a simple text search is available.

The following fields are checked:

- Summary
- Issue key

![contentId-1918503025](/cms_trial/assets/61077786-a92a-4669-9946-a994235f0fe4.png)

 The search results include:

- Changes made directly to a task.

  ![image-20250314-121816.png](/cms_trial/assets/0deb3b1f-b154-4f73-9e03-36db9528b759.png)
- Changes that are a result of other task modifications (such as a move of a parent in the structure).

  ![image-20250314-121854.png](/cms_trial/assets/2e026119-97be-417d-9426-70a8d5280079.png)

  Results that do not match the search are hidden.

  ![image-20250314-121926.png](/cms_trial/assets/d2893e9e-0895-49ac-baca-9c8d34370eb5.png)

### Date range

Narrow down the list based on when a change took place:

![contentId-1918503025](/cms_trial/assets/618bf3f6-6f57-4f21-b7bc-ffb0c05a1eca.png)

## Snipe to task

For more information, check [the Filters page](https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/1793328307/Filters#Snipe-to-task).

## Refresh button

Use the **refresh** button to reload the info in the tab.

![contentId-1918503025](/cms_trial/assets/b19e6f14-baa4-488e-95fc-4bf079a5a6df.png)

 Any new changes are marked as 'new'.

![contentId-1918503025](/cms_trial/assets/69722d62-3120-4230-a714-629ea5df1697.png)

---

## Constraints

### Scenario mode

Changes made in [scenario mode](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297668364) are not logged until a scenario is merged into the live version.

### Log

The change log contains data from the last **30 days**.

### Number of listed changes

Change log displays up to **80 positions**.

To find a change that is not visible, use the search function.

### Number of change items (within a change)

Change log displays up to **30 task details** associated with a given change.

Use the search function to narrow down the results and see information on a given task.

---

## Save issue changes to Jira Cloud issue comments

Depending on [app configuration](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298387307), changes made to issues are also listed as issue comments in Jira.

---

## Send 'Issue Updated' notification after task changes

You can receive notifications whenever any changes are introduced to a task. The App Admin can enable this option under the **Additional task settings** on the **App Configuration** > **General** > **Fields** page.

---

## OKR notifications

Set up the [OKR notifications](/cms_trial/space/SPM/1918832829/OKR+Notifications/) to receive emails whenever any of your OKRs require an update.