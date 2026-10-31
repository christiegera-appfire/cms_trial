# Search box

## Search box (old navigation)

Click to expand the guide

## Overview

The **search box** functionality lets you quickly find the things of your interest and filter out unwanted tasks or boxes. The search box operates in two modes:

- **Text search mode** filters information based on the Jira summary field (boxes and tasks)
- **JQL mode** filters tasks using JQL queries

The search box is available in the following [modules](/cms_trial/space/SPM/1918535028/BigPicture+modules/):

- [Overview](/cms_trial/space/SPM/1918502655/Overview+module/) (text search mode only)
- [Gantt](/cms_trial/space/SPM/1918797129/Gantt+module/)
- [Scope](/cms_trial/space/SPM/1918666763/Scope+module/)
- [Board](/cms_trial/space/SPM/1918796888/Board+module/)
- [Risks](/cms_trial/space/SPM/1918666681/Risks+module/)
- [Calendar](/cms_trial/space/SPM/1918699000/Calendar+module/)
- [Resources](/cms_trial/space/SPM/1918535629/Resources+module/)
- [Teams](/cms_trial/space/SPM/1918829775/Teams+module/) (text search mode only)

## Search modes

The text search is the default mode. Click the icon next to the search field to switch between the TEXT and the JQL modes:

![text-jql.png](/cms_trial/assets/7a9dd0d1-f487-4c16-8394-406831569ff7.png)

### Text search

You can use the text fields and the task key in most modules to locate your tasks. Available text fields depend on your [connected tools](/cms_trial/space/SPM/1918633230/Integrations/) (Trello, Jira, etc.).

Text search also applies to [basic tasks](/cms_trial/space/SPM/1918405930/Basic+tasks+%2F+BigPicture+tasks/).

For example, the search checks the contents of **all text fields** of Jira issues, such as:

- Key (text search will also go over the task key field)
- Summary
- Description
- Environment
- Comments
- Custom fields

  - Free text field (unlimited text)
  - Text field (<225 characters)
  - Read-only text field

![text-search.png](/cms_trial/assets/6287af60-acde-4375-bf63-ee36535e570e.png)

In the case of the Overview module, which shows Boxes, you can text search using:

- Box Id
- Box Name
- Box Summary
- Box Description

Search applies also to a hidden column(s). The box with results is visible once the search criteria are met.

### Text search limitations - use of square brackets

❌ The text search does NOT support using square brackets - the Jira' text~' search applies limitations.

## JQL Search

Start typing in the search box to open the JQL drop-down, which will help you find the query.

![jql-search.png](/cms_trial/assets/428434dd-2753-4e25-8d82-75398b565d93.png)

The icon will change to red if the JQL query you typed is incorrect.

![Incorrect JQL query highlighted in red](/cms_trial/assets/5338419b-9499-4a9b-a373-ef2c0cf79440.png)

For example, to search for a task in the Done status category, type in the following JQL query: "`statusCategory = Done`".

["](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298027991)The App does NOT support ORDER BY" JQL - therefore, it can't be executed.

## Active search

The active search box will be cleared automatically when you switch to another module and then return to the previous module.

## Apply filters

You can see an orange dot on the filter icon when the filter is active.

Tasks that do NOT match the filter will be grayed-out. This applies to parent tasks, so you can trace how lower-level tasks contribute to higher-level items.

## Snipe to result

![snapie-to-result.png](/cms_trial/assets/8657f1d4-bf21-4abf-a179-4e962cdbb74f.png)

### Availability

The feature is available in the following modules:

- Gantt
- Scope
- Board (Backlog)

Use the **Snipe to result** option to highlight all tasks that fit the search criteria. It works similarly to the "Ctrl+F" feature in any web browser. The whole row is highlighted not only a searched text. Tasks are visible on the WBS and chart (timeline).

How does **Snipe to result** work?

- Highlights all items matching the search (the currently selected task is highlighted with a darker color).
- Expands the task tree to make the results visible.
- It takes you to each item.
- Counts the number of matches.
- Works in both TEXT and JQL modes.

![snipe-to-result.png](/cms_trial/assets/6d7a6889-b892-4159-a7ee-e5e4b170afc0.png)

You can easily switch between the results by using the arrows in the search box.

- Snipe can be turned on/off at any point. Turning it on/off does NOT affect the search itself (doesn't clear it). In other words, the 'snipe' option changes how the 'search' filter behaves. It is a modification of a search filter function.
- Tasks in the Infobar are NOT highlighted.

**Note**: If a filer option **Show basic tasks when using Jira filters** is active, **all** basic tasks are included in the search results. When you snipe between the tasks, basic tasks are included in the rotation (even when they don’t match the search query).

![show-basic-tasks.png](/cms_trial/assets/5f63f812-9834-412a-b5ac-a37ca5b0290e.png)

## Snipe to task

The option is available in the Gantt module, Change History panel.

The "**snipe to task"**button takes you to a task and selects it.

![change-history-snipe.png](/cms_trial/assets/fe993117-cb08-4379-b826-f0401e434ff3.png)

## Clear the search

To clear the search box, delete your search query, press Enter, or click the magnifying glass button.

## Search box (new navigation)

Click to expand the guide

## Overview

The **search box** functionality lets you quickly find the things of your interest and filter out unwanted tasks or boxes. The search box operates in two modes:

- **Text search mode** filters information based on the Jira summary field (boxes and tasks)
- **JQL mode** filters tasks using JQL queries

The search box is available in the following [modules](/cms_trial/space/SPM/1918535028/BigPicture+modules/):

- [Overview](/cms_trial/space/SPM/1918502655/Overview+module/) (text search mode only)
- [Gantt](/cms_trial/space/SPM/1918797129/Gantt+module/)
- [Scope](/cms_trial/space/SPM/1918666763/Scope+module/)
- [Board](/cms_trial/space/SPM/1918796888/Board+module/)
- [Risks](/cms_trial/space/SPM/1918666681/Risks+module/)
- [Calendar](/cms_trial/space/SPM/1918699000/Calendar+module/)
- [Resources](/cms_trial/space/SPM/1918535629/Resources+module/)
- [Teams](/cms_trial/space/SPM/1918829775/Teams+module/) (text search mode only)

## Search modes

The text search is the default mode. Click the icon next to the search field to switch between the TEXT and the JQL modes.

![Screenshot of the serach box in the Gantt module.](/cms_trial/assets/33b79be3-4ccb-4043-bf06-7fedbfd4e53c.png)

### Text search

You can use the text fields and the task key in most modules to locate your tasks. Available text fields depend on your [connected tools](/cms_trial/space/SPM/1918633230/Integrations/) (Trello, Jira, etc.).

Text search also applies to [BigPicture tasks](/cms_trial/space/SPM/1918405930/Basic+tasks+%2F+BigPicture+tasks/).

For example, the search checks the contents of **all text fields** of Jira work items, such as:

- Key (text search will also go over the task key field)
- Summary
- Description
- Environment
- Comments
- Custom fields

  - Free text field (unlimited text)
  - Text field (<225 characters)
  - Read-only text field

![Screenshot of an example showing how to use the search box in the Gantt module.](/cms_trial/assets/57882bad-4d06-4766-9dc2-74208a0b4947.png)

In the case of the Overview module, which shows boxes, you can text search using:

- Box ID
- Box Name
- Box Summary
- Box Description

Search also applies to hidden columns. The box with results is visible once the search criteria are met.

### Text search limitations - use of square brackets

❌ The text search does NOT support using square brackets - the Jira' text~' search applies limitations.

## JQL search

Start typing in the search box to open the JQL drop-down, which will help you find the query.

![Screenshot of the JQL search in the Gantt module.](/cms_trial/assets/54ac06e3-8fd7-4036-b9db-5347017e532a.png)

The icon will change to red if the JQL query you typed is incorrect.

![Incorrect JQL query highlighted in red](/cms_trial/assets/5338419b-9499-4a9b-a373-ef2c0cf79440.png)

For example, to search for a task in the Done status category, type in the following JQL query: "`statusCategory = Done`".

["](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298027991)The App does NOT support ORDER BY" JQL - therefore, it can't be executed.

## Active search

The active search box will be cleared automatically when you switch to another module and then return to the previous module.

## Apply filters

You can see an orange dot on the filter icon when the filter is active.

Tasks that do NOT match the filter will be grayed-out. This applies to parent tasks, so you can trace how lower-level tasks contribute to higher-level items.

## Snipe to result

### Availability

The feature is available in the following modules:

- Gantt
- Scope
- Board (Backlog)

Use the **Snipe to result** option to highlight all tasks that fit the search criteria. It works similarly to the "Ctrl+F" feature in any web browser. The whole row is highlighted not only the searched text. Tasks are visible on the WBS and chart (timeline).

![Screenshot of the Snipe to result button in the search box in the Gantt module.](/cms_trial/assets/66dd3d74-b246-4b78-8963-4f274993f4a1.png)

How does **Snipe to result** work?

- Highlights all items matching the search (the currently selected task is highlighted with a darker color).
- Expands the task tree to make the results visible.
- It takes you to each item.
- Counts the number of matches.
- Works in both TEXT and JQL modes.

![Screenshot of using the Snipe to result option in the Gantt module.](/cms_trial/assets/53a38626-bbd5-4ab0-b056-5506694abd3e.png)

You can easily switch between the results by using the arrows in the search box.

- Snipe can be turned on/off at any point. Turning it on/off does NOT affect the search itself (doesn't clear it). In other words, the snipe option changes how the search filter behaves. It is a modification of a search filter function.
- Tasks in the Infobar are NOT highlighted.

**Note**: If the filter option **Show BigPicture tasks when using Jira filters** is active, **all** BigPicture tasks are included in the search results. When you snipe between the tasks, BigPicture tasks are included in the rotation (even when they don’t match the search query).

![Screenshot of the Show BigPicture tasks when using Jira filters option enabled in the Gantt module.](/cms_trial/assets/11f42d40-7967-4b6c-a1b3-4bd9d35b7692.png)

## Snipe to task

The option is available in the Gantt module, **Change history** panel. The **Snipe to task**button takes you to a task and selects it.

![Screenshot of the Snipe to task option in the Gantt module.](/cms_trial/assets/10e9747d-988e-4acb-b1e0-3ebbe39da69f.png)

## Clear the search

To clear the search box, delete your search query, press Enter, or click the magnifying glass button.