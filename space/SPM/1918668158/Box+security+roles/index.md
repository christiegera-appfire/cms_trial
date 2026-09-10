# Box security roles

## Box security roles

Operations available to a user depend on their security roles.

| **Security role** | **Description** |
| --- | --- |
| - Box Admin | Users or groups with this role have all the permissions granted except for accessing the [App Administration](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918829342) page.  Sub-boxes inherit the Box Admin role.  A Box Admin can:   - administer the Box (access the [box configuration](/cms_trial/space/SPM/1918666176/Box+configuration/) section) - create sub-boxes (child boxes) - create a sub-box using a box type with the **Inherited only** mode - [edit a box](/cms_trial/space/SPM/1918635162/Edit+box+details+(name%2C+start%2Fend+dates)/) (name and start and end date) - [delete a box](/cms_trial/space/SPM/1918635005/Delete+box/) - [archive a box](/cms_trial/space/SPM/1918634657/Archive+box/) - [change a box status](/cms_trial/space/SPM/1918829911/Box+lifecycle/) (not started, in progress, closed) - [duplicate a box](/cms_trial/space/SPM/1918635048/Duplicate+box+and+box+scope/) configuration and use it to create a new box - determine who can create, edit, and delete [baselines](/cms_trial/space/SPM/1918404564/Baselines/) (other users can still view baselines);    - Box Admin and Box Editors (default)   - Box Admins  Baselines security settings on the box configuration page.  - [re-synchronize](/cms_trial/space/SPM/1918404058/Data+synchronization+with+connected+tools/) the box - edit the box content (as described in the Box editor role), and change the box configuration settings. |
| Box Editor | Sub-boxes inherit the Box Editor role.  A Box Editor can:   - [edit the box](/cms_trial/space/SPM/1918635162/Edit+box+details+(name%2C+start%2Fend+dates)/) (name and start and end date) - add, edit, and delete objectives - add, edit, and delete tasks - add, edit, and delete dependencies - switch between the column views - switch between the risk card views - manually change the [task structure](/cms_trial/space/SPM/1918667217/Manage+task+structure/) - [duplicate box](/cms_trial/space/SPM/1918635048/Duplicate+box+and+box+scope/) configuration and use it to create a new box - change the scheduling mode of tasks (including Locked tasks - modify current column view (they can make temporary changes to what they see on the screen, but they cannot save the new setup and make permanent changes to existing column view configurations) |
| Box Viewer | This role is inherited when you create sub-boxes. Users or groups with this role will not have access to the box configuration. They can view the box content in a read-only way and use the [export](https://appfire.atlassian.net/wiki/spaces/BTc) functionality. |
| Sub-box Creator | The Sub-box Creator role is not inherited. Sub-Box Creator can create Project boxes as sub-boxes under a Portfolio box.  Sub-box Creators cannot create a sub-box they cannot delete later.  If you grant users a Sub-box Creator role on the Home (root) box level, they will be able to create their own Project boxes but will not be permitted to access or edit other boxes nested under the Home box.  [Unmapped block: nestedExpand] |
| Resource Admin | The Resource Admin role is effectively an extended App User role, which means that such a user:   - has basic access to the app (can access their user profile and see the App dropdown in the header) - can access boxes based on individual box security settings - does not receive access to all Boxes automatically like App Admin - additionally is allowed to administer resource-related global configuration (**Administration** > **Resources** page with all subpages, no access to box types, security) - cannot access app configuration unless the user is host platform Admin simultaneously. |

### Risk Management

|  | **Box Admin** | **Box Editor** | **Box Viewer** |
| --- | --- | --- | --- |
| View risks within existing registers | ✅ | ✅ | ✅ |
| View reports | ✅ | ✅ | ✅ |
| Create risks | ✅ | ✅ | ❌ |
| Assess risks | ✅ | ✅ | ❌ |
| Create new risk register | ✅ | ✅ | ❌ |
| Edit calculations/ add new calculations | ✅ | ✅ | ❌ |
| Manage General settings | ✅ | ✅ | ❌ |
| Archive/ unarchive RRs | ✅ | ✅ | ❌ |
| Delete RRs | ✅ | ❌ | ❌ |

## Permissions

In addition to the Jira permissions and security settings, which the app always respects, you can grant security roles to individual users or to Jira user groups.

Creating groups requires Jira admin permissions.

The roles can be defined for each Box separately or inherited automatically when you create sub-level Boxes.

## Security and access

The Box security settings can be configured only when the 'Default Roles' option is selected in the App's configuration. Otherwise, all users will be granted the highest level permissions.

To change the assigned security roles of a given Box, go to **Box Configuration** > **Security**.

**Important:** Only a user with a minimum Box admin security role can access and manage the Box configuration.

This configuration page will not be visible if the inheritance mode is set to "Inherited only" in the **App's administration** > **Box types** > **Security**.

The Inheritance mode depends on the box type. When creating a new Box, you must select a type—security settings, including the Inheritance mode and the role template, are copied.

![Screen showing the Box types in the Overview module in the BigPicture](/cms_trial/assets/31f22b69-3588-45e7-8587-30b3a84d9146.png)![Screenshot showing security permissions available in BigPicture](/cms_trial/assets/1e641ab4-da9c-4a59-baba-2b09cccc0bed.png)

## Inheritance of roles

Security roles are always [inherited](/cms_trial/space/SPM/1918700886/Inheritance+mode/) from the upper-level boxes, starting from the Home (root) box. When you create a new box, it will inherit the security roles so that you do not need to assign them from scratch.

When you create sub-boxes, the following roles are inherited:

- Box Admin
- Box Editor
- Box Viewer

The Sub-Box Creator role is not inherited, as it would allow users to create sub-boxes they could not delete.

User roles inherited from upper-level boxes are not listed in **Box Configuration** > **Security**. They can be viewed only at the upper level.

## Default box type roles

When you create a new Box, security roles are copied from a Box-type role template. In the settings of each Box type, you can assign roles to users. Then, when you create a new Box, those user roles are copied. Users added based on the template are visible in the **Box Configuration** > **Security section**.

You can assign default roles in the box type configuration to save time when assigning the security roles.

## Restricting access

App and Jira administrators have access to all existing boxes. Users who have no access to a particular box or are not assigned to any security role will not see the box in the Overview module and the [box switcher](/cms_trial/space/SPM/1918667414/Navigate+between+boxes+(box+switcher)/) unless a user has access to a sub-box (but not to the upper-level box). The upper-level box will be displayed as a greyed-out row (without links) to show the box structure properly:

![image2022-10-4_15-8-19.png](/cms_trial/assets/a26b73a6-448d-41f7-97b8-8b112402d169.png)

## Security roles

Roles can be assigned to individual users or entire Jira user groups.

The "Access Status" column can display two statuses:

- **Granted** - informs that a role has been assigned to a user successfully.
- **No access** - informs that a role has been assigned to a user, but global App permissions are missing. The user doesn't have general access to the App. To grant global permissions to the user, go to **Administration** > **Security** and add the user to AppAdmin or AppUser global permissions.

"Access Status" is shown for added users, not for groups.

![contentId-1918668158](/cms_trial/assets/1fd56d8c-a245-4d0b-8243-b657187f21d8.png)![contentId-1918668158](/cms_trial/assets/dc3370cf-489d-4a46-9d1f-f289ce4973d4.png)![contentId-1918668158](/cms_trial/assets/96e72447-6d20-4bc2-864c-48907b0d3446.png)