# Useful tools and scripts for post-migration script adjustment

Power Scripts will be unavailable during scheduled maintenance on August 8-9, 2026. Don't start a Data Center to Cloud migration during this time. Once maintenance is complete, update both your Data Center app and Power Scripts Cloud to the latest version before starting a migration.

You can use some tools and methods to help convert, update, and clean up scripts when migrating from Jira DC to Jira Cloud, including workflow conversion, filter updates, and bulk script modifications.

## Script conversion assistance with WorkFlow Pro

[WorkFlow Pro](https://marketplace.atlassian.com/apps/1235422/workflow-pro-ai-assistant-for-jira?hosting=cloud&tab=overview) is an AI chat agent run on Rovo that simplifies Jira automation processes. This application is currently being trained on the complete range of Apprifre workflow and automation apps, including the Simple Issue Language (SIL) used in Power Scripts. While Workflow Pro is new and its training is still ongoing, it can provide significant help for converting scripts after Jira DC to Cloud migration.

---

## Scripts for cleaning up saved filters

You can use scripts to audit filters and update the syntax of specific functions used in saved filters.

Script to identify filters that need updating based on function used

This analysis script helps assess the impact before making changes by identifying which filters need updating. It's a safe, read-only tool to use before running the actual update script.

```text
for(JFilter f in admGetAllFilters()) {
    string oldFunction = "hasLinkType";
    
    if(contains(f.jql, oldFunction)) {
        runnerLog("Filter \"" + f.name + "\" [" + f.id + "] owned by " + userFullName(f.owner) + " <strong style=\"color:red;\">contains</strong> the function for removal: <strong>" + oldFunction + "</strong>", true);
    } else {
        runnerLog("Filter \"" + f.name + "\" [" + f.id + "] owned by " + userFullName(f.owner) + " <strong style=\"color:green;\">does not contain</strong> the function for removal: <strong>" + oldFunction + "</strong>", true);
    }
}
```

Script to update the syntax of function used in saved filters

When migrating JQL queries from Jira DC to Cloud, use this template to convert function syntax from the `issueFunction in` format to the new equals operator format:

```text
//Starting JQL format:
issueFunction in FUNCTION_NAME("PARAMETER") and ADDITIONAL_CONDITIONS

//Changes to:
FUNCTION_NAME = "PARAMETER" and ADDITIONAL_CONDITIONS
```

Where:

- FUNCTION\_NAME represents any JQL function name
- PARAMETER represents the function's parameter
- ADDITIONAL\_CONDITIONS represents any additional JQL conditions

#### Example

This example shows how the transformation can work on a specific JQL query.

```text
//starting JQL format
issueFunction in hasLinkType("Blockers") and resolution is empty

//would be changed to:
hasLinkType = "Blockers" and resolution is empty
```

This query is looking for:

1. Issues that have a link of type Blockers.
2. AND are unresolved (resolution is empty)

```text
for(JFilter f in admGetAllFilters()) {
    string oldFunction = "hasLinkType";
    string newFunction = "hasLinkType";
    
    if(contains(f.jql, oldFunction)) {
        string jql = f.jql;    
        string [] pieces = split(f.jql, oldFunction);
        
        jql = replace(pieces[0], "issueFunction in ", "") + newFunction;
        
        pieces[1] = replace(pieces[1], "(", " = ");
        pieces[1] = replace(pieces[1], ")", "");
        
        jql += pieces[1];
        f.jql = jql;
        
        admUpdateFilter(f);
        runnerLog("Filter \"" + f.name + "\" [" + f.id + "] owned by " + userFullName(f.owner) + " has been updated to use the new syntax for function: <strong>" + oldFunction + "</strong>", true);
    }
}
```

For each filter containing the old `hasLinkType` syntax, the script:

1. Splits the JQL at `hasLinkType`
2. Removes `issueFunction in` from the first part
3. Replaces parentheses with an equal sign (`=`)
4. Reconstructs the JQL with the new syntax
5. Updates the filter with the new JQL

---

## How to make bulk changes on scripts

After migrating to Jira Cloud, scripts often require bulk changes. A common task is identifying scripts that use hard-coded custom field IDs (for example, `customfield_`). Here's how to search across all scripts for these references and perform the update:

1. In the SIL Manager, right-click the **silprograms** folder, then click **Download**.

   ![This screenshot shows the expanded actions menu for the silprograms folder.](/cms_trial/assets/5afa5d2d-5368-4081-bbb2-de5e9c2645aa.png)
2. Extract the downloaded zip file and open it in a tool such as [VS Code](https://code.visualstudio.com/).
3. Use find and replace features to search and update all files in the selected folder.

   ![This screenshot shows the Find and Replace menus available from the Edit drop-down in VS Code.](/cms_trial/assets/adffbfb6-a10e-41a7-9843-1b572a3cfe52.png)
4. Compress (zip) the updated files.
5. Go back to Power Scripts and navigate to the **Self Help** > **Backup/Restore** tab.
6. Next, upload the zip file you saved.

![Power Scripts for Jira Cloud gadget parameter input](/cms_trial/assets/0197bbfd-e5cf-4ddd-a883-0ff5a0cdbda6.png)

Uploading the zip file will replace ALL files in the **silprograms** folder.