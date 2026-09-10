# Dashboard permissions

## Overview

We believe in transparency by default, and what better way of communicating your information than using reporting dashboards. However, there are several reasons to restrict access to certain information to only a specific part of your organization. Dashboard Hub provides anAdvanced Restrictions feature.

Did you know that you can provide access to certain dashboards to customers of your Jira Service Management Customer Portal? Learn how in [Manage access to the Jira Service Management Customer Portal](https://support.appfire.com/space/RDD/146309699/Manage+access+to+the+Jira+Service+Management+Customer+Portal).

Our permission levels are similar to Confluence page restrictions, and we refer to them in the same way:

- "Anyone can view and edit"
- "Anyone can view, some can edit"
- "Only specific people can view or edit"

You can access and change the dashboard restrictions from two places:

- Click the open lock icon [open lock icon] at the top of any dashboard, or
- Open the *Dashboard settings* page from the *More Actions* menu.

Remember to save your settings.

## Anyone can view and edit

[open lock icon] Open lock icon

This setting means that **anyone** in your Jira or Confluence instance can access, view, and edit the dashboard content:

Accessible content does not include datasources. Datasources have their own access restrictions; refer to [Learn about datasources](https://support.appfire.com/space/RDD/146309943/Learn+about+datasources).

![Dashboard Hub Dashboard permissions page example](/cms_trial/assets/fdbfd1a7-e926-4ef9-9604-97ba4d70e662.png)

If you want everyone to have viewing permission but only specific users, groups and/or projects to edit it, then select **Anyone can view, some can edit.**

## Anyone can view, some can edit

[closed lock icon]Close lock icon

This setting means that **anyone** in your Jira or Confluence instance is able to **view** the dashboard content, but only **some** users/groups/projects **can edit** it:

- **Anyone can** **view** the content
- **Some users/groups/projects can** **edit** the content

When you select this option, you are restricting who can edit the dashboard. But still **anyone** in your Jira or Confluence instance will be able to view the dashboard content.

If you cannot search for users/groups, remember that you need the **Global permission** "**Browse users and groups**". If a user is unable to find users, it is likely that they are not part of a group with this permission. See the [Confluence support article](https://confluence.atlassian.com/jirakb/unable-to-browse-for-users-and-groups-120521888.html) for more information.

![Dashboard Hub Dashboard permissions dashboard preview](/cms_trial/assets/e8b2a26e-f940-4e30-b57f-f9ff06ee4d0e.png)

**Assign users/groups/projects to edit**

1. Type a user's name, group,, or project into the search bar. You can add as many people, groups and projects as needed.
2. Since anyone can already view the dashboard, the selected users/groups/projects display a fixed “Can edit”.
3. Select **Add** to add them to the list.
4. Select **Save** to save the changes.

To remove users/groups/projects, click **Remove** next to their name.

If you still want to restrict specific people's access to your dashboard, select **Only specific people can view or edit**.

## Only specific people can view or edit

[red lock icon icon] Red lock icon

This setting means that **only selected users/groups/projects** in your Jira or Confluence instance are able to **view and/or edit** the dashboard content:

- **Some users/groups/projects can view** the content
- **Some users/groups/projects can** **edit** the content

This is the most restrictive setting. Your dashboard can be completely private or restricted to a few selected users/groups/projects.

![Dashboard Hub Dashboard permissions dashboard preview](/cms_trial/assets/21d75012-87e2-47a5-8f39-c0dbf00cdbe6.png)

**Assign users/groups/projects to view and/or edit**

1. Type a user's name/group/project into the search bar. You can add as many people/groups/projects as needed.
2. Select the access type: Can view or Can edit
3. Select **Add** to add them to the list.
4. Select **Save** to save the changes.

To remove users/groups/projects, click **Remove** next to their name.

## Important notes

### Groups

If a user is in more than one group and one of those groups has access to view the dashboard, then that user will be able to see it.

### Projects

In addition to selecting individual users or groups, you can add **Jira projects** to the dashboard’s permission settings. Any user with **“browse” access** to the project will automatically have **view/edit permissions** for the associated dashboard.

What are Project roles in Jira? Similar in concept to groups, with the main difference being that group membership is global, whereas project role membership is project-specific. See [What are Jira Permissions? | Atlassian](https://www.atlassian.com/software/jira/guides/permissions/overview#what-are-project-roles) for more information.

![Dashboard Hub projectbased dashboard permissions diagram](/cms_trial/assets/ef6d6f2a-b985-4c92-8b2f-5b69115e48d7.jpg)

### Admins

Take into account that in the setting “Anyone can view, some can edit”, admins can still edit the content (similar to the [Admin key feature](https://support.atlassian.com/confluence-cloud/docs/bypass-access-restrictions-on-a-page-with-admin-key/) in Confluence’s cloud premium). To avoid this situation, set the setting “Only specific people can view or edit”.

### Public links

If a user is accessing a public link, permissions are not checked. It doesn’t matter if that user is logged in. Learn how public links work in [Share a dashboard with a public link](/cms_trial/space/RDD/146310576/Share+a+dashboard+with+a+public+link/).

## Why are there separate permissions for the Customer Portal?

- **Different Access Models**: Jira users are licensed users with access to Jira projects and dashboards. In contrast, Customer Portal users are external participants with limited access, typically only through the JSM portal. Treating them the same could unintentionally expose sensitive internal data.
- **Improved Control and Security**: By managing permissions separately, you can ensure that Customer Portal users only see dashboards explicitly shared with them, reducing the risk of unauthorized access and ensuring compliance with internal data policies.
- **Tailored Experience**: This separation lets you create dashboards designed specifically for external users, with simplified views and relevant information, without compromising internal reporting needs.
- **Consistent with Jira’s model:** This mirrors how Jira handles permissions, for example accessing requests through the Customer Portal follows a different permission model than accessing the same work items in Jira’s interface.