# Manage roles and permissions

![TryItButton (2).png](/cms_trial/assets/9e5c9f0d-576a-4904-b708-ac448f2c0b30.png)

The Role Management settings enable administrators to configure which Jira users have access to 7pace Timetracker tools and what they can do within the tool.

## Watch the video

Review the following video to learn how to manage roles in 7pace Timetracker.

Video transcript

7pace Timetracker includes Role Management settings for determining what a Jira user can do in the app. To access Role Management click Apps > Timetracker. Then, in the left hand pane, click Settings, click Role Management. There are four roles in 7pace: Admin, Manager, Team, and Individual. Hover over the help icon to the right of each role to see its permissions. Click the role name to expand it and view the Jira groups and users assigned to that role. Click each tile to expand it. To add a user or group, click the + button to the right. Search for a user or group, or select one from the pull-down menu. To remove a user or a group, click the Delete button. Changes to role membership are saved automatically. In summary, 7pace Timetracker's Role Management tool can be used to control what Jira users can do within the app. Thanks for watching.

## Manage roles

The **Role Management** settings enable you to configure which Jira users have specific permissions within 7pace Timetracker. Until a user has been added to 7pace, they will not be able to add time to issues.

To access the Role Management tool:

1. Go to **Apps** > **7pace Timetracker**.
2. Click **Settings** in the left-hand column.
3. Click **Role Management**. The *Manage Roles* window opens (pictured, below).

   ![Manage Roles dialog with roles displayed.](/cms_trial/assets/40b3a139-7613-440e-92d4-c216cd62b9e9.png)

The *Manage Roles* configurations are organized into four tiers each with different permissions within 7pace Timetracker. Hover over the **Help** icon to the right of each role to see the included permissions.

**Note**: Project permissions and visibility are controlled through Jira and still apply within 7pace Timetracker; if a user has no access to a project, they will not be able to log time against issues from that project. Additionally, 7pace Timetracker Admins and Managers will not be able to view or edit other users' worklogs for those projects.

The roles and their permissions (summarized) are:

- **Admin** - All permissions granted, including the ability to change app settings, manage role membership, and manage and lock time periods. See **Role-specific settings** below.
- **Global Approval Manager** – Full approval and locking permissions across all users and periods, without access to core 7pace app settings. Global Approval Managers can approve or reject any user’s worklogs (including non‑submitted time), lock and unlock approval periods, and override local manager decisions when needed.
- **Manager** - Time entry permission, including the ability to see other users’ logged time and modify (add, edit, or delete) time on behalf of other users.
- **Team** - Time entry permission and the ability to see logged time by other users.
- **Individual** - Time entry permission only. Individuals can see only their own worklogs.

### Manager vs. Global Approval Manager

- **Managers** approve time of their team (lock the period for the given users). They can only approve time of team members who submitted the time entry.
- **Global managers** lock whole periods (globally locking time for the whole company)

#### Best practice

A common misconception is that anyone responsible for approving time should be a Global Manager. This is not the intended setup**.**

To maintain a healthy 7pace environment, follow these guiding principles:

- **Empower Team Leads:** Assign the **Manager** role to those who need to oversee the day-to-day work of their direct reports. This ensures that time is validated by the people closest to the work.
- **Restrict Global Access:** The **Global Approval Manager** role should be reserved for a small handful of individuals (e.g., Payroll Administrators or HR Directors).
- **The Workflow Goal:** Use Managers to lock team progress throughout the month, and reserve Global Managers for the final lock that closes the books for the entire company.

<https://youtu.be/7KGTUogKqN4>

**Warning**: Permissions use AND logic in 7pace Timetracker. If a Jira user is added as an individual AND as a member of a group that has also been added to 7pace, they will have all of the permissions of the most permissive level.

|  |  |  |
| --- | --- | --- |
| **User Role** | **Settings pages** | **App functions** |
| **Approval page** | **Approval settings page** | **7pace settings page** | **Lock time** | **Approve / Reject submitted time** | **Approve / Reject NON submitted time** | **Manager selection** |
| **Admin** | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **Global Approval Manager** | Yes | Yes | No | Yes | Yes | Yes | Yes |
| **Manager** | Yes | No | No | No | Yes | No | Yes |
| **Team (Individual)** | No | No | No | No | No | No | Yes |

### Role-specific settings

There are a few role-specific settings that should be noted.

- Jira Site Administrators are automatically added to the **Admin** group. Site admins will always have full permissions in 7pace Timetracker.
- The **Team** role has the option to include all users with permission to browse projects and edit their own workloads. Turning this option on will give all Jira users access to the Team role; turning it off requires users to be added manually for them to have access to 7pace Timetracker.

### Add or delete a user or group

To add a user or a group to a role:

1. Expand the role by clicking the caret ( ▢ ).
2. To view Jira Groups that have already been added to Groups, or Users who have already been added, expand that section.
3. Click the plus beside **Groups** or **Users**.
4. Search for a Group or User, or select one from the list.
5. To delete an existing user, click the **Delete** ( ▢ )button.

All changes save automatically.

Typically, it takes 7pace Timetracker approximately one hour to process new users added to a group. To expedite this process, click **Refresh cache to ensure permissions are up to date** in the *Manage Roles* page.

![Manager Roles dialog with Refresh cache option highlighted.](/cms_trial/assets/f234147b-e23f-488a-9787-a85628412096.png)