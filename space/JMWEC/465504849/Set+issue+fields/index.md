# Set issue fields

When you add this post function to a transition and then trigger the transition, JMWE sets one or more field values of the target work item(s). The target work item can be either the one that triggered the transition or a work item related to the one that triggered the transition. The values for the fields can be provided either as text (with optional [**Nunjucks**](http://mozilla.github.io/nunjucks/templating.html)annotations) or as a JSON object. For example:

- Text - Can be a simple string (for text fields), the string representation of a number, date, or boolean value, or the string representation of a complex value, such as a Version name, a username, a Project key, etc. Multiple values can be separated by commas. You can also use [**Nunjucks**](http://mozilla.github.io/nunjucks/templating.html)annotations to insert information about the work item, the transition being executed, or the current user into the field, using the `issue`, `transition`, and `currentUser` variables, respectively.
- JSON value - Requires the option `Treat value as JSON` (explained below). The value can be a String, a Number, a Boolean, or an Object. It can also be an array of such values.

To find out more about the type of value expected by this post function for different field types, see [Expected value for each field type](/cms_trial/space/JMWEC/466256753/Expected+value+for+each+field+type/).

**Note**: When copying field values using this post function, some consideration is required for specific fields in the destination issue(s):

- **Sprint** - If you are setting the **Sprint** field and you try to copy the value for a closed sprint, that value will not copy. If you are copying multiple sprint values to the **Sprint** field and one of those values is a closed sprint, that value will not be copied (but the other sprint values will be copied).

![Post function configuration to set field values on work item transition](/cms_trial/assets/96745d0d-8c9e-4ad6-9d61-d7a0844d41e9.png)

**To add the 'Set issue fields' post function to a transition:**

1. Click **Edit** for the workflow that has the transition you wish to add the post function to.
2. Select the transition in the Workflow Designer.
3. Click **Post Functions** in the properties panel (or select the **Post Functions** tab).
4. Click**Add post function**.
5. Select *Set issue fields* from the list of post functions.
6. Click **Add**. The *Set issue fields post function*screen will open, where you can configure the post function as needed. See below for more information.
7. Click **Add** to complete the configuration and add the post function to the transition.

After adding, move the post function to the appropriate position according to [Placing post functions in a transition](/cms_trial/space/JMWEC/466289149/Adding+extensions+to+transitions/).

## Issue(s) to operate on

**Target Issue(s)** - Use this to select the target issue(s) on which the selected field(s) needs to be set. Select one of the following:

- **Current issue** - Sets the value of the selected field(s) on the current issue. (Default option*)*
- **Sub-tasks of the current issue** -Sets the value of the selected field(s) on the sub-tasks of the current issue.
- **Parent of the current sub-task** - Sets the value of the selected field(s) on the parent of the current issue
- **Issues that belong to the current issue (Epic)** - Sets the value of the selected field(s) on the issues that belong to the current Epic.
- **Epic of the current issue** -Sets the value of the selected field(s) on the Epic of the current issue.
- **Child issues of the current issue in the Portfolio hierarchy** - Sets the value of the selected field(s) on the child issues of the current issue in the Portfolio hierarchy.
- **Parent issue of the current issue in the Portfolio hierarchy** - Sets the value of the selected field(s) on the parent issue of the current issue in the Portfolio hierarchy.
- **Issues linked to the current issue through any link type** - Sets the value of the selected field(s) on all issues linked to the current issue.
- **Issues linked to the current issue through the following link type** - Sets the value of the selected field(s) on issues linked to the current issue through a specific link type.  
  **Issue Link** (displayed only when the previous option is selected): Select an issue link type from the drop-down.
- **Issues returned by the following Nunjucks template** -Sets the value of the selected field(s) on the issues returned by the result of a Nunjucks template. Enter a Nunjucks template, which is a comma-separated list of valid issue keys.   
  For example:

  - `"TEST-1"`
  - `"TEST-1","TEST-2"`
  - `{{ issue.fields.parent.key }}`
  - `{{ issue.fields.subtasks | join(",", "key") }}`
- **Issues returned by the following JQL search** - Set the value of the selected field(s) on the issues returned by a JQL search. Enter a JQL search expression.   
  For example:

  - `project = TEST` returns issues of the project with the key TEST
  - `project = {{ issue.fields.project.key }} and assignee = {{currentUser._accountId}}` returns issues of a project that belong to the project with key TEST and the assignee is the current user
  - ```text
    {% if issue.fields.assignee %}
        assignee = {{issue.fields.assignee._accountId}}
    {% else %}
        issuekey=INVALID-1
    {% endif %}
    ```

The {% if %} block is necessary to avoid an invalid JQL query when the issue is unassigned. In this case, the template returns a valid JQL query that returns no issue (`issuekey=INVALID-1`).

## Set Fields

**Add Field(s)** - Select one or more fields from the drop-down to add them to the panel below, where you can set:

- **Value** - Enter a value to be assigned to the respective field in the target issue using a Nunjucks template. See [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/), to know more about adding dynamic content such as issue, transition, or user information to the selected field.
- **Option** - Select one or more options to check the specified target field value(s) as specified and set the value accordingly. Available options:

  - **Treat value as JSON** -Sets the respective field value(s) from a JSON object or an array of objects. It considers the `Value` in the value template and parse it like a JSON string into a JavaScript object. This will be passed back to Jira as the value of the field. To learn about the *JSON value* expected by the post function, see [Expected value for each field type](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/78481552).
  - **Set only if field is empty** -Sets the value of the selected field only if the field in the target issue(s) is empty.
  - **Ignore empty value** -Does not set (clear) the selected field, if the value is empty or null.
  - **Append value(s) to the field** -Appends the specified value(s) to the selected field of the current issue. This is applicable only to multi-valued fields.
  - **Remove source value(s) from destination field** - Remove the value(s) in the source field from the destination field.

Click **Add** to add the respective field to the list of fields to be set using the post function. You can edit or delete a field using the **Edit** or **Delete** icons of the respective field.

## Advanced options

Expand this section to see advanced configurations including which user will run the post function, conditional execution, and delayed execution.

### Run As

- **Run as current user** - The current user will be the author of the assignee change.
- **Run as add-on user** - The add-on user will be the author of the assignee change.
- **Selected user** - The user selected will be the author of the assignee change.
- **User in selected field** - The user value from the selected field will be the author of the assignee change.
- **Selected user** - The user value returned from the Nunjucks template will be the author of the assignee change.

If you select any option other than "Run as add-on user", so that the assignment appears to be done by the current user or a specific user, the selected user will need to have the **Edit Issues** permission.

### Conditional execution

Check **Run this post-function only if a condition is verified** to execute this post function based on the result of a Nunjucks template; see [Conditional execution](/cms_trial/space/JMWEC/466256678/Conditional+Execution/).

### Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.

JMWE shows an error message on the issue view if any error occurs during the execution of the post function. This message is only displayed if the current user is a Jira administrator.