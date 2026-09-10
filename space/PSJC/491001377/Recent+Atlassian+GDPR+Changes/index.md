# Recent Atlassian GDPR Changes

## Problem

When scripting with functions such as `getUserByFullName()` or `currentUser()`, the format of the user key returns an unexpected result, such as `JIRAUSER10000`.

## Background

As of Jira 8.2, user keys have been changed to protect user identity to comply with GDPR regulations. For more information, see these Atlassian pages describing the change:

- <https://www.atlassian.com/trust/privacy/gdpr>
- <https://confluence.atlassian.com/jiracore/gdpr-changes-in-jira-975041009.html>

## Converting the user key to username

If you have existing scripts that were written before Jira 8.2, they were most likely written with the assumption that the user key and username are basically the same. Due to the changes Atlassian has implemented, this is no longer the case. To that end, you must modify scripts that have functions that return user keys intended for use as usernames.

To convert the userkey to the username, use the `userKeyToUsername()` function:

```text
userKeyToUsername("userkey goes here")
```

OR

```text
userKeyToUsername(currentUser())
```

For example:

```text
string userName = userKeyToUserName(currentUser());
```

For more information on the userKeyToUsername() function, see this documentation:

[userKeyToUsername](/cms_trial/space/PSJC/434374398/userKeyToUsername/)

For a complete list of data available from the JUser struct, see this reference on predefined structure types:

[Predefined structure types reference](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/)

## Inconsistent user results

All the changes made to the user key and user name have been made by Atlassian. Consider exploring the user tables in your Jira instance such as `app_user` and `cwd_user` to get a better idea of how user keys and usernames are handled on the backend.

```text
string [] result = sql("jiraDB", "SELECT * FROM app_user");
runnerLog(result);
```

You can use a third-party database app to conduct queries such as pgAdmin. To use the `sql()` function as posted above, you must first create a database connection to Jira's database. Refer to the following documentation for more information:

[SQL Datasource configuration](/cms_trial/space/PSJC/490996148/SQL+Datasource+configuration/)

Here is the documentation for the sql function:

[sql](/cms_trial/space/PSJC/434864654/sql/)

The following Atlassian documentation seems to be a good outline of navigating user tables.

<https://developer.atlassian.com/server/jira/platform/database-user-and-group-tables/>

## Additional Help

Need help implementing this script? Talk to me directly to me by clicking on the bot on this page.