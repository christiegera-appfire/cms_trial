# BigPicture security and permissions in Jira

Jira global permissions are system-wide and granted to user groups. Site admins or Jira admins define global permissions per instance. If a company has two instances, global permissions are set separately for each instance.

## Global permissions BigPicture needs

Site admins or Jira admins can configure global permissions on the **Jira settings** > **System** > **Global permissions** page.

There are six global permissions available in Jira:

- Administer Jira
- Browse users and groups
- Share dashboards and filters
- Manage group filter subscriptions
- Make bulk changes
- Create team-managed projects

BigPicture needs three global permissions to operate in Jira:

- **Administer Jira**
- **Browse users and groups**
- **Share dashboards and filters**

The table presents global permissions BigPicture needs in Jira and their explanation. Learn more about global permissions in the [Manage global permissions](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/) article.

| **Global permission** | **Explanation** |
| --- | --- |
| Administer Jira | Create and administer projects, issue types, fields, workflows, and schemes for all projects. Users with this permission can perform most administration tasks, except managing users, importing and exporting data, and editing system email settings.  Users with the Administer Jira permission can log in at any time, but their access may be restricted depending on their application access. |
| Browse users and groups | View and select users or groups from the user picker. Users with this permission can see the names of all users and groups on your site, provided they have the Browse Project permission granted. They can also @mention people on issues. |
| Share dashboards and filters | Share dashboards and filters with other users. |

BigPicture has access to three listed global permissions through membership in groups:

- atlassian-addons-admin
- jira-service management-users.
- jira-software-users
- jira-workmanagement-users

If BigPicture is removed from one of the groups (e.g., atlassian-addons-admin), it does **NOT** mean BigPicture loses access to Jira. BigPicture can still access Jira through membership in the remaining groups.

BigPicture has to be removed from all groups to lose access to Jira.

## Security

In BigPicture, you can grant security roles to individual users or Jira user groups. The roles can be defined for each box separately or automatically inherited when creating sub-level boxes.

BigPicture **always respects** Jira permissions and security settings.

## Technical user

When BigPicture cannot indicate the real user responsible for an action, a [technical user](/cms_trial/space/SPM/1918766683/Technical+info/) is used for data synchronization between BigPicture and Jira. That includes background synchronizations or situations requiring higher permissions to maintain data integrity.

For BigPicture to work correctly, the technical user must have full access to all Jira issues handled by BigPicture (in the scope of all boxes).

The technical user is created automatically when BigPicture is hosted on Jira Cloud. It defaults to the anonymous user and **cannot** be changed.

## What BigPicture can affect in Jira

Due to global permissions BigPicture acquires in Jira, BigPicture can create and change Jira issues and their fields, sprints, and versions.

**BigPicture CANNOT make changes to:**

- All Jira settings
- Jira projects (name, key, avatar, permissions, and other configurations)
- Boards configuration
- Filters configuration
- Users