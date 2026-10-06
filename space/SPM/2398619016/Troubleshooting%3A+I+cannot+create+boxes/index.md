# Troubleshooting: I cannot create boxes

## Problem

- You can open the app and see the existing box or boxes, but you cannot create any new boxes. The **+Add new** button is grayed out in the Overview module.

![BigPicture user sees the plus button grayed out, which means they are not allowed to create new boxes.](/cms_trial/assets/e0a9dd23-5036-4043-89a6-9a6effb5aff3.png)![BigPicture user sees the plus button grayed out, which means they are not allowed to create new boxes.](/cms_trial/assets/01e40809-b5cb-41e1-ae79-fed36d7eb1ba.png)

## Solution

- BigPicture App User needs a relevant box-level security role to be permitted to create boxes.
- Who can solve the problem? app admin jira admin box admin
- Where to solve it? **Configuration** > **Security**

There are four [box-level roles](/cms_trial/space/SPM/1918797447/Box-level+permissions/):

- Box Admin
- Box Editor
- Box Viewer
- Sub-box Creator

Only Box Admins and Sub-Box Creators can create new boxes:

- under a specific box in the box hierarchy
- under a Home/root box

## Detailed steps

### Scenario 1: Create boxes under a specific box

In the first scenario, a Box Admin can grant a Box Sub-creator role to another user, which will allow them to create sub-boxes under a specific box.

Box Admins can add users to specific box-level roles on the [box configuration](/cms_trial/space/SPM/1918666176/Box+configuration/) page.

![A configuration page of the Expansion 2025 portfolio box.](/cms_trial/assets/8482807f-aa1d-4747-a151-1a89ef3cbb23.png)

For example, a Sub-box Creator of a selected Portfolio box can create project boxes, such as Agile, Classic, etc., within that portfolio. Once they create a box, they automatically become Box Admins of the boxes they create under that Portfolio box.

### Scenario 2: Create boxes under a Home/root box

This scenario is similar to the previous one, but there is a small but significant difference.

A Jira or App Admin can assign an individual user or a team a Sub-box Creator role in the Home/root box.

![A configuration page of the root box.](/cms_trial/assets/04ed0152-9c82-404c-b9f2-eb86fb5f78bf.png)

As a result, a Sub-box Creator user on the root box level can create portfolio, program, and project boxes directly under a root box. Once they create a box, they automatically become Box Admins of the boxes they create under the Home box.

The Sub-box Creator role does not permit them to view, manage, or edit any of the boxes in the box hierarchy (unless they are permitted to do so on an individual basis).

For that reason, in the Overview module, Sub-box Creators cannot see boxes other than the Home and parent box (but cannot open them), and the boxes they created (of which they became Box Admins).

## More information

- [Box-level permissions](/cms_trial/space/SPM/1918797447/Box-level+permissions/)
- [Inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/)