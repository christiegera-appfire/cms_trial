# "Failed in running JQL search query" error in Bulk Operations page

## Summary

When performing a JQL search query in the Bulk Operations tab of Salesforce, the error **"**Failure in running JQL search query**"** appears.

![contentId-3092055528](/cms_trial/assets/4f5ca6cf-23a1-4c81-8f58-4d53b7148717.png)

## Environment

- JIRA Cloud

## Diagnostics Steps

Run a check if the project still exists in your Jira Cloud site with the following methods:

- - Go to **Projects**> **View all projects**.
  - Using the project ID from the bulk operation search into this URL:

    ```text
    https://your-domain.atlassian.net/secure/project/EditProject!default.jspa?pid=<projectID>
    ```
  - Using the Atlassian API (if you are using a [team-managed project](https://support.atlassian.com/jira-software-cloud/docs/is-my-project-team-managed-or-company-managed/)):

    ```text
    https://your-domain.atlassian.net/rest/api/3/project
    ```

    inlineExtension

## Cause

The project is archived or moved to the trash but the [bindings](https://apps-docs.servicerocket.com/salesforce-jira/binding-a-project-to-a-connection) still exist. The Bindings page will show that the project is orphaned and unknown.

![contentId-3092055528](/cms_trial/assets/46b1a1cb-fe73-4ebb-b2b3-519f8911cf74.png)

## Workaround

Not applicable.

## Resolution

1. Go to the **gear Icon** > **Projects**. URL Example: (<https://domain-name.atlassian.net/jira/settings/projects/manage>)
2. Click the **Trash**or **Archive** tab to search for the project.
3. Proceed to unarchive the project or restore the project from the trash.

For more information on project archive and project trash features, look at the following documentation:

- [Moving a project to trash](https://support.atlassian.com/jira-cloud-administration/docs/move-a-project-to-trash/)
- [Archiving a project](https://support.atlassian.com/jira-cloud-administration/docs/archive-a-project/)