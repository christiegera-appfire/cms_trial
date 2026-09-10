# Advanced Roadmaps

This article describes the integration points and possible use cases of JQL Search Extensions with Advanced Roadmaps.

Advanced Roadmaps is a feature of Jira Premium that is used for project management and project portfolio management. You can leverage its power with the additional JQL keywords and functions provided by **JQL Search Extensions**.

## Integration points

## Scope definition

JQL Search Extensions helps define a precise scope of an Advanced Roadmaps plan. You can source issues with additional JQL keywords and [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) filters.

It’s possible, for example, to have a plan with a subset of initiatives or epics and their children. You will typically create the [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) filter for the board and reuse it in the plan.

![contentId-604209557](/cms_trial/assets/9de6c7d1-599e-4d96-ae59-9b721a7a6fc0.png)

**To use a filter in Advanced Roadmaps:**

1. Create a filter in [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/).
2. Select the filter in the plan configuration: **Configure** > **Issue sources**.

Refer to the examples in the Use Cases section below.

## External use

It’s a common requirement to access the contents of a plan outside of Advanced Roadmaps, for example, to create a report in a third-party app or tool.

If you define the scope with a Jira filter, you can use this filter in:

- dashboard gadgets
- boards
- Jira search - simply use this syntax `filter="Your filter name"`
- Third-party apps that accept filters and JQL

## Use cases

## Source a subset of epics with their full hierarchy

You don’t need to add a whole Jira project to the scope of a plan. You can create a plan that includes selected epics, their associated stories, and subtasks.

If you have a list of specific epic keys that should be in scope, run and save the following query as a filter and use it as a scope:

`key in (EPIC-2, EPIC-5, EPIC-8) OR issue in childrenOfIssuesInQueryRecursive("key in (EPIC-2, EPIC-5, EPIC-8)")`

You can also choose epics that specify some dynamic criteria, for example, the epics with labels:

`(type=Epic and labels='myFeature') OR issue in childrenOfIssuesInQueryRecursive("type=Epic and labels='myFeature'")`

The above query could be limited to one project or it can source the issues from multiple projects.

## Source a subset of initiatives with their full hierarchy

This use case is similar to the previous use case with epics. You can create a plan that includes selected initiatives and all their associated initiatives.

Use the `childrenOfIssuesInQueryRecursive` function:

`key in (INT-2, INT-5, INT-8) OR issue in childrenOfIssuesInQueryRecursive("key in (INT-2, INT-5, INT-8)")`

Or with more complex criteria:

`(type=Initiative and labels='myVision') OR issue in childrenOfIssuesInQueryRecursive("type=Initiative and labels='myVision'")`

## Source issues linked to your project

You can create a plan that includes issues from your project and external issues linked to your project.

`project=MYPROJ OR linksIssueProject=MYPROJ or linkedByIssueProject=MYPROJ`

If you only want to include the issues linked with the particular link type, you can create, run, and save the following query as a filter:

`project=MYPROJ OR issue in linkedIssuesOfQuery("project=MYPROJ", "is blocked by")`

You can also get a full hierarchy of the linked issues by creating a nested filter:

1. Create a filter with:  
   `issue in linkedIssuesOfQuery("project=MYPROJ", "is blocked by")`  
   and call it `Blockers`
2. Create another filter that nests the first filter:  
   `project=MYPROJ OR filter="Blockers" OR issue in childrenOfIssuesInQueryRecursive("filter='Blockers'")`.
3. Use the filter as your scope in the plan configuration.