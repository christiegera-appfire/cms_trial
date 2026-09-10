# Sprint Burndown

## Overview

A burndown chart shows the amount of work remaining in a sprint and the work completed. This is a big help for your team because they can track progress, predict whether they can meet the goals, and stay aware of scope changes.

- In the horizontal axis (x-axis), the **period of time** in days that the sprint lasts.
- In the vertical axis (y-axis), the amount of work planned for the sprint in the **estimation statistic** you choose when configuring the gadget. The unit of measurement can be: Story points, story points estimate, original time estimate or issue count.

Learn about [Configure estimation and tracking](https://support.atlassian.com/jira-software-cloud/docs/configure-estimation-and-tracking/) in classic boards.

![Dashboard Hub Sprint burndown chart](/cms_trial/assets/5815c6c7-b610-4b09-a813-e3bb98b027ed.png)

### **Remaining work**

The green line represents the total amount of work left in the sprint, according to your team's estimates in either story points, story points estimate, original time estimate, or issue count. Here, you should check if it increases, which indicates scope creep, that is, growth in the scope of the sprint.

### **Guideline**

This blue line is a guide for your team to approximate where they should be to finish the work on time, provided the work was done in a linear progression.

Your team’s green line should be below the blue line. Meaning that they are on track to finish everything online before the end of the sprint.

## How to configure the gadget

This section explains how to add and configure the gadget.

**To add the gadget to a dashboard:**

1. Click **Edit** in your dashboard, then click **Add Gadget**.
2. Use the *Search* bar in the *Add gadget* page to find the required gadget.
3. Select the **Sprint Burndown** gadget.
4. (*optional*) The name field is completed by default. You can edit the name to make it more meaningful to your team.
5. Select the datasource from where you want to retrieve sprint statistics. To learn more about datasource types, see [Datasources](/cms_trial/space/RDD/2116682228/Datasources/).
6. Select whether to view sprint data based on boards or sprints.
7. Select the boards or sprints based on the option you choose in step 6.
8. (optional) **Estimation statistic:** Choose how your team estimates how much work is committed in a sprint:

   - **Story points** (company-managed projects, former classic projects): Your team will calculate the velocity using the story points they did in the sprint.
   - **Story points estimate** (team-managed projects, former next-gen projects): Your team will calculate the velocity using the story point estimates they made during the sprint.
   - **Original time estimate**: Your team will calculate the velocity using the time estimations they did in the sprint; the duration of the issues in hours or days in the **Original Estimate** field.
   - **Issue count**: Your team will calculate the velocity using the number of issues completed in the sprint. And they won’t need to enter estimates!
   - Any **numeric** or **duration time** custom field in the Jira system
9. (*optional*) **Use data from Jira native Burndown Chart**: If you base this report on boards, you can use this option to align with Jira’s native agile reports. This option is only available for datasources configured to use a Jira API token.

## Integrations

- Jira Software

## Dashboards

Go to our [Agile Team live dashboard](https://staging-eu.dts-dh.appfire.app/jira/shared/dashboard?boardToken=VTJGc2RHVmtYMS9jZUN6VmZXeVNHWWZHQll0U05WMkhGOWNvQitOVFZFbEpuOGszWDFCT2ZEWWdGdmR5Rm1EK05XTEo1K1VBSXNMa1VuKzltYnRFNzdaMUlwam1ZRG1CYStZZlZmR3I4VnhCVU8yTzJnb2h1cksrM0cwaFM1MThhVXg2dGVCNktHOS9UVWloV3EwU2VhSkc4ZElpMUtvSmlkNFVQVTdoeVlZcERBSVprR1hxM0FJM1lxSjN1dXpOaWZxVXJTcTNXM3l5K3NDTXUxTVo4NlpYSGVEeHovaUFXRkxINlE0dVZmQlZwTHAvY1hpTUkvK1hMT0pydHZ0NU1OVG9SMzIrZUtMSm0wb3AvdnFYRmc9PQ==) to see an example of the gadget with live data.

## Templates

To create a similar dashboard, use our [Scrum software team template.](/cms_trial/space/RDD/146310016/Scrum+software+team+template/)