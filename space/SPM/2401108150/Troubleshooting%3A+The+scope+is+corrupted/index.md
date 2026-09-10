# Troubleshooting: The scope is corrupted

Encountering a `box Scope is corrupted` error in BigPicture or seeing scope configuration issues highlighted in red indicates that the application is unable to properly interpret or implement the defined scope for a specific box. This can lead to tasks not appearing as expected, difficulties saving scope changes, and hinder your ability to manage your projects effectively within that box.

This article provides a comprehensive guide to understanding and resolving the common causes of a corrupted box scope.

## Symptoms

- An explicit `box Scope is corrupted` error message.
- Visual indicators, often in red, within the box configuration's source section.
- Failure to save changes after attempting to modify the box scope.
- Incomplete or incorrect display of tasks within the box modules (for example, Gantt, Scope).
- Seeing `No access items` for tasks that should be included in the scope.

## Causes

The root causes of a corrupted box scope typically stem from inconsistencies or permission problems between BigPicture's configuration and the connected tool (most commonly Jira):

1. Missing or invalid scope elements in the connected tool:

   - Deleted elements: A Jira space, filter, or board used to define the box's scope has been permanently deleted in Jira. BigPicture's configuration still references these non-existent items.
   - Archived Projects: A Jira space included in the box scope has been archived in Jira. While archived projects still exist, they may not be actively accessible or synchronized like active projects, leading to scope issues.
   - Incorrect or Outdated References: The Work items from Jira might contain references to elements that have been renamed or moved without updating the BigPicture configuration.
2. Problems with the Scope Owner's Access and Status:

   - Insufficient permissions: The user designated as the scope owner for the box lacks the necessary permissions (minimum viewing access) in the connected tool to see and access *all* the projects, filters, boards, or individual issues included in the box's defined scope. BigPicture relies on the scope owner's permissions to pull tasks into the box.
   - Inactive user account: The scope owner's user account in the connected tool (for example, Jira) has been deactivated or removed.
   - External permission changes: Recent alterations to the Scope Owner's permissions or to project/issue security settings in the connected tool have inadvertently revoked their access to elements within the box's scope.
3. Issues with JQL queries in automatic rules:

   - Invalid JQL syntax: The JQL (Jira Query Language) used to define the scope using Automatic rules contains errors in its syntax, preventing BigPicture from executing the query correctly.
   - Incorrect JQL functions or references: Using JQL functions that are not supported or incorrectly referencing fields, groups (for example, using `membersOf()` with Jira Teams instead of Groups), or values can lead to scope corruption.
4. Permission restrictions on tasks or projects:

   - Issue security levels: In company-managed Jira spaces, specific issues may have security levels applied that restrict access, even for the scope owner or other users. A red lock icon on a Jira issue often indicates active security settings.
   - Role-restricted permissions: In team-managed Jira Cloud projects, permissions can be restricted to specific roles. Since BigPicture, as an add-on, cannot typically be added to these roles, it may be unable to access tasks with such restrictions, resulting in "No access" items and potential scope inconsistencies.
5. Synchronization discrepancies or cache issues:

   - Occasionally, discrepancies between the connected tool and BigPicture's synchronized data can occur. An outdated cache within BigPicture might hold information of an old scope, leading to perceived corruption.
6. Complexity and scale of the scope (less common direct cause, but can exacerbate issues):

   - While BigPicture is designed to handle large scopes, an excessively complex Work items from Jira with numerous rules or a very high number of tasks (though the system is tested with up to 30,000 tasks), combined with other underlying issues, can potentially contribute to performance or synchronization problems that manifest as scope issues.

## **Solution**

To resolve a corrupted box scope, systematically investigate and correct the potential causes:

1. Access the box configuration: Navigate to the box's configuration, reporting the error. If you cannot access the box directly, go to the Overview module, find the box, click **Options** **menu** (**…**), and select **Configuration**.
2. Go to **Tasks** > **Work items from Jira** in box configuration. This section is where you will identify the specific problematic elements, often highlighted in red.
3. Verify scope elements in the connected tool:

   - Carefully review all listed Jira spaces, filters, and boards in Work items from Jira.
   - Log in to your connected Jira instance and confirm that each element exists and is active.
   - Remove any references to deleted or archived projects, filters, or boards from the BigPicture Work items from Jira.
4. Examine and Correct JQL Queries:

   - If using automatic rules with JQL, inspect the queries for syntax errors. Use Jira's JQL search to test the query and ensure it returns the expected results.
   - Verify that the JQL uses correct field names and function syntax. Be mindful of specific functions like `membersOf()` and ensure they are used with Jira Groups if required.
5. Check and adjust scope owner:

   - Identify the user set as the Scope Owner in the box configuration.
   - In the connected tool (for example, Jira), confirm that this user's account is active.
   - Crucially, verify that the Scope Owner has at least viewing permissions for *all* the projects, filters, boards, and individual issues within the box's defined scope. Adjust their permissions in Jira if necessary. Consider using a dedicated service account with broad viewing permissions as the Scope Owner if your organization's policies allow.
6. Address task and project permission issues:

   - If *No access* items appear, investigate the permissions for those tasks in Jira.
   - For company-managed projects using Issue Security Levels, ensure that the *atlassian-addons-project-access* Project Role is included in the relevant Security Schemes to grant BigPicture access.
   - For team-managed projects with role-restricted permissions, this can limit BigPicture's access. Review whether these restrictions are necessary for the tasks you need in BigPicture.
7. Clear BigPicture cache: Sometimes, clearing the app cache can resolve synchronization issues that might present as scope corruption. Consult your BigPicture or Jira administrator about clearing the BigPicture plugin cache.
8. Save and Clear Log: After making any corrections, click **Save** in the Work items from Jira. If the issues are resolved, the scope should save successfully. Finally, open the *box warnings* dialog and click the **Clear log** button to dismiss the corruption warning message.

By diligently following these steps and ensuring consistency and correct permissions between BigPicture and your connected tool, you can effectively troubleshoot and resolve the `box Scope is corrupte`d error, restoring full functionality to your boxes.