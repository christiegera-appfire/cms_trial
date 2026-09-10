# Identify issues related to a service desk project

This use case combines a JQL Search Extensions keyword with Power Script’s SIL Manager and Scheduler to automatically add a label to issues from Support so they are easier for developers to view and prioritize.

If you are not already using Power Scripts, you can try out these features with a free trial license. Visit our Power Scripts [marketplace listing](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?hosting=cloud&tab=overview) to learn more.

### Problem to solve

Development teams can often encounter a backlog of issues, causing delays in addressing customer service desk tickets. Many support tickets are delayed because they aren't properly flagged or prioritized. This results in poor customer experiences, with [73% of customers switching providers](https://www.zendesk.com/blog/customer-service-statistics/#) due to slow issue resolution.

### Solution

Create a scheduled task that adds a *Support* label to all issues linked to support tickets. This allows these issues to be easily identified and prioritized in Jira filters or dashboards, ensuring that development teams don’t overlook them.

|  |  |
| --- | --- |
| **Scenario** | A telecommunications company receives a support ticket from a key enterprise client reporting a system outage. The ticket is linked to an internal bug in the development project. Without a *Support* label, the development team does not prioritize the fix, leading to extended downtime for the client. Let’s automate the labeling process so these tickets aren’t missed, leading to faster resolution and improved customer satisfaction. |
| **JSE keyword** | `linkedByIssueProject` |
| **PowerScripts features** | SIL Manager and Scheduler |
| **Method** | 1. In Jira, go to **Settings** > **Apps**. 2. In the Apps sidebar menu, under *POWER SCRIPTS*, select **SIL Manager**. 3. On the *SIL Manager* page, select **File** > **New file** to create a new file. 4. Add the following script to the file, and replace `MyProject` with your project details.  ```text    string [] issues = selectIssues("project = MyProject AND linkedByIssueProject = SUPPORT AND (labels IS EMPTY OR labels != support)");    for(string i in issues) {      %issueKey%.labels += "support";    }    ``` 5. Enter a name for the file, then click the **Save** icon in the top menu to save the file. 6. Select **Power Apps Config** in the left sidebar. The *Power Apps Config* menu displays. 7. Select **Advanced** > **Scheduler** to display the *Scheduled Jobs* page. 8. Click **Schedule job**. The *Schedule new job* window displays. 9. Select **Interval** for the *Job type*. Alternatively, use a CRON expression to define the interval. 10. Set the interval when the script should run, for example, 1h. 11. Select the **Edit** icon in the *Script* field. 12. Select the saved file from the list and click **Select**. JSE-Power-Scripts-select-ticker-tracker.png 13. In the *Schedule new job* window, select the **Run as** user. JSE-Power-Scripts-schedule-new-job-support.png 14. Click **Save**. Your saved scheduled job displays in the list of scheduled jobs. You can later edit or delete the job as required. JSE-PowerScripts-scheduler-support-tickets.png Now, every 60 minutes, this script will run and add the label `Support` to any issues that match the JQL query used in the script. |