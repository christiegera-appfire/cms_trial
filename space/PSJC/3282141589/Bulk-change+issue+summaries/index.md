# Bulk-change issue summaries

## What's it handy for?

Power Scripts is a Swiss Army Knife that can help you customize Jira to your needs by building advanced automations with easy-to-use SIL (Simple Issue Language). This recipe shows you how to make bulk updates to issue summary fields with one short script, using ready-made [Script Snippets](/cms_trial/space/PSJC/723320834/Script+Snippets/) (short snippets of code).

- **Save time**: Instead of making manual updates, perform tasks at scale.
- **Reduce errors**: Bulk changes ensure that no manual errors can slip in.
- **Turbocharged automation**: Ready-made scripts can be customized to your scenario.

## To get started

1. Open the SIL Manager – your central repository where all scripts are stored in a file system.
2. Start building your script with the "Bulk change issues" [Script Snippet](/cms_trial/space/PSJC/723320834/Script+Snippets/).
3. Customize your script with the "[Current Issue] Subtask" Script Snippet.
4. Once you're done customizing the script, save it and test it.

## Example script

The script below selects issues from a JQL query and iterates over their subtasks, appending a tag to each subtask's summary field.

```java
const string jql = "project = HP"; // change the JQL to match your reality 

for(string k in selectIssues(jql, 100)) { // select first 100 issues 

    for(string s in subtasks(k)) { //iterate over subtasks of current issue

        %s%.summary += "[H1 Planning]";

    }
}
```

For more information about Script Snippets, see the [Script Snippets](/cms_trial/space/PSJC/723320834/Script+Snippets/) documentation.