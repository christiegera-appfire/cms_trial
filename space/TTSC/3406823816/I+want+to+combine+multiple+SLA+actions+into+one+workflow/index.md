# I want to combine multiple SLA actions into one workflow

🤔 **Context:** A support manager wants one SLA event to trigger a complete response instead of creating separate configurations for every step.

🌧️ **User problem:** A single SLA event often requires more than one follow-up. When a resolution SLA breaches, the team may need to notify a manager, alert a Slack channel, change the priority, assign the work item to someone senior, and add a comment for visibility. If each step is configured separately, the process can become harder to manage, easier to misconfigure, and more difficult to review later.

☔ **Solution:** Using Time to SLA’s Actions feature!

Time to SLA allows you to combine multiple action types in the same SLA action setup. You can configure one action that sends an email, posts a Slack message, triggers Jira automation, changes the assignee, adds a comment, changes the status, updates a Jira field, or changes the priority.

![image-20260629-113331.png](/cms_trial/assets/78963a26-f30f-4376-b318-5248bdeafb10.png)

For example, when a Time to resolution SLA breaches, one combined action can notify the incident manager by email, send a Slack message to the support channel, change the priority to Highest, assign the work item to a senior team member, and add an internal comment explaining the escalation. This helps teams create a complete SLA response without building and maintaining separate configurations for each step.

[**Time to SLA multi-action workflow configuration**](/cms_trial/space/TTSC/35881090/Actions/)

## Problem solved!