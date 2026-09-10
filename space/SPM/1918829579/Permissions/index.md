# Permissions

To fully benefit from the available security options, you need to combine multiple settings in Jira and BigPicture.

This article provides only an overview of the security roles in BigPicture. To learn more about a particular role, follow the link to the dedicated page.

BigPicture respects Jira permission settings. This means:

- If a user is not permitted to view or edit an issue, they will not be able to do so in BigPicture.
- If a user is permitted to view only a set of specific issues in a selected box, they will not be allowed to view the remaining ones.

This ensures that no user can accidentally access or edit items in BigPicture for which they do not have permission in Jira.

Jira Admins always have full, unrestricted access to all boxes and the app.

## Available user security roles

### Global roles (app-level roles)

Global roles ([app-level roles](/cms_trial/space/SPM/1918535770/App-level+permissions/)) define access to the app and the respective pages of the *App Administration*.

There are two global roles:

- App User. App Users can see and open the BigPicture app under Jira’s **Apps**.
- App Admin. App Admins, like Jira Admins, have unrestricted access to every box and app setting in BigPicture.
- Resource Admins. Resource Admins have access to all resource-related pages on the App Administration page and can carry out all available operations on those pages.

### Box-level roles

Box-level roles determine which boxes users can access and what actions they are permitted to perform in each box.

There are four box-level roles:

- Box Viewer. Box Viewers can open but cannot manage a box.
- Box Editor. Box Editors can edit box settings and, to some extent, box contents.
- Box Admin. Box Admins can fully manage box settings and its contents.
- Sub-box Creator. Sub-box Creators can create child boxes but cannot access the parent box.

### Module-level roles

The Financials, OKR, and Priorities modules have extra security settings that limit what users can do within each module. Visit the individual [module permission](/cms_trial/space/SPM/1918536362/Module-specific+permissions/) pages for more details.

## Access to the app

App-level and box-level roles go together.

The App User global role grants permission to open BigPicture, but it does not permit users to view, edit, or manage individual boxes, even if they have relevant permissions granted in Jira.

Non-App Users will see that their access to the app is denied.

![App users can open BigPicture but they will have no access to it if they have no box-level role assigned.](/cms_trial/assets/36013d55-9d73-4886-9798-8ab30167d9d9.png)

It also works the other way round. If the user is permitted to view, edit, and manage any box but was not granted the App User role, they will have insufficient permissions to access the app. As a result, they will not see BigPicture under Jira’s Apps and will not be able to see and open the boxes.

![Insufficient permissions in BigPicture.](/cms_trial/assets/f6eb853e-d208-47db-ab24-a2547e38c809.png)

When the App or Box Admin assigns a box-level role to a Jira user who is not an App User, they will see a warning message informing them that such a user was not granted access to the app.

![A warning message informing about the insufficient global permissions.](/cms_trial/assets/7029a9c5-0a96-4341-9679-410ae3728967.png)

## Access to boxes

### Inheritance of the security roles

[Security roles are inherited](/cms_trial/space/SPM/1918700886/Inheritance+mode/) from parents to children, never the other way round. The box role can be acquired in two ways, depending on the [box type](/cms_trial/space/SPM/1918830000/Box+types/) settings:

- Own with inherited (roles can be inherited and also assigned manually)
- Inherited only (roles can only be inherited; manual assignment is unavailable)

In the screenshot below, the roles assigned in the porfolio box will be inherited by all project boxes and their children (if they have any).

In addition, the roles added in the *Sport App* hybrid project will be inherited by the *Deployment*, *Initation*, and *Operational preparation* child boxes. The same principle applies to the *Software development* project box.

On the other hand, both classic projects under portfolio have no children. For that reason, they inherit roles from the portfolio box and can have their own roles additionally assigned, but they will not pass on those roles until they have child boxes.

![The direction of the security role inheritance.](/cms_trial/assets/f6d4b2c4-5c99-41e6-90a7-18fde227be71.png)

For example, a Project Manager may need access to multiple projects. A Box Admin in the the portfolio box can grant the manager also the Box Admin role. This way, they will gain access to all boxes that belong to the portfolio box. Otherwise, the portfolio Box Admin would need to assign the Project Manager the Box Admin role in each box on the individual basis.

- User roles inherited from upper-level boxes are not listed in the [**box configuration**](/cms_trial/space/SPM/1918666176/Box+configuration/) > **Security**. They can be viewed only at the upper level of the hierarchy, in the parent box where they were originally added.
- Remember tha Program Increments and Iterations are boxes, too. They are usually used to organize tasks within a given project box. There is no need to add a separate set of users to those boxes. Everyone who is meant to work on a project is added to the parent project box.

When you create sub-boxes, the following roles are inherited:

- Box Admin
- Box Editor
- Box Viewer

The Sub-box Creator is not inherited, as it would potentially allow users to create sub-boxes they could not delete.

### Home (root) box

Roles are always inherited from the upper-level boxes.

Therefore, the security roles granted in the Home (root) box apply to all sub-boxes in the hierarchy (all sub-boxes and their children nested under the Home box).

For example, if someone is a Box Admin of the Home (root) box, they automatically have the same permissions in all sub-boxes throughout the entire hierarchy.

If you want to grant a user the same role in all boxes, assign it in the Home (root) box. It will be inherited by every box in the box hierarchy.

### Individual box

To change the assigned security roles within a given Box, go to **box configuration** > **Security**.

### Box type

On the box type configuration page, you can create a security role template (grant users various roles). Thank to this, each time you create a new box of that type, the roles are copied from the template into your new box. A Box Admin can later manage the access of those users in a box configuration.

## Box-level roles: Comparison

### App Admin vs. Home Box Viewer

You may want some people to be able to view all boxes, but not to be able to make changes to them. If you add a user as App Admin, they have full access to everything. But, if you add someone as a Viewer to the "Home" (root) box, they can see all boxes and their contents but cannot edit them.

### App Admin vs. Box Admin

You may also want someone to have Admin access to all boxes but not to the App itself. An App Admin can, for example, edit box types.

If you want a person to be able to carry out all possible operations on boxes but not change the app settings, grant them a Box Admin role in the Home (root) box. A Home Box Admin can see all the boxes and can configure them, delete them, move them, etc., but is not permitted to access and edit app settings.

## Permissions to everyone

Wyen you enable the **Permissions to everyone** option, every Jira user is granted the App Admin role, allowing them to edit settings on the app level and in every box (depending on Jira security settings).

However, we do not recommend using this option if you work on large Jira instances with dozens of boxes and you need to ensure that all app settings remain as they should and the box data is not viewed by unauthorized users.

![Permissions for everyone settings overrides grants App User and App Admin role to every Jira user.](/cms_trial/assets/f181729d-49a1-4a79-adaa-cc6d26000723.png)

## Match security roles

Security roles should match. If someone can edit a Jira project, make sure they are also permitted to edit a corresponding box in BigPicture, and the other way round.

## Insufficient Jira permissions (warning)

If you see the warning message whilst trying to access BigPicture for Jira Cloud, follow the steps described on the [Jira related issues](/cms_trial/space/SPM/1918764358/Jira+related+issues/) page.