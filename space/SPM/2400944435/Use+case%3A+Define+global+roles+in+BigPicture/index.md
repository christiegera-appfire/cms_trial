# Use case: Define global roles in BigPicture

|  |  |
| --- | --- |
| **Goal** | How do I define global roles for a user group in BigPicture? |
| **Scenario** | A BigPicture admin has twenty members in a Jira group. All twenty members should be configured the same, using a global role that grants them read-only access. |
| **Key benefits** | Define read-only access once and apply the role to every BigPicture box, for every user in the group. |

## Preconditions

Required configuration

- There are twenty members in the Jira-users group.
- All 20 members should be granted read-only access to BigPicture boxes. They can view data but should not be able to make changes.
- app admin
- jira admin

## Define global roles step-by-step

Global roles are assigned to the Home box in BigPicture. Once a user or group is assigned a role in the Home box, every sub-box inherits the permissions. The following steps illustrate this example.

1. Open the Home box in the *Overview* module.
2. From the Module Switcher, select **Configuration**.
3. In the left-hand pane, click **Security** > **Security**.
4. Expand the **box Viewer** role tree.
5. Expand **Groups**.

   ![Expand the Box Viewer role tree and groups.](/cms_trial/assets/fe6c5be4-33a5-4520-94b1-9f7a0181efb1.png)
6. Begin typing the name of the group, **Jira-users**. Enter a checkmark next to the group name.

   ![After locating the group in the dropdown, enter a checkmark to assign the role.](/cms_trial/assets/c9a9b7e2-a281-4564-be59-914ef3fd7597.png)
7. All members of the Jira-users group now have **box Viewer** access in the Home box. By assigning the role at the Home box, members of the group automatically have viewer access to *all* boxes created in BigPicture.

## Expected outcomes

After assigning the Jira-users group to the box Viewer role, members can view tasks in BigPicture boxes but can’t make any changes.

For example, when a member of the Jira-users group attempts to move a task in the Gantt chart, the following message displays:

![Box Viewers use BigPicture in read-only mode.](/cms_trial/assets/ccd54954-31bc-431a-bcbf-3396d2dc6e1d.png)

## Learn more

- [BigPicture security and permissions in Jira](/cms_trial/space/SPM/1918667044/BigPicture+security+and+permissions+in+Jira/)
- [Box security roles](/cms_trial/space/SPM/1918668158/Box+security+roles/)
- [Concept of a box](/cms_trial/space/SPM/1918404963/Concept+of+a+box/)
- [Box hierarchy](/cms_trial/space/SPM/1918535907/Box+hierarchy/)
- [Navigate between boxes (box switcher)](/cms_trial/space/SPM/1918667414/Navigate+between+boxes+(box+switcher)/)
- [Inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/)