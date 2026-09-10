# Build an escalation service

This use case combines a JQL Search Extensions keyword with Power Script’s SIL Manager and Scheduler to create a scheduled task (escalation service) that finds issues linked to high-priority ones and updates the priority to match.

If you are not already using Power Scripts, you can try out these features with a free trial license. Visit our Power Scripts [marketplace listing](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?hosting=cloud&tab=overview) to learn more.

### Problem to solve

In large organizations, multiple teams often work on related issues across different projects. If the priority of an issue dependency increases, the team responsible for the linked issue may remain unaware, causing misaligned priorities. Research shows that misalignment in issue prioritization can delay critical task completion by [30-50%](https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/making-collaboration-across-functions-a-reality) and lead to operational inefficiencies.

### Solution

An escalation service can be built to automatically monitor linked issues. This automation checks for any linked issues whose priority has been upgraded to High and updates the related tickets’ priority as needed. Power Scripts and JQL Search Extensions provide the mechanism for this check and update, ensuring real-time alignment between teams.

|  |  |
| --- | --- |
| **Scenario** | Imagine a support team handling a high-priority customer issue linked to a development task with a medium priority. Without automated synchronization, the development team can not immediately address the critical bug, which can delay fixes. By implementing the escalation service, the linked issue's priority is updated to High, alerting the development team to resolve it on time. |
| **JQL Search Extensions keyword** | `linkedIssuePriority` |
| **Power Scripts features** | SIL Manager and Scheduler |
| **Method** | 1. In Jira, go to **Settings** > **Apps**. 2. In the Apps sidebar menu, under *POWER SCRIPTS*, select **SIL Manager**. 3. On the *SIL Manager* page, select **File** > **New file** to create a new file. 4. Add the following script to the file, and replace `MyProject` with your project details.  ```text    string [] issues = selectIssues("project = MyProject AND linkedIssuePriority = 'High' AND priority != 'High' AND statusCategory != Done");    for(string issueKey in issues) {      %issueKey%.priority = "High";    }    ``` 5. Enter a name for the file, then click the **Save** icon in the top menu to save the file. 6. Select **Power Apps Config** in the left sidebar. The *Power Apps Config* menu displays. 7. Select **Advanced** > **Scheduler** to display the *Scheduled Jobs* page. 8. Click **Schedule job**. The *Schedule new job* window displays. 9. Select **Interval** for the Job type. Alternatively, use a CRON expression to define the interval. 10. Set the interval when the script should run, for example,1h. 11. Select the **Edit** icon in the *Script* field. 12. Select the saved file from the list and click **Select**. PowerScripts-scheduler-select-file.png 13. In the *Schedule new job* window, select the **Run as** user. JSE-PowerScripts-Scheduler.png 14. Click **Save**. Your saved scheduled job displays in the list of scheduled jobs. You can later edit or delete the job as required. PowerScripts-saved-scheduled-job.png Now, this script will run every 60 minutes and update the priority of any issues that match the JQL query used in the script. |