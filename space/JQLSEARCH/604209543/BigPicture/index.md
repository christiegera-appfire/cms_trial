# BigPicture

This article describes the integration points and suggested use cases for JQL Search Extensions with BigPicture.

[BigPicture](https://marketplace.atlassian.com/apps/1212259/bigpicture-project-management-ppm?tab=overview&hosting=cloud) is Appfire’s popular project management and project portfolio management app for Jira. You can leverage its power with additional JQL keywords and functions that **JQL Search Extensions** provides.

## Integration points

### Scope definition

JQL Search Extensions helps to define a precise scope of BigPicture boxes.

You can source issues with:

- filters
- a narrowing JQL

It’s possible, for example, to have a box with a subset of initiatives or epics and their children.

![Screenshot of a BigPicture box.](/cms_trial/assets/14e882b4-ffcd-4df4-aaa9-da4e0f7693a9.png)

You will typically create the [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) filter for the board and reuse it in the box.

The process of creating the filter from scratch looks like this:

1. Create a filter in [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/).
2. Wait for BigPicture to sync the filters list (see the note below).
3. Use the filter in BigPicture’s box configuration: Task → Scope Definition → Automatic Rules

BigPicture caches the list of filters and refreshes it every few hours.

Admins can force the refresh by clearing the BigPicture cache:

1. Go to**Apps**> **Manage your apps** > **BigPicture configuration**.
2. Click **Clear cache**.

## Quick filters

You can use JQL Search Extensions keywords and [filters](/cms_trial/space/JQLSEARCH/604209567/Extended+Search+filters/) in your BigPicture quick filters.

Create a quick filter that uses the JQL extensions:

![Screenshot of a list of quick filters in BigPicture.](/cms_trial/assets/2fc1db45-2f9f-4efb-a8ab-5167030f0d71.png)

Use the quick filter that highlights the matching issues:

![Screenshot of a list of matching issues in BigPicture quick filters.](/cms_trial/assets/69ba7e4b-049c-4b23-ae47-873364b121b6.png)

Be sure to review the examples in the Use Cases section on this page.

## Quick search bar

You can use JQL Search Extensions keywords and filters in the quick search bar.

![contentId-604209543](/cms_trial/assets/7f382f3e-daad-408b-934b-fe8ed0806eea.png)

1. In the box view, click the **Search** icon (🔍).
2. If not in JQL mode, click the **ABC** icon to change to JQL.
3. Enter your JQL query.

In JQL, you can refer to filters using the syntax, `filter="Your filter name"`.

## External use

It’s a common requirement to access the contents of a box outside of BigPicture, for example, to create a report in a third-party app or tool.

If you define the scope with a Jira filter, you can use this filter in:

- dashboard gadgets
- boards
- Jira search - use the syntax, `filter="Your filter name"`
- 3rd party apps that accept filters and JQL

## Use cases

### Source a subset of epics with their full hierarchy

You don’t need to add a whole Jira project to the scope of a box. You can create a box with selected epics, their stories, and subtasks.

If you have a list of specific epic keys that should be in scope, create the following [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) filter and use it as a scope:

`key in (EPIC-2, EPIC-5, EPIC-8) OR issue in childrenOfIssuesInQueryRecursive("key in (EPIC-2, EPIC-5, EPIC-8)")`

You can also choose epics that specify some dynamic criteria, for example, the epics with labels:

`(type=Epic and labels='myFeature') OR issue in childrenOfIssuesInQueryRecursive("type=Epic and labels='myFeature'")`

The above query could be limited to one project, or it can source the issues from multiple projects.

### Source a subset of initiatives with their full hierarchy

This use case is similar to the previous use case with epics. You can create a box that includes selected initiatives and all their children.

Depending on how initiatives are configured, you can use the following methods to source a subset of initiatives.

**Parent Link (Advanced roadmaps)**

If you use the Parent Link, then go with the `childrenOfIssuesInQueryRecursive` function:

`key in (INT-2, INT-5, INT-8) OR issue in childrenOfIssuesInQueryRecursive("key in (INT-2, INT-5, INT-8)")`

Or with more complex criteria:

`(type=Initiative and labels='myVision') OR issue in childrenOfIssuesInQueryRecursive("type=Initiative and labels='myVision'")`

### Link-based hierarchy

If your initiatives are link-based, use the `linkedIssuesOfQuery` function and a nested filter:

1. Create an [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) filter:   
   `key in (INT-2, INT-5, INT-8) OR issue in linkedIssuesOfQuery("key in (INT-2, INT-5, INT-8)", "your initiative link name")`  
   and call it “My initiatives and epics”
2. Create another filter that nests a filter created in step 1:  
   `filter="My initiatives and epics" OR issue in childrenOfIssuesInQueryRecursive("filter='My initiatives and epics'")`  
   This filter matches:

   1. the selected initiatives and the linked issues (epics)
   2. all levels of children of the linked epics
3. Use the filter as your scope in the box configuration

### Source issues linked to your project

You can use a filter to create a box that includes issues from your project and external issues linked to your project.

Use `project=MYPROJ OR linksIssueProject=MYPROJ or linkedByIssueProject=MYPROJ`.

If you only want to include the issues linked with the particular link type, you can create an [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/)filter:

`project=MYPROJ OR issue in linkedIssuesOfQuery("project=MYPROJ", "is blocked by")`

You can also get a full hierarchy of the linked issues by creating a nested filter:

1. Create an [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) filter:  
   `issue in linkedIssuesOfQuery("project=MYPROJ", "is blocked by")`  
   and call it “Blockers”
2. Create another filter that nests the first filter:  
   `project=MYPROJ OR filter="Blockers" OR issue in childrenOfIssuesInQueryRecursive("filter='Blockers'")`
3. Use the filter as your scope in the box configuration.

### Highlight the blocked tasks

Create a quick filter:

`linkType="is blocked by"`

You can now see what tasks are blocked by other tasks.

### Highlight the tasks with a high number of dependencies

Create a quick filter with JQL:

`linksCount>2`

You can see the tasks that have a specific number of links. In this example, all the tasks with more than 2 links are going to be highlighted.

### Highlight finished epics that have outstanding tasks

Create a quick filter with JQL:

`type=Epic and status=Done and issuesInEpicToDoCount>0 or issuesInEpicInProgressCount>0`

You can now see all the finished epics with tasks that need to be looked at.