# Project Timeline

## Overview

A project timeline represents visually the overview of a project, when it starts, when it finishes, the amount of work pending, in progress and done… So it’s a schedule for your team, which helps to keep projects on track, avoid roadblocks and give a nice looking high-level overview.

This gadget displays the timeline of a set of projects, making the sometimes overwhelming duty of handling several deadlines at once, more manageable.

![Dashboard Hub project timeline](/cms_trial/assets/301611ee-f19c-4883-bb79-e083a14188cf.png)

The representation of the timeline for each project may have peculiarities depending on the existence of dates:

- If the project **has no creation date** (this happens when Projectrak has been installed after the project was created) but it **has an end date**, then, the starting of the timeline has a degraded color.
- If the project **has the creation date** (if Projectrak is installed when the project is created, then the creation date is set automatically) but it **has no end date**, then, the ending of the timeline has a degraded color.
- If the project has **no creation date nor end date**, then, there is no timeline.

Besides that, the timeline indicates the pending, in progress and done issues of each project. If you hover it, you’ll see the percentage and the number of issues in “To do”, “In progress” and/or “Done”.

Learn everything about Projectrak’s [Advanced search with PQL (Project query language)](https://confluence.deiser.com/projectrakcloud/advanced-search-with-pql-project-query-language-110955414.html)

## Configuration

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource**, select a Projectrak datasource (see [Add and manage datasources](/cms_trial/space/RDD/146309293/Add+and+manage+datasources/)).
- The **PQL (****Project** **Query Language) query** to filter the list of projects (see the DEISER’s Projectrak [Advanced search with PQL](https://confluence.deiser.com/projectrakcloud/advanced-search-with-pql-project-query-language-110955414.html) documentation). If you don’t add a PQL query and click “Load”, the gadget will request all the content in the source instance, this might cause performance issues. We recommend to add at least one clause, for example to list all the projects that are “On track” and the lead of those projects is the current user, use the clause `Status = "On track" and lead = currentUser()`. And remember that the gadget returns the results of the query, which are not fixed and could change over time.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring each of the remaining gadgets individually with the same default configuration.

## Integrations

- ![contentId-146311445](/cms_trial/assets/1b6c0239-b16c-4346-8559-f51887794ad2.png)

Projectrak

We are working on our growing catalog of [Dashboard gadgets - KPIs and metrics](/cms_trial/space/RDD/146309915/Dashboard+gadgets+-+KPIs+and+metrics/) and [Product and data connections](/cms_trial/space/RDD/146310010/Product+and+data+connections/), but contact us you want us to expedite a specific one, visit our [Help and support](/cms_trial/space/RDD/146309984/Help+and+support/).

## Dashboards

This gadget appears in the following dashboard: [Project Tracking Insights template](/cms_trial/space/RDD/146310779/Project+Tracking+Insights+template/).