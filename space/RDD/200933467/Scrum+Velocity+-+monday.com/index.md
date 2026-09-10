# Scrum Velocity - monday.com

## Overview

Velocity in Agile teams using Scrum has been a central topic of many discussions. It’s due that is a key metric to forecast delivery dates and set the number of product backlog tasks to plan in upcoming sprints. Putting discussions aside, having a way to measure the work is a great help for many teams, so we created this gadget.

The **Scrum Velocity** chart gadget shows the velocity of your Scrum team. This velocity is calculated based on the average of completed estimates from a set of sprints.

![Dashboard Hub Scrum Velocity monday.com chart preview](/cms_trial/assets/36e998da-3c98-44b9-a094-d262fc9716da.png)

### Sprints

The sprints are located in the selected workspace, in the *Sprints* board. By default, the **last 5 sprints are displayed**, but users can select 3, 5, 10, 25, or 50 sprints among the previously selected project/boards.

**Filter by sprint state**

In case you want to display sprints in a specific state (active, future and/or closed), just select the state(s) to be filtered.

### Metrics to display

By default, two metrics are always displayed:

**Commitment**: The amount of work in the sprint when it began. The bar/line for each sprint shows the total estimate of all issues in the sprint when it begins. After the sprint has started, any stories added to the sprint, or any changes made to estimates, will not be included in this total.

**Completed**: The amount of work done during the sprint. The bar/line in each sprint shows the total completed estimates when the sprint ends. Any scope changes made after the sprint started are included in this total.

Optional metrics that can be selected:

**Reopened**: The amount of work due to issues reopened during a sprint.

**Added**: How much work was added to a sprint after its start (estimation of issues added to sprint).

**Estimate Change**: The amount of work due to changes in the estimation of **story points** changes.

**Pending**: Represents the total amount of work left in the sprint, according to your team's estimates in either story points, story points estimate, original time estimate, or issue count.

**Removed work**: How much work was removed from a sprint after its start (estimation of issues removed from sprint).

And you can change the color of each of the different metrics just by clicking in the colored circle of each metric:

### Velocity

Velocity is calculated by taking the average of the total completed estimates over the last several sprints. Example, the team's velocity is (17.5 + 13.5 + 38.5 + 18 + 33 + 28) / 6 = 24.75 (we've ignored the zero story point sprint). This means that the team can be expected to complete around 24.75 story points worth of work in the next sprint.

This value should become more accurate and reliable over time as more data becomes available and the team improves at estimating issues.

## Configuration

Name your gadget meaningfully, so everyone knows at a glance what it is about and when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource**, indicate the monday.com account where you want to fetch the data from.
- The **workspace** where the sprints are located. The workspace has to be from monday.com *dev*, and the board *Sprints* is required.
- The **Number of sprints**, by default, the **last 5 sprints are displayed**, but users can select 3, 5, 10, 25, or 50 sprints among the previously selected project/boards.
- The **Sprint State(s)**, choose among the three different states: Active, future and/or closed.
- The **estimation statistic**, choose how your team estimates the how much work is committed in a sprint:

  - Story points (*Estimated SP* column). Your team will burn down the story points estimations they did.
  - Issue count. Your team will burn down the number of issues completed (when the column *Status* is *Done*). And they won’t need to enter estimates in the backlog.
- The **Data visualization configuration**, here you can select whether to display four optional metrics

  - **Reopened work**: The amount of work due to issues reopened during a sprint.
  - **Added work**: The amount of work added to a sprint after its start.
  - **Estimate Change**: The amount of work due to changes in the estimation of **story points**.
  - **Pending work**: Total amount of work left in the sprint.
  - **Removed work**: The amount of work removed from the sprint.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring one by one the rest of the gadgets with the same default configuration.

## Integrations

- :monday.com: dev

monday dev

We are working on our growing catalog of [Product and data connections](/cms_trial/space/RDD/146310010/Product+and+data+connections/), but drop us a line in case you want us to expedite a specific one, visit our [Help and support](/cms_trial/space/RDD/146309984/Help+and+support/).

## Dashboards

This gadget appears in the following dashboard: [Agile Dev for monday.com template](/cms_trial/space/RDD/200278357/Agile+Dev+for+monday.com+template/) (see [Agile Dev monday.com dashboard](https://appfire.atlassian.net/wiki/label/RDD/agile_dev_monday)).