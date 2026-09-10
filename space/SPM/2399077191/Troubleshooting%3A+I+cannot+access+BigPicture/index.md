# Troubleshooting: I cannot access BigPicture

## Problem

- You can see the BigPicture app under Jira’s **Apps,** but you are denied access to view any boxes in BigPicture.

![Access denied to BigPicture splash screen.](/cms_trial/assets/19c10b9d-92da-4366-9b1a-4e80ee47a85c.png)

## Solution

If you can see the BigPicture app in the dropdown under **Apps** in Jira, but upon opening the app, you cannot access any data, it means you were not granted permission to any box in BigPicture.

- Box-level roles are assigned to individuals and teams, granting them access to the individual boxes.
- Who can solve the problem? app admin jira admin box admin
- Where to solve it? **Box configuration page** > **Security**

There are four [box-level roles](/cms_trial/space/SPM/1918797447/Box-level+permissions/):

- Box Admin
- Box Editor
- Box Viewer
- Sub-box Creator

You can assign any of these roles to the selected user or group of users on the Home box or individual box levels.

In the following scenarios, we will mention only the Box Viewer role, as this role is sufficient for the user to get access to the BigPicture box/boxes, but it does not permit the viewer to manage them or create new boxes. Depending on your needs, an App or a Box Admin can assign you a higher box-level role.

### Scenario 1: You are permitted to view all boxes in the box hierarchy

In this scenario, you are permitted to see all the boxes created in the organization.

Your Jira or App Admin, or a Home Box Admin, can add you to the Box Viewer role in the Home/root box:

1. Navigate to the Home box and open it in the Overview module.
2. On the **box configuration** > **Security** page, use a dropdown to add an individual user or a group of users to the Box Viewer role.

![Home box security settings.](/cms_trial/assets/47fc1ccb-e156-43d0-8cb1-677b01bd8a1f.png)

When you are added, you can see the entire box hierarchy in the Overview module.

### Scenario 2: You are permitted to view only a part of the box hierarchy

In this scenario, you are permitted to see only those boxes to which you were given a relevant box-level role.

A Box Admin can add you to the Box Viewer (or higher) role in a selected box:

1. Navigate to the box you want to grant permission to another person or group.
2. On the **box configuration** > **Security** page, use a dropdown to add an individual user or a group of users to the Box Viewer role.

When you are added, you can see only those boxes in the Overview module to which you were granted a specific box-level role.

![Box viewer of the Agile box.](/cms_trial/assets/ac05b6a1-481e-4684-9a3a-8af19393320a.png)

## Next steps after fixing the issue

The App User and the Box Viewer roles let you access the app only. To be able to do anything more in the app, such as create, edit, and manage boxes, the App Admin or the Box Admin must also assign you the relevant box-level role.

Visit the [Troubleshooting: I cannot create boxes](/cms_trial/space/SPM/2398619016/Troubleshooting%3A+I+cannot+create+boxes/) page to learn more.

## More information

- [App-level permissions](/cms_trial/space/SPM/1918535770/App-level+permissions/)
- [Box-level permissions](/cms_trial/space/SPM/1918797447/Box-level+permissions/)