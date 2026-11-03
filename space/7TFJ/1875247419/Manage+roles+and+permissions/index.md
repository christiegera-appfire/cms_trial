# Manage roles and permissions

![TryItButton (2).png](/cms_trial/assets/f87a7b0c-d5fe-4fad-b84e-fc891df548dd.png)

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

   ![Manage Roles dialog with roles displayed.](/cms_trial/assets/1bd8de22-e9b4-431f-8e37-632260e44079.png)

The *Manage Roles* configurations are organized into four tiers each with different permissions within 7pace Timetracker. Hover over the **Help** icon to the right of each role to see the included permissions.

**Note**: Project permissions and visibility are controlled through Jira and still apply within 7pace Timetracker; if a user has no access to a project, they will not be able to log time against issues from that project. Additionally, 7pace Timetracker Admins and Managers will not be able to view or edit other users' worklogs for those projects.

**Approvals use direct and group role assignments only**

Approval features use only the users and Jira groups that you add to a role in **Role Management**. Users who get access only through Jira permissions are not included in approval features. This includes the Team role option *"Include all users with permission to browse projects and edit their own worklogs"*.

These users can still log time, but they:

- are not listed in **Approval Management** when the **Role-based users** filter is on,
- do not receive approval reminder emails, and
- cannot be selected as a manager when time is submitted for approval.

To include a user in approvals, add the user, or a Jira group they belong to, to a role.

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

### Roles in approval workflows

#### Who can be selected as a manager

When users submit their time for approval, the manager list shows only users who have the **Manager** or **Global Approval Manager** role.

- Users who have **only the Admin role** are **not** listed. This includes Jira Site Administrators, who are added to Admin automatically. To let an admin approve submitted time, also add them to the **Manager** or **Global Approval Manager** role.
- **Recent** shows managers from the last five periods who still have a manager role.
- If a manager loses their manager role, existing submissions assigned to them stay valid. Users can still resubmit to them, but they see a warning. New submissions cannot be assigned to them.

#### Who receives approval reminders

Reminder emails go to every user who can track time through a **direct user assignment** or a **Jira group assignment** in Role Management.

- A user no longer needs to have opened 7pace Timetracker to receive reminders.
- 7pace does not check whether the Jira account is active. If a deactivated user is still assigned directly, or is still a member of an assigned group, they can still receive reminders. Remove them from the role or group to stop this.
- Users whose period is already **Submitted** or **Approved** do not receive reminders.
- Users who have access only through Jira permissions do not receive reminders.

If 7pace cannot load up-to-date role information, it skips reminders for that run. This prevents emails from going to the wrong people. Approval and rejection summary emails are still sent.

**Warning**: Permissions add up. If a user has more than one role, either directly or through Jira groups, they get all permissions from all of those roles. For example, a user added as **Individual** who is also in a group assigned to **Manager** has Manager permissions.

| **User role** | **Approval page** | **Approval settings page** | **7pace settings page** | **Lock time** | **Approve/reject submitted time** | **Approve/reject non-submitted time** | **Can choose a manager when submitting** | **Can be selected as a manager** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Admin** | Yes | Yes | Yes | Yes | Yes | Yes | Yes | **No**¹ |
| **Global Approval Manager** | Yes | Yes | No | Yes | Yes | Yes | Yes | Yes |
| **Manager** | Yes | No | No | No | Yes | No | Yes | Yes |
| **Team** | No | No | No | No | No | No | Yes | No |
| **Individual** | No | No | No | No | No | No | Yes | No |

¹ Admins can be selected as a manager only if they also have the Manager or Global Approval Manager role.

*Please confirm the Individual row with product. It is copied from the Team row.*

### Role-specific settings

There are a few role-specific settings that should be noted.

- Jira Site Administrators are automatically added to the **Admin** group. Site admins will always have full permissions in 7pace Timetracker. Site administrators are not listed as managers when time is submitted, unless they are also added to the **Manager** or **Global Approval Manager** role.
- The **Team** role has the option to include all users with permission to browse projects and edit their own worklogs. Turning this option on will give all Jira users access to the Team role; turning it off requires users to be added manually for them to have access to 7pace Timetracker.

  Users who get the Team role only through this option are not included in approval features (reminders, Approval Management role filter). Add them directly or through a Jira group if they should take part in approvals.

### Add or delete a user or group

To add a user or a group to a role:

1. Expand the role by clicking the caret ( ▢ ).
2. To view Jira Groups that have already been added to Groups, or Users who have already been added, expand that section.
3. Click the plus beside **Groups** or **Users**.
4. Search for a Group or User, or select one from the list.
5. To delete an existing user, click the **Delete** ( ▢ )button.

All changes save automatically.

Changes to direct user assignments apply right away. Changes to Jira group membership can take some time to show up in 7pace Timetracker, including in approval reminders and manager lists. To apply group changes faster, click **Refresh cache to ensure permissions are up to date** on the *Manage Roles* page.

![Manager Roles dialog with Refresh cache option highlighted.](/cms_trial/assets/b8dcbfb4-426b-4f8e-a3d2-ac58bc762fb3.png)