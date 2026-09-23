# Manage teams

## Manage teams (old navigation)

## Team attributes

Team codes are used to identify teams assigned to tasks by the BigPicture modules and, when synchronized, by Jira. A **team code** is not case-sensitive but will always be saved and displayed in capital letters.

Each created team has a unique team code, which you need to specify when creating a new team.

### Configuration

Depending on [resources configuration](/cms_trial/space/SPM/1918764262/Resource+management/), a team code is stored as one of the following fields:

- Labels type
- Select list (single choice type)
- None (not synchronized)

You can use these fields in your JQL to create quick filters or a Jira board dedicated to a specific team.

Image — asset pipeline pending  
Screenshot of the Team code field in the Teams module.

Team codes are usually displayed next to the team name. For example, when you switch to the **Team** **view** in the Resources module, the team code is displayed next to each team name and in the task details dialog.

Image — asset pipeline pending  
Screenshot of the team code label in the Resources module.

### Labels

Labels are very convenient but prone to typos. BigPicture can automatically generate labels while you're assigning a team. The team code used as a label has the following format: **team#TEAMCODE**.

For example, Team Saphire uses the "SAPH" team code. The team label is added when you assign the team to a task.

Image — asset pipeline pending  
Screenshot of a Jira issue page with the team label field.

### Select list

**Select list** fields require you to predefine available options. When you use the **Select list** type field, only the TEAMCODE is used.

In the example below, the custom field labeled **Team code custom field** is populated with the Quality Assurance Team's code (QA).

Image — asset pipeline pending  
Screenshot of a Jira issue page with the Select list type field.

### Team board link

Team assignment **is NOT** synchronized with Jira.

Use the **board link** to specify which Jira boards your teams use. This way, BigPicture can automatically create sprints on that board when you add a new synchronized box.

To learn more about synchronization, see the [the Work items from Jira](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Work%20items%20for%20Jira%20elements%20and%20actions&linkCreation=true&fromPageId=1918635643).

Image — asset pipeline pending  
Screenshot of the Board name column in the Teams module.

#### Add Jira board link

To add a Jira board link to a selected team:

1. Go to the **Teams module** in BigPicture.
2. Click on the team to expand the **Details** sidebar.
3. Go to the **Details** tab.
4. Select a Jira board from the drop-down menu. The drop-down shows a list of previously created [Jira Scrum boards](https://support.atlassian.com/jira-software-cloud/docs/create-a-board/).

   Image — asset pipeline pending  
   Screenshot of all Jira boards.
5. Click **Save**.

   Image — asset pipeline pending  
   Screenshot of adding a Jira board to a selected team in the Teams module.

## Manage teams (new navigation)

## Team attributes

Team codes are used to identify teams assigned to tasks by the BigPicture modules and, when synchronized, by Jira. A **team code** is not case-sensitive but will always be saved and displayed in capital letters.

Each created team has a unique team code, which you need to specify when creating a new team.

### Configuration

Depending on [resources configuration](/cms_trial/space/SPM/1918764262/Resource+management/), a team code is stored as one of the following fields:

- Labels type
- Select list (single choice type)
- None (not synchronized)

You can use these fields in your JQL to create quick filters or a Jira board dedicated to a specific team.

Image — asset pipeline pending  
teams-code-color.png

Team codes are usually displayed next to the team name. For example, when you switch to the **Team** **view** in the Resources module, the team code is displayed next to each team name and in the task details dialog.

### Labels

Labels are very convenient but prone to typos. BigPicture can automatically generate labels while you're assigning a team. The team code used as a label has the following format: **team#TEAMCODE**.

For example, Team Saphire uses the "SAPH" team code. The team label is added when you assign the team to a task.

Image — asset pipeline pending  
Screenshot of a Jira issue page with the team label field.

### Select list

**Select list** fields require you to predefine available options. When you use the **Select list** type field, only the TEAMCODE is used.

In the example below, the custom field labeled **Team code custom field** is populated with the Quality Assurance Team's code (QA).

Image — asset pipeline pending  
Screenshot of a Jira issue page with the Select list type field.

### Team board link

Team assignment **is NOT** synchronized with Jira.

Use the **board link** to specify which Jira boards your teams use. This way, BigPicture can automatically create sprints on that board when you add a new synchronized box.

To learn more about synchronization, see the [the Work items from Jira](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=Work%20items%20for%20Jira%20elements%20and%20actions&linkCreation=true&fromPageId=1918635643).

Image — asset pipeline pending  
teams-board.png

#### Add Jira board link

To add a Jira board link to a selected team:

1. Go to the **Teams module** in BigPicture.
2. Click the team to expand the **Details** sidebar.
3. Go to the **Details** tab.
4. Select a Jira board from the drop-down menu. The drop-down shows a list of previously created [Jira Scrum boards](https://support.atlassian.com/jira-software-cloud/docs/create-a-board/).

   Image — asset pipeline pending  
   Screenshot of all Jira boards.
5. Click **Save**.