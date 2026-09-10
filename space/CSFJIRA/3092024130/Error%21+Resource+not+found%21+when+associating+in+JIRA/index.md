# Error! Resource not found! when associating in JIRA

## Summary

When associating a Salesforce record in JIRA, the error**"Error! Resource not found!"**appears on the screen.  In addition, users are unable to configure the **Association Configuration.**

![error.png](/cms_trial/assets/78fd0626-f7f1-4ca7-92c7-ac67cf709bc0.png)

## Environment

- JIRA Cloud
- Salesforce JIRA Cloud Connector

## Diagnostics Steps

### Permission

Check whether the edit-issue permission of that project contains the project role **atlassian-addons-project-access**

### Integration user

1. Navigate to ***<base-url>*****/jira/people/557058:3e2ef232-d5c4-4c0e-94b0-977a305ebaae**
2. Click the menu via the 3 dotted lines **(...)** and select **Manage Access**

![contentId-3092024130](/cms_trial/assets/cf56d125-e212-41be-a7ce-1f657c6d8571.png?version=1&modificationDate=1678792051952&cacheVersion=1&api=v2)

1. Click on ***...*** and select **View Jira project Roles**

![contentId-3092024130](/cms_trial/assets/fcd37348-8294-4f9a-b3d8-901a35f18fa7.png?version=1&modificationDate=1678792052035&cacheVersion=1&api=v2)

1. Check whether the Salesforce JIRA Integration user is part of the role **atlassian-addons-project-access** for all projects

## Cause

The installation process of the connector did not complete properly.

## Workaround

Not applicable.

## Resolution

Re-install the connector and make sure that the role **atlassian-addons-project-access** is on every permission.