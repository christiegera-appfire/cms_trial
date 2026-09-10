# Migrating to current post functions

Changes to the Atlassian platform require that JMWE remove all obsolete post functions from JMWE Cloud by the **end of December 2025**. When obsolete post functions are removed from JMWE, existing instances no longer execute. You will no longer be able to:

- **Add** a new instance of any obsolete post functions.
- **Edit** any existing obsolete post functions.
- **Execute any obsolete post function - automatically or manually.**

For your automations to continue functioning as designed, you must replace each obsolete post function with its current version. Every obsolete post function has a replacement that accomplishes the same result. See **Replacement post functions** below for a full list of current post functions to use when updating your automations.

The steps for replacing obsolete post functions are:

1. Locate the obsolete post function.
2. Determine the replacement post function.
3. Recreate the post function configuration.
4. Delete the obsolete post function.

Before removing the obsolete post function, create the updated version so you can verify that the configuration has been transferred fully.

## Locate obsolete post functions

There are a few places you need to check for obsolete post functions, and each has a method of locating obsolete post functions. The JMWE Administration screens where you need to check for obsolete post functions are:

- [JMWE Workflow Extensions](/cms_trial/space/JMWEC/466321411/JMWE+workflow+extensions/)
- [Shared Actions](/cms_trial/space/JMWEC/466288975/Shared+actions/)
- [Scheduled Actions](/cms_trial/space/JMWEC/466321868/Scheduled+actions/)
- [Event-based Actions](/cms_trial/space/JMWEC/465473524/Event-based+actions/)

### JMWE Workflow Extensions

![JMWE for Jira Cloud workflow extensions page with name filtering capabilities](/cms_trial/assets/cf225a87-e700-4791-9043-916da1248e8a.png)

The **JMWE Workflow Extensions** page lists all JMWE extensions that have been added to each Workflow. You can use this page to locate any obsolete post functions by using the filter on the **Name** column (pictured right).

You need to search each Workflow separately.

To locate obsolete post functions:

1. Select the Workflow you want to search from the **Workflow** pulldown menu.
2. Click the **Filter** button ( ▢ ) to the right of the **Name** column.
3. Enter the name of each obsolete post function in the text field. The list of post functions automatically filters as you type.
4. In a separate window, open the Workflow you need to update.
5. Locate the transition listed in the **Transition** column for the obsolete post function and open it.
6. Open the *Post Functions* tab. Locate the obsolete post function in the list.

Before removing the obsolete post function, create the updated version so you can verify that the configuration has been transferred fully.

1. Click **Add post function** in the upper right to add the replacement post function. When prompted, select the appropriate current post function using the list below.
2. Configure the new post function as needed; see individual pages under [Resolving deprecated post functions](/cms_trial/space/JMWEC/2162262242/Resolving+deprecated+post+functions/) for specific steps on moving to the new versions.
3. Once your new post function is configured and moved to the correct order within the transition, disable the obsolete post function.
4. Publish your Workflow and verify that the new post function has the same results. After you’ve verified that the results of the new post function are acceptable, you can delete the obsolete post function.

### Action administration pages

Shared actions, Scheduled actions, and Event-based actions all have the same mechanism for locating obsolete post functions - the **Post-functions** column of the main administration page. To locate obsolete post functions:

Before removing the obsolete post function, create the updated version so you can verify that the configuration has been transferred fully.

1. Open the administration page for the Actions you will be searching.
2. Click the **Filter** button ( ▢ ) beside the **Post-functions** column
3. Select the name of each obsolete post function, or enter the name of each obsolete post function in the text field. The list of Actions automatically filters for just the Actions that include the obsolete post function.
4. For each Action that needs to be updated:

   1. Click the link to open the Action editor.
   2. Click **THEN** to view the list of included post functions.
   3. Click **Add post function** in the upper right to add the replacement post function. When prompted, select the appropriate current post function using the list below.
   4. Configure the new post function as needed; see individual pages under [Resolving deprecated post functions](/cms_trial/space/JMWEC/2162262242/Resolving+deprecated+post+functions/) for specific steps on moving to the new versions.
   5. Once your new post function is configured and moved to the correct order within the Action, delete the obsolete post function.
   6. Save your Action and verify that it has the same results.

## Replacement post functions

Each of the obsolete post functions has been replaced with a current version that includes the full functionality of the older version. It is **highly recommended** that you migrate to the current version of each post function before October 2025, as obsolete post functions will be removed from JMWE as of that month.

| **Obsolete post function** | **Current post function** |
| --- | --- |
| [Assign to last role member](/cms_trial/space/JMWEC/466225934/Assign+to+last+role+member+(Deprecated)/) | [Assign issue(s)](/cms_trial/space/JMWEC/1133772861/Assign+issue(s)/) |
| [Assign to role member](/cms_trial/space/JMWEC/466257482/Assign+to+role+member+(Deprecated)/) | [Assign issue(s)](/cms_trial/space/JMWEC/1133772861/Assign+issue(s)/) |
| [Clear fields of linked issues](/cms_trial/space/JMWEC/466289629/Clear+fields+of+linked+issues+(Deprecated)/) | [Clear fields](/cms_trial/space/JMWEC/466226128/Clear+fields/) |
| [Comment linked issues](/cms_trial/space/JMWEC/465373854/Comment+linked+issues+(Deprecated)/) | [Comment issue(s)](/cms_trial/space/JMWEC/466322568/Comment+issue(s)/) |
| [Copy field value from linked issues](/cms_trial/space/JMWEC/466322381/Copy+field+value+from+linked+issues+(Deprecated)/) | [Copy issue fields](/cms_trial/space/JMWEC/466323304/Copy+issue+fields/) |
| [Copy field value from parent issue](/cms_trial/space/JMWEC/466257573/Copy+field+value+from+parent+issue+(Deprecated)/) | [Copy issue fields](/cms_trial/space/JMWEC/466323304/Copy+issue+fields/) |
| [Copy field value to linked issues](/cms_trial/space/JMWEC/466257072/Copy+field+value+to+linked+issues+(Deprecated)/) | [Copy issue fields](/cms_trial/space/JMWEC/466323304/Copy+issue+fields/) |
| [Copy field value to parent issue](/cms_trial/space/JMWEC/466257136/Copy+field+value+to+parent+issue+(Deprecated)/) | [Copy issue fields](/cms_trial/space/JMWEC/466323304/Copy+issue+fields/) |
| [Copy value from field to field](/cms_trial/space/JMWEC/466225614/Copy+value+from+field+to+field+(Deprecated)/) | [Copy issue fields](/cms_trial/space/JMWEC/466323304/Copy+issue+fields/) |
| [Set field value of linked issues](/cms_trial/space/JMWEC/465504997/Set+field+value+of+linked+issues+(Deprecated)/) | [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) |
| [Transition linked issues](/cms_trial/space/JMWEC/466257658/Transition+linked+issues+(Deprecated)/) | [Transition issue(s)](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/) |
| [Transition parent issue](/cms_trial/space/JMWEC/465242394/Transition+parent+issue+(Deprecated)/) | [Transition issue(s)](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/) |