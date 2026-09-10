# Gantt gadget

**Depreciated** **by Atlassian**

[Atlassian ended support for gadgets in Confluence 7.0](https://confluence.atlassian.com/doc/gadgets-moved-to-a-marketplace-app-from-confluence-9-2-onwards-1431545691.html) and completed their removal in Confluence 9.0 to reduce technical debt.

In Confluence 9.0, pages that were using gadgets show a grey ‘Unknown macro’ placeholder where gadgets were embedded.

The Gantt Gadget proves very useful as it mirrors the Gantt module in a read-only way.

## Security and access

To view the Gadgets on both the Confluence pages and Jira Dashboards, you need at least a Box Viewer security role.

You can add the Gantt Gadget to your Jira dashboard or Confluence page.

![big-picture-gantt.png](/cms_trial/assets/5e6caa56-62c7-41a7-908d-5aefa6dba2cc.png)

Add the Gantt Gadget to see your schedule on the Dashboard of Confluence page.

There's no limit on the number of gadgets you can display on your dashboard.

The Gantt Gadget shows the same Column View configuration as selected in the Gantt module. Hence, we recommend creating a dedicated Box to maintain only the desired Column View.

## Editing the Gadget

Click on the '...' button in the top-right corner of the Gadget to edit the content:

![reporting.png](/cms_trial/assets/4ff69459-1d44-4f66-a30f-cd7fc7c70d1b.png)

You can change the source data or display additional information, including:

![big-picture-gantt-settings.png](/cms_trial/assets/f9b9d208-2b9a-411e-a589-aa6edd7575c1.png)

The Box list is in alphabetical order:

![reporting-new-agile-project.png](/cms_trial/assets/bd184d63-9db1-422c-a4e5-5c98e8b2b483.png)

### Box

Choose the Box to serve as the data source for the Gantt Gadget. The Box list will only display Boxes to which you have access – your Security Role needs to be set to the Box Viewer at the minimum.

### Display Task Structure

Display or hide the Task Structure. By default, it is displayed next to the 'Summary' field. You can change the field next to which the Task Structure is displayed in the Box Configuration > Gantt > Column Views (requires the Box Admin Security Role).

### Display InfoBar

Enable the Infobar to view the crucial Box information, including:

- Milestones,
- Tasks overdue,
- Tasks on the Critical path,
- Task dependencies.

### Display Resources

Show the Resource utilization panel. On the Resource panel on the Gantt gadget, it is possible to choose between original estimate, remaining estimate or story points effort modes on the Jira Cloud like it is possible on the Jira server. Effort mode dropdown is added to the Advanced options section under Resources toggle as shown below:

![big-gantt-height.png](/cms_trial/assets/d164d67e-0a74-45d5-a5ae-15393c622573.png)

### Effort mode

It is possible to choose between original estimate, remaining estimate or story points effort modes on the Jira Cloud like it is possible on the Jira server.

![reporting-original-estimate.png](/cms_trial/assets/c6612b97-0a31-4d61-93d4-c395e4501d5f.png)

### Refresh Interval

You can set the gadget information refresh interval to:

- Never
- 15 minutes
- 30 minutes
- 1 hour
- 2 hours

## Filtering

The Gantt gadget has the same set of filters as the Gantt module (Quick filters, Date range, text, and JQL search).

Filtering in a gadget is independent of filtering in the Gantt module view (you can activate a different set of filters in a gadget and in a module).

### Filters activated per user

Each user can activate a different set of filters in the gadget. It won't affect what other users see. Each user has their own view.

### Multiple gadgets with different filters

Filters are set separately for each gadget. You can add multiple Gantt gadgets to your Dashboard and change scope/filters separately for each of them.

![multiple-gadgets.png](/cms_trial/assets/751f7922-22b2-48bd-b723-8bec07727014.png)