# Update OKR

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

On the update page, you can update the progress and status of individual OKRs as your teams work toward them. We suggest updating the OKR status regularly, either weekly or monthly, to stay focused on OKRs while working on daily tasks.

You can update the following OKR details:

- [Status](/cms_trial/space/SPM/1918702011/OKR+status+and+progress/)
- [Current progress/Current value](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918701108) (for manual OKRs)

## Update OKR (screen)

When updating an OKR, an update screen pops up. You can enter the following data on the OKR update screen:

![Objective update screen.](/cms_trial/assets/ad9101b4-242b-4e9c-95d0-8e40947f49cc.png)

- **Date of update** - The current date is automatically filled in, but you can edit it.
- **+Add time** - Add time if your teams make quick progress on the KRs and update them more than once per day.
- **Choose a status** - You do not need to change the OKR status if it has not changed. The previous status, if available, will appear below.
- **Update current progress**/**Update current value** - For a manual OKR, you can update progress manually.
- **Write an update comment for others** - Briefly describe the progress made and include any relevant information for others.

### Status

You can update the status using the [API](https://developer.bigpicture.one/reference/updatekeyresult).

## Update OKR

### On the OKR details panel

1. Click the **Update** button.
2. An update screen appears.
3. Enter new details on the OKR update screen.
4. **Submit** to finish the process.

### On the OKR details page

1. Click the **Update** button located in the upper right corner.
2. An update screen appears.
3. Enter the details on the OKR update screen.
4. **Submit** to finish the process.

### Using API

Visit the [developer portal](https://developer.bigpicture.one/reference/updatekeyresult) for more details.

## Review the OKR status changes

### On the OKR details panel

You can see the latest updates displayed directly on the OKR details panel. If they were not previously loaded, click the **Load more updates** link to view them. If there are more updates that fit the screen, click the link again to review more historical changes.

![OKR updates on the OKR side panel.](/cms_trial/assets/f32d82d6-ebf1-494b-b8a6-51b799ec650b.png)

Automated updates done using the API are labeled.

![image-20260601-085959.png](/cms_trial/assets/97a0bf5c-72da-4098-a550-b69ce5783a70.png)

### On the OKR details page

The OKR update appears in the [**Status changes**](/cms_trial/space/SPM/1918505492/Goal%27s+lifecycle/) section on the [*OKR details*](/cms_trial/space/SPM/1918536390/OKR+details+page/) page. This section lists all the status changes introduced to the individual OKR. It will help during OKR review meetings and when preparing OKR reports.

![OKR status changes on the OKR details page.](/cms_trial/assets/1f29533e-e7c4-4886-8797-b6b154218b06.png)

**Show automated updates (toggle)**

Toggle this switch to show or hide all automatic updates from OKRobot, auto-KRs, or APIs. This includes system-generated messages from creating OKRs, changing statuses, or importing OKR data to BigPicture.

This toggle is enabled by default. This is a user-specific setting, meaning your preference will not affect the visibility of automatic updates for other team members.

You cannot hide historical API records.

![image-20260601-085710.png](/cms_trial/assets/de2b11f8-2bb6-42a5-b77a-16e8e762e9e7.png)

### On the Progress Dashboard

The [*Progress Dashboard*](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918801225) page provides an overview of OKR progress, highlighting recent successes and identifying OKRs that are off track or at risk. You can also review statuses over time and use the filters to track only those OKRs you are interested in.

![Screenshot of the Progress Dashboard in the OKR module.](/cms_trial/assets/fca811b2-142b-42a1-b29a-087216cb076d.png)

Automated updates done using API are labeled.

![image-20260601-091141.png](/cms_trial/assets/103195b4-01f6-4ce5-8abb-f11da4c820f5.png)