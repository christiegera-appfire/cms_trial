# Sprint Health

## Overview

All the important metrics of a sprint at a quick glance to check the health and progress of your team. The % of progress can be measure either using *story points* (make sure all issues are estimated), time (the *original time estimate*), *story points estimate* or *issue count*.

Learn about [Configure estimation and tracking](https://support.atlassian.com/jira-software-cloud/docs/configure-estimation-and-tracking/) in classic boards.

This gadget displays useful information about the progress of the sprint:

- The % progress of each status of your working process.
- The number of days left to finish the sprint.
- The blockers left: This field counts all the pending issues with a link “blocks”, which indicate that they are blocking other issue.
- The flagged left: This field counts all the pending issues that have been [flagged](https://support.atlassian.com/jira-software-cloud/docs/flag-an-issue/) as impediments.
- The % scope change in comparison to how the sprint started. When an issue is added/removed, the scope changes. If an issue without estimation is added/removed from the sprint, the scope won’t be affected.

  ![Dashboard Hub Dashboard Hub Cloud sprint health](/cms_trial/assets/a22ded9b-cdc9-4383-8e7c-36ecab8a0fd9.png)

## Configuration

1. Provide a meaningful name for the gadget so everyone knows at a glance what it is about and when to use it.
2. Select the datasource, where **Current** indicates the Jira instance where the app is installed.
3. Select the project and board where the issues are located. By default, all the issues are displayed, no matter the active sprint they belong to, in case there are parallel sprints.
4. For the **estimation statistic**, choose how your team estimates the amount of work committed in a sprint. Remember, issues without an estimation are not reflected in the calculation.

   1. Story points (company-managed projects, former classic projects). The progress of your team will be measured by the story points estimations they did in the backlog.
   2. Story points estimate (team-managed projects, former next-gen projects). The progress of your team will be measured by the story points estimations they did in the backlog.  
      Original time estimate. The progress of your team will be measured by the time estimations they did in the backlog i.e., duration of the issues in hours or days in the **Original Estimate** field.
   3. Issue count. The progress of your team will be measured by the number of issues completed. And they won’t need to enter estimates in the backlog. Therefore, the sum of the issues in a status divided by how many issues are in total in the sprint, for example, 50 issues in the sprint, 25 are in status “Done”, so 50% is indicated
5. Choose whether to use the current settings for all the compatible gadgets in the dashboard. This option avoids configuring the rest of the gadgets individually.

## Integrations

- [jira software icon]

Jira Software

We are working on our growing catalog of [Dashboard gadgets - KPIs and metrics](/cms_trial/space/RDD/146309915/Dashboard+gadgets+-+KPIs+and+metrics/) and [Product and data connections](/cms_trial/space/RDD/146310010/Product+and+data+connections/). If you don’t see what you need, let us know through our [support portal](https://appf.re/support).

## Dashboards

This gadget appears in the following dashboard: [Scrum software team template](/cms_trial/space/RDD/146310016/Scrum+software+team+template/). See:

Scrum Software Team dashboard