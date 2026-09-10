# Agents' Workload

## Overview

Service desk agents are the first point of contact between customers and our organization. They are natural problem solvers, so they will absorb as many requests as possible. But this comes at a price: Burnout and an increase in breaches of SLAs. That’s why it’s important to analyze the agents' workload and keep a balanced workload among the agents. On the other side, it’s also important for agents to compare themselves and see how they are doing.

This gadget displays the workload of agents for the **period selected**, with two SLAs. For example:

- **1st SLA as Time to resolution**. Indicates the average time of the time to resolution: Time from an issue creation until a resolution is provided. And also the % of SLA met for those issues.
- **2nd SLA as Time to first response**. Indicates the average time of the time to first response: Time from an issue creation until the first response is given. And also the % of SLA met for those issues.
- **Workload**. The workload of the agent indicates the total assigned requests out of the total requests.

The gadget also displays the **Total Resolutions** by agent in a bar chart. A resolution involves any way an issue can be closed.

We recommend selecting a queue with all the requests (for that period), so you’ll be able to see the workload but also the resolutions. Because if you choose a queue with all **unresolved** requests, the **total resolutions will be zero**.

However, you can also use a custom JQL or filter to retrieve your data.

![Dashboard Hub Agents' workload and info](/cms_trial/assets/07608060-af93-47ed-b6b0-a7465a590515.png)

## Configuration

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource**, where **This Jira instance** indicates the Jira Service Management instance where the app is installed.
- Data based on either

  - The **JQL (Jira Query Language) query or filter** to filter the list of issues (see the [JQL documentation](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/)). For example, to list all the issues of the project Teams in Space use the clause `project = "TIS”`. Remember that the gadget returns dynamically the query results, which are not fixed and could change over time.
  - Or the **projects** and **queues** where the data comes from, remember that SLAs can be found in Service Desk projects.
- The **First** and **Second SLA**, to display the SLAs to be retrieved.
- The **period** you want to analyze the workload of agents.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring one by one the rest of the gadgets with the same default configuration

## Integrations

- [jira service management icon]

Jira Service Management

We are working on our growing catalog of [Dashboard gadgets - KPIs and metrics](/cms_trial/space/RDD/146309915/Dashboard+gadgets+-+KPIs+and+metrics/) and [Product and data connections](/cms_trial/space/RDD/146310010/Product+and+data+connections/), but contact us you want us to expedite a specific one, visit our [Help and support](/cms_trial/space/RDD/146309984/Help+and+support/).

## Dashboards

This gadget appears in the following dashboard: [IT Service Management team template](/cms_trial/space/RDD/146309962/IT+Service+Management+team+template/).