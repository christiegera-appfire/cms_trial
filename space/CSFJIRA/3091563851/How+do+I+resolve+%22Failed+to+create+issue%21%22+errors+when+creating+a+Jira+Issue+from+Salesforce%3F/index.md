# How do I resolve "Failed to create issue!" errors when creating a Jira Issue from Salesforce?

## Symptoms

- Salesforce throws the error message "Failed to create an issue!" upon creating a Jira issue from the Salesforce Visualforce pages.
- The Connector is configured with [Changing the Reporter and Assignee of an Issue](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754222/Changing+the+Reporter+and+Assignee+of+an+Issue).

## Cause

The app user does not have sufficient privileges to modify reporter in the Jira project. This problem might be caused by a known bug reported at <https://ecosystem.atlassian.net/browse/AC-1876> .

## Resolution

Ensure either the user *Salesforce & Jira Cloud Connector* OR project role "*atlassian-addons-project-access"* has the "**Modify Reporter**" Project permission.