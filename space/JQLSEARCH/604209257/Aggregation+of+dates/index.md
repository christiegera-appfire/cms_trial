# Aggregation of dates

In case there are more than 100 timestamps to be stored for a particular date related JQL keyword the timestamps will be aggregated by day with time reset to start of the day (midnight). This means that the keyword won't be time sensitive, it will only be date sensitive for a particular Jira issue.

This applies to the following keywords:

- **attachedOnDate**
- **updatedOnDates**
- **commentedOnDate**
- **commentUpdatedDate**

For example if the issue was updated 150 times over a course of 5 days, the updatedOnDates queries for that particular issue will see 5 timestamps for each day only.