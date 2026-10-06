# Overview module permissions

In general, you can find information on Security settings on the following pages:

- [App-level permissions](/cms_trial/space/SPM/1918535770/App-level+permissions/)
- [Box-level permissions](/cms_trial/space/SPM/1918797447/Box-level+permissions/)
- [Module-specific permissions](/cms_trial/space/SPM/1918536362/Module-specific+permissions/)

Security roles are always inherited from upper-level boxes. Therefore, security roles defined in the Home (root) box function as a default for all boxes in the hierarchy. If someone is a Box Admin of the Home (root) box, they automatically have the same permissions in all sub-boxes through the hierarchy.

Security roles are always inherited from upper-level Boxes (starting with the Root Box). This way, every time you create a new box, it will inherit the security roles - you do not need to assign them from scratch.

When you create sub-boxes, the following roles are inherited:

- Box Admin
- Box Editor
- Box Viewer

The sub-Box Creator role is not inherited, as it would potentially allow users to create sub-Boxes they can't delete. To learn more about the sub-Box creator role, scroll down to the relevant section of this page.

For example, if there is a "SAFe ART (Smart house App)" Box nested under the root:

- All Boxes under "SAFe ART (Smart house App)" will inherit the roles from it - including Iterations and Program Increments (a user who is an Editor in the "SAFe ART (Smart house App)" will also be an Editor in Program Increments and Iterations)

  ![Overview module, box with sub-boxes](/cms_trial/assets/510dc311-147d-45a7-92a1-024036f63c0c.png)
- All roles set up for the Home (root) Box will be inherited by the "SAFe ART (Smart house App)" and its sub-Boxes

  ![Overview module, Home box](/cms_trial/assets/45887725-39e3-4f1e-af79-6151e72eb0a8.png)

You can't make a Box private to prevent users from upper-level Boxes from having access.

Inherited roles are not listed in Box Configuration > Security. Only roles assigned to the Box are listed. An Admin can manually add users if the Inheritance mode allows it. Additionally, users are granted roles based on Box Type settings when a new Box is created.

![Settings, Security section](/cms_trial/assets/ea1c70b3-9de4-49f8-8836-82f48e547a4b.png)

## Box Lead

A Box Lead is not a security role; this setting doesn't automatically grant any permissions. To access a Box, a user must also be assigned some security role within a given Box.

A Box Lead assignment enables a "My focus" filter in the application's overview.

When you click “My focus,” only the Boxes in which you are the “Box Lead” will be listed. Boxes in which you are an admin/viewer/editor/sub-Box creator will not be displayed:

![Overview module, My focus section](/cms_trial/assets/db088c2a-fde4-46ba-b5de-a8048d0d9cc1.png)