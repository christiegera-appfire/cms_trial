# Email issue

A post-function that sends a notification email about the current issue or issues related to the current issue.

![Email issue(s) post function configuration screen](/cms_trial/assets/e89167db-4eb1-4a53-8779-e13209c3f0fd.png)

**To add 'Email issue' post-function to a transition:**

1. Click **Edit** for the workflow that has the transition you wish to add the post-function on.
2. In the Workflow Designer, select the transition.
3. Click on `Post Functions`in the properties panel.
4. Click on `Add` `post function`.
5. Select `Email issue` from the list of post-functions.
6. Click on `Add` to add the post-function on the transition.
7. Select the “Target issue” (see below)
8. Input the subject of the Email in `Subject.`
9. Select the recipients in `Recipients.`
10. Click on `Add` to add the post-function to the transition.

JMWE shows an error message on the issue view if any error occurs during the execution of the post-function. This message is only displayed if the current user is a Jira administrator.

When you add this post-function to a transition and trigger the transition, the add-on sends an Email notification about each target issue to the specified recipients.

## Issue(s) to operate on

Select the issues whose recipients should receive the email. They can be:

- **Current issue:** Select this option to send a notification email for the current issue. *This is the default option.*
- **Sub-tasks of the current issue:** Select this option to send a notification email for each subtask of the current issue
- **Parent issue of the current sub-task:** Select this option to send a notification email for the parent of the current issue
- **Issues that belong to the current issue (Epic):** Select this option to send a notification email for each issue that belongs to the current Epic
- **Epic of the current issue:** Select this option to send a notification email for the Epic of the current issue
- **Child issues of the current issue in the Portfolio hierarchy:** Select this option to send a notification email for each child issue of the current issue in the Portfolio hierarchy
- **Parent issue of the current issue in the Portfolio hierarchy:** Select this option to send a notification email for the parent issue of the current issue in the Portfolio hierarchy
- **Issues linked to the current issue through any link type:** Select this option to send a notification email for each issue linked to the current issue
- **Issues linked to the current issue through the following link type:** Select this option to send a notification email for each issue linked to the current issue through a specific link type. Select the specific link type under “Issue link”
- **Issues returned by the following Nunjucks template:** Select this option to send a notification email for each issue returned by the result of a Nunjucks template. Input a Nunjucks template which is a comma-separated list of valid issue keys. For example:

  - `"TEST-1"`
  - `"TEST-1","TEST-2"`
  - `{{ issue.fields.parent.key }}`
  - `{{ issue.fields.subtasks | join(",", "key") }}`
- **Issues returned by a JQL search**: Select this option to send a notification email for each issue returned by a JQL search. Input a JQL search expression. For example:

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

## Email content

Specify the subject and body of the email in this section. Click on the "Expected value" help tab of the Nunjucks editor to know the expected value for the subject and the body.

### **Subject**

Input the subject of the notification Email. For example:

```javascript
Issue {{targetIssue.key}} - {{targetIssue.fields.summary}} resolved
```

### **Text Body**

Input the raw text version of the body of the notification email. This will be used for users who have opted to receive emails in text format (see [user preference settings](https://confluence.atlassian.com/adminjiraserver071/configuring-the-user-default-settings-802592314.html)) or if you do not provide an HTML version below, and the user preference is set to receive emails in an HTML format. For example:

```javascript
Hi,

Issue {{targetIssue.key}} - {{targetIssue.fields.summary}} has been resolved.

Regards,
{{currentUser.displayName}}
```

### **Html Body**

Input the HTML version of the body of the notification email. For example:

```javascript
<br>Hi,</br>
 
<br>Issue <i>{{targetIssue.key}} - {{targetIssue.fields.summary}}</i> has been resolved.</br>
 
<br>Regards,</br>
<br>{{currentUser.displayName}}</br>
```

If you don't provide one, it will be generated automatically from the raw text version [above](#). Note that in the Nunjucks tester for the HTML body, a rendered version of the result is displayed as HTML-rendered value.

### Length limitations

Please note that the Text and HTML body *after processing the Nunjucks template* is limited to **10000 characters**. See this known [Jira Cloud issue](https://ecosystem.atlassian.net/browse/ACJIRA-1937) for details.

A fully-rendered HTML version of fields that are configured to use the Wiki Style Renderer (in the Field Configuration), such as Description, Comments, Environment etc., is now accessible under `issue.renderedFields`. For example:

| Field value (with Wiki markup) | Template | Returns | HTML rendered value in the tester |
| --- | --- | --- | --- |
| Hi  \_This is a test Email\_  Regards Radhika | `{{ targetIssue.renderedFields.description }}` | <p>Hi</p>  <p><em>This is a test Email</em></p>  <p>Regards<br/> Radhika</p> | Hi  *This is a test Email*  Regards Radhika |
| Hi,  The issue has been resolved.  Regards  Radhika | `{{ targetIssue.renderedFields.comment.comments | first | field('body') }}` | Hi, <br/>  <br/> The issue has been resolved. <br/>  <br/> Regards <br/> Radhika | Hi,  The issue has been resolved.  Regards  Radhika |

For performance reasons, renderedFields are only available in this post-function and in the [Nunjucks tester](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=mwecs&title=Nunjucks%20template%20editor%20and%20tester&linkCreation=true&fromPageId=449675818).

## Recipients

The notification Email is sent to the recipients selected in this section.

**Issue members:** You can notify the Reporter (only when the "Notify users of their own changes" in "User Default Settings" is set), Assignee, Watchers and Voters of the target issue using this option

**Specific users:** You can notify specific users using this option.

**Users in field(s):**You can notify users in a Single/Multi-user picker field(s). If a field is not of type User picker, it must contain a [String](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html) representing the *accountId*or comma separated *accountId(s)*.

**Users from template:**You can notify users with *accountId(s)* returned from a Nunjucks template. This can be used, for example, to notify certain users based on a condition ("if" statement). For example:

`{{ targetIssue.fields.SingleUserPicker.accountId }}`

`{{ targetIssue.fields.MultiUserPicker | join(',',"accountId") }}`

`{{ targetIssue.fields.TextField }}`where the Text field contains a [String](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html) representing the *accountId*or comma separated *accountId(s)*

`{% if targetIssue.fields.priority.name == "Critical" %}{{targetIssue.fields.reporter}}{% endif %}` returns the Reporter as Recipient when the priority is **Critical**

To send an email to all members of all Service Desk Organizations associated with the request:

```text
{% set users = [] %}
{% for org in issue.fields["Organizations"] %}
{% set users = users.concat(org.id | usersInOrganization) %}
{% endfor %}
{{ users | join(",","accountId") }}
```

**Email addresses:**You can send the email to explicit email addresses, separated by commas. *This option is only available to Jira Service Desk customers*.

⚠️ Note that a new Service Desk Customer will be created for each email address (don't worry, they don't count towards your license).

**Specific groups:** You can notify members of specific groups using this option.

**Project role members:** You can notify members of specific Project roles using this option.

**Groups from template:**You can notify groups with group *name(s)* returned from a Nunjucks template. If a field is not of type Group picker, it must contain a [String](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html) representing the group *name* or comma separated group *names*. For example:

{{ targetIssue.fields.MultiGroupPicker | join(',',"name") }}

{{ targetIssue[.fields.SingleGroupPicker.name](http://issue.fields.SingleGroupPicker.name) }}

{{ targetIssue.fields.Textfield }}, where the Text field contains a [String](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html) representing the group *name* or comma separated group *names.*

The user executing the post-function (by default the current user) will not receive any notification unless they select the "Notify me of my changes" option on their User Preferences page

Customize this post-function using the additional options provided as part of the post-function. The options are:

## Run As

This option enables you to configure as which Jira user the post-function will run.

- **Current user** - The current user will be the author of the action.
- **Add-on user** -The add-on user will be the author of the action.
- **Selected user** -The user in the **Select user** field will be the author of the action.

  - **Select user** - *Only available when* ***Selected user*** *is set.* Select a user from the pull-down menu. Enter a name to search for a specific user account.
- **User in selected field** - The user value from the **Select field** field.

  - **Select field** - *Only available when* ***User in selected field*** *is set.* Select a User Picker field; if you select a User Picker (multiple users) field, only the first user will be used.
- **User from script** - The user value returned from a Nunjucks script.

If you select any option other than **Run as add-on user**, so that the assignment appears to be done by the current user or a specific user, the selected user will need to have the **Edit Issues** permission for the issue being updated.

## Conditional execution

It is possible to configure the post-function to execute (or not execute) only in specific circumstances. The **Conditional execution** option sets this behavior:

- **Run this post-function only if a condition is verified**: Select this option to execute this post-function based on the result of a Nunjucks template. See [Conditional execution](https://appfire.atlassian.net/wiki/display/JMWEC/Conditional+execution) for more information.

  - **Condition**: *This option only displays when* ***Run this post-function only if a condition is verified****, above, is checked.* Enter the Nunjucks template as needed.

## Delayed execution

Post functions are provided with an option to delay execution for a set number of seconds using the **Delayed execution** option (Figure 1, right). To delay execution, select the number of seconds to wait until the post-function is run; any value between 1 second (the default) up to a maximum of 20 seconds can be selected.

Workflows that depend on post functions being executed in a specific order can fail due to the asynchronous nature of Connect post-functions in **Jira Cloud**. One workaround is to delay the execution of a post-function, thereby creating a more predictable execution order. For example, on the approval of a Story you want to create sub-tasks and immediately transition them; in this case, you will have to delay the execution of the Transition Linked Issues post-function, so that the sub-tasks are created before they are transitioned. See the sample use case, below.

Where possible, it is recommended to use the [Sequence of post-functions](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/449413536) post-function or [Shared action](https://appfire.atlassian.net/wiki/spaces/MWECS/pages/448398940) post-function to execute a series of post-functions in a specific sequence instead of applying a delay.