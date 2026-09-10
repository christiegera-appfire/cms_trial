# Customer satisfaction

## Overview

A way to assess how the team is performing is by sending a survey to customers when a request is resolved. Then, review their comments and ratings to understand what went well, what went badly, and then improve your service levels.

This gadget is **multi-project**, so you can report across your whole portfolio of projects.

This gadget displays the customer satisfaction average rating in a period of time, together with the last customer satisfaction rating. It also displays a comparison with the previous period of time, to quickly evaluate if the team is doing better or needs improvement.

![Dashboard Hub Customer satisfaction](/cms_trial/assets/21eb187b-70ec-49ee-a3e7-41f496becafb.png)

## Configuration

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource**, where **Current** indicates the Jira Service Management instance where the app is installed.
- Data based on either

  - The **JQL (Jira Query Language) query or filter** to filter the list of issues (see the [JQL documentation](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/)). For example, to list all the issues of the project Teams in Space use the clause `project = "TIS”`. Remember that the gadget returns dynamically the query results, which are not fixed and could change over time.
  - Or the **projects** and the **queues** where the requests are. Ensure that you select a queue that displays closed issues, since the customer satisfaction feedback survey (CSAT) is sent when the issues are resolved.
- The **period of time** you want to display the customer satisfaction ratings.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring one by one the rest of the gadgets with the same default configuration

## Integrations

- [jira service management icon]

Jira Service Management

We are working on our growing catalog of [Dashboard gadgets - KPIs and metrics](/cms_trial/space/RDD/146309915/Dashboard+gadgets+-+KPIs+and+metrics/) and [Product and data connections](/cms_trial/space/RDD/146310010/Product+and+data+connections/), but contact us you want us to expedite a specific one, visit our [Help and support](/cms_trial/space/RDD/146309984/Help+and+support/).

## Dashboards

This gadget appears in the following dashboard: [IT Service Management team template](/cms_trial/space/RDD/146309962/IT+Service+Management+team+template/).