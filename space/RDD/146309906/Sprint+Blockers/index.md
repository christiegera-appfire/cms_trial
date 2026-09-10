# Sprint Blockers

## Overview

This gadget displays all the pending impediments or blockers of a sprint. For an issue to be identified as an impediment or blocker, it has to meet any of the following criteria:

- The issue is flagged as important. These issues are displayed in yellow and with the flag icon (see [Jira cloud flag an issue](https://support.atlassian.com/jira-software-cloud/docs/flag-an-issue/)).
- The issue has a *blocks* link to another issue, which in turn is linked with a *blocked by* relationship to the blocker issue.

Some users identify blockers using a workflow state *Blocker* and a column *Blocked*, with labels, or with a priority *Blocker*.

![Dashboard Hub Sprint Blockers page example](/cms_trial/assets/29835faf-dd83-4684-91d0-91ec72d82df4.png)

## Configuration

1. Provide a meaningful name for the gadget so everyone knows what information it displays.
2. Complete the remaining fields as applicable:

   1. The datasource, where **Current** indicates the Jira instance where the app is installed.
   2. The project and the board where the issues are located. By default, all the issues are displayed, no matter the active sprint they belong to, in case there are parallel sprints.
   3. Choose whether to use the current settings for all the compatible gadgets in the dashboard. This option avoids configuring the rest of the gadgets individually.

      ![Dashboard Hub Sprint Blockers dashboard example](/cms_trial/assets/c4a112d6-b33c-4c47-966c-4262651499c8.png)

## Dashboards

This gadget appears in the following live dashboard: [Agile Sprint live dashboard](https://staging-eu.dts-dh.appfire.app/jira/shared/dashboard?boardToken=VTJGc2RHVmtYMS9jZUN6VmZXeVNHWWZHQll0U05WMkhGOWNvQitOVFZFbEpuOGszWDFCT2ZEWWdGdmR5Rm1EK05XTEo1K1VBSXNMa1VuKzltYnRFNzdaMUlwam1ZRG1CYStZZlZmR3I4VnhCVU8yTzJnb2h1cksrM0cwaFM1MThhVXg2dGVCNktHOS9UVWloV3EwU2VhSkc4ZElpMUtvSmlkNFVQVTdoeVlZcERBSVprR1hxM0FJM1lxSjN1dXpOaWZxVXJTcTNXM3l5K3NDTXUxTVo4NlpYSGVEeHovaUFXRkxINlE0dVZmQlZwTHAvY1hpTUkvK1hMT0pydHZ0NU1OVG9SMzIrZUtMSm0wb3AvdnFYRmc9PQ==).

See [Scrum Software Team](/cms_trial/space/RDD/146310016/Scrum+software+team+template/) template to learn more.