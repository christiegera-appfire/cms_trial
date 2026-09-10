# Copy value from field to field (Deprecated)

This post function has been deprecated for some time, and will be completely removed by the end of **December 2025**. Once this post function has been removed from JMWE, you will not be able to:

- **Add** another instance
- **Edit** any existing instances
- **Execute any instances - automatically or manually**

## Replacing this post function

This post function has been replaced with the [Copy issue fields](/cms_trial/space/JMWEC/466323304/Copy+issue+fields/) post function. Use the table below to migrate your configuration; settings should be migrated to the new post function exactly as they exist in the obsolete one, except where noted.

| **Configuration option** | **Migrate to** | **Notes** |
| --- | --- | --- |
| The **Copy issue fields** post function includes additional options for the source issue and destination issue of the fields to be copied. | Source issue(s) → Current issue |  |
| Destination issue(s) → Current issue |  |
| From field | Fields to copy → Source field |  |
| Return “parent-child” for cascading custom fields |  |  |
| To field | Fields to copy → Destination field |  |
| Options → Copy only if not set | Fields to copy → Additional options → Set only if field is empty |  |
| Options → Create missing value(s) |  |  |
| Options → Ignore empty values |  |  |
| Options → Add value(s) to the issue |  |  |
| Options → Send notifications | Advanced options → Settings → Allow Jira to send notifications for this change |  |
| Advanced options → Settings → Run as | Advanced options → Settings → Run as |  |
| Advanced options → Settings → Run this post-function only if a condition is verified | Advanced options → Settings → Run this post-function only if a condition is verified |  |
| Advanced options → Settings → Delay the execution of this post-function | Advanced options → Settings → Delay the execution of this post-function |  |

A workflow post-function that copies the value(s) of a selected field to another field of the same issue.

**To add 'Copy value from field to field' post-function to a transition :**

1. Click **Edit** for the workflow that has the transition you wish to add the post-function on.
2. In the Workflow Designer, select the transition.
3. Click on `Post Functions`in the properties panel.
4. Click on `Add` `post function`.
5. Select `Copy value from field to field` from the list of post-functions.
6. Click on `Add` to add the post-function on the transition.

   ![JMWE for Jira Cloud workflow transition function for copying values between fields](/cms_trial/assets/bd2677d2-fc6e-4dc5-8b82-35306cf927ae.png)
7. Select the field name from the `From field` drop-down.
8. Select the field name from the `To field` drop-down.
9. Click on `Add` to add the post-function to the transition.

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. *This message is displayed only if the current user is a Jira administrator.*

When you add this post-function to a transition and trigger the transition, the add-on copies the value(s) of the selected `From field` to the `To field`of the current issue.

### Options

- **Return "parent-child" for cascading custom fields:** This option is applicable for the **Select list (cascading)** custom fields. If you select the `Return "parent-child" for cascading custom fields` option, values from both the parent and child lists are copied into the destination field. For example**,**a custom cascading field has the values `A` and `1` in the parent and its child lists respectively. When this field is copied into a text field

  - without the option, the value `1` is copied into the text field
  - with the option, the value `A - 1` is copied into the text field.

- **Copy only if not set:** Copies the value(s) of the `From field` to the `To field` of the current issue, only when the `To field` is empty on the current issue.

- **Create missing value(s):** Allows creating any missing Component/s or Version/s while setting or copying a field that expects Versions or Components. Note this is applicable for version and component fields.

- **Ignore empty value:** Will not set (clear) the destination field of the current issue, if the value of the source field is empty or null.

- **Add value(s) to the destination field:** Appends the value(s) of the selected `From field` to the `To field` of the current issue. This is applicable only to multi-valued fields.

- **Send notifications:** Jira sends notifications for the change in the selected `To field` value on the current issue. You can control the default value of the `"Send notifications"` option in the **Configuration** page under JMWE administration. Click [here](/cms_trial/space/JMWEC/465503776/JMWE+Administration/) for more information.

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

### Delayed execution

---

### Use case

A typical use case for this post-function is to copy a field to another field value of the same issue during a transition. Consider a use case where you want to set the components of an issue with a value selected from a cascading field that carries the Main and Sub-components in parent and child. To configure this:

- Add the *Copy value from field to field* post-function to the **Create** transition of the issue workflow.
- Select the `Cascading` field as the `From field`.
- Select the `Components` field as the `To field.`
- Select `Return "parent - child" for cascading custom fields` option.

Note: The Component name should be in `Component - Subcomponent` format.

See [here](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/78481302/Use+cases+for+post-functions#Copy-value-from-field-to-field) for more use cases.