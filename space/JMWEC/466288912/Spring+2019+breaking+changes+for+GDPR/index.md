# Spring 2019 breaking changes for GDPR

Atlassian is making changes to Jira Cloud to provide users with more control over their profile information - both in response to recent changes to data privacy legislation (i.e. GDPR) and as part of a broader effort to improve customer trust. These efforts include [**major breaking changes**](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) [to the Jira REST API](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/) on top of which all apps, including JMWE for Jira Cloud, are built.

Despite our best efforts to makes the changes transparent to our customers, **they** **will have an impact on your workflows**, and **you will need to make changes to some of the JMWE workflow post-functions you have configured**.

## **Automatically find and fix post-functions affected by Atlassian's GDPR changes**

Our new **GDPR Migration Tool**helps you identify and implement the changes required by Atlassian's GDPR updates. It:

- Offers a one-click migration option that applies *some* of the required changes automatically;
- Lists all the JMWE post-functions in your workflows that require changes;
- Allows you to edit these post-functions directly from the tool.

The GDPR Migration Tool is available from the Apps section of the Jira admin. You can also navigate to it via *<Your base URL>/plugins/servlet/ac/com.innovalog.jmwe.jira-misc-workflow-extensions/gdpr-checker.*

## What is happening

Atlassian is changing the way Jira Users are exposed through its APIs. In particular, they are replacing the *username* and *user key* identifying attributes with a single, opaque *accountId* identifier. They are also hiding, by default, many other user attributes, such as the *email address*, *full name*, *avatar*, etc., although these attributes can be made available again by the organization managing the Jira Cloud instance.  These changes impact user information *received from Jira*, as well as user information *sent to Jira*.

## Impact on your workflows

All the JMWE post-functions you have configured on your workflows *might* be impacted by these changes, if their configuration is referencing users one way or another. Here is a summary of the configuration options that will be impacted:

- Every "Run as this user:" option
- Any Conditional Execution option that refers to the `name` or `key` attribute (field) of a user object (e.g. `issue.fields.assignee`) in its conditional execution template. For example:

```text
{{ issue.fields.assignee.name == "admin" }}
```

- The "This user:" option of the "Author of copied comments" section of the "Copy comments to linked issues" post-function.
- The "Specific users" and "Users from template" options of the Email Issue post-function
- The "JQL expression" option of the Link issues to the current issue post-function, if it includes a user-type field criteria.
- Any Value option of any field set by post-functions such as Set Field Value, Create Issue, Transition Issues, etc., when the field contains *users* (such as the built-in Assignee and Reporter fields, or any Single-user or Multi-user Picker custom field), even if the value is a constant (a *username* string such as `admin`)
- And in general, any Nunjucks Template that either *returns a username* or *accesses the name or key attribute of a user object.*

To find out how to identify the post-functions that are impacted, and how to fix them, refer to the [Identifying required changes and making them](#Spring2019breakingchangesforGDPR-fix) section below.

## Timeline of the changes

The changes described above will be rolled out in multiple phases, in order to minimize the impact on your organization.

#### Phase 1

When: April 21, 2019

What: we are releasing a new version of JMWE for Jira Cloud that is fully compatible with all your existing workflows, but enables you to *identify the post-functions that need changes*, and *make these changes ahead of time*.

#### Phase 2

When: ~~April 29~~ ~~May 16~~ ~~June 2~~**June 11, 2019**

What: Atlassian will deploy the GDPR breaking changes mentioned above. However, they will offer a *compatibility API* that will allow JMWE for Jira Cloud to continue supporting *most* of the existing post-function configurations, even if they still refer to usernames and user keys. The only post-functions that will *stop working* are those that include a Nunjucks template that compares a username to a constant string. For example:

```text
{{ issue.fields.assignee.name == "admin" }}
```

#### Phase 3

When: *to be announced later by Atlassian*, but no earlier than June 30, 2019

What: Atlassian will *remove* the compatibility API introduced in Phase 2. At that point, *all your post-functions* will need to have been updated as described below.

## Identifying required changes and making them

The latest version of JMWE for Jira Cloud introduces a new **GDPR Migration Tool** that lists all the JMWE post-functions in your workflows that require changes and allows you to edit these post-functions directly from the tool. It also offers a one-click migration option that applies *some* of the required changes automatically. The GDPR Migration Tool is available from the Apps section of the Jira administration pages, alongside other JMWE administration pages such as the JMWE Logs.

We recommend you use the GDPR Migration Tool to identify and implement all the changes you need to make to your workflows. However, you can use any other tool, such as Jira's workflow editor and JMWE Logs, to identify and make these changes.

Required changes fall into the following categories, which also correspond to "Deprecation warning messages" logged into the JMWE Logs when post-functions are executed:

## Attempting to access the 'name' field of a user object

This warning will be logged by post-functions that refer to the `name` property (field) of a user object *in a Nunjucks template*. For example:

- Returning the value of a user-type field:

```text
{{ issue.fields.reporter.name }}
```

- Returning the current user:

```text
{{ currentUser.name }}
```

- Checking the assignee against a specific user:

```text
{{ issue.fields.assignee.name == "admin" }}
```

#### How to fix

The reference to the `name` property must be replaced with a reference to the `accountId` property. For example:

- Returning the value of a user-type field:

```text
{{ issue.fields.reporter.accountId }}
```

- Returning the current user:

```text
{{ currentUser.accountId }}
```

Note that fields that expect a reference to a user as their value (fields that used to expect a username or a comma-separated list of usernames, such as the Assignee field or Multi-user picker custom fields) now expect an accountId or a comma-separated list of accountIds, but they will temporarily continue to accept usernames (until phase 3).

- Checking the assignee against a specific user:

```text
{{ issue.fields.assignee.accountId == "accountId:aaaaa-bbbbb-ccccc-ddddd" }}
```

Note that you can use the "User lookup" button of the Nunjucks editor toolbar to look up the account ID of a specific user and insert it in your template.

In some cases, you might want to replace the reference to the `name` property with a reference to the `displayName` property when used inside a Nunjucks template returning *text*, such as in the Text or Html Body options of an Email Issue post-function, to display a readable user name:

```text
This issue was created by {{ issue.fields.reporter.displayName }}.
```

Note that the `currentUser` variable does not have a `displayName` property. Instead, you need to use the `userInfo` Nunjucks filter to get the *display name* of the current user:

```text
This issue was transitioned by {{ currentUser | userInfo("displayName") }}.
```

#### When to fix

These warnings need to be fixed *at the latest* **before**:

- Returning the value of a user-type field, or the current user: **phase 3**
- Comparing the value of a user-type field with a specific user: **phase 2**

## Attempting to access the 'key' field of a user object

This warning will be logged by post-functions that refer to the `key` property (field) of a user object *in a Nunjucks template*. For example:

- Checking the assignee against a specific user:

```text
{{ issue.fields.assignee.key == "admin" }}
```

#### How to fix

The reference to the `key` property must be replaced with a reference to the `accountId` property. For example:

- Checking the assignee against a specific user:

```text
{{ issue.fields.assignee.accountId == "accountId:aaaaa-bbbbb-ccccc-ddddd" }}
```

Note that you can use the "User lookup" button of the Nunjucks editor toolbar to look up the account ID of a specific user and insert it in your template.

#### When to fix

These warnings need to be fixed *at the latest* **before phase 2.**

## This post-function still uses a username as the runAs user

This warning will be logged by post-functions that were configured with the "Run as this user" option before JMWE for Jira Cloud 1.1.11 was released.

#### How to fix

Run the "Automatic Migration" option of the GDPR Migration Tool.

#### When to fix

These warnings need to be fixed *at the latest* **before phase 3.**

## This post-function still uses a username as the 'comment author'

This warning will be logged by the Copy Comments to Linked Issues post-function if it was configured with the "Author of copied comments" option set to "this user" before JMWE for Jira Cloud 1.1.11 was released.

#### How to fix

Run the "Automatic Migration" option of the GDPR Migration Tool.

#### When to fix

These warnings need to be fixed *at the latest* **before phase 3.**

## This post-function still uses a username as the 'comment as' user

This warning will be logged by the Create Issue(s) post-function if it was configured with the "Add a comment to the current issue" option with the "Create comment as this user" sub-option before JMWE for Jira Cloud 1.1.11 was released.

#### How to fix

Run the "Automatic Migration" option of the GDPR Migration Tool.

#### When to fix

These warnings need to be fixed *at the latest* **before phase 3.**

## This post-function still uses user names/keys and must be updated to use accountIds instead

This warning will be logged by any post-function that is somehow manipulating a username or user key. The most common case will be when setting a user-type field to a username, using a value such as:

- a username

```text
admin
```

- a template returning a username:

  ```text
  {{ issue.fields.assignee.name }}
  ```

  or

  ```text
  {% if issue.fields.assignee != null %}
  {{ issue.fields.assignee.name }}
  {% else %}
  admin
  {% endif %}
  ```

Note that this warning can appear together with an "Attempting to access the 'name' field of a user object" warning. Fixing the latter will fix the former.

#### How to fix

The simple cases, such as setting a field to a username constant, will be automatically handled by the Automatic Migration of the GDPR Migration Tool. In most other cases, you will need to update usernames in Nunjucks Templates to accountIds. If you can't figure out why your post-function is logging this warning message, please open a support request on our [Help Desk](https://appfire.atlassian.net/servicedesk/customer/portal/11).

#### When to fix

These warnings need to be fixed *at the latest* **before phase 3.**

### June 16 update

Atlassian pushed back once again the deployment of the first wave of breaking changes ("Phase 2" below) to **early July**. You have therefore up to the end of June to make the changes required for Phase 2 (see below).

### May 31 update

Atlassian pushed back once again the deployment of the first wave of breaking changes ("Phase 2" below) to **June 11**. You have therefore up to June 11 to make the changes required for Phase 2 (see below).

### May 24 update

Atlassian pushed back the deployment of the first wave of breaking changes ("Phase 2" below) to **June 2** at the earliest. You have therefore up to June 2 to make the changes required for Phase 2 (see below).

### May 8th update

We just released a new **GDPR Migration Tool** available from the Apps section of the Jira admin, to help you identify and implement the changes required by Atlassian's upcoming GDPR changes. It lists all the JMWE post-functions in your workflows that require changes, allows you to edit these post-functions directly from the tool, and offers a one-click migration option that applies *some* of the required changes automatically.

### April 26 update

Atlassian just pushed back the deployment of the first wave of breaking changes ("Phase 2" below) to **May 16**. You have therefore up to May 16 to make the changes required for Phase 2 (see below).