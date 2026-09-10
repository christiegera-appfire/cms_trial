# Manage permissions on datasources

If you grant use access to a datasource and later revoke it, gadgets already using this datasource will continue to function, but it won’t be available for new configurations. See [Learn about datasources](/cms_trial/space/RDD/146309943/Learn+about+datasources/) for more information.

## Overview

Datasources fetch and display information from external products, which sometimes require extended permissions to access restricted or confidential data. In this case, you can configure permissions and indicate who can use and/or edit your datasources. You’ll find the following options to set up access restrictions:

- **Anyone can use and edit**
- **Anyone can use, some can edit**
- **Only specific people can use or edit**

You can configure permissions when you create a datasource or by editing it on the *Manage Datasources* page.

![Selecting datasource permissions from the Manage Datasources page.](/cms_trial/assets/158c3c68-dd72-4674-8093-21b8ecafcc4b.png)

## Anyone can use and edit

**Open lock icon**

This setting means that **anyone** in your Jira or Confluence instance can **use** that datasource:

- **Anyone can** **use** the datasource to configure individual gadgets.
- **Anyone can** **edit** the datasource configuration and permissions.

This restriction is recommended to access services and products where anyone can look into the information.

For those cases when you want everyone using a specific datasource, but only specific users, groups and/or projects editing it (for example, global admins), you have to select the next permission level **Anyone can use, some can edit.**

## Anyone can use, some can edit

**Closed lock icon**

This setting means that **anyone** in your Jira or Confluence instance is able to **use** the datasource, but only **some** users/groups/projects **can edit** it:

- **Anyone can** **use** the datasource to configure individual gadgets
- **Some users/groups/projects can** **edit** the datasource configuration and permissions

Selecting this option restricts who can edit the dashboard. However, **anyone** in your Jira or Confluence instance can still use the datasource to configure individual datasources.

If you cannot search for users or groups, remember that you need the **Global permission** **Browse users and groups**. If a user cannot find users, it is likely that they are not part of a group with this permission. See more: <https://confluence.atlassian.com/jirakb/unable-to-browse-for-users-and-groups-120521888.html>

### Assign users, groups, or projects to edit

1. Type a user's name, group, or project into the search bar. You can add as many people, groups, and projects as needed.
2. Since anyone can already use the datasource, the selected users, groups, or projects display a fixed *Can edit*.
3. Select **Add** to add them to the list.
4. Select **Save** to save the changes.

To remove users, groups, or projects, click **Remove** next to their name.

For the most restricted permission, select **Only specific people can use or edit**.

## Only specific people can use or edit

**Red lock icon**

This setting means that **only selected users/groups/projects** in your Jira or Confluence instance are able to **use and/or edit** the datasource:

- **Some users/groups/projects can use** the datasource to configure individual gadgets.
- **Some users/groups/projects can** **edit** the datasource configuration and permissions.

This is the most restrictive setting. Your datasource can be completely private or restricted to a few selected users, groups, and projects.

**Assign users/groups/projects to use and/or edit**

1. Type a user's name, group, or project into the search bar. You can add as many people, groups, and projects as needed.
2. Select the access type: **Can use** or **Can edit**.
3. Select **Add** to add them to the list.
4. Select **Save** to save the changes.

To remove users, groups, or projects, click **Remove** next to their name.

## Restrict datasource sharing

Admins can disable the sharing ability. Navigate to the app **Global Settings** > **Datasource Restrictions** and enable the **Restrict Datasource Sharing** toggle. When enabled, users won’t be able to grant permissions to others, making all datasources private and accessible only by their creators.

![On the Global Settings page, the Restrict Datasource Sharing option is shown.](/cms_trial/assets/c48aae60-2f6a-419b-8ef8-cb907657cf4a.png)

## Important notes

### Groups

If a user is in more than one group and one of those groups has access to use the datasource, then that user will be able to use the datasource.

### Projects

In addition to selecting individual users or groups, you can add **Jira projects** to the datasource’s permission settings. Any user with **“browse” access** to the project will automatically have **use/edit permissions** for the associated datasource.

What are Project roles in Jira? Similar in concept to groups, the main difference is that group membership is global, whereas project role membership is project-specific. See [What are project roles](https://www.atlassian.com/software/jira/guides/permissions/overview#what-are-project-roles) in the Atlassian documentation for more information.

![Selecting a datasource permission for Jira projects.ts](/cms_trial/assets/8473c5a1-f344-44d4-a36d-b93554b17f2a.png)

### Admins

Consider that in the setting, Anyone can use, some can edit, and admins can still edit the content (similar to the [Admin key feature](https://support.atlassian.com/confluence-cloud/docs/bypass-access-restrictions-on-a-page-with-admin-key/) in Confluence’s cloud premium). To avoid this situation, use the **Only specific people can use or edit** setting instead.