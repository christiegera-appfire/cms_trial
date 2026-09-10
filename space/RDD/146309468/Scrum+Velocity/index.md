# Scrum Velocity

## Overview

The **Scrum Velocity** chart gadget shows your Scrum team's velocity, calculated as the average of completed estimates across a set of sprints. Velocity in Agile teams using Scrum is a key metric to forecast delivery dates and set the number of product backlog tasks to plan in upcoming sprints.

![Dashboard Hub Scrum Velocity chart preview](/cms_trial/assets/0c1e1121-2a58-47c4-bdcd-c753a7b67f12.jpg)

## Sprints

The sprints are located in either a software project or a Jira board:

![Dashboard Hub Scrum Velocity sprint boards setting](/cms_trial/assets/e716ed01-33ef-4fc0-ab33-2ffcc88e8f53.png)

By default, the last five sprints are displayed, but you can select 3, 5, 10, 25, or 50 sprints based on the previously selected projects or boards.

### **Filter by sprint state**

If you want to display sprints in a specific state (active, future and/or closed), select the state(s) to be filtered.

![Dashboard Hub Scrum Velocity chart by sprint](/cms_trial/assets/e50f8a44-820b-44fd-94f8-38ae33e41726.png)

This gadget is multi-project/multi-board, so you can report across your entire portfolio of Scrum projects.

## Estimation statistic

The y-axis displays the statistic selected to assess the velocity of your team(s). The estimation statistic can be any numeric or duration time custom field in the Jira system. However, the most common fields are:

- **Story points** (company-managed projects, former classic projects). Your team will calculate the velocity using the story points they did in the sprint.
- **Story points estimate** (team-managed projects, former next-gen projects). Your team will calculate the velocity using the story points estimations they did in the sprint.
- **Original time estimate**. Your team will calculate the velocity using the time estimations they did in the sprint, which is the duration of the issues in hours or days in the **Original Estimate** field.
- **Issue count**. Your team will calculate the velocity using the number of issues completed in the sprint. And they won’t need to enter estimates!
- Any **numeric** or **duration time** custom field in the Jira system.

## View Type

You can select from three different visual metaphors to represent your chart: Grouped bar chart, Stacked bar chart, and Multi line chart.

![Dashboard Hub Scrum Velocity view type setting](/cms_trial/assets/b73041b7-4ea2-4c5a-a07b-b65878d72e31.png)

### Metrics to display

By default, two metrics are always displayed:

- **Commitment**: The amount of work in the sprint when it began. The bar/line for each sprint shows the total estimate of all issues in the sprint when it begins. After the sprint has started, any stories added to the sprint, or any changes made to estimates, will not be included in this total.
- **Completed**: The amount of work done during the sprint. The bar/line in each sprint shows the total completed estimates when the sprint ends. Any scope changes made after the sprint started are included in this total.
- **Optional metrics:**

  - **Reopened**: The amount of work due to issues reopened during a sprint.
  - **Added**: How much work was added to a sprint after its start (estimation of issues added to sprint).
  - **Estimate Change**: The amount of work due to changes in the estimation of **story points** changes.
  - **Pending**: Represents the total amount of work left in the sprint, according to your team's estimates in either story points, story points estimate, original time estimate, or issue count.

    ![Dashboard Hub Scrum Velocity metrics setting](/cms_trial/assets/8038e2bf-95c1-483d-806c-0a56a2a4ac00.png)

    To change the color of a metric, click the corresponding colored circle.

    ![Dashboard Hub Scrum Velocity color picker](/cms_trial/assets/bf0bf356-5fe6-4fda-a928-2c309acf9549.png)

## Velocity

Velocity is calculated by taking the average of the total completed estimates over the last several sprints. For example, the team's velocity is (17.5 + 13.5 + 38.5 + 18 + 33 + 28) / 6 = 24.75. This means that the team can be expected to complete around 24.75 story points worth of work in the next sprint.

This value should become more accurate and reliable over time as more data becomes available and the team improves at estimating issues.

Estimates from sub-tasks are not included in the Velocity Chart's calculation. (Only estimates from *parent tasks* are included.)

Velocity calculation differs from Jira’s native velocity formula. If you want to align the report to Jira’s Velocity Report, you can use the option in the gadget configuration. This pulls data from Jira’s built-in Agile reports instead of building the report from JQL searches and work item changelogs.

## How to configure the gadget

This section explains how to add and configure the gadget.

**To add the gadget to a dashboard:**

1. Click **Edit** in your dashboard, then click **Add Gadget**.
2. Use the *Search* bar in the *Add gadget* page to find the required gadget.
3. Select the **Scrum Velocity** gadget.
4. (*optional*) The name field is completed by default. You can edit the name to make it more meaningful to your team.
5. Select the datasource from where you want to retrieve sprint statistics. To learn more about datasource types, see [Datasources](/cms_trial/space/RDD/2116682228/Datasources/).
6. Select whether to view sprint data based on boards or sprints.
7. Select the boards or sprints based on the option you choose in step 6.
8. (*optional*) If you select the Boards option above, select the number of sprints to display. You can use the filter options to limit sprints based on status: Active, Future, or Closed.
9. (optional) **Display sprints by time period**: By default, the last sprints are displayed. If you define a time period, only sprints with an end date (close date) within that period are shown.
10. (*optional*) **Use data from Jira native Velocity Report**: If you base this report on boards, you can use this option to align with Jira’s native Agile reports. This option is only available for datasources connected through a Jira API token.
11. Select a view type to best visualize data. The options are table view, pie chart, and bar or line charts.
12. (*optional*) Depending on the view type you select, choose how to group the data. See the filtering options in the next section for more information.
13. **Estimation statistic**: Choose how your team estimates how much work is committed in a sprint.
14. **View Type**: Select the view type that best represents the data you want to report on.
15. **Data visualization configuration**: Commitment and Completed are selected by default. Select any optional metrics to to display.
16. Click **Add** to save the configuration and add the gadget to your dashboard.

## Integrations

- Jira Software

## Templates

This gadget is included in the [Scrum software team template](/cms_trial/space/RDD/146310016/Scrum+software+team+template/).