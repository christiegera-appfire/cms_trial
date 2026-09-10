# Copy field value to linked issues (Deprecated)

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
| Destination issue(s) | If the obsolete post function is set to **Any**, use **Issues linked to the current issue through any link type**.  If the obsolete post function is set to a specific link type, select **Issues linked to the current issue through the following link type**, and set the **Issue link** field to the appropriate link type. |
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

A workflow post-function that copies the value(s) of a selected field into the same/different field of all issues linked to the current issue through a selected link type.

**To add 'Copy field value to linked issues' post-function to a transition :**

1. Click **Edit** for the workflow that has the transition you wish to add the post-function on.
2. In the Workflow Designer, select the transition.
3. Click on `Post Functions`in the properties panel.
4. Click on `Add` `post function`.
5. Select `Copy field value to linked issues` from the list of post-functions.
6. Click on `Add` to add the post-function on the transition.

   ![JMWE for Jira Cloud workflow transition function for setting linked issue field values](/cms_trial/assets/6cfbf927-cd4e-4f42-af55-22f6797eebb9.png)
7. Select the field from the `Field` drop-down.
8. Select the destination field from the `Destination field` drop-down. See below for information on this option.
9. Select the link type from the `Issue Link Type` drop-down.
10. Click on `Add` to add the post-function to the transition.
11. After adding, move the post-function to the appropriate position according to [Placing post-functions in a transition](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Adding%20post%20functions%20to%20transitions&linkCreation=true&fromPageId=466257072) document.

See [here](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/78481395/Copy+field+value+to+linked+issues#Use-case) for a use case of the post-function

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. *This message is displayed only if the current user is a Jira administrator.*

When you add this post-function to a transition and trigger the transition, the add-on copies the value(s) of the selected field into the same field of all issues linked to the current issue through the selected link type.

### **Options**

- **Destination field:** Allows copying to a different field than the source field. For example, automatically add the Reporter of the parent Epic to the Watchers of a User Story. Note that if the source field is read-only, you cannot select `Same as source field` in this option.

- **Copy only if not set:** Copies the value(s) of the selected field into the same/different field of all the linked issues, only when the field is empty on the linked issue(s).

- **Create missing value(s):** Allows creating any missing Component/s or Version/s while setting or copying a field that expects Versions or Components. Note this is applicable for version and component fields.

- **Ignore empty value:** Will not set (clear) the selected field of the linked issues, if the value from the current issue is empty or null.

- **Add value(s) to the linked issue:** Appends the value(s) of the selected field to the same/different field of all the linked issues. This is applicable only to multi-valued fields.

- **Send notifications:** JIRA sends notifications for the change in the selected field value on all the linked issues. You can control the default value of the `"Send notifications"` option in the **Configuration** page under JMWE administration. Click [here](/cms_trial/space/JMWEC/465503776/JMWE+Administration/) for more information.

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

Note that you can use this function to copy a field to

- A parent issue of a sub-task by using the built-in `is Subtask of`link type and vice versa using the `is Parent of` link type
- The Epic of an issue by using the built-in `belongs to Epic` link type and vice-versa using the `is Epic of` link type

---

### Use case

A typical use case for this post-function is to copy a field value to issues linked to the current issue during a transition. Consider a workflow where you want to copy the Fix Version/s field from the Stories to Epic, after resolving a user story.

- Add the *Copy field value to linked issues* post-function to the **Resolve** transition of the Story workflow.
- Choose the `has Epic` link type.
- Select `Fix Version/s` in `Source Field`.
- Select `Same as source field` in the `Destination field`.
- Check `Add value(s) to the linked issue` option.

See [here](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/78481302/Use+cases+for+post-functions#Copy-field-value-to-linked-issues) for more use cases