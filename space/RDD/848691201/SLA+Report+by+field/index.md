# SLA Report by field

## Overview

Track SLA performance based on selected fields so you can understand the impact of SLAs across various criteria. In service management, different fields can significantly impact SLA adherence - extracting insights here helps you ensure customer satisfaction.

This gadget displays the average SLA time and the percentage of SLAs met, broken down by the dimension in the selected field. For example, for a field called Customer, you could display two different SLAs for each of your customers.

The gadget also displays the Total Resolutions for each value of the selected field.

![Dashboard Hub sla report by field](/cms_trial/assets/e67b642f-011b-47b6-88f3-fb5883e43b36.png)

## Configuration

Name your gadget meaningfully so everyone knows at a glance what it's about and when to use it. Fill out the rest of the fields as applicable, namely:

- The datasource, where *This Jira instance* indicates the Jira Service Management instance where the app is installed.
- Data based on either

  - The JQL (Jira Query Language) query or filter to filter the list of issues (see the [JQL documentation](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/)). For example, to list all the issues in the Teams in Space project, use the clause `project = "TIS"`. Remember that the gadget dynamically returns the query results, which aren't fixed and can change over time.
  - Or the projects and queues the data comes from - remember that SLAs are found in Service Desk projects.
- The field to report on - this can be any Jira field or custom field.
- The First SLA and Second SLA fields specify which SLAs to retrieve.
- The period of time to retrieve the data from.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option saves you from configuring the rest of the gadgets one by one with the same default settings.

## Integrations

- [jira service management icon]

Jira Service Management

We are working on our growing catalog of [Dashboard gadgets - KPIs and metrics](/cms_trial/space/RDD/146309915/Dashboard+gadgets+-+KPIs+and+metrics/) and [Product and data connections](/cms_trial/space/RDD/146310010/Product+and+data+connections/), but contact us if you want us to expedite a specific one - visit our [Help and support](/cms_trial/space/RDD/146309984/Help+and+support/).

## Dashboards

This gadget appears in the following dashboard: [IT Service Management team template](/cms_trial/space/RDD/146309962/IT+Service+Management+team+template/).