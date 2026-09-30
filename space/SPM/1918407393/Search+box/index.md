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

Image — asset pipeline pending  
text-jql.png

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

Image — asset pipeline pending  
text-search.png

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

Image — asset pipeline pending  
jql-search.png

The icon will change to red if the JQL query you typed is incorrect.

Image — asset pipeline pending  
Incorrect JQL query highlighted in red

For example, to search for a task in the Done status category, type in the following JQL query: "`statusCategory = Done`".

["](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298027991)The App does NOT support ORDER BY" JQL - therefore, it can't be executed.

## Active search

The active search box will be cleared automatically when you switch to another module and then return to the previous module.

## Apply filters

You can see an orange dot on the filter icon when the filter is active.

Tasks that do NOT match the filter will be grayed-out. This applies to parent tasks, so you can trace how lower-level tasks contribute to higher-level items.

## Snipe to result

Image — asset pipeline pending  
snapie-to-result.png

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

Image — asset pipeline pending  
snipe-to-result.png

You can easily switch between the results by using the arrows in the search box.

- Snipe can be turned on/off at any point. Turning it on/off does NOT affect the search itself (doesn't clear it). In other words, the 'snipe' option changes how the 'search' filter behaves. It is a modification of a search filter function.
- Tasks in the Infobar are NOT highlighted.

**Note**: If a filer option **Show basic tasks when using Jira filters** is active, **all** basic tasks are included in the search results. When you snipe between the tasks, basic tasks are included in the rotation (even when they don’t match the search query).

Image — asset pipeline pending  
show-basic-tasks.png

## Snipe to task

The option is available in the Gantt module, Change History panel.

The "**snipe to task"**button takes you to a task and selects it.

Image — asset pipeline pending  
change-history-snipe.png

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

Image — asset pipeline pending  
Screenshot of the serach box in the Gantt module.

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

Image — asset pipeline pending  
Screenshot of an example showing how to use the search box in the Gantt module.

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

Image — asset pipeline pending  
Screenshot of the JQL search in the Gantt module.

The icon will change to red if the JQL query you typed is incorrect.

Image — asset pipeline pending  
Incorrect JQL query highlighted in red

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

Image — asset pipeline pending  
Screenshot of the Snipe to result button in the search box in the Gantt module.

How does **Snipe to result** work?

- Highlights all items matching the search (the currently selected task is highlighted with a darker color).
- Expands the task tree to make the results visible.
- It takes you to each item.
- Counts the number of matches.
- Works in both TEXT and JQL modes.

Image — asset pipeline pending  
Screenshot of using the Snipe to result option in the Gantt module.

You can easily switch between the results by using the arrows in the search box.

- Snipe can be turned on/off at any point. Turning it on/off does NOT affect the search itself (doesn't clear it). In other words, the snipe option changes how the search filter behaves. It is a modification of a search filter function.
- Tasks in the Infobar are NOT highlighted.

**Note**: If the filter option **Show BigPicture tasks when using Jira filters** is active, **all** BigPicture tasks are included in the search results. When you snipe between the tasks, BigPicture tasks are included in the rotation (even when they don’t match the search query).

Image — asset pipeline pending  
Screenshot of the Show BigPicture tasks when using Jira filters option enabled in the Gantt module.

## Snipe to task

The option is available in the Gantt module, **Change history** panel. The **Snipe to task**button takes you to a task and selects it.

Image — asset pipeline pending  
Screenshot of the Snipe to task option in the Gantt module.

## Clear the search

To clear the search box, delete your search query, press Enter, or click the magnifying glass button.