# Performance tests results

## How tests were executed

The machine on which tests were executed has 16GB of RAM memory (1600MHz), a PLEXTOR PX-256M5 SSD drive, and a single Intel Core i7 4790K 4.00 GHz processor.

Tests were executed on Jira 7.4, running against Postgres 9.6. The instance has:

- Issues: 1,053,030
- Issues that were moved: 1,000,000
- Comments: 4,029,535
- Projects: 402
- Worklogs: 1,504,565

Each query in the results was executed 50 times to collect min/max/avg values. There were five concurrent threads executing the query one after another (so at any given time Jira was running five searches concurrently).

## Testing impact of jira.search.maxclause

The following tests measured the impact of raising **jira.search.maxclause** limit to a higher value than the default (65k). To better understand what this limit is and how to raise it, see [How to resolve com.atlassian.jira.issue.search.ClauseTooComplexSearchException](/cms_trial/space/JQLSEARCH/604209735/How+to+resolve+com.atlassian.jira.issue.search.ClauseTooComplexSearchException/) .

| **Query** | **jira.search.maxclause** | **Min** | **Max** | **Avg** |
| --- | --- | --- | --- | --- |
| issue in movedIssues() | 65000 | 1.145sec | 2.555sec | 1.637sec |
| issue in commentedAfter("2018-05-26") | 65000 | 0.721sec | 1.176sec | 0.921sec |
| issue in commentsCountLessThan("10") | 65000 | 0.665sec | 1.604sec | 0.912sec |

| **Query** | **jira.search.maxclause** | **Min** | **Max** | **Avg** |
| --- | --- | --- | --- | --- |
| issue in movedIssues() | 130000 | 1.790sec | 5.876sec | 2.724sec |
| issue in commentedAfter("2018-05-26") | 130000 | 1.360sec | 3.069sec | 2.153sec |
| issue in commentsCountLessThan("10") | 130000 | 1.170sec | 2.544sec | 1.874sec |

| **Query** | **jira.search.maxclause** | **Min** | **Max** | **Avg** |
| --- | --- | --- | --- | --- |
| issue in movedIssues() | 260000 | 5.483sec | 10.201sec | 7.050sec |
| issue in commentedAfter("2018-05-26") | 260000 | 4.388sec | 9.744sec | 6.254sec |
| issue in commentsCountLessThan("10") | 260000 | 2.357sec | 7.571sec | 5.370sec |

Memory was raised to 4GB for 500k jira.search.maxclause, to stay within GC Overhead limit.

| **Query** | **jira.search.maxclause** | **Min** | **Max** | **Avg** |
| --- | --- | --- | --- | --- |
| issue in movedIssues() | 500000 | 5.686sec | 11.345sec | 9.099sec |
| issue in commentedAfter("2018-05-26") | 500000 | 5.316sec | 13.021sec | 10.422sec |
| issue in commentsCountLessThan("10") | 500000 | 8.069sec | 12.272sec | 9.973sec |

### Conclusions

Raising the limit or jira.search. max clause will require more CPU and memory; it all depends on the machine that Jira is running on. Before raising the limit to higher values, we recommend that you ensure the server has enough CPU power.

## Performance of non-subquery-based functions

The following tests were executed with Jira.search. max clause limit of 65,000. Not all of the functions returned the number of issues equal to the limit. For example, *issue in movedIssues()* returned issues over the limit, but *issue in movedIssues("ABII")* returned around 6k issues, which is a more realistic scenario.

| **Query** | **Min** | **Max** | **Avg** |
| --- | --- | --- | --- |
| issue in movedIssues() | 1.219sec | 5.733sec | 1.851sec |
| issue in movedIssues("ABII") | 0.394sec | 0.960sec | 0.528sec |
| issue in commentedAfter("2018-05-26") | 0.715sec | 1.434sec | 0.889sec |
| issue in commentedAfter("2019-06-26") | 1.946sec | 5.860sec | 2.911sec |
| issue in commentedBefore("2018-10-26") | 0.906sec | 1.520sec | 1.102sec |
| issue in commentedByUser("admin") | 0.708sec | 5.846sec | 4.242sec |
| issue in commentedByUser(taahonmrs) | 1.967sec | 3.082sec | 2.812sec |
| issue in commentsCountLessThan("10") | 0.655sec | 0.933sec | 0.743sec |
| issue in commentsCountGreaterThan(4) | 0.733sec | 1.383sec | 0.931sec |
| issue in linksCountLessThan(1) | 1.441sec | 1.826sec | 1.592sec |
| issue in linksCountGreaterThan(1) | 1.685sec | 2.238sec | 1.845sec |
| issue in subtaskCountGreaterThan("1") | 0.911sec | 1.677sec | 1.088sec |
| issue in subtaskCountLessThan("2") | 0.670sec | 1.017sec | 0.824sec |
| issue in subTaskPriority("low") | 1.118sec | 2.027sec | 1.343sec |
| issue in subTaskPriority("low", "high", "highest", "lowest", "medium") | 1.661sec | 2.134sec | 1.894sec |
| issue in subTaskType("Sub-Task", "SubtaskType2", "SubtaskType3", "SubtaskType4", "SubtaskType5", "SubtaskType6", "SubtaskType7", "SubtaskType8", "SubtaskType9", "SubtaskType10", "SubtaskType11", "SubtaskType12", "SubtaskType13", "SubtaskType14", "SubtaskType15", "SubtaskType16", "SubtaskType17", "SubtaskType18", "SubtaskType19", "SubtaskType20", "SubtaskType21") | 1.729sec | 2.539sec | 2.032sec |
| issue in subTaskStatus("In Progress", "To Do", "Done", "Reopened", "Closed", "Resolved") | 1.684sec | 2.162sec | 1.918sec |
| issue in subTaskStatusCategory("To Do", "In Progress", "Done") | 1.754sec | 2.249sec | 1.953sec |

The following chart shows the CPU and memory footprint on the JVM that Jira was running on.

![CPU and Memory impact on the JVM running Jira](/cms_trial/assets/368b5bc1-d1b9-48d8-bf12-f585248e7868.png)See time results for jira.search.maxclause limit of 500k

| **Query** | **Min** | **Max** | **Avg** |
| --- | --- | --- | --- |
| issue in movedIssues() | 4.365sec | 12.662sec | 9.544sec |
| issue in movedIssues("ABII") | 0.399sec | 1.055sec | 0.521sec |
| issue in commentedAfter("2018-05-26") | 7.094sec | 12.432sec | 10.880sec |
| issue in commentedAfter("2019-06-26") | 2.308sec | 6.657sec | 4.551sec |
| issue in commentedBefore("2018-10-26") | 4.076sec | 10.076sec | 6.297sec |
| issue in commentedByUser("admin") | 3.834sec | 14.821sec | 11.728sec |
| issue in commentedByUser(taahonmrs) | 2.080sec | 3.128sec | 2.702sec |
| issue in commentsCountLessThan("10") | 8.532sec | 12.416sec | 10.391sec |
| issue in commentsCountGreaterThan(4) | 4.205sec | 6.999sec | 5.964sec |
| issue in linksCountLessThan(1) | 9.604sec | 12.550sec | 11.595sec |
| issue in linksCountGreaterThan(1) | 1.720sec | 2.162sec | 1.957sec |
| issue in subtaskCountGreaterThan("1") | 0.861sec | 1.302sec | 1.043sec |
| issue in subtaskCountLessThan("2") | 1.499sec | 2.705sec | 1.795sec |
| issue in subTaskPriority("low") | 1.121sec | 1.848sec | 1.319sec |
| issue in subTaskPriority("low", "high", "highest", "lowest", "medium") | 1.797sec | 2.164sec | 1.949sec |
| issue in subTaskType("Sub-Task", "SubtaskType2", "SubtaskType3", "SubtaskType4", "SubtaskType5", "SubtaskType6", "SubtaskType7", "SubtaskType8", "SubtaskType9", "SubtaskType10", "SubtaskType11", "SubtaskType12", "SubtaskType13", "SubtaskType14", "SubtaskType15", "SubtaskType16", "SubtaskType17", "SubtaskType18", "SubtaskType19", "SubtaskType20", "SubtaskType21") | 1.795sec | 2.246sec | 1.938sec |
| issue in subTaskStatus("In Progress", "To Do", "Done", "Reopened", "Closed", "Resolved") | 1.784sec | 2.289sec | 1.939sec |
| issue in subTaskStatusCategory("To Do", "In Progress", "Done") | 1.781sec | 2.593sec | 2.024sec |

## Testing the impact of the subquery limit

The following table presents the timings of JQL functions that accept subqueries. To prevent instances from running out of memory or becoming unstable due to the impact generated on the Lucene index, we developed a protection that will load no more issues than the specified limit. The default value is 10,000 which can be too low for bigger instances. This limit can be raised by setting a systemProperty called ***com.digitaltoucan.jqlextensions.subquery.limit***(this, however, comes with a performance impact). To raise the limit, refer to [Subquery limits](/cms_trial/space/JQLSEARCH/604209716/Subquery+limits/). Instead of increasing the limit to larger numbers, we recommend restricting the number of issues through a query. For example, instead of loading all issues in the subquery, try to load only issues from a given project, or only issues that are still open.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Query** | **SubQuery limit** | **Min** | **Max** | **Avg** |
| issue in allIssuesInEpic("") | 5000 | 0.669sec | 1.587sec | 0.855sec |
| issue in allIssuesInEpic("") | 10000 | 1.172sec | 1.449sec | 1.287sec |
| issue in allIssuesInEpic("") | 20000 | 2.264sec | 2.702sec | 2.416sec |
| issue in allIssuesInEpic("") | 30000 | 3.215sec | 4.634sec | 3.514sec |
| issue in allIssuesInEpic("resolution is Empty") | 5000 | 0.687sec | 0.911sec | 0.777sec |
| issue in allIssuesInEpic("resolution is Empty") | 10000 | 1.212sec | 1.477sec | 1.322sec |
| issue in allIssuesInEpic("resolution is Empty") | 20000 | 2.322sec | 2.892sec | 2.496sec |
| issue in allIssuesInEpic("resolution is Empty") | 30000 | 3.302sec | 4.002sec | 3.552sec |
| issue in epicOf("") | 5000 | 0.804sec | 0.986sec | 0.868sec |
| issue in epicOf("") | 10000 | 1.594sec | 1.727sec | 1.653sec |
| issue in epicOf("") | 20000 | 2.997sec | 3.811sec | 3.188sec |
| issue in epicOf("") | 30000 | 4.558sec | 5.436sec | 5.031sec |
| issue in epicOf("\"Epic Link\" is not Empty") | 5000 | 0.538sec | 0.700sec | 0.600sec |
| issue in epicOf("\"Epic Link\" is not Empty") | 10000 | 0.538sec | 0.684sec | 0.594sec |
| issue in epicOf("\"Epic Link\" is not Empty") | 20000 | 0.528sec | 0.654sec | 0.586sec |
| issue in epicOf("\"Epic Link\" is not Empty") | 30000 | 0.472sec | 0.755sec | 0.576sec |
| issue in fieldMatch("", "summary", ".\*") | 5000 | 0.333sec | 0.633sec | 0.424sec |
| issue in fieldMatch("", "summary", ".\*") | 10000 | 0.523sec | 0.689sec | 0.579sec |
| issue in fieldMatch("", "summary", ".\*") | 20000 | 0.879sec | 1.058sec | 0.966sec |
| issue in fieldMatch("", "summary", ".\*") | 30000 | 1.239sec | 1.880sec | 1.384sec |
| issue in fieldMatch("project = SFTSFTS", "summary", ".\*") | 5000 | 0.236sec | 0.585sec | 0.324sec |
| issue in fieldMatch("project = SFTSFTS", "summary", ".\*") | 10000 | 0.415sec | 0.686sec | 0.477sec |
| issue in fieldMatch("project = SFTSFTS", "summary", ".\*") | 20000 | 0.715sec | 1.194sec | 0.826sec |
| issue in fieldMatch("project = SFTSFTS", "summary", ".\*") | 30000 | 1.026sec | 1.558sec | 1.123sec |
| issue in fieldsHaveSameValue("fixVersion", "affectedVersion") | 5000 | 0.358sec | 0.462sec | 0.399sec |
| issue in fieldsHaveSameValue("fixVersion", "affectedVersion") | 10000 | 0.508sec | 0.666sec | 0.566sec |
| issue in fieldsHaveSameValue("fixVersion", "affectedVersion") | 20000 | 0.864sec | 1.322sec | 0.959sec |
| issue in fieldsHaveSameValue("fixVersion", "affectedVersion") | 30000 | 1.203sec | 1.701sec | 1.349sec |
| issue in parentOf("") | 5000 | 0.241sec | 0.385sec | 0.298sec |
| issue in parentOf("") | 10000 | 0.374sec | 0.539sec | 0.431sec |
| issue in parentOf("") | 20000 | 0.697sec | 0.806sec | 0.743sec |
| issue in parentOf("") | 30000 | 0.931sec | 1.134sec | 1.030sec |
| issue in parentOf("issuetype in subTaskIssueTypes()") | 5000 | 0.299sec | 0.507sec | 0.354sec |
| issue in parentOf("issuetype in subTaskIssueTypes()") | 10000 | 0.462sec | 0.600sec | 0.512sec |
| issue in parentOf("issuetype in subTaskIssueTypes()") | 20000 | 0.739sec | 1.276sec | 0.854sec |
| issue in parentOf("issuetype in subTaskIssueTypes()") | 30000 | 0.985sec | 1.659sec | 1.144sec |
| issue in subtaskOf("") | 5000 | 0.403sec | 0.761sec | 0.574sec |
| issue in subtaskOf("") | 10000 | 0.648sec | 1.006sec | 0.864sec |
| issue in subtaskOf("") | 20000 | 1.405sec | 1.740sec | 1.540sec |
| issue in subtaskOf("") | 30000 | 2.180sec | 3.043sec | 2.617sec |
| issue in links("", "blocks") | 5000 | 0.314sec | 0.781sec | 0.421sec |
| issue in links("", "blocks") | 10000 | 0.529sec | 0.793sec | 0.627sec |
| issue in links("", "blocks") | 20000 | 1.094sec | 1.843sec | 1.293sec |
| issue in links("", "blocks") | 30000 | 1.475sec | 2.487sec | 1.979sec |
| issue in linkedBy("", "is blocked by") | 5000 | 0.320sec | 0.650sec | 0.392sec |
| issue in linkedBy("", "is blocked by") | 10000 | 0.524sec | 0.676sec | 0.606sec |
| issue in linkedBy("", "is blocked by") | 20000 | 1.070sec | 2.112sec | 1.262sec |
| issue in linkedBy("", "is blocked by") | 30000 | 1.658sec | 2.359sec | 2.031sec |