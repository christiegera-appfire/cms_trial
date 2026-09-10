# Update remote links

This use case combines a JQL Search Extensions (JSE) keyword with Power Script’s SIL Manager to run a one-off automation to update the URL of remote links in open issues belonging to a project.

If you are not already using Power Scripts, you can try out these features with a free trial license. Visit our Power Scripts [marketplace listing](https://marketplace.atlassian.com/apps/43318/power-scripts-jira-workflow-automation?hosting=cloud&tab=overview) to learn more.

### Problem to solve

The website or service linked in project documentation often changes over time. If these links remain outdated, it can lead to misinformation, broken references, and confusion for stakeholders. Outdated documentation can also lead to an increase in task completion time due to backtracking and searching for the correct information.

### Solution

Use a one-time automation process that scans all Jira issues for specific remote links and replaces the URLs with the new, correct ones. Power Scripts can search through all relevant issues and replace outdated links with a single script execution.

|  |  |
| --- | --- |
| **Scenario** | A software team working on a project referenced the Digital Toucan website in their issues, but the site has since been rebranded to Appfire. Manually updating each issue would be time-consuming, potentially taking several hours or even days. Use Power Scripts to replace `digitaltoucan` with `appfire` in all issue URLs to complete this process in minutes, ensuring consistency across the project. |
| **JSE keyword** | `fixedVersionsReleased` |
| **PowerScripts features** | SIL Manager |
| **Method** | 1. In Jira, go to **Settings** > **Apps**. 2. In the Apps sidebar menu, under *POWER SCRIPTS*, select **SIL Manager**. 3. On the *SIL Manager* page, select **File** > **New file** to create a new file. 4. Add the following script to the file, and replace the project and link parameters with your project details.  ```text    string [] issues = selectIssues("project = MyProject AND fixVersionsReleased > 0 AND statusCategory != Done");    for(string issueKey in issues) {      for(JRemoteIssueLink link in getWebLinksForIssue(issueKey)) {          link.url = replace(link.url, "digitaltoucan", "appfire");          updateWebLink(issueKey, link);      }    }    ``` 5. Click the **Check** **script** icon to ensure that it is correct. 6. Click the **Run** icon. A run script done status displays if the run is successful. Screenshot of the successful script run in the SIL Manager. |