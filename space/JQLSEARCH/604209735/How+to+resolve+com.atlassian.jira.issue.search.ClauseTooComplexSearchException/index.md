# How to resolve com.atlassian.jira.issue.search.ClauseTooComplexSearchException

## Warning in the search regarding luceneClauseParamsLimit

```text
"Function linksCountEqualTo returns more issues than defined by luceneClauseParamsLimit! Read more about it in our documentation https://jqlsearchextensions.atlassian.net/wiki/spaces/JQLSEARCH/pages/1227554844/How+to+solve+com.atlassian.jira.issue.search.ClauseTooComplexSearchException"
```

Our functions are protected from exceeding *luceneClauseParamsLimit*. The above warning message can appear after the search. This will most commonly happen on large Jira instances after searching for `issue in linksCountEqualTo(0) or issue in linksCountLessThan(10)` because they will return all issues without links or all issues with less than 10 links (which in most cases mean all issues from the instance). To resolve this, you can use this negation in your query, for example, to find all issues without links, you can search `issue not in linksCountGreaterThan(0)`, which returns far fewer issues and results are not trimmed.

## Error in the logs ClauseTooComplexSearchException

If JQL Search Extensions functions return 0 results and a line like the one below is printed to the logs, it means you are affected by a [known Jira issue](https://jira.atlassian.com/browse/JRASERVER-19350) [JRASERVER-19350].

```text
2019-07-29 02:16:42,245 http-nio-80-exec-116 ERROR ra185165 136x31430237x9 6e0p70 153.53.2.125,192.127.253.68 /rest/issueNav/1/issueTable [c.a.j.p.i.service.issuetable.DefaultIssueTableService]com.atlassian.jira.issue.search.ClauseTooComplexSearchException: A the following query was too complex to generate a query from: {issue in functionName()}
```

### How this affects you

To evaluate JQL search, Jira uses the Apache Lucene framework. To protect Lucene (and your Jira instance) against extremely large queries, there is a limit to the number of issues that can be returned by a JQL function. By default, Jira has this limit configured to 65,000 issues, so whenever the JQL function returns a larger number of issues, the query will fail to evaluate and produce the logline mentioned above.

### How to resolve this issue

It is possible to raise the limit by setting the Jira property, jira.search. max clause. However, this can impact performance and should be tested on your installation. To understand the impact of raising this limit, see our [Performance test results](/cms_trial/space/JQLSEARCH/604209740/Performance+tests+results/) page. Generally, if your instance has some spare CPU and memory during day-to-day activity, it is reasonable to increase the limit.

To raise the limit, follow the steps in Atlassian’s documentation: <https://confluence.atlassian.com/jirakb/how-to-edit-the-jira-config-properties-file-317194938.html>

1. Edit (or create if missing) `jira-config.properties` which should be under the Jira Home directory.
2. Search for an entry called `jira.search.maxclause` (if there is no such entry, create a new one).
3. Set the value for `jira.search.maxclause` to the number that will suit your instance, for example 120000.

   ```text
   jira.search.maxclauses = 120000
   ```
4. Restart Jira and verify that the problem is resolved by running your query again.