# Shared Action post-function

A post function that runs an Action (a sequence of one or more JMWE post-functions), created in the [Shared Actions](/cms_trial/space/JMWEC/466288975/Shared+actions/) page, on the current issue or issues related to the current issue.

JMWE shows an error message on the issue view if any error occurs during the execution of the post function. This message is only displayed if the current user is a Jira administrator.

![Shared Action post function configuration screen](/cms_trial/assets/cf618172-782f-4990-9b50-4c2cf10b2dc5.png)

**To add the 'Shared Action' post function to a transition:**

1. Click **Edit** for the workflow that has the transition, you wish to add the post-function on.
2. In the Workflow Designer, select the transition.
3. Click on **Post Functions** in the properties panel.
4. Click on **Add post function**.
5. Select **Shared Action post-function** from the list of post-functions.
6. Click on **Add** to add the post-function on the transition.
7. Select the target issue. See **Issue(s) to operate on,** below.
8. Select one of the listed Shared Actions. See [Shared Actions](/cms_trial/space/JMWEC/466288975/Shared+actions/) for more information
9. Click on **Add** to add the post-function to the transition.

## Issue(s) to operate on

Select the issues on which the Shared action should run. They can be:

- **Target issues**

  - **Current issue** - Run the Shared action on the current issue. *This is the default option.*
  - **Sub-tasks of the current issue -** Run the Shared action on each sub-task of the current issue.
  - **Parent issue of the current sub-task** - Run the Shared action on the parent of the current issue.
  - **Issues that belong to the current issue (Epic)** - Run the shared action on each issue that belongs to the current Epic.
  - **Epic of the current issue -** Run the Shared action on the Epic of the current issue.
  - **Child issues of the current issue in the Portfolio hierarchy** - Run the Shared action on each child issue of the current issue in the Portfolio hierarchy.
  - **Parent issue of the current issue in the Portfolio hierarchy** - Run the Shared action on the parent issue of the current issue in the Portfolio hierarchy.
  - **Issues linked to the current issue through any link type** - Run the Shared action on all issues linked to the current issue.
  - **Issues linked to the current issue through the following link type** - Run the Shared action on the linked issues of a specific link type. Select the specific link type under “Issue link”.
  - **Issues returned by the following Nunjucks template**- Run the Shared action on the issues returned by the result of a [Nunjucks template](/cms_trial/space/JMWEC/465503811/Using+Nunjucks+Templates/). Input a Nunjucks template which is a comma-separated list of valid issue keys. For example:

    - `"TEST-1"`
    - `"TEST-1","TEST-2"`
    - `{{ issue.fields.parent.key }}`
    - `{{ issue.fields.subtasks | join(",", "key") }}`
  - **Issues returned by a JQL search** - Run the Shared action on issues returned by a JQL search. Input a JQL search expression. For example:

    - `project = TEST` returns issues of the project with the key TEST
    - `project = {{ issue.fields.project.key }} and assignee = {{currentUser._accountId}}` returns issues of a project that belong to the project with key TEST and the assignee is the current user

      ```text
      {% if issue.fields.assignee %}
          assignee = {{issue.fields.assignee._accountId}}
      {% else %}
          issuekey=INVALID-1
      {% endif %}
      ```

**Note**: The `{% if %}` block is necessary to avoid an invalid JQL query when the issue is unassigned. In that case, the template will return a valid JQL query that returns no issue (`issuekey=INVALID-1`).

- **Description** - Give this instance of the Shared action a description.

## Shared Action

Select the Shared Action to execute. See [Shared Actions](/cms_trial/space/JMWEC/466288975/Shared+actions/) for more information on creating these types of actions.

## Advanced Options

### Error handling

- **Stop the action if a post-function encounters an error** - By default, even if one of the post functions fails with an error, the remaining post functions in the action will still run. Select this option to stop the execution of subsequent post functions after an error occurs.

### Conditional execution

It is possible to configure the post-function to execute (or not execute) only in specific circumstances. The **Conditional execution** option sets this behavior:

- **Run this post-function only if a condition is verified**: Select this option to execute this post-function based on the result of a Nunjucks template. See [Conditional execution](https://appfire.atlassian.net/wiki/display/JMWEC/Conditional+execution) for more information.

  - **Condition**: *This option only displays when* ***Run this post-function only if a condition is verified****, above, is checked.* Enter the Nunjucks template as needed.

### Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.

## Passing variables within a sequence

Using the `{% setContextVar %}` Nunjucks tag, you can pass data from one post-function to all subsequent post-functions.

`context`: Holds all the *context variables* added in the current post-function. For example, if you create a context variable `myVar` in the first post-function of the sequence:

```groovy
{% setContextVar myVar = "a value" %}
```

This variable will then be available in subsequent post-functions as:

```groovy
{{ context.myVar }}
```

Note that the context variable will not function correctly when used in the [Nunjucks Template tester](/cms_trial/space/JMWEC/465373737/Nunjucks+Template+Tester/).

## Variables specific to the Create Issue(s) post-function

`newIssueKey:` Stores the issue key of the *last* issue created by a Create Issue(s) post-function in the sequence. You can access it as:

```groovy
{{ context.newIssueKey }}
```

`newIssueKeys:` Stores an array of the keys of all the issues created by any Create Issue(s) post-function in the sequence. You can access the created issues from

```groovy
{{ context.newIssueKeys }}
```

For example: to add a comment on the current issue with the keys of the issue created

```groovy
Issues created are:
{{ context.newIssueKeys | join(",") }}
```

You can access the information of a specific issue using the [issue](/cms_trial/space/JMWEC/465373638/Custom+filters/) filter. For example: To get the assignee of the issue created by the Create issue post-function:

```javascript
{{ context.newIssueKey | issue("assignee") | field("fields.assignee.displayName") }}
```