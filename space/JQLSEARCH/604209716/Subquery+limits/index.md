# Subquery limits

## What is a subquery limit?

Some JQL Search Extensions functions allow you to specify a subquery JQL, for example,  `allIssuesInEpic` function. This subquery function can be matched anywhere from 0 to all issues of your instance, which, in very large instances, could cause some trouble. To protect your Jira instance from outages, extensive CPU or memory usage, or simply overloading the Jira Lucene index, JQL subquery-based functions are protected with a limit. By default, this limit is configured to 10,000 issues, however, instances running on strong server machines can process more than 10,000 issues without trouble. A Jira administrator can raise the limit if needed. To learn more about the impact this limit has on JQL execution, see our [performance test results](/cms_trial/space/JQLSEARCH/604209740/Performance+tests+results/) page.

## Functions affected by the subquery limit

- allIssuesInEpic
- epicOf
- fieldMatch
- fieldsHaveSameValue
- parentOf
- subtaskOf
- links
- linkedBy

## How to raise the limit

The subquery limit can be raised by specifying a system property called *com.digitaltoucan.jqlextensions.subquery.limit*. For example, to raise the limit to 30,000 you need to configure a system property to:

```text
-Dcom.digitaltoucan.jqlextensions.subquery.limit=30000
```

To learn how to set a system property on a Jira instance, refer to Atlassian’s Jira documentation page <https://confluence.atlassian.com/adminjiraserver/setting-properties-and-options-on-startup-938847831.html>