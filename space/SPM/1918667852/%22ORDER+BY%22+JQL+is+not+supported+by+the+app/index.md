# "ORDER BY" JQL is not supported by the app

JQL related to the order in which tasks are displayed conflicts with how the module shows tasks - therefore, it can’t be executed.

For example:

```text
order by "Start date" ASC
```

"ORDER BY" JQL is ignored, but the rest of the query is executed normally.

```text
"ORDER BY" JQL keyword is not supported by the App and was ignored. The rest of the query was executed.
```

ℹ️**This restriction applies to both JQL-based Quick Filters and manual use of JQL related to search functionality.**