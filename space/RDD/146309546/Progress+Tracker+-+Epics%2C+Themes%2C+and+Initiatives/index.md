# Progress Tracker - Epics, Themes, and Initiatives

This page explains how to use the Progress Tracker gadget in Dashboard Hub to track progress across your work type hierarchy.

## Overview

When organizing work in Jira, a consistent work type hierarchy helps split larger items into smaller individual work items to track progress, dependencies, and highlight problems that could impact the timelines. The Progress Tracker gadget can display progress at the Epic, Theme, Initiative level, or other work types by different estimation statistics. Epics are particularly useful when breaking down projects and products into work that individual team members can work in.

To learn more about work type hierarchy in Jira, see [Configure the work type hierarchy](https://support.atlassian.com/jira-cloud-administration/docs/configure-the-issue-type-hierarchy/) in the Atlassian support documentation. Levels above Epic are available in Jira Cloud Premium and Enterprise. You can also configure [custom hierarchy levels](https://support.atlassian.com/jira-software-cloud/docs/configure-custom-hierarchy-levels-in-advanced-roadmaps/).

## Views

This gadget offers two ways to track progress: **Extended view** and **List view**.

### Extended view

This view displays fewer items but in a graphical format to track progress at a glance . The completion status is displayed as a donut chart with the percentage value in the center.

![The Progress Tracker gadget showing progress across Epics as a percentage complete.](/cms_trial/assets/cbc57b84-32b9-47bb-90e6-342b61f20c53.png)

### List view

This view is intended for when you need to display several items at once. All the key information is still available, but using a lean design.

![Example of a List view showing Epics progress for more granular views.](/cms_trial/assets/d2583df2-f539-4af9-a210-1777c159da87.png)

## Customizable date fields

In the gadget configuration, select which date fields will be used as the Start and Due dates. The selected date fields automatically inherit their names as the displayed labels by default.

You can customize the labels shown in the gadget by editing the displayed names. If you map the **Due Date** field to a custom field called **Last final date**, you can rename it to display as **Project end** in the gadget. Or use the **Created** date as the **Start Date** and the **Updated** as the **Due Date**.

![Example of adding Created and Updated dates on the Progress Tracker.](/cms_trial/assets/a5762b24-93a4-4581-b174-9ce8ff1401dc.jpg)

## How to configure the gadget

1. Provide a meaningful name for the gadget so everyone knows what information it displays.
2. Select the datasource, where **Current** indicates the Jira instance where the app is installed.
3. Choose how to populate the gadget. You can use the result of the a JQL query or a saved JQL filter. See the [JQL documentation](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/) to learn more. We recommend filtering as much as possible to optimize the dashboard's performance. Note that the gadget returns the query results, which are dynamic and can change over time.
4. Select the date fields to be used as the Start and Due dates, and customize the labels shown in the gadget by editing the displayed names.
5. Select the estimation statistic to show how the completed work is indicated. Work items without an estimation are not reflected in the calculation.

   - **Issue count:** The work done is measured by the number of child work items completed.
   - **Story points** (company-managed projects, former classic projects): The work done is measured by the story points estimations on the child work items.
   - **Story points estimate** (team-managed projects, former next-gen projects): The work done is measured by the story points estimations on the child work items.
   - **Entity type**: choose what type of issue do you want to track progress: *Epics, Themes, Initiatives or other issue types* that can hold children issues.

Entity type options are dependent on the datasource. If your datasource is a Jira Data Center instance, only the Epic entity type is available.

1. Select the View type:

   - **List View:** Work items are displayed in a table-like format to maximize the number of items displayed.
   - **Extended View**: Work items are displayed in a visual way with a donut chart.

## Integrations

- **Jira Software**

- **Jira Service Management**

## Dashboards

This gadget is not included in any of our pre-defined dashboards.