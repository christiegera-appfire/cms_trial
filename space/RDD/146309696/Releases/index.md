# Releases

## Overview

In Jira Software, each release is referred to as a version. Versions have different statuses (unreleased, archived or released) depending on the stage of your software cycle.

This gadget displays the last *n* number of versions of the set of selected projects over a period of time.

Imagine that you have to report every quarter the released versions of all the products in your company. Configure the gadget to return versions with a status of '*released'* during the last quarter. For each project, it shows the version name, the version status (unreleased, archived or released), the number of issues in each status and the start and release dates (if any).

## Configuration

Name your gadget meaningfully, so everyone knows at a glance when to use it. Fill out the rest of the fields as applicable, namely:

- The **datasource**, where **Current** indicates the Jira instance where the app is installed.
- The **projects** of the releases to be displayed, you can select as many as you need to.
- The **estimation statistic**, choose how the work in the releases is indicated. Remember, issues without an estimation are not reflected in the calculation.

  - Story points (company-managed projects, former classic projects). The work done in the release will be measured by the story points estimations the team did in the backlog
  - Story points estimate (team-managed projects, former next-gen projects). The work done in the release will be measured by the story points estimations the team did in the backlog.
  - Original time estimate. The work done in the release will be measured by the time estimations the team did in the backlog i.e., duration of the issues in hours or days in the **Original Estimate** field.
  - Issue count. The work done in the release will be measured by the number of issues completed. And they won’t need to enter estimates in the backlog. Thus the sum of the issues in a status divided by how many issues are in total in the sprint e.g., 50 issues in the sprint, 25 are in status “Done” so 50% is indicated

Learn about [Configure estimation and tracking](https://support.atlassian.com/jira-software-cloud/docs/configure-estimation-and-tracking/) in classic boards

- The **number of releases** to be retrieved.
- The **release status** of the retrieved releases: Released, unreleased and archived. If none is selected, all statuses are considered.
- The **period to retrieve**. Note that the *release date* is only mandatory for those releases with status *released*. Thus, only releases with a release date within the specified period of time are retrieved.
- Finally, indicate if you want to use the current settings for all the compatible gadgets in the dashboard. This option eases the pain of configuring one by one the rest of the gadgets with the same default configuration

## Integrations

- [jira software icon]

Jira Software

We are working on our growing catalog of [Dashboard gadgets - KPIs and metrics](/cms_trial/space/RDD/146309915/Dashboard+gadgets+-+KPIs+and+metrics/), but drop us a line in case you want us to expedite a specific one, visit our [Help and support](/cms_trial/space/RDD/146309984/Help+and+support/).

## Dashboards

This gadget appears in the following dashboard: [Scrum software team template](/cms_trial/space/RDD/146310016/Scrum+software+team+template/)