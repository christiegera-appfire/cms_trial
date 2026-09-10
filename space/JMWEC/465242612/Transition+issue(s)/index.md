# Transition issue(s)

A workflow post-function that triggers a transition on the current issue or issue related to the current issue. This can be used to move an issue one step further in the workflow.

![Transition issue(s) post function configuration](/cms_trial/assets/7fdf7a3c-42eb-4844-8507-87b34c71000b.png)

**To add the 'Transition current issue' post-function to a transition :**

1. Click **Edit** for the workflow that has the transition you wish to add the post-function on.
2. In the Workflow Designer, select the transition.
3. Click on `Post Functions`in the properties panel.
4. Click on `Add` `post function`.
5. Select `Transition current issue` from the list of post-functions.
6. Click on `Add` to add the post-function on the transition.
7. Select the “Target issue” (see below)
8. Specify transition(s) either in the table or as a result of the calculated Nunjucks template. See **Transition(s)**, below, for more information.
9. Click on `Add` to add the post-function to the transition.
10. After adding, move the post-function to the appropriate position according to [Placing post-functions in a transition](/cms_trial/space/JMWEC/466289149/Adding+extensions+to+transitions/) document.

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. This message is only displayed if the current user is a Jira administrator.

When you add this post-function to a transition and trigger the transition, the add-on will transition the target issues using the specified transition, assuming it is valid for the current status and available to the current or selected user.

## Issue(s) to operate on

Select the issues to be transitioned. They can be:

- **Current issue:** Select this option to transition the current issue. *This is the default option.*
- **Sub-tasks of the current issue:** Select this option to transition the sub-tasks of the current issue
- **Parent issue of the current sub-task:** Select this option to transition the parent of the current issue
- **Issues that belong to the current issue (Epic):** Select this option to transition the issues that belong to the current Epic
- **Epic of the current issue:** Select this option to transition the Epic of the current issue
- **Child issues of the current issue in the Portfolio hierarchy:** Select this option to transition the child issues of the current issue in the Portfolio hierarchy
- **Parent issue of the current issue in the Portfolio hierarchy:** Select this option to transition the parent issue of the current issue in the Portfolio hierarchy
- **Issues linked to the current issue through any link type:** Select this option to transition all issues linked to the current issue
- **Issues linked to the current issue through the following link type:** Select this option to transition the linked issues of a specific link type. Select the specific link type under “Issue link”
- **Issues returned by the following Nunjucks template:**Select this option to transition the issues returned by the result of a Nunjucks template. Input a Nunjucks template which is a comma-separated list of valid issue keys. For example:

  - `"TEST-1"`
  - `"TEST-1","TEST-2"`
  - `{{ issue.fields.parent.key }}`
  - `{{ issue.fields.subtasks | join(",", "key") }}`
- **Issues returned by a JQL search**: Select this option to transition the issues returned by the result of a JQL search. Input a JQL search expression. For example:

  - `project = TEST` returns issues of the project with the key TEST
  - `project = {{ issue.fields.project.key }} and assignee = {{currentUser._accountId}}` returns issues of a project that belong to the project with key TEST and the assignee is the current user
  - ```text
    {% if issue.fields.assignee %}
        assignee = {{issue.fields.assignee._accountId}}
    {% else %}
        issuekey=INVALID-1
    {% endif %}
    ```

    Note that the {% if %} block is necessary to avoid an invalid JQL query when the issue is unassigned. In that case, the template will return a valid JQL query that returns no issue (`issuekey=INVALID-1`).

## Transition(s)

### **Trigger one of the following transitions**

Input the transition `name(s)` or `id(s)` and optionally the workflow name manually or using the Transition picker. If you do not specify the workflow name (manually) the app will not check for a specific workflow. The app triggers the *first* transition specified in the table that is applicable to the issue in context.

**To pick a transition using the Transition picker:**

- Click on Transition picker
- Choose a workflow from Workflow name
- Select a transition from the list of transitions displayed
- Finally, click on either

  - `Use Transition Name` - recommended if you want the post-function to search for the transition to trigger by name, which is useful when targeting multiple workflows.
  - `Use Transition ID` - if you want to differentiate between transitions that bear the same name.
- Click on Add.

**To remove a transition:** Click on the `Remove` link for the specific transition

**To reorder transitions:** Select and move the transition in the table to reorder the list

### **Trigger a calculated transition**

Input a Nunjucks template that returns one or more transition `name(s)` or `id(s)` and optionally the workflow name. To specify a workflow name, write a Nunjucks template that returns the transition `name` or `ID` along with the workflow name separated by `@@.`For example: `Done@@HR workflow`.

To return multiple transitions, write a Nunjucks template that returns transition `names` or `IDs` each on a separate line. For example:

```groovy
2@@Default Jira Workflow
Done@@Another workflow
Close
```

Example of a template returning transition name:

```groovy
{%if issue.fields.priority.name == "Blocker"%}
  Escalate
{% else %}
  Assign
{% endif %}
```

## **Run As**

This option enables you to configure as which Jira user the post-function will run.

- **Current user** - The current user will be the author of the action.
- **Add-on user** -The add-on user will be the author of the action.
- **Selected user** -The user in the **Select user** field will be the author of the action.

  - **Select user** - *Only available when* ***Selected user*** *is set.* Select a user from the pull-down menu. Enter a name to search for a specific user account.
- **User in selected field** - The user value from the **Select field** field.

  - **Select field** - *Only available when* ***User in selected field*** *is set.* Select a User Picker field; if you select a User Picker (multiple users) field, only the first user will be used.
- **User from script** - The user value returned from a Nunjucks script.

If you select any option other than **Run as add-on user**, so that the assignment appears to be done by the current user or a specific user, the selected user will need to have the **Edit Issues** permission for the issue being updated.

## **Transition screen**

If the transition uses a transition screen you might want/need to provide a value for fields(*such as Resolution*) present on the screen. Look below to know how to add/set/remove fields.

- **To add a field**: Select a field from the list of fields and click on`Add.`
- **To Remove an added field**: Click the remove button to the left of the field.
- **To Set a field value**:

  - **Copy value from current issue**: Set the value of the transitioned issue’s field using the value from the same field of the issue that triggered the transition.
  - **Set to other field of current issue**: Set the value of the transitioned issue’s field using a value from a different field of the issue that triggered the transition. Select the source field from the pulldown menu.
  - **Set field value to**: You can set the field to a specific value, either a static value or a dynamic value using Nunjucks annotations.  
    For example: To set the Assignee to Charlie, you can specify the `accountId` (use [Lookup user](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=mwecs&title=Nunjucks%20template%20editor%20and%20tester&linkCreation=true&fromPageId=449446354) feature to know the accountId) of user Charlie in the value box.

Likewise, you might also want to provide a *comment* during that transition.**This will only work if the triggered transition is associated with a transition screen.**

**Note**: Currently, some variables are not available in Nunjucks when using the **Transition issue(s)** post-function. Unavailable variables include:

- **targetIssue**
- **linkedIssue**

- **Comment :** adds a comment to the current issue. The `Comment` can be any simple text, e.g. `This is a comment.` You can also use [**Nunjucks**](http://mozilla.github.io/nunjucks/templating.html)annotations in the comment using variables. To find out more about the variables, see [Using Nunjucks Templates](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/).
- **Comment visibility :**

  - **Restrict to Group :** Restricts the visibility of the comment to a specified group. When you select a valid group name in the `Restrict to Group` field, the comment will be visible only to the members of the specified group. For no restriction, leave the field blank.
  - **Restrict to Project Role :** Restricts the visibility of the comment to a selected project role. When you select a project role from the drop-down `Restrict to Project Role` field, the comment will be visible only to the members of the selected project role. For no restriction, leave the field blank.
  - **Restrict to Internal (Jira Service Desk only) :** Restricts the visibility of the comment to the Service Desk Agents and Collaborators only.

## **Conditional execution**

To execute this post-function based on the result of a Nunjucks template see [Conditional execution](/cms_trial/space/JMWEC/466256678/Conditional+Execution/).

## **Delayed execution**

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.

The **Run as add-on user** and **Run as this user** options are useful if the current user doesn't have the permission to trigger the specified transition on the current issue.

Also, note that the specified transition can be hidden from users using the `Hide Transition` condition.