# Copy field value from parent issue (Deprecated)

This post function has been deprecated for some time, and will be completely removed by the end of **December 2025**. Once this post function has been removed from JMWE, you will not be able to:

- **Add** another instance
- **Edit** any existing instances
- **Execute any instances - automatically or manually**

## Replacing this post function

This post function has been replaced with the [Clear fields](/cms_trial/space/JMWEC/466226128/Clear+fields/) post function. Use the table below to migrate your configuration; settings should be migrated to the new post function exactly as they exist in the obsolete one, except where noted.

| **Configuration option** | **Migrate to** | **Notes** |
| --- | --- | --- |
| The **Copy issue fields** post function includes additional options for the source issue and destination issue of the fields to be copied. | Source issue(s) → Parent issue of the current sub-task |  |
| Destination issue(s) → Current issue |  |
| Source field | Fields to copy → Source field | For each instance of **Copy field value from linked issues**, add a field by clicking the **Add** button. |
| Destination field | Fields to copy → Destination field |
| Options → Copy only if not set | Fields to copy → Additional options → Set only if field is empty |  |
| Options → Create missing value(s) |  |  |
| Options → Ignore empty values |  |  |
| Options → Add value(s) to the issue |  |  |
| Options → Send notifications | Advanced options → Settings → Allow Jira to send notifications for this change |  |
| Advanced options → Settings → Run as | Advanced options → Settings → Run as |  |
| Advanced options → Settings → Run this post-function only if a condition is verified | Advanced options → Settings → Run this post-function only if a condition is verified |  |
| Advanced options → Settings → Delay the execution of this post-function | Advanced options → Settings → Delay the execution of this post-function |  |

A workflow post-function that sets the value(s) of a selected field with value(s) from the same/different field of an issue's parent issue.

**To add the 'Copy field value from parent issue' post function to a transition :**

1. Click **Edit** for the workflow that has the transition you wish to add the post-function on.
2. In the Workflow Designer, select the transition.
3. Click on `Post Functions`in the properties panel.
4. Click on `Add` `post function`.
5. Select `Copy field value from parent issue` from the list of post-functions.
6. Click on `Add` to add the post-function on the transition.

   ![JMWE for Jira Cloud workflow transition function for copying parent issue field values](/cms_trial/assets/2a34347d-fd7f-4c55-852e-8157f1eb3479.png)
7. Select the field from the `Field` drop-down.
8. Select the destination field from the `Destination field` drop-down. See below for information on this option.
9. Click on `Add` to add the post-function to the transition.
10. After adding, move the post-function to the appropriate position according to [Placing post-functions in a transition](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Adding%20post%20functions%20to%20transitions&linkCreation=true&fromPageId=466257573) document.

See [here](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/78481406/Copy+field+value+from+parent+issue#Use-case) for a case for this post-function

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. *This message is displayed only if the current user is a Jira administrator.*

When you add this post-function to a transition and trigger the transition, the add-on sets the value(s) of the selected field to the value(s) from the same/different field of the issue's parent issue.

### **Options**

- **Destination field:** Allows copying to a different field than the source field. For example, automatically add the Reporter of the parent Epic to the Watchers of a User Story. Note that if the source field is read-only, you cannot select `Same as source field` in this option.
- **Copy only if not set:** Copies the value of the selected field, only when the field is empty on the current issue.
- **Create missing value(s):** Allows creating any missing Component/s or Version/s while setting or copying a field that expects Versions or Components. Note this is applicable for version and component fields.
- **Ignore empty value:** Will not set (clear) the selected field of the current issue, if the value from the parent issue is empty or null.
- **Add parent value(s) to the current issue:** Appends the selected field of the current issue with value(s) from the same/different field of its parent issue. This is applicable only to multi-valued fields.
- **Send notifications:** JIRA sends notifications for the change in the selected field value on the current issue. You can control the default value of the `"Send notifications"` option in the **Configuration** page under JMWE administration. Click [here](/cms_trial/space/JMWEC/465503776/JMWE+Administration/) for more information.

### Conditional execution

To execute this post-function based on the result of a Nunjucks template see [Conditional execution](https://appfire.atlassian.net/wiki/display/JMWEC/Conditional+execution).

### Run As

- **Run as current user:** The current user will be the author of the field change.
- **Run as add-on user:** The add-on user will be the author of the field change.
- **Run as this user:** Any user selected in this field will be the author of the field change.

Running this post-function as any user other than the "Add-on user" is discouraged

If you select any option other than "Run as add-on user", so that the change appears to be done by the current user or a specific user, the following must be true:

- The *destination* field must be present on the Edit screen applicable to the issue being modified
- The selected user must have the **Edit issues** permission on the issue being modified

### **Delayed execution**

The parent/child relationship in JIRA refers to Issues and their Subtasks, not to the Epics and their Stories.

If you wish to copy a field from an **Epic** to a **Story**, you can use the [Copy field value from linked issues](/cms_trial/space/JMWEC/466322381/Copy+field+value+from+linked+issues+(Deprecated)/) post-function.

---

### Use case

A typical use case for this post-function is to set the value(s) of a selected field with value(s) from the same/different field of an issue's parent issue. Consider a use case where you want to copy the Fix Versions of the subtask from the parent. To configure this:

- Add the *Copy field value from parent issue* post-function to the **Create** transition of the sub-task workflow.
- Select `Fix Version/s`in `Source Field`.
- Select `Same as source field` in the `Destination field`.

Refer [here](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/78481302/Use+cases+for+post-functions#Copy-field-value-from-parent-issue) for more use cases