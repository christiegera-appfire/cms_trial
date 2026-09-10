# Deprecated post functions

### Deprecated post functions will be removed

Due to updates in the Atlassian platform, the deprecated post functions in this section will be completely removed from JMWE Cloud by the **end of December 2025**. These post functions have been obsolete for some time, and now must be replaced. When this change occurs, you will not be able to:

- **Add** an obsolete post function
- **Edit** any existing obsolete post functions
- **Execute any obsolete post function - automatically or manually**

In order for your automations to continue to function, **you** ***must migrate*** obsolete post functions before they are removed. All functions that are possible with deprecated post functions are available in their current equivalents.

This section includes an overview of how to migrate any deprecated post functions still in Workflows or Actions, as well as specific steps for each of the deprecated post functions.

- [**Migrate to current post functions**](/cms_trial/space/JMWEC/2104656018/Migrating+to+current+post+functions/) - For details on how to locate deprecated post functions in your instance; using the [JMWE Workflow Extensions](/cms_trial/space/JMWEC/466321411/JMWE+workflow+extensions/) page you can locate obsolete post functions in your Workflows using a filter on the Name column, and each of the Actions pages ([Shared](/cms_trial/space/JMWEC/466288975/Shared+actions/), [Scheduled](/cms_trial/space/JMWEC/466321868/Scheduled+actions/), and [Event-based Actions](/cms_trial/space/JMWEC/465473524/Event-based+actions/)) includes a column filter for post functions that are included in an Action.
- [**Identifying all deprecated post functions**](/cms_trial/space/JMWEC/2453340227/Identifying+all+deprecated+post+functions/) - A method exists to identify all deprecated post functions across all workflows using a Python script and the Jira Cloud Workflow REST API (as opposed to working one workflow at a time through the [JMWE workflow extenstions](/cms_trial/space/JMWEC/466321411/JMWE+workflow+extensions/) Administration page).
- [**Resolving deprecated post functions**](/cms_trial/space/JMWEC/2162262242/Resolving+deprecated+post+functions/) - Each of these pages include details on a specific post function, including steps on how to move to a current post function.

## Replacement post functions

Each of the obsolete post functions has been replaced with a current version that includes the full functionality of the older version. It is **highly recommended** that you migrate to the current version of each post function before December 2025, as obsolete post functions will be removed from JMWE as of that month.

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