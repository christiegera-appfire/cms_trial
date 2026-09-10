# Sequence of Post-functions

A post function that runs a sequence of JMWE post functions on the current issue (or issues related to the current issue). Using this post function is the safest way of guaranteeing that a series of post-functions run *in a predictable order* during a transition - it is easier and more reliable than using [Delayed execution](/cms_trial/space/JMWEC/466322009/Delayed+execution/) on each post function (as was previously recommended).

For example, consider that during a transition you need to first create a new issue (using the [Create Issue(s)](/cms_trial/space/JMWEC/466256916/Create+issue(s)/) post-function) and *then* send a notification email mentioning the new issue (using the [Email Issue](/cms_trial/space/JMWEC/466322658/Email+issue/) post-function). In this scenario, you need to make sure that the first post function has finished running before starting the second, which is something that Jira Cloud doesn't guarantee if you don't use a **Sequence of post functions** post function.

![Sequence of Post Functions configuration screen](/cms_trial/assets/6989d58b-af50-4453-a98a-ed6345e7b387.png)

**To add the 'Sequence of Post-functions' post function to a transition:**

1. Click **Edit** for the workflow that has the transition you wish to add the post-function on.
2. In the Workflow Designer, select the transition.
3. Click **Post Functions** in the properties panel.
4. Click **Add post function**.
5. Select **Sequence of Post-functions** from the list of post functions.
6. Click **Add** to navigate to the *Create issue(s) post-function*screen where you can add configuration details to the post-function. See below for configuration details.
7. Click **Add** to add the post-function to the transition.

After adding the post function, move it to the appropriate position according to [Placing post functions in a transition](/cms_trial/space/JMWEC/466289149/Adding+extensions+to+transitions/).

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. This message is only displayed if the current user is a Jira administrator.

## Issue(s) to operate on

Select the issues on which the sequence of post-functions should be run.

- **Target issue(s)**

  - **Current issue** - Select this option to run the sequence of post-functions on the current issue. *This is the default option.*
  - **Sub-tasks of the current issue -** Select this option to run the sequence of post-functions on the sub-tasks of the current issue
  - **Parent issue of the current sub-task** - Select this option to run the sequence of post-functions on the parent of the current issue
  - **Issues that belong to the current issue (Epic)** - Select this option to run the sequence of post-functions on the issues that belong to the current Epic
  - **Epic of the current issue** - Select this option to run the sequence of post-functions on the Epic of the current issue
  - **Child issues of the current issue in the Portfolio hierarchy** - Select this option to run the sequence of post-functions on the child issues of the current issue in the Portfolio hierarchy
  - **Parent issue of the current issue in the Portfolio hierarchy** - Select this option to run the sequence of post-functions on the parent issue of the current issue in the Portfolio hierarchy
  - **Issues linked to the current issue through any link type** - Select this option to run the sequence of post-functions on all issues linked to the current issue
  - **Issues linked to the current issue through the following link type** - Select this option to run the sequence of post-functions on the linked issues of a specific link type. Select the specific link type under “Issue link”
  - **Issues returned by the following Nunjucks template** - Select this option to run the sequence of post-functions on issues returned by the result of a Nunjucks template. Input a Nunjucks template which is a comma-separated list of valid issue keys. For example:  
    `"TEST-1"`  
    `"TEST-1","TEST-2"`  
    `{{ targetIssue.fields.parent.key }}`  
    `{{ targetIssue.fields.subtasks | join(",", "key") }}`
  - **Issues returned by a JQL search**:  Select this option to run the sequence of post-functions on issues returned by a JQL search. Input a JQL search expression. For example:  
    `project = TEST` returns issues of the project with the key TEST  
    `project = {{ targetIssue.fields.project.key }} and assignee = {{currentUser._accountId}}` returns issues of a project that belong to the project with key TEST and the assignee is the current user

    ```text
    {% if targetIssue.fields.assignee %}
        assignee = {{targetIssue.fields.assignee._accountId}}
    {% else %}
        issuekey=INVALID-1
    {% endif %}
    ```

**Note**:the `{% if %}` block is necessary to avoid an invalid JQL query when the issue is unassigned. In that case, the template will return a valid JQL query that returns no issue (`issuekey=INVALID-1`).

## Post-functions

![JMWE for Jira Cloud post function sequence with function ordering interface](/cms_trial/assets/c623340c-cfad-4350-9438-bb04e2e4afcd.png)

Create the ordered list of post functions to be run against the selected issue. The following controls are available:

- Click **Add post function** to add a post function to the list.
- To reorder post functions, use the handle ( [hamburger icon icon] ) to drag and drop a post function to its new position in the order.
- Click **Caret** ( [caret down icon] )to show or hide a post function’s configuration.

  - Click **Edit** ( [edit pencil icon] )to edit the post function configuration.
  - Click **Remove** ( [delete icon] )to completely remove a post function from the sequence.   
    ⚠️ **Note**: this cannot be undone!

## Error handling

**Skip subsequent post-functions if a post-function encounters an error** - By default, even if one of the post functions fails with an error, the remaining post functions in the sequence will still run. Select this option to stop the execution of subsequent post functions after an error occurs.

## Conditional execution

It is possible to configure the post-function to execute (or not execute) only in specific circumstances. The **Conditional execution** option sets this behavior:

- **Run this post-function only if a condition is verified**: Select this option to execute this post-function based on the result of a Nunjucks template. See [Conditional execution](https://appfire.atlassian.net/wiki/display/JMWEC/Conditional+execution) for more information.

  - **Condition**: *This option only displays when* ***Run this post-function only if a condition is verified****, above, is checked.* Enter the Nunjucks template as needed.

## Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.

## Passing variables within a sequence

By using the `{% setContextVar %}` Nunjucks tag you can pass data from one post function to a subsequent post function.

`context`: Holds all the *context variables* added in the current post-function. For example, if you create a context variable `myVar` in the first post-function of the sequence:

```groovy
{% setContextVar myVar = "a value" %}
```

This variable will then be available to subsequent post-functions as:

```groovy
{{ context.myVar }}
```

**Note**: this variable will not be available in the Nunjucks tester.

### Variables specific to the Create Issue post-function

### `newIssueKey:` Stores the issue key of the *last* issue created by a Create Issue(s) post-function in the sequence. You can access it as:

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