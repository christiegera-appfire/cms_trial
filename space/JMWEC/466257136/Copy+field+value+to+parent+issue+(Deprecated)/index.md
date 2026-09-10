# Copy field value to parent issue (Deprecated)

This post function has been deprecated for some time, and will be completely removed by the end of **December 2025**. Once this post function has been removed from JMWE, you will not be able to:

- **Add** another instance
- **Edit** any existing instances
- **Execute any instances - automatically or manually**

## Replacing this post function

This post function has been replaced with the [Copy issue fields](/cms_trial/space/JMWEC/466323304/Copy+issue+fields/) post function. Use the table below to migrate your configuration; settings should be migrated to the new post function exactly as they exist in the obsolete one, except where noted.

**Tip**: The obsolete post function could only be configured to copy a single field value. The current post function can be configured to copy multiple fields within a single post function. If you have several individual **Copy field value from linked issues** post functions in the same project, they can be grouped together into a single **Copy issue fields** post function!

| **Configuration option** | **Migrate to** | **Notes** |
| --- | --- | --- |
| The **Copy issue fields** post function includes additional options for the source issue and destination issue of the fields to be copied. | Source issue(s) → Current issue |  |
| Destination issue(s) → Parent issue of the current sub-task |  |
| Source field | Fields to copy → Source field | For each instance of **Copy field value from linked issues**, add a field by clicking the **Add** button. |
| Destination field | Fields to copy → Destination field |
| Issue Link Type | Fields to copy → Destination issue(s) |  |
| Options → Copy only if not set | Fields to copy → Additional options → Set only if field is empty |  |
| Options → Create missing value(s) |  |  |
| Options → Ignore empty values |  |  |
| Options → Add value(s) to the issue |  |  |
| Options → Send notifications | Advanced options → Settings → Allow Jira to send notifications for this change |  |
| Advanced options → Settings → Run as | Advanced options → Settings → Run as |  |
| Advanced options → Settings → Run this post-function only if a condition is verified | Advanced options → Settings → Run this post-function only if a condition is verified |  |
| Advanced options → Settings → Delay the execution of this post-function | Advanced options → Settings → Delay the execution of this post-function |  |

A workflow post-function that copies the value(s) of a selected field to the same/different field of the issue's parent issue.

**To add 'Copy field value to parent issue' post-function to a transition :**

1. Click **Edit** for the workflow that has the transition you wish to add the post-function on.
2. In the Workflow Designer, select the transition.
3. Click on `Post Functions`in the properties panel.
4. Click on `Add` `post function`.
5. Select `Copy field value to parent issue` from the list of post-functions.
6. Click on `Add` to add the post-function on the transition.

   ![JMWE for Jira Cloud workflow transition function for setting parent issue field values](/cms_trial/assets/08b3aec9-966f-4f5c-9f8a-63c62f5bbb1b.png)
7. Select the field from the `Field` drop-down.
8. Select the destination field from the `Destination field` drop-down. See below for information on this option.
9. After adding, move the post-function to the appropriate position according to [Placing post-functions in a transition](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Adding%20post%20functions%20to%20transitions&linkCreation=true&fromPageId=466257136) document.

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. *This message is displayed only if the current user is a Jira administrator.*

When you add this post-function to a transition and trigger the transition, the add-on copies the value(s) of the selected field to the same/different field of the issue's parent issue.

### **Options**

- **Destination field:** Allows copying to a different field than the source field. For example, automatically add the Reporter of the parent Epic to the Watchers of a User Story. Note that if the source field is read-only, you cannot select `Same as source field` in this option.

- **Copy only if not set:** Copies the value(s) of the selected field into the same/different field of the issue's parent issue, only when the field is empty on the parent issue.

- **Create missing value(s):** Allows creating any missing Component/s or Version/s while setting or copying a field that expects Versions or Components. Note this is applicable for version and component fields.

- **Ignore empty value:** Will not set (clear) the selected field of the parent issue, if the value from the current issue is empty or null.

- **Add subtask's value(s) to the parent issue:** Appends the value(s) of the selected field to the same/different field of the issue's parent issue. This is applicable only to multi-valued fields.

- **Send notifications:** Jira sends notifications for the change in the selected field value on the parent issue. You can control the default value of the `"Send notifications"` option in the **Configuration** page under JMWE administration. Click [here](/cms_trial/space/JMWEC/465503776/JMWE+Administration/) for more information.

### **Conditional execution**

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

The parent/child relationship in Jira refers to issues and their subtasks, not to the Epics and their Stories.

If you wish to copy a field from a **Story** to an **Epic**, you should use the [Copy field value to linked issues](/cms_trial/space/JMWEC/466257072/Copy+field+value+to+linked+issues+(Deprecated)/) post-function.