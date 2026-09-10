# JQL Search Extensions - Data Center

## What is JQL Search Extensions for Jira Data Center (JSE)?

JSE for Jira Data Center provides more than 50 JQL extensions to deliver more precise and flexible searching in Jira. It improves issue tracking, including filtering by attachments, links, subtasks, comments, and versions, which is especially useful in managing large projects and instances. Users can share saved filters across teams to enhance collaboration and reduce time spent searching.

### Use the additional functions directly in Jira’s advanced search

All the extensions are implemented as JQL **functions** that perform calculations with the value used in `()`. All functions are preceded by `issue in`, for example, `issue in commentedBefore("2022-09-11")`.

See our complete list of functions on the [JQL functions reference](/cms_trial/space/JQLSEARCH/1865482654/JQL+functions+reference/) page.

For Jira Cloud, many of our JQL extensions are implemented as JQL **keywords** as references to issue metadata, resulting in indexed searches. Keywords are followed by operators, for example, `commentedOnDate < "2018-05-26"`. Looking to migrate to Jira Cloud? Learn more about the differences between our apps on the Migrations page.