# I want to trigger Jira automation from SLA events

🤔 **Context:** A Jira admin wants SLA events to start existing Jira automation rules so the team can connect SLA performance with their wider Jira workflows.

🌧️ **User problem:** Many teams already use Jira automation to move work items, add labels, create subtasks, notify stakeholders, or update custom fields. However, SLA events often need to be part of those workflows too. If an SLA is breached or about to breach, the team may want Jira to create an escalation task, move the work item to a different queue, or alert a project lead. Without a direct way to trigger automation from SLA events, admins may need to rely on manual updates or create complicated workarounds.

☔ **Solution:** UsingTime to SLA Actions!

The Actions feature allows you to trigger Jira automation from SLA actions. You can choose the SLA, select the goals, define the SLA event that should trigger the action, and connect it with Jira automation.

For example, when a First response SLA breaches, Time to SLA can trigger a Jira automation rule that adds an `SLA breached` label, creates a follow-up task for the team lead, moves the work item into an escalation queue, and notifies the project owner. This lets teams use SLA events as the starting point for broader automated processes in Jira.

[**Time to SLA Jira automation action configuration**](/cms_trial/space/TTSC/3308945429/Create+actions/)

## Problem solved!