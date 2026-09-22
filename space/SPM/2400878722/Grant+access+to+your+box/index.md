# Grant access to your box

## What will I learn on this page?

> 💡 On this page, we will show you how to assign (as a BigPicture admin) box permissions to users or groups.

You will learn about:

- App **access** settings.
- **Role** configuration settings.
- Assign a role to a user or group.

After reviewing this page, you’ll understand how to:

- Grant access to BigPicture.
- Access box role configuration settings.
- Assign box roles to users or groups.

## Why should I grant access / assign roles?

Defining roles and granting access in BigPicture ensures that the right people can see and manage the right information in BigPicture. By assigning roles, you control who can (and who cannot) plan work, update progress, or adjust settings, which helps keep your projects organized and secure. Clear access rules also reduce errors and confusion, making it easier for teams to collaborate effectively from the start.

## BigPicture app access step-by-step

Review the following video to learn how to grant BigPicture access to users and groups.

The first step in configuring BigPicture for users or groups is to grant them app access. Use the following steps to assign the **App User** role to an individual:

1. Click the wrench icon in the upper right-hand corner and select **Security**.

   ![Select Security from the dropdown menu.](/cms_trial/assets/a9832236-daa5-45ed-bdba-b581e084f36e.png)
2. Five app role permissions are displayed, along with descriptions:

   1. **App Admin** - Administrative access to every box and to business administration.
   2. **App Financial Admin** - Full access to the Financials module (only for boxes the user has access to) and can edit hourly rates.
   3. **App Financial Viewer** - Access to the Financials module (only for boxes the user has access to) without edit permissions.
   4. **App Resource Admin** - Basic access to BigPicture (same as an App User) and additional access to the Resources module.
   5. **App User** - Basic access to BigPicture that is dependent on individual permissions at the box level. (See the following section, Role configuration settings.)

      ![App access settings in BigPicture.](/cms_trial/assets/c1fcb831-5079-436f-a19e-85a71108ef7e.png)
3. Expand **App User** > **Users** and locate the appropriate user in the dropdown menu. Note that you can search for a user by typing the first few letters of their name.
4. Enter a checkmark next to the user’s name.

## Role configuration step-by-step

Role define user’s permissions within a box.

### Check roles

Use the following steps to view box roles in BigPicture:

1. Open the Module Switcher and click **Configuration** (you can also right-click the box’s row in the box tree).

   ![To begin, click the Configuration link in the Module Switcher.](/cms_trial/assets/732d63e6-977c-41b9-87fa-52676046998b.png)
2. In the left-hand panel, click **Security** > **Security**.
3. The Security page displays four available roles, defined below.

   1. **box Admin**: Administrators should assign this role to users or groups requiring full access to a box, including the ability to assign roles.
   2. **box Editor** - box editors have access to *all* modules within a box (Gantt, Scope, Board, etc.). However, they can’t update the box configuration or create and delete boxes.
   3. **box Viewer** - box viewers have read-only access to boxes. They can’t make changes to tasks, including moving them in the Gantt module.
   4. **Sub-box Creator** - Sub-box creators have access to create child boxes in the box they have access to. An example use of a sub-box creator is granting the role to a Project Manager who requires access to the box that defines their project. However, that same Project Manager should not have access to projects outside their responsibility in the organization.

      ![There are four box roles in BigPicture, Box Admin, Box Editor, Box Viewer, and Sub-Box Creator.](/cms_trial/assets/0894a672-82d7-48a3-841c-aa6e79cf88a0.png)
4. The number next to each role indicates the number of users assigned to the role.

### Assign a role to a user or group

Now that you understand the four box roles available in BigPicture, the following video describes the process of assigning a role to a user or group:

Or, follow these steps:

1. Open the Module Switcher and click **Configuration**.
2. In the left-hand pane, click **Security** > **Security**.
3. Expand the role you plan to assign, for example, **box Admin**.
4. Listings display for **Users** and **Groups**.

   ![Users and groups can be assigned a role.](/cms_trial/assets/ab5c1129-d9f8-4390-9353-aa8b3a800a99.png)
5. Expand the appropriate option. In this example, **Users**. Existing users display:

   ![Expand Users. A list of existing users displays and a dropdown to add a new user.](/cms_trial/assets/399bd34f-dcbf-48b6-b9a0-fe2c65ee7d4a.png)
6. To add the role to a user, locate them in the list. Alternatively, begin typing the user’s name, and the list filters automatically. Enter a check mark next to the user’s name.

   ![Locate the user in the dropdown or search by entering a few letters of the user's name.](/cms_trial/assets/4df5b146-a8e9-4f1b-8253-46d474f99ad9.png)
7. The list now includes the new user.

   ![The role is added to the user and the person displays in the list.](/cms_trial/assets/ab310086-9c95-4f22-81ea-d0fc3fc9648e.png)

## Explore other use cases

- [Global roles in BigPicture](https://appfire.atlassian.net/wiki/spaces/~anna.cieplota/pages/1957101569)

## Prerequisites

To complete the steps in this article, users must be assigned Admin access in BigPicture.

## Troubleshooting

- [I don’t see any data in BigPicture.](/cms_trial/space/SPM/2399077191/Troubleshooting%3A+I+cannot+access+BigPicture/)
- [I opened BigPicture and didn’t see any boxes.](https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/1961164869)

## Learn more

- [BigPicture security and permissions in Jira](/cms_trial/space/SPM/1918667044/BigPicture+security+and+permissions+in+Jira/)
- [Box security roles](/cms_trial/space/SPM/1918668158/Box+security+roles/)
- [Concept of a box](/cms_trial/space/SPM/1918404963/Concept+of+a+box/)
- [Box hierarchy](/cms_trial/space/SPM/1918535907/Box+hierarchy/)
- [Navigate between boxes (box switcher)](/cms_trial/space/SPM/1918667414/Navigate+between+boxes+(box+switcher)/)
- [Inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/)