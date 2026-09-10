# Project by Status

## Overview

When in charge of a portfolio (programs and individual projects), the quickest indicator a manager has is the project status. The project status indicates in a single word the current stage of the project. Then, further details like the key accomplishments, upcoming milestones, consumed resources, etc. are displayed in the individual project report.

Projectrak allows you to track and monitor KPIs and metrics to support business decisions, and charts like the Project by Status gadget are key to summarize the portfolio's overall progress and keep all stakeholders informed of progress at the same time.

This gadget displays the percentage of projects per status in a pie chart, from the set of projects returned by a PQL query.

![Dashboard Hub project by status](/cms_trial/assets/d02b7e5b-e39d-4950-9d39-f4fc8f07c2ee.png)

## Configuration

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource**, select a Projectrak datasource (see [Add and manage datasources](/cms_trial/space/RDD/146309293/Add+and+manage+datasources/)).
- The **PQL (****Projec****t Query Language) query** to filter the list of projects (see the DEISER’s Projectrak [Advanced search with PQL](https://confluence.deiser.com/projectrakcloud/advanced-search-with-pql-project-query-language-110955414.html) documentation). If you don’t add a PQL query and click “Load”, the gadget will request all the content in the source instance, this might cause performance issues. We recommend to add at least one clause, for example to list all the projects that are “On track” and the lead of those projects is the current user, use the clause `Status = "On track" and lead = currentUser()`. And remember that the gadget returns the results of the query, which are not fixed and could change over time.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring one by one the rest of the gadgets with the same default configuration.

## Integrations

- ![contentId-146311373](/cms_trial/assets/52efb4ac-b02d-435e-ac97-de38167c1a70.png)

Projectrak

We are working on our growing catalog of [Dashboard gadgets - KPIs and metrics](/cms_trial/space/RDD/146309915/Dashboard+gadgets+-+KPIs+and+metrics/) and [Product and data connections](/cms_trial/space/RDD/146310010/Product+and+data+connections/), but contact us you want us to expedite a specific one, visit our [Help and support](/cms_trial/space/RDD/146309984/Help+and+support/).

## Dashboards

This gadget appears in the following dashboard: [Project Tracking Insights template](/cms_trial/space/RDD/146310779/Project+Tracking+Insights+template/).