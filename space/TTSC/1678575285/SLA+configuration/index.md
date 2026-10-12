# SLA configuration

Configure service level agreements (SLAs) in Time to SLA to track how long your team takes to respond to or resolve Jira work items.

To set up an SLA, define when time should be tracked, set a target for completion, and select the working calendar to use. You can also configure actions to notify your team or update Jira work items when specific SLA events occur.

## 1. Configure calendars

Calendars define when SLA time counts. They let you account for your team's working hours, time zones, holidays, and exceptions.

For example, if your support team works Monday through Friday, from 9 AM to 5 PM, you can configure a calendar so that SLA time counts only during those hours.

You can assign calendars to individual SLA goals to accommodate different schedules.

- [Create calendars](/cms_trial/space/TTSC/35750012/Create+calendars/): Create and manage calendars, working hours, holidays, and exceptions.
- [FAQ: Calendars](/cms_trial/space/TTSC/35881031/FAQ%3A+Calendars/): Find answers to common questions about calendar configuration.

## 2. Define SLAs

An SLA specifies which work items to track, how much time is available to meet a target, and when the timer starts, pauses, and stops.

For example, you can configure an SLA that gives your support team four business hours to respond to high-priority requests.

Start with the [Define SLAs](/cms_trial/space/TTSC/35651691/Define+SLAs/) guide for step-by-step instructions. Configure these components:

- [SLA conditions](/cms_trial/space/TTSC/35456221/SLA+conditions/): Define when the SLA starts, pauses, and ends based on events or changes in Jira work items.
- [SLA goals](/cms_trial/space/TTSC/35390901/SLA+goals/): Set time targets or deadlines. You can create different goals for different types of work items, such as high-priority and low-priority requests.
- [Calculation methods](/cms_trial/space/TTSC/35456295/Calculation+methods/): Determine how elapsed time is calculated across SLA cycles.

For troubleshooting common issues when configuring SLAs, refer to [FAQ: SLAs](/cms_trial/space/TTSC/34932181/FAQ%3A+SLAs/).

## 3. Configure SLA actions

SLA actions let you respond automatically to SLA events, such as when an SLA starts, approaches its target, or breaches.

For example, you can send a Slack message when an SLA is approaching its deadline or change a work item's priority when an SLA breaches.

Available actions include:

- [Send an email](/cms_trial/space/TTSC/3308945429/Create+actions/)
- [Send a Slack message](/cms_trial/space/TTSC/3308945429/Create+actions/)
- [Trigger Jira automation](/cms_trial/space/TTSC/3308945429/Create+actions/)
- [Change assignee](/cms_trial/space/TTSC/3308945429/Create+actions/)
- [Add a comment](/cms_trial/space/TTSC/3308945429/Create+actions/)
- [Set Jira field](/cms_trial/space/TTSC/3308945429/Create+actions/)
- [Change priority](/cms_trial/space/TTSC/3308945429/Create+actions/)

To configure and manage actions, see:

- [Create actions](/cms_trial/space/TTSC/3308945429/Create+actions/) – Configure actions and their triggers.
- [Action parameters](/cms_trial/space/TTSC/35881100/Action+parameters/) – Personalize messages and comments with dynamic SLA and work item values.
- [Mute notifications](/cms_trial/space/TTSC/169978040/Mute+notifications/) – Temporarily disable SLA notifications for selected work items or SLAs.

## Next steps

After configuring an SLA, open a Jira work item that matches its scope to [view the SLA panel](/cms_trial/space/TTSC/35815641/Track+SLAs/) and monitor its progress.

You can also use Time to SLA [reports and gadgets](/cms_trial/space/TTSC/36012079/Reports/) to analyze SLA performance across multiple work items.