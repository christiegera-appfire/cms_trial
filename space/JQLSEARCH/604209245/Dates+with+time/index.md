# Dates with time

Most Jira date fields also contain the time component. Jira doesn’t currently support convenient use of `=` and `IN` operators with timestamps. You should use the comparison operators instead: `<`, `<=`, `>`, `>=`

The following JQL keywords contain timestamps:

- **attachedOnDate**
- **updatedOnDates**
- **commentedOnDate**
- **commentUpdatedDate**

For example, this query fails to find issues commented on a particular day:   
`commentedOnDate="2020/06/01"`   
Jira returns an empty result even if there are issues that were commented on 1 June.

The workaround is to search for the range of dates:   
`commentedOnDate>="2020/06/01" AND commentedOnDate<"2020/06/02"`  
Jira returns issues that were commented between midnight 1 June and midnight 2 June.