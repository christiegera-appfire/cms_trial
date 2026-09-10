# Project Timesheet

## Overview

To properly manage a project with several assets and resources, timesheets are indispensable for project managers. Timesheets provide an overview of both, estimated and logged time, allowing to better keep track and discover bottlenecks or problems.

Projectrak allows the use of cumulative fields to see aggregated values of all issues in each project, making the most of time and duration fields to track times.

This gadget displays the timesheet of a list of projects (based on a PQL query) with their estimated and logged times (time spent and remaining). For each of the projects returned by the PQL query, the original estimate for the project as well as the amount of time spent and time remaining for each of the projects (including a percent value). Remember that you need to have populated these fields beforehand:

- **Original estimate:**A field in which you have the original estimate value for the project. You can select a Projectrak *Original Estimate* field.
- **Time spent:**The time spent is always based on the sum of all the time spent on the issues.
- **Remaining:**The **Remaining** estimate is the **Original estimate** minus the **Time spent**.

![Dashboard Hub Project Timesheet report configuration](/cms_trial/assets/2e9e0b30-73e0-4edc-a7dd-1be1f02a0117.png)![Dashboard Hub project timesheet](/cms_trial/assets/1cc9ae27-39da-484b-81f4-51a1a769a4bf.png)

In Projectrak you need to create a field **Time Spent** of type Cumulative (Server/Data Center) or Formula (Cloud) and add it to the layout of your projects.

![Dashboard Hub Time Spent](/cms_trial/assets/ca0cf97a-693c-48c7-991b-f497da28bf4f.png)

![Dashboard Hub Project Timesheet chart configuration](/cms_trial/assets/49ab1f04-1990-4fd2-9181-d6dac3b83be4.png)

## Configuration

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:The **datasource**, select a Projectrak datasource (see [Add and manage datasources](/cms_trial/space/RDD/146309293/Add+and+manage+datasources/)).

- The **datasource**, select a Projectrak datasource (see [Add and manage datasources](/cms_trial/space/RDD/146309293/Add+and+manage+datasources/)).
- The **Time Unit** format**,** select the format of the time result:

  - By default: e.g., 2w 1d 3h 15m
  - Days: e.g., 11d 3.2h
  - Hours: e.g., 91.2h
  - Pretty: e.g., 2 weeks 4 days 4 hours 30 minutes
- The **Original Estimate** field, select the project field that holds the original estimated time.
- The **Time Spent** field, select the project field that holds the time spent, either a cumulative (Server/Data Center) or a formula type.
- The **PQL (****Project** **Query Language) query** to filter the list of projects (see the DEISER’s Projectrak [Advanced search with PQL](https://confluence.deiser.com/projectrakcloud/advanced-search-with-pql-project-query-language-110955414.html) documentation). If you don’t add a PQL query and click “Load”, the gadget will request all the content in the source instance, this might cause performance issues. We recommend to add at least one clause, for example to list all the projects that are “On track” and the lead of those projects is the current user, use the clause `Status = "On track" and lead = currentUser()`. And remember that the gadget returns the results of the query, which are not fixed and could change over time.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring one by one the rest of the gadgets with the same default configuration.

## Integrations

- ![contentId-146311515](/cms_trial/assets/170f7f03-3d67-4945-87a4-838ee8cc3ebe.png)

Projectrak

We are working on our growing catalog of [Dashboard gadgets - KPIs and metrics](/cms_trial/space/RDD/146309915/Dashboard+gadgets+-+KPIs+and+metrics/) and [Product and data connections](/cms_trial/space/RDD/146310010/Product+and+data+connections/), but contact us you want us to expedite a specific one, visit our [Help and support](/cms_trial/space/RDD/146309984/Help+and+support/).

## Dashboards

This gadget appears in the following dashboard: [Project Tracking Insights template](/cms_trial/space/RDD/146310779/Project+Tracking+Insights+template/).