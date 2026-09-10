# App access rule

## What is the app access rule?

The app access rule is a new Atlassian data security policy rule that allows organizations to limit access to content by third-party apps in Confluence spaces and Jira projects. The app access rule is currently available in the Early Access Programme. See, <https://support.atlassian.com/security-and-access-policies/docs/app-access-rule-coverage-summary/> for more details.

## What happens if the app access rule blocks JQL Search Extensions for Jira?

If JQL Search Extensions is on your list of blocked apps, it won’t be able to access issues in any of the restricted projects. New queries will not return any issues from restricted projects. Saved filters created before the introduction of the app access rule will not sync data from restricted projects.

## How do I know if the app access rule blocks JQL Search Extensions for Jira?

If you have an app access rule for your data security policy, JQL Search Extensions displays a warning banner on the Extended Search page and on your saved Extended Search filters page. The app does not identify which projects are restricted. Check your app access rule to determine if the rule blocks JQL Search Extensions from accessing any projects.

## Manage the app access rule for JQL Search Extensions for Jira

If you want to allow the app to access projects in Jira, you can use an allow list or a block list, depending on how you have defined the default permission for the rule. You can either remove the app from a block list or add it to an allowlist. See, <https://support.atlassian.com/security-and-access-policies/docs/block-app-access/> for detailed instructions.