# Update remote links

This use case combines a JQL Search Extensions keyword with Power Script’s SIL Manager to run a one-off automation to update the URL of remote links in open issues belonging to a project.

If you are not already using JQL Search Extensions, you can try out these features with a free trial license. Visit our JQL Search Extensions [marketplace listing](https://marketplace.atlassian.com/apps/1214791/jql-search-extensions-for-jira?hosting=cloud&tab=overview) to learn more.

|  |  |
| --- | --- |
| **Scenario** | *The main website for a Jira project has changed after work on issues has been planned.*  **Solution**: Run a script that replaces all existing links for open issues with the new URL. |
| **JSE keyword** | `fixedVersionsReleased` |
| **PowerScripts features** | SIL Manager |
| **Method** | 1. In Jira, go to **Settings** > **Apps** > **Manage apps**. 2. In the Apps sidebar menu, under *Power Scripts*, select **SIL Manager**. 3. On the *SIL Manager* page, select **File** > **New file** to create a new file. 4. Add the following script to the file, and replace the project and link parameters with your project details.  ```text    string [] issues = selectIssues("project = MyProject AND fixVersionsReleased > 0 AND statusCategory != Done");    for(string issueKey in issues) {      for(JRemoteIssueLink link in getWebLinksForIssue(issueKey)) {          link.url = replace(link.url, "digitaltoucan", "appfire");          updateWebLink(issueKey, link);      }    }    ``` 5. Click the **Check** **script** icon to ensure that it is correct. 6. Click the **Run** icon. A run script done status displays if the run is successful. Power Scripts for Jira Cloud SIL Runner gadget usage interface |