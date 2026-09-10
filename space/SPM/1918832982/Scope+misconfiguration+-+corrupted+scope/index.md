# Scope misconfiguration - corrupted scope

## Scope misconfiguration - corrupted scope (old navigation)

Once all the issues have been addressed, clear the log by clicking the "Clear log" button within the "Box warnings" dialog. Even if issues have been addressed, the dialog box won't disappear until the log has been cleared.

## Causes of scope misconfiguration

The error appears when the current [scope definition](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/) of a box can't be implemented because:

- A scope element (Jira project, filter, board) ceased to exist - JQL used to define box scope leads to a deleted item.
- A project included in the box scope has been archived.
- A Scope Owner lacks permission to access at least one of the scope elements.
- A Scope Owner is no longer active (the user account in the connected tool has been disabled).

This error can occur when:

1. Some permissions/settings have been changed in the external tool - the scope used to function properly, but now it is corrupted. For example, the Scope Owner user account has been disabled in Jira.
2. A scope element (Jira project, filter, board) has been deleted. Tasks from a deleted project are no longer displayed in modules. When you go to the scope definition, the problem will be indicated in red.

   ![contentId-1918832982](/cms_trial/assets/6e4faba9-9b3b-4cb7-a524-014261d9b9ab.png)
3. You are trying to define the scope of a box. If there are any problems, after clicking "Save," you will immediately see the message informing you that the scope has not been properly configured.

   ![contentId-1918832982](/cms_trial/assets/ed9ecaeb-89ce-42d6-841c-feeb820e036a.png)
4. The user adds to a Box a new task (Jira issue) that the Scope Owner can't access (keep in mind, when you create a new task, for example, directly in Gantt, you always have to make sure the item will be created in the correct Jira project).

   ![contentId-1918832982](/cms_trial/assets/6967412f-3acb-4dcc-88d1-8b3f63c46ec3.png)![contentId-1918832982](/cms_trial/assets/883afd69-f721-4502-bb24-522f8982a4f2.png)
5. Permissions are missing in team-managed projects. There is no access to Jira Cloud issues with role-restricted permissions (this option is available for team-managed projects in Jira Clouds).

   ![contentId-1918832982](/cms_trial/assets/29bb3e85-536a-4169-aff9-586f75243bb1.png)![contentId-1918832982](/cms_trial/assets/0317f1fa-a69b-429b-a8e8-9d2af68ed249.png)

   If you decide to restrict an issue for specific roles, BigPicture will not be able to access such issues, and you will see them as "No access" items in the app.

   ![contentId-1918832982](/cms_trial/assets/a0d9bd4a-861f-48e1-a5d8-19e600ad89e2.png)

   This situation happens because it is impossible to add an add-on to any project role (including BigPicture). We encourage you to [vote for the issue](https://jira.atlassian.com/browse/JRACLOUD-79918) we reported to Atlassian describing this inconvenience.

   ![contentId-1918832982](/cms_trial/assets/718fa51f-2f80-4e6e-addb-e671a23e63f2.png)
6. There are missing permissions on the issue security level (company-managed projects in Jira Cloud).   
   The warnings appear when trying to move tasks on the Gantt module (BigPicture is trying to change the "Start date" and "End date" fields).

   ![contentId-1918832982](/cms_trial/assets/de6f6e94-1728-46f3-85ba-b0b857f10e3f.png)

   You can have trouble accessing specific issues in BigPicture as you will see "No access" items in scope.

   ![contentId-1918832982](/cms_trial/assets/d97d1711-d247-4295-ad85-b887d5ad88a8.png)

   This situation can occur because single tasks might have a security level set. If the lock icon is red, the settings are active.

   ![contentId-1918832982](/cms_trial/assets/d70b1a39-75c0-4f6a-9abd-91073ac9308b.png)![contentId-1918832982](/cms_trial/assets/b2bc1499-c30e-470e-a3f0-da6791ae5a67.png)

   It is recommended to make sure that proper permissions for add-ons are granted to a particular Issue Security Level: The "**atlassian-addons-project-access**" Project Role has to be added to the Security Level you are using.

   ![contentId-1918832982](/cms_trial/assets/7857bb39-20b6-4a54-b8b0-602b2d55fe64.png)

## Automatic rules check

You can't access [box configuration](/cms_trial/space/SPM/1918666176/Box+configuration/) if a box is in 'Closed' [status](/cms_trial/space/SPM/1918829911/Box+lifecycle/).

Every box has a scope—it contains a collection of tasks from connected tools such as Jira and Trello. The box scope can be found in the box configuration under **Tasks** > **Scope definition**. To fix the problem, go to the box's scope definition and verify the automatic rules. Make sure that no invalid JQL has been used and that all added boards, filters, and projects still exist.

You can click the "scope settings" button to go directly to the scope definition.

![contentId-1918832982](/cms_trial/assets/5ee4e856-3499-401a-aec4-2d57be25eb42.png)

When you go to the scope definition, the problem will be indicated in red.

![contentId-1918832982](/cms_trial/assets/30ac271b-30ff-417c-a9f2-b285682bd97f.png)

If the incorrect box scope does not allow you to load the box/Program, you can access the box configuration from the Overview by clicking on the '…' on the right side.

## Scope Owner check

A box can only contain items the Scope Owner can access (viewing access is sufficient). If you try to add items the Scope Owner doesn't have access to, you won't be able to successfully save the scope.

![contentId-1918832982](/cms_trial/assets/52f5d061-23a5-4271-ae5e-07c7680a5d87.png)

A Scope Owner doesn't have to be an actual user added to the box in any capacity(doesn't have to be a Box Admin, Editor, or Viewer).

Permissions of the Scope Owner user account (within the external tool) are the basis for the sync of tasks. Tasks will be pulled into the scope of a box only if the Scope Owner can access them (at least as a viewer).

For example, Angela is the Scope Owner in the BigPicture demo (Jira server instance name) and selected the PI Planning project as the scope of the "PI Planning (Smart house project)" box. If there are tasks that Angela is not allowed to view in that project, those tasks can't be added to the scope of the box.

When connecting with Trello, you need to specify the Scope Owner for each connection. Once a connection is established, you cannot change the Scope Owner.

If you set up a Jira user account called "BigPicture" and this user has at least viewing access to all projects, you can easily always list them as the Scope Owner.

Keep in mind that there is no possibility of a person accidentally accessing or editing items they shouldn't (based on their Jira permissions).

A user can't use the App to see anything they can't already see in the connected tool (such as Jira) - those items will be [greyed out](/cms_trial/space/SPM/1918829579/Permissions/).

Suppose Jira permissions don't allow a user to see or edit an issue. In that case, they won't be able to do it using the app, as BigPicture and BigGantt allow users to perform only the actions they can perform in the connected tool. If a user has access only to half the issues in a box/Program, the other half will be marked as "No access".

## Scope misconfiguration - corrupted scope (new navigation)

Once all the issues have been addressed, clear the log by clicking the "Clear log" button within the "Box warnings" dialog. Even if issues have been addressed, the dialog box won't disappear until the log has been cleared.

## Causes of scope misconfiguration

The error appears when the current [work items from Jira](/cms_trial/space/SPM/1918634319/Populate+a+box+with+tasks+(work+items+from+Jira)/) of a box can't be implemented because:

- A chosen element (Jira project, filter, board) ceased to exist - JQL used to define box scope leads to a deleted item.
- A project included in the box scope has been archived.
- A Scope Owner lacks permission to access at least one of the scope elements.
- A Scope Owner is no longer active (the user account in the connected tool has been disabled).

This error can occur when:

1. Some permissions/settings have been changed in the external tool - the scope used to function properly, but now it is corrupted. For example, the Scope Owner user account has been disabled in Jira.
2. A scope element (Jira project, filter, board) has been deleted. Tasks from a deleted project are no longer displayed in modules. When you go to the scope definition, the problem will be indicated in red.
3. You are trying to define the scope of a box. If there are any problems, after clicking "Save," you will immediately see the message informing you that the scope has not been properly configured.
4. The user adds to a Box a new task (Jira issue) that the Scope Owner can't access (keep in mind, when you create a new task, for example, directly in Gantt, you always have to make sure the item will be created in the correct Jira project).
5. Permissions are missing in team-managed projects. There is no access to Jira Cloud issues with role-restricted permissions (this option is available for team-managed projects in Jira Clouds).

   ![contentId-1918832982](/cms_trial/assets/29bb3e85-536a-4169-aff9-586f75243bb1.png)![contentId-1918832982](/cms_trial/assets/0317f1fa-a69b-429b-a8e8-9d2af68ed249.png)

   If you decide to restrict an issue for specific roles, BigPicture will not be able to access such issues, and you will see them as "No access" items in the app.

   ![contentId-1918832982](/cms_trial/assets/a0d9bd4a-861f-48e1-a5d8-19e600ad89e2.png)

   This situation happens because it is impossible to add an add-on to any project role (including BigPicture). We encourage you to [vote for the issue](https://jira.atlassian.com/browse/JRACLOUD-79918) we reported to Atlassian describing this inconvenience.

   ![contentId-1918832982](/cms_trial/assets/718fa51f-2f80-4e6e-addb-e671a23e63f2.png)
6. There are missing permissions on the issue security level (company-managed projects in Jira Cloud).   
   The warnings appear when trying to move tasks on the Gantt module (BigPicture is trying to change the "Start date" and "End date" fields).

   ![contentId-1918832982](/cms_trial/assets/de6f6e94-1728-46f3-85ba-b0b857f10e3f.png)

   You can have trouble accessing specific issues in BigPicture as you will see "No access" items in scope.

   ![contentId-1918832982](/cms_trial/assets/d97d1711-d247-4295-ad85-b887d5ad88a8.png)

   This situation can occur because single tasks might have a security level set. If the lock icon is red, the settings are active.

   ![contentId-1918832982](/cms_trial/assets/d70b1a39-75c0-4f6a-9abd-91073ac9308b.png)![contentId-1918832982](/cms_trial/assets/b2bc1499-c30e-470e-a3f0-da6791ae5a67.png)

   It is recommended to make sure that proper permissions for add-ons are granted to a particular Issue Security Level: The "**atlassian-addons-project-access**" Project Role has to be added to the Security Level you are using.

   ![contentId-1918832982](/cms_trial/assets/7857bb39-20b6-4a54-b8b0-602b2d55fe64.png)

## Automatic rules check

You can't access [box configuration](/cms_trial/space/SPM/1918666176/Box+configuration/) if a box is in 'Closed' [status](/cms_trial/space/SPM/1918829911/Box+lifecycle/).

Every box has a scope—it contains a collection of tasks from connected tools such as Jira and Trello. The box scope can be found in the box configuration under **Tasks** > **Work items from Jira**. To fix the problem, go to the box's scope definition and verify the automatic rules. Make sure that no invalid JQL has been used and that all added boards, filters, and projects still exist.

You can click the "scope settings" button to go directly to the Work items from Jira.

![contentId-1918832982](/cms_trial/assets/5ee4e856-3499-401a-aec4-2d57be25eb42.png)

When you go to the scope definition, the problem will be indicated in red.

If the incorrect box scope does not allow you to load the box/Program, you can access the box configuration from the Overview by clicking on the '…' on the right side.

## Scope Owner check

A box can only contain items the Scope Owner can access (viewing access is sufficient). If you try to add items the Scope Owner doesn't have access to, you won't be able to successfully save the scope.

A Scope Owner doesn't have to be an actual user added to the box in any capacity(doesn't have to be a Box Admin, Editor, or Viewer).

Permissions of the Scope Owner user account (within the external tool) are the basis for the sync of tasks. Tasks will be pulled into the scope of a box only if the Scope Owner can access them (at least as a viewer).

For example, Angela is the Scope Owner in the BigPicture demo (Jira server instance name) and selected the PI Planning project as the scope of the "PI Planning (Smart house project)" box. If there are tasks that Angela is not allowed to view in that project, those tasks can't be added to the scope of the box.

When connecting with Trello, you need to specify the Scope Owner for each connection. Once a connection is established, you cannot change the Scope Owner.

If you set up a Jira user account called "BigPicture" and this user has at least viewing access to all projects, you can easily always list them as the Scope Owner.

Keep in mind that there is no possibility of a person accidentally accessing or editing items they shouldn't (based on their Jira permissions).

A user can't use the App to see anything they can't already see in the connected tool (such as Jira) - those items will be [greyed out](/cms_trial/space/SPM/1918829579/Permissions/).

Suppose Jira permissions don't allow a user to see or edit an issue. In that case, they won't be able to do it using the app, as BigPicture and BigGantt allow users to perform only the actions they can perform in the connected tool. If a user has access only to half the issues in a box/Program, the other half will be marked as "No access".