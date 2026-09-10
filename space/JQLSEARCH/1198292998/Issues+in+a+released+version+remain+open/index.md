# Issues in a released version remain open

This use case combines a JQL Search Extensions keyword with Power Script’s SIL Manager and Scheduler to identify issues planned for a release that remain open after the version is released.

If you are not already using Power Scripts, you can try out these features with a free trial license. Visit our Power Scripts [marketplace listing](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?hosting=cloud&tab=overview) to learn more.

### Problem to solve

When product versions are released, unresolved issues that are still open can create confusion and lead to incomplete release documentation. These issues can reflect work that was either forgotten or deprioritized. Unresolved issues in released versions can reduce release clarity, complicate post-release management, and result in inaccurate reporting.

### Solution

Use automation to check for open issues in released versions periodically. If any open issues are found, Power Scripts automatically notifies the issue owner to either close the ticket or provide an update. This ensures that post-release cleanup happens without repeated manual follow-ups.

|  |  |
| --- | --- |
| **Scenario** | A software company releases a version in which several tickets remain open due to unresolved bugs that were either deferred or left in the backlog. The manual task of identifying and updating these tickets could take days or weeks, delaying future planning cycles and resulting in costly inefficiencies.  Let’s automate the task of finding the issues and adding a comment reminding the ticket owners that the version was released and to update them where appropriate. |
| **JSE keyword** | `fixedVersionsReleased` |
| **PowerScripts features** | SIL Manager and Scheduler |
| **Method** | 1. In Jira, go to **Settings** > **Apps**. 2. In the Apps sidebar menu, under *POWER SCRIPTS*, select **SIL Manager**. 3. On the *SIL Manager* page, select **File** > **New file** to create a new file. 4. Add the following script to the file, and replace `MyProject` with your project details. 5. This example uses the comment, `This issue is in a version that was released. Should it be closed?` . You can change the comment to meet your scenario if needed.  ```text    string [] issues = selectIssues("project = MyProject AND fixVersionsReleased > 0 AND statusCategory != Done");    for(string issueKey in issues) {      addComment(issueKey, "admin", "This issue is in a version that was released. Should it be closed?");    }    ``` 6. Enter a name for the file, then click the **Save** icon in the top menu to save the file. 7. Select **Power Apps Config** in the left sidebar. The *Power Apps Config* menu displays. 8. Select **Advanced** > **Scheduler** to display the *Scheduled Jobs* page. 9. Click **Schedule job**. The *Schedule new job* window displays. 10. Select **Interval** for the *Job type*. Alternatively, use a CRON expression to define the interval. 11. Set the interval when the script should run, for example, 3d. 12. Select the **Edit** icon in the *Script* field. 13. Select the saved file from the list and click **Select**. Screenshot of the Select File window in the Power Scripts scheduler. 14. In the *Schedule new job* window, select the **Run as** user. Screenshot of the Schedule new job window configured as described on this page. 15. Click **Save**. Your saved scheduled job displays in the list of scheduled jobs. You can later edit or delete the job as required. Screenshot of the list of scheduled jobs as described on this page. Now, every 3 days, this script will run and add the comment you defined in the script to any issues that match the JQL query used in the script. |