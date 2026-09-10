# Service Desk Queue

## Overview

Queues are where the service desk team will spend most of their time, where the requests are triaged and prioritized. Queues also provide key information on issues, like the summary, status, customer, and very important, times. Times (spent, to first response, etc.) make us keep the focus, so SLAs are not breached.

This gadget displays a specific queue with the important information for each request. Visualizing a queue helps to align your team’s goals and acts as a to do list.

![Dashboard Hub Service Desk team's queue](/cms_trial/assets/57a29e43-d89d-4add-b14a-b77f45b91a2a.png)

## Configuration

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource**, where **Current** indicates the Jira Service Management instance where the app is installed.
- Data based on either

  - The **JQL (Jira Query Language) query or filter** to filter the list of issues (see the [JQL documentation](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/)). For example, to list all the issues of the project Teams in Space use the clause `project = "TIS”`. Remember that the gadget returns dynamically the query results, which are not fixed and could change over time.
  - Or the **project** and **queue** where the data comes from, remember that SLAs can be found in Service Desk projects.
- The **period of time** you want to display in the time series of the graph.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring one by one the rest of the gadgets with the same default configuration

## Integrations

- [jira service management icon]

Jira Service Management

We are working on our growing catalog of [Dashboard gadgets - KPIs and metrics](/cms_trial/space/RDD/146309915/Dashboard+gadgets+-+KPIs+and+metrics/) and [Product and data connections](/cms_trial/space/RDD/146310010/Product+and+data+connections/), but contact us you want us to expedite a specific one, visit our [Help and support](/cms_trial/space/RDD/146309984/Help+and+support/).

## Dashboards

This gadget appears in the following dashboard: [IT Service Management team template](/cms_trial/space/RDD/146309962/IT+Service+Management+team+template/).