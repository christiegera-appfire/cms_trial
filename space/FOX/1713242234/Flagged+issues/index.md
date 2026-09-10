# Flagged issues

Foxly supports flagged issues created in Jira’s backlog experience.

![Foxly window showing flagged issues](/cms_trial/assets/674faf27-1a8d-469b-b33a-e98e68c963c1.png)

### To flag an issue

1. Go to your board or backlog in Jira.
2. Select an issue and select  > **Add flag**.

You can also add a comment when you're adding a flag to or removing a flag from an issue. You may want to do this to indicate your reason for adding or removing the flag.

Flagged issues are visible to all members of a project.

You can perform this action with your keyboard via Jira’s command palette. Use **command** + **K** (for Mac) or **Ctrl + K** (for Windows) to open the command palette while you’re in Jira. [Read more about Jira’s command palette](https://support.atlassian.com/jira-software-cloud/docs/what-is-the-command-palette/)

## Search for flagged issues

The flag for an issue is stored in a custom checkbox field called "Flagged", which has only one value: `Impediment`. Use the JQL query `Flagged = Impediment` to find flagged issues.

For more details, see <https://support.atlassian.com/jira-software-cloud/docs/flag-an-issue/>.