# Clear fields of linked issues (Deprecated)

This post function has been deprecated for some time, and will be completely removed by the end of **December 2025**. Once this post function has been removed from JMWE, you will not be able to:

- **Add** another instance
- **Edit** any existing instances
- **Execute any instances - automatically or manually**

## Replacing this post function

This post function has been replaced with the [Clear fields](/cms_trial/space/JMWEC/466226128/Clear+fields/) post function. Use the table below to migrate your configuration; settings should be migrated to the new post function exactly as they exist in the obsolete one, except where noted.

| **Configuration option** | **Migrate to** | **Notes** |
| --- | --- | --- |
| Issue Link Type | Target issues | If the obsolete post function is set to **Any**, use **Issues linked to the current issue through any link type**.  If the obsolete post function is set to a specific link type, select **Issues linked to the current issue through the following link type**, and set the **Issue link** field to the appropriate link type. |
| Field(s) | Fields |  |
| Advanced options → Settings → Run as | Advanced options → Settings → Run as |  |
| Advanced options → Settings → Run this post-function only if a condition is verified | Advanced options → Settings → Run this post-function only if a condition is verified |  |
| Advanced options → Settings → Delay the execution of this post-function | Advanced options → Settings → Delay the execution of this post-function |  |

A workflow post-function that clears the value of the selected field(s) of the issues linked to the current issue through a specific link type.

**To add the 'Clear field value of linked issues' post-function to a transition:**

1. Click **Edit** for the workflow that has the transition you wish to configure the post-function on.
2. In the Workflow Designer, select the transition.
3. Click on `Post Functions`in the properties panel.
4. Click othe n `Add post function`.
5. Selecthe t `Clear field value of linked issues` from the list of post-functions.
6. Click on `Add` to add the post-function on the transition.

   ![JMWE for Jira Cloud workflow transition function dialog for clearing linked issue fields](/cms_trial/assets/8276eb9c-241f-4fb6-a479-99bf6f236625.png)
7. Select the issue link from the `Issue Link` field.
8. Choose the field(s) that should be cleared from `Fields.`
9. Click on `Add` to add the post-function to the transition.

Here are a few [Use cases](/cms_trial/space/JMWEC/466225276/Use+cases/) for this post-function

When you add this post-function to a transition and trigger it, the add-on clears the selected field(s) of the issues linked to the current issue through the specified link type.

### **Run As**

- **Run as current user:** The current user will be the author of the change.

- **Run as add-on user:** The add-on user will be the author of the change.

- **Run as this user:** Any user selected in this field will be the author of the change.

If you select any option other than "Run as add-on user", so that the assignment appears to be done by the current user or a specific user, the selected user will need to have the **Edit Issues** permission.

### **Conditional execution**

To execute this post-function based on the result of a Nunjucks template see [Conditional execution](/cms_trial/space/JMWEC/466256678/Conditional+Execution/).

### **Delayed execution**

Note that you can use this function to clear the fields of the:

- parent issue of a sub-task by using the `is Subtask of` link type and vice versa using the `is Parent of` link type
- Epic of an issue by using the `belongs to Epic` link type and vice-versa using the `is Epic of` link type
- Parent of the portfolio hierarchy by using the `belongs to Initiative` link type and vice-versa using the `is Initiative of` link type

---

A workflow post-function that clears the value of the selected field(s) of the issues linked to the current issue through a specific link type.

#### [light bulb on icon] Clear a set of fields on all the linked issues of the current issue when an Abort is triggered on the current issue

Steps

- Add the *Clear field value of linked issues*post-function to the **Abort**transition of the workflow.
- Select all the fields to be emptied from `Field`