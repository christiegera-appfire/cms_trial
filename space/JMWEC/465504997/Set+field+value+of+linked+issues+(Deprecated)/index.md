# Set field value of linked issues (Deprecated)

This post function has been deprecated for some time, and will be completely removed by the end of **December 2025**. Once this post function has been removed from JMWE, you will not be able to:

- **Add** another instance
- **Edit** any existing instances
- **Execute any instances - automatically or manually**

## Replacing this post function

This post function has been replaced with the [Set issue fields](/cms_trial/space/JMWEC/465504849/Set+issue+fields/) post function. Use the table below to migrate your configuration; settings should be migrated to the new post function exactly as they exist in the obsolete one, except where noted.

| **Configuration option** | **Migrate to** | **Notes** |
| --- | --- | --- |
| Field | Fields to update → Field |  |
| Issue Link Type | Target issue | If the obsolete post function is set to **Any**, use **Issues linked to the current issue through any link type**.  If the obsolete post function is set to a specific link type, select **Issues linked to the current issue through the following link type**, and set the **Issue link** field to the appropriate link type |
| Value | Fields to update → New value |  |
| Options → Treat value as JSON | Fields to update → Additional options → Treat value as JSON |  |
| Options → Copy only if not set | Fields to update → Additional options → Set only if field is empty |  |
| Options → Create missing value(s) |  |  |
| Options → Ignore empty values |  |  |
| Options → Add value(s) to the issue |  |  |
| Options → Send notifications | Advanced options → Settings → Allow Jira to send notifications for this change |  |
| Advanced options → Settings → Run as | Advanced options → Settings → Run as |  |
| Advanced options → Settings → Run this post-function only if a condition is verified | Advanced options → Settings → Run this post-function only if a condition is verified |  |
| Advanced options → Settings → Delay the execution of this post-function | Advanced options → Settings → Delay the execution of this post-function |  |

A workflow post-function that sets the value(s) of a selected field of all issues linked to the current issue through a selected link type. The value can be provided either as text (with optional Nunjucks annotations) or as a JSON value.

**To add 'Set field value of linked issues' post-function to a transition :**

1. Click **Edit** for the workflow that has the transition you wish to add the post-function on.
2. In the Workflow Designer, select the transition.
3. Click on `Post Functions`in the properties panel.
4. Click on `Add` `post function`.
5. Select `Set field value of linked issues` from the list of post-functions.
6. Click on `Add` to add the post-function on the transition.
7. Select the field from the `Field` drop-down.
8. Select the link type from the `Issue Link Type` drop-down.
9. Input a value in the `Value` field. To input the issue or linked issue or transition or current user information in the `Value` field see, [How to insert information using Nunjucks annotations](https://appfire.atlassian.net/wiki/display/IN/How+to+insert+information+using+Nunjucks+annotations).
10. Click on `Add` to add the post-function to the transition.
11. After adding, move the post-function to the appropriate position according to [Placing post-functions in a transition](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=jmwec&title=Adding%20post%20functions%20to%20transitions&linkCreation=true&fromPageId=465504997) document.

![JMWE for Jira Cloud workflow transition function for setting linked issue field values](/cms_trial/assets/d4d6eb4a-c5c9-433b-900d-f30b3587160c.png)

When you add this post-function to a transition and trigger the transition, the add-on sets the specified value(s) on the selected field of all issues linked to the current issue through the selected link type. The value can be provided either as text (with optional [**Nunjucks**](http://mozilla.github.io/nunjucks/templating.html)annotations) or as a JSON value.

- In the case of text, it can be a simple string (for text typed fields), the string representation of a number, date or boolean value, or the string representation of a complex value, such as a Version name, a username, a Project key, etc. Multiple values can be separated by commas. You can also use [**Nunjucks**](http://mozilla.github.io/nunjucks/templating.html)annotations to insert issue, linked issue, transition and current user information into`Value`, using the 'issue', 'linkedIssue', 'transition' and 'currentUser' variables, respectively.
- In the case of a JSON value, which requires the option `Treat value as JSON` (explained below), it can be a String, a Number, a Boolean or an Object. It can also be an array of such values.

To find out more about the type of value expected by this post-function for each field type, see [Expected value for each field type](/cms_trial/space/JMWEC/466256753/Expected+value+for+each+field+type/).

### **Options**

- **Treat value as JSON:** Sets the field value from a JSON object or array of objects. It will take the `Value` in the value template and parse it like a JSON string into a JavaScript object. This will be passed back to Jira as the value of the field. To learn about the *JSON value* expected by the post-function, see [Expected value for each field type](/cms_trial/space/JMWEC/466256753/Expected+value+for+each+field+type/).

- **Copy only if not set:** Sets the value of the selected field on all linked issues only if the field is empty on the linked issues.

- **Create missing value(s):** Allows creating any missing Component/s or Version/s while setting or copying a field that expects Versions or Components. Note this is applicable for version and component fields.

- **Ignore empty value:** Will not set (clear) the selected field of linked issue(s), if `Value` is empty or null.

- **Add value(s) to the linked issue:** Appends the specified value(s) to the selected field of all the linked issues. This is applicable only to multi-valued fields.

- **Send notifications:** Jira sends notifications for the change in the selected field value on the linked issue(s). You can control the default value of the `"Send notifications"` option in the **Configuration** page under JMWE administration. Click [here](/cms_trial/space/JMWEC/465503776/JMWE+Administration/) for more information.

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

Note that you can use this function to set the value of a field of the:

- parent issue of a sub-task by using the `is Subtask of`link type and vice versa using the `is Parent of` link type
- Epic of an issue by using the `belongs to Epic` link type and vice-versa using the `is Epic of` link type
- Parent of the portfolio hierarchy by using the `belongs to Initiative` link type and vice-versa using the `is Initiative of` link type