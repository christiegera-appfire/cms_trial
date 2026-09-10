# Project Leaders Workload

## Overview

Projectrak (in its server/DC versions) comes with an option to bulk replace a project lead from specific projects. And it’s not by chance but because there’s a physical limit for leaders on the number of projects they can handle. Each project has its own peculiarities, deadlines, budgets and associated stress, which often leads to burnout and fatigue.

This gadget provides a chart to easily visualize how many projects a leader has assigned, with its corresponding % calculated from the result of the PQL query. Similar to the [Project Stakeholders Workload](/cms_trial/space/RDD/146311454/Project+Stakeholders+Workload/), but with the focus on highlighting which leaders are more active in the organization.

![Dashboard Hub project leaders workload](/cms_trial/assets/ed480700-0ef6-464f-b874-3b842cb9e8ba.png)

## Configuration

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource**, select a Projectrak datasource (see [Add and manage datasources](/cms_trial/space/RDD/146309293/Add+and+manage+datasources/)).
- The **PQL (****Projec****t Query Language) query** to filter the list of projects (see the DEISER’s Projectrak [Advanced search with PQL](https://confluence.deiser.com/projectrakcloud/advanced-search-with-pql-project-query-language-110955414.html) documentation). If you don’t add a PQL query and click “Load”, the gadget will request all the content in the source instance, this might cause performance issues. We recommend to add at least one clause, for example to list all the projects that are “On track” and the lead of those projects is the current user, use the clause `Status = "On track" and lead = currentUser()`. And remember that the gadget returns the results of the query, which are not fixed and could change over time.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring one by one the rest of the gadgets with the same default configuration

## Integrations

- ![contentId-146311498](/cms_trial/assets/c502527a-5813-4920-b289-b1a5d9aa7152.png)

Projectrak

We are working on our growing catalog of [Dashboard gadgets - KPIs and metrics](/cms_trial/space/RDD/146309915/Dashboard+gadgets+-+KPIs+and+metrics/) and [Product and data connections](/cms_trial/space/RDD/146310010/Product+and+data+connections/), but contact us you want us to expedite a specific one, visit our [Help and support](/cms_trial/space/RDD/146309984/Help+and+support/).

## Dashboards

This gadget appears in the following dashboard: [Project Tracking Insights template](/cms_trial/space/RDD/146310779/Project+Tracking+Insights+template/).