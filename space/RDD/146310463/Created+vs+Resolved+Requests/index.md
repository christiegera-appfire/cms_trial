# Created vs Resolved Requests

## Overview

When your customers are creating more requests than the ones the teams can resolve, your queues are creating a debt. And this debt means that requests take longer to be resolved, so it impacts in an increase of SLA breaches, bad reviews, and lower customer satisfaction.

This gadget is **multi-project**, so you can report across your whole portfolio of projects

This gadget displays the number of requests created and resolved from specific queue of your service desk over a period of time:

- Total count of requests created and resolved.
- A graph with the timeline of requests created and resolved. When the red line exceeds the green, it indicates that customers are generating more requests than the team is resolving.
- A pie chart comparing the percentages of created vs resolved.

![Dashboard Hub created vs resolved](/cms_trial/assets/be57a87d-2507-4998-8753-0acb13217a6d.png)

## Configuration

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource**, where **Current** indicates the Jira Service Management instance where the app is installed.
- Data based on either

  - The **JQL (Jira Query Language) query or filter** to filter the list of issues (see the [JQL documentation](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/)). For example, to list all the issues of the project Teams in Space use the clause `project = "TIS”`. Remember that the gadget returns dynamically the query results, which are not fixed and could change over time.
  - Or the **projects** and **queues** where the data comes from, remember that SLAs can be found in Service Desk projects.
- The **period of time** you want to display statistics of the requests.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring one by one the rest of the gadgets with the same default configuration

## Integrations

- [jira service management icon]

Jira Service Management

We are working on our growing catalog of [Dashboard gadgets - KPIs and metrics](/cms_trial/space/RDD/146309915/Dashboard+gadgets+-+KPIs+and+metrics/) and [Product and data connections](/cms_trial/space/RDD/146310010/Product+and+data+connections/), but contact us you want us to expedite a specific one, visit our [Help and support](/cms_trial/space/RDD/146309984/Help+and+support/).

## Dashboards

This gadget appears in the following dashboard: [IT Service Management team template](/cms_trial/space/RDD/146309962/IT+Service+Management+team+template/).