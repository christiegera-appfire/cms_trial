# Agile sprints

The examples on this page describe how to build a JQL search using [JQL Search Extensions](https://marketplace.atlassian.com/plugins/jql-extensions/cloud/overview).

## Agile JQL functions

**JQL functions** are accessible from the [Extended Search](/cms_trial/space/JQLSEARCH/604209464/Extended+Search/) page or via [Extended Search filters](/cms_trial/space/JQLSEARCH/604209567/Extended+Search+filters/) in Jira advanced search. When using functions, the issues returned are based on the subquery defined in parentheses.

### nextSprint()

Find issues that are planned for the next sprint. Pass a Jira board name or board ID as an argument.

`issue in nextSprint("ACME board")`

`issue in nextSprint(10)`

### previousSprint()

Find issues that were part of a previous sprint. Pass a Jira board name or board ID as an argument.

`issue in previousSprint("ACME board")`

`issue in previousSprint(10)`

### addedToSprintAfterStart()

Find issues that were added to the sprint after the sprint was started. Handy to identify a scope creep in the sprint. Pass a Jira board name or board ID as a first argument. Optionally, pass a sprint name or sprint ID as a second argument. By default, the active sprint is used in the search.

`issue in addedToSprintAfterStart("ACME board")` - issues added after the current sprint was started

`issue in addedToSprintAfterStart("ACME board", "ACME Sprint 5")` - issues added after sprint 5 was started

`issue in addedToSprintAfterStart(10, 55)` - as above, using IDs