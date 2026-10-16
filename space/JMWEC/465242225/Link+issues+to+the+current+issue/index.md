# Link issues to the current issue

A post function that will link the current issue to all issues that satisfy a parameterized JQL query.

When you add this post function to a transition and trigger it, the add-on links the current issue to the specified number of issues that satisfy the specified parameterized JQL query.

[Unmapped macro: 47fa61b6-fe1c-40c9-b236-623cdbc35833/4d8fa66b-88bf-4899-a37e-5926131c46ac/static/multiexcerpt-fast-include-block-macro — no content to fall back on]

JMWE shows an error message on the issue view if any error occurs during the execution of the post function. *This message is displayed only if the current user is a Jira administrator.*

![Link Issues to the Current Issue configuration screen](/cms_trial/assets/6e525ecf-191e-4307-b77d-626583d7abae.png)

## Issues to link

- **JQL Filter** - Input a JQL expression that returns the issues to link to the current issue. You can insert [issue, transition, currentUser and now](/cms_trial/space/JMWEC/465373277/Variables+in+Nunjucks+Templates/) variables in your JQL expression and test it using the [JQL expression tester](/cms_trial/space/JMWEC/466290063/JQL+expression+editor+and+tester/) provided in this post function.

  **Examples:**

  - `project = TEST`returns the issues of the project whose key is TEST
  - `assignee is EMPTY` returns all the unassigned issues.
  - `project=TEST order by created desc`returns the issues of the project whose key is `TEST` in descending order by `Created` time

To specify a condition on a user, you need to specify an accountId *without the accountId: prefix*. For example: `assignee = 557058:472c64c9-2567-4213-839b-86bf21558300`. You can access the prefix-less accountId of a user through the `_accountId` property.

**Note**: If the current issue satisfies the specified JQL query, an error is logged because you cannot link an issue with itself.

**Examples:**

```java
project = {{ issue.fields.project.key }} and assignee = {{currentUser._accountId}}
```

```java
{% if issue.fields.assignee %}
    assignee = {{issue.fields.assignee._accountId}}
{% else %}
    issuekey=INVALID-1
{% endif %}
```

You can find more information about searching for Jira issues using JQL here: [Advanced searching](https://confluence.atlassian.com/jirasoftwarecloud/advanced-searching-764478330.html) and [Search Jira like a boss with JQL](https://confluence.atlassian.com/jiracore/blog/2015/07/search-jira-like-a-boss-with-jql).

- **Max. Issues** - Input the maximum number of issues that the JQL expression should return. The value cannot be more than 50.
- **Nunjucks condition** - Select this option to filter the issues returned by the JQL search. Input a Nunjucks template in the **Filter Expression** that returns `true` if the issue returned by the JQL search should be linked to the current issue. The filter script is evaluated for each issue returned by the JQL search, in turn, and that issue is available through the `targetIssue` variable. This is especially useful when you want to filter linked issues that cannot be filtered using the JQL.   
    
  For example, filtering issues refining a text search with an exact match that cannot be done with JQL. For example to check for issues with `summary ~ "MacBook Pro"` the JQL returns all issues with “MacBook” and “Pro” in the summary (say, “MacBook for Pro users”). In such a case, you should be using the “Filter Expression” to filter issues that have “MacBook Pro” in the summary with a Nunjucks template as follows:

```text
{{ issue.fields.summary.includes("MacBook Pro") }}
```

## Link type

- **Issue Link Type** - Select the link type to be created between the current issue and the issues returned from the JQL expression.

## Advanced options

Expand this section to see advanced configurations including which user will run the post function, conditional execution, and delayed execution.

## Run As

This option enables you to configure as which Jira user the post function will run.

- **Current user** - The current user will be the author of the action.
- **Add-on user** -The add-on user will be the author of the action.
- **Selected user** -The user in the **Select user** field will be the author of the action.

  - **Select user** - *Only available when* ***Selected user*** *is set.* Select a user from the pull-down menu. Enter a name to search for a specific user account.
- **User in selected field** - The user value from the **Select field** field.

  - **Select field** - *Only available when* ***User in selected field*** *is set.* Select a User Picker field; if you select a User Picker (multiple users) field, only the first user will be used.
- **User from script** - The user value returned from a Nunjucks script.

If you select any option other than **Run as add-on user**, so that the assignment appears to be done by the current user or a specific user, the selected user will need to have the **Edit Issues** permission for the issue being updated.

## Conditional execution

It is possible to configure the post function to execute (or not execute) only in specific circumstances. The **Conditional execution** option sets this behavior:

- **Run this post-function only if a condition is verified**: Select this option to execute this post-function based on the result of a Nunjucks template. See [Conditional execution](https://appfire.atlassian.net/wiki/display/JMWEC/Conditional+execution) for more information.

  - **Condition**: *This option only displays when* ***Run this post-function only if a condition is verified****, above, is checked.* Enter the Nunjucks template as needed.

## Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post function, so that the sub-tasks are created before they are transitioned.

Where possible, it is recommended to use the [Sequence of post-functions](/cms_trial/space/JMWEC/466322933/Sequence+of+post+functions/) post function or [Shared action](/cms_trial/space/JMWEC/466323396/Shared+Action+post+function/) post function to execute a series of post functions in a specific sequence instead of applying a delay.