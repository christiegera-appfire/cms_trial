# Filter projects in the Create Jira Issue dialog box

You can control what bound projects appear in the **Projects** menu on the **Create Jira Issue** dialog box on Salesforce.

This guide shows you how to create a project filter and apply that filter when creating a new Jira Issue.

## Create a project filter

1. Log into your Salesforce and click **Settings** > **Setup**.
2. In the sidebar, use **Quick Find** to type `Installed Packages` then click the **Installed Packages** link that appears.
3. Look for *JIRA Cloud for Salesforce* and click **Configure**.
4. On the configuration screen, scroll to the **Issue Creation** section and click the **pencil icon**.

   ![Issue Creation.png](/cms_trial/assets/bbad9043-b075-4212-8191-d5d1ee9c72c7.png)
5. You have three **Filter Types** to choose from:

   - **Allow All Projects** - The default option. All bound projects will be listed in the **Create Jira Issue** dialog box.
   - **Whitelist** - Only allow selected bound projects to be listed in the **Create Jira Issue** dialog.
   - **Blacklist** - Allow all bound projects *except* the selected projects to be listed in the **Create Jira Issue** dialog box.
6. For this example, we've selected **Whitelist** for the **Filter Type**.  
   You will then be asked to select what bound projects to include in the whitelist.
7. We've selected the *ITSM Project TCW* project to be whitelisted.  
   Now, only these projects appear in the **Create Jira Issue** dialog.

   ![project tag filter.png](/cms_trial/assets/15465245-267a-42d5-ba27-9906f5ed216a.png)
8. After clicking **Save**, the **Filter Type** and the bound project that was selected will be displayed on the top right of the **Issue Creation** section:

   ![issue created.png](/cms_trial/assets/e218f508-3c0d-44a8-935b-50199b15df74.png)

## Filter by project when creating a new Jira issue

1. After creating the filter, [create a new Jira issue](/cms_trial/space/CSFJIRA/3091792703/Create+a+Jira+work+item+from+Salesforce/).
2. In the **Create Jira Issue** dialog box, you can now choose which bound project to create the new Jira issue in.

   ![contentId-1873511284](/cms_trial/assets/c6fce2cc-0aa0-48c5-9af6-9c974aa5d575.png)
3. The projects that appear on this menu are dependent on the **Filter Type** and selected bound projects in the **Project Filter** configuration shown above.

## Related information

- [Filter Jira comments in Salesforce cases](/cms_trial/space/CSFJIRA/1873413366/Filter+Jira+comments+in+Salesforce+Cases/)