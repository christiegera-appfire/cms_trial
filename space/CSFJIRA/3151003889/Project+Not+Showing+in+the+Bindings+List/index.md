# Project Not Showing in the Bindings List

## \uD83E\uDD14 Problem

This article addresses an issue where a configured Jira-Salesforce binding does not appear in the Bindings list, yet attempts to recreate it result in an error stating that a binding already exists. This typically occurs due to insufficient project-level permissions.

### Symptoms

1. A binding for a specific Jira project and Salesforce connection is created, but does not appear in the Bindings list.
2. When attempting to recreate the binding, the following error is displayed:

"Error! Validation failed: Project: [Project ID] already bound to a Connection!"

1. The project might be missing from the selection dropdown when creating a *New Binding*.

## \uD83C\uDF31 Solution

Connector for Salesforce & Jira requires the user to have the Administer Project permission for the project to view or manage its associated bindings. Being a Jira Global Administrator, who provides access to the app settings, does not automatically grant these project-specific permissions.

To fix this:

1. Verify if the user can access the **Project Settings** of the Jira project in question.
2. If the user is not a Project Administrator, grant them the **Administer Projects** permission within that project's permission scheme.
3. Refresh the *Bindings* page in the Salesforce Connector. The binding should now be visible.

## \uD83D\uDCCE Related articles