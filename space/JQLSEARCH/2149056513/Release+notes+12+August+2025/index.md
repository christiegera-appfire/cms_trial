# Release notes 12 August 2025

**Release date**: August 12, 2025

Our team is pleased to announce the latest release of JQL Search Extensions for Jira Cloud.

---

## New features

## Popular functions available during initial indexing

You can now try searching with the following JQL Search Extensions functions before the initial indexing process is complete:

- linkedIssuesOfQuery()
- childrenOfIssuesInQuery()
- childrenOfIssuesInQueryRecursive()
- parentsOfIssuesInQuery()
- parentsOfIssuesInQueryRecursive()
- wildcardMatch()

This update lets you get started with the app right away instead of waiting for the entire indexing process to be complete.

## Enhancements

## Support for floating dates

You can now add units to the expressions for the `dateCompare` and `dateCompareIgnoreTime` functions to compare a date with a floating date instead of a fixed date.

You can use + or - with the following units:

- `y` - Years
- `M` - Months
- `w` - Weeks
- `d` - Days
- `h` - Hours
- `m` - Minutes

### Examples

```text
issue in dateCompare(“resolutiondate +1d < duedate +1w”) AND project = DEV
```

```text
issue in dateCompareIgnoreTime (“resolutiondate +1d < duedate +1w”) AND project = DEV
```

See the [Date Compare functions](/cms_trial/space/JQLSEARCH/604209909/Field+values/) to learn more about using dates in queries.

---

## Bug fixes

The following bug fix is included in this release summary.

- **Incorrect data shown in the table of returned issues**: The Resolution and Assignee columns now show the correct data for the returned issues.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/1214791/jql-search-extensions-for-jira?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket with our [support team](https://appf.re/support).
- Do you love using our app? [Let us know](https://marketplace.atlassian.com/apps/1214791/jql-search-extensions-for-jira?hosting=cloud&tab=reviews) what you think.

**Credits**

Thank you to our valued customers. You are the driving force behind why we create software, and we appreciate your trust in JQL Search Extensions!