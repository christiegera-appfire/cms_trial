# Update OKR

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

On the update page, you can update the progress and status of individual OKRs as your teams work toward them. We suggest updating the OKR status regularly, either weekly or monthly, to stay focused on OKRs while working on daily tasks.

You can manually update the following OKR details:

- [Status](/cms_trial/space/SPM/1918702011/OKR+status+and+progress/)
- [Current progress/Current value](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918701108) (for manual OKRs)

The app also generates automatic updates for auto-OKRs from OKRobot when:

- OKR is updated via API.
- OKR progress is updated when the associated work item status changes (and affects auto-KR progress).

You cannot edit or delete those updates.

## Update OKR (screen)

When updating an OKR, an update screen pops up. You can enter the following data on the OKR update screen:

![Objective update screen.](/cms_trial/assets/ed50e392-ae9e-4440-bbd3-1a3f7755a4c4.png)

- **Date of update** - The current date is automatically filled in, but you can edit it.
- **+Add time** - Add time if your teams make quick progress on the KRs and update them more than once per day.
- **Choose a status** - You do not need to change the OKR status if it has not changed. The previous status, if available, will appear below.
- **Update current progress**/**Update current value** - For a manual OKR, you can update progress manually.
- **Write an update comment for others** - Briefly describe the progress made and include any relevant information for others.

### Status

You can update the status using the [API](https://developer.bigpicture.one/reference/updatekeyresult).

## Update OKR

You can update OKR on the [*Overview*](/cms_trial/space/SPM/1918834317/OKR+Overview/) page (OKR details panel, context menu) and on the [*OKR Details*](/cms_trial/space/SPM/1918536390/OKR+details+page/) page.

1. Open the OKR update modal on one of the following:

   1. *OKR Details* page:

      1. Click the **Update progress** button located in the upper-right corner.
   2. *Overview* page > context menu:

      1. Click **More actions** (**…**) and select **Post an update** from the menu.
   3. *Overview* page > OKR Details side panel > **Activity** section:

      1. Click **Add update** (plus icon) on the section header.
2. An OKR update modal displays.
3. Enter new details on the OKR update screen.
4. Click **Submit** to finish.

### Update OKR via API

Visit the [developer portal](https://developer.bigpicture.one/reference/updatekeyresult) for more details.

## Review the OKR updates

You can review the history of automatic and manual progress or status updates on the:

- ***OKR Details*** page > **Progress** tab > **Activity** section.
- **OKR Details side panel** > **Activity** section.

Visit the [OKR Details page](/cms_trial/space/SPM/1918536390/OKR+details+page/) and the [OKR Details side panel](/cms_trial/space/SPM/1918865686/OKR+Details+side+panel/) for more information.

Automated updates made using the API and OKRobot are marked with the appropriate label.

![The activity section.](/cms_trial/assets/bb14f8e3-77c4-41c7-9d75-920bc345649e.png)

For the latest updates, you can view them in the **Last update** column on the [*Progress Dashboard*](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918801225) page.

![image-20260601-091141.png](/cms_trial/assets/b10bd845-19f4-459c-8d29-fc715dbfc9d6.png)