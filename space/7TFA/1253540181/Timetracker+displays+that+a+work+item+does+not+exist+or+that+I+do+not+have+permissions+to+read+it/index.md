# Timetracker displays that a work item does not exist or that I do not have permissions to read it

Why am I seeing the message, "You don't have access to all projects. Time calculation might not be accurate" on the Times Explorer tab?

## Question

Why, when I try to open a work item on the "Times Explorer" page, do I receive the following message(s):

- *“Work item ### does not exist, or you do not have permissions to read it*”
- *“You have no access to this item. Please ask your administrator for permissions or set up Service Account“*

### Answer

This message might occur because of the following reasons:

1. You do not have access or permissions to the work item (i.e. you do not have access to the project in which the work item is a part).
2. The work item was deleted. Data cannot be displayed for deleted items (or items in the Recycle Bin). So instead of deleting work items, use the “Removed” selection in the “State” dropdown of the work item you no longer want to include to make this message disappear, and/or if you want to retain historical data in Timetracker.
3. You do not have the Service Account configured and/or you do not have a Service Account with adequate permissions selected. The Service Account feature allows users with lesser permissions to view read-only data that would not normally be available to them.

If you are a project collection administrator, in **7pace Timetracker DevOps Services (cloud)**, navigate to the “Settings” page of Timetracker, select “Reporting and API” and then expand “Service Account”. Here, set yourself as the Service Account for all users, which will allow your team members to view work items within ‘Times Explorer’ (as well as ‘Budgets’ and the ‘API’) properly without receiving an access denied message. For more information on configuring the Service Account for DevOps Services, please see [7pace Timetracker Service Account](/cms_trial/space/7TFA/1253540778/7pace+Timetracker+Service+Account/).

In**7pace Timetracker for DevOps Server (on-prem)**, as an administrator, you can configure it in the configuration tool of Timetracker so that all users of the system can view data that may not be available to those with lower permission levels. Select a user who belongs to the Project Collection Administrator user group in the config tool to achieve this. As an admin, you would set up or change the Service Account in the configuration tool wizard of 7pace Timetracker (see [7pace Timetracker Service Account](/cms_trial/space/7TFA/1253540778/7pace+Timetracker+Service+Account/) for more information on this process).

Therefore, if you can't view some work items, ask your admin to add more permissions to you or, as detailed above, to set themselves as the Service Account in Settings, so that you can view this page properly.