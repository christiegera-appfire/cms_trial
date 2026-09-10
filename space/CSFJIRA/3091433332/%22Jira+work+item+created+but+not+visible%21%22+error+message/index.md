# "Jira work item created but not visible!" error message

## Summary

A "Jira work item created but not visible!" message is displayed after a Jira work item is created from Salesforce. Even after the Jira work item is successfully created, it is not displayed in the *Jira Issues* section in Salesforce, and it does not appear in searches either.

![image-20250603-121047.png](/cms_trial/assets/c5092104-4319-4644-a536-3d8e1e440146.png)

## Environment

- Jira Cloud

## Diagnostics Steps

Not applicable.

## Cause

A work item security level has been configured for the Project you are working with, but the connector's role **atlassian-addons-project-access** or the integration user has not been added yet into the security level. Please check this Atlassian documentation to find out more about security levels:

- [https://support.atlassian.com/jira-cloud-administration/docs/configure-issue-security-schemes/](https://support.atlassian.com/jira-cloud-administration/docs/configure-issue-security-schemes/?__hstc=72543820.ab19c70c621fe76686456a1bcc7fc053.1607582925293.1609750265128.1609811073162.68&__hssc=72543820.2.1609811073162&__hsfp=563081268)

## Workaround

Not applicable.

## Resolution

Make sure the connector's role **atlassian-addons-project-access** or the integration user has been added into the security level you have configured.