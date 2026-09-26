# OKR milestones

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

OKR Milestones break down long-term goals into time-bound checkpoints between your start and target values. They let teams to measure incremental progress, flag trajectory risks early with automated status updates (Upcoming, Achieved, or Missed), and keep OKRs on track well before the final deadline.

You can create and manage OKR milestones only in the OKR module.

## Permissions

Adding and managing OKR milestones requires **Edit OKR** permission.

## Create a new OKR milestone

You can define milestones between a start value and a specific target value for any OKR (Strategic theme, Objective, Key Result).

You can create up to 12 milestones per OKR.

1. On the [*OKR details*](/cms_trial/space/SPM/1918536390/OKR+details+page/) page, go to the **Progress** tab.
2. In the **Milestones** section, click **Add milestone** (plus icon).
3. The **Add milestone** modal displays. On this modal, add:

   ![add-milestone.png](/cms_trial/assets/b3bd0f25-6a77-4192-b3db-1293d575a734.png)
   1. **Name**.
   2. **Description** (optional).
   3. **Target value** (Milestones use the same measurement unit as the parent OKR. See: [OKR progress](/cms_trial/space/SPM/2325021322/OKR+progress/)).
   4. **Due date** (Must be between the OKR expected start date and expected end date).
4. Click **Add milestone**.
5. The milestone is now shown on the Progress chart and in the **Milestones** section.

## Delete/Edit OKR milestones

After you create it, you can edit and delete it.

1. On the *OKR Details* page, go to the **Progress** > **Milestones** section.
2. Click **More actions** (**…**) next to the milestone and select from the menu:

   1. **Edit**.
   2. **Delete**.

### Edit

1. The **Edit milestone** modal displays. Change the milestone name, description, target value, and/or due date as you see fit.
2. Click **Save changes**.

![The Edit milestone modal.](/cms_trial/assets/05463357-7e55-4c66-9a92-7a74c12c6950.png)

### Delete

A confirmation modal displays. Click **Delete** to confirm deleting the OKR milestone. This action cannot be undone.

![The Delete milestone modal.](/cms_trial/assets/d867c501-2d2b-4ff8-ab00-ed4d84589b39.png)

## Filter/Sort OKR milestones

1. On the *OKR Details* page, go to the **Progress** > **Milestones** section.
2. Click **Filter** and select:

   1. Filter by status: **All**, **Upcoming**, **Achieved**, or **Missed**.
   2. Sort by: **Due date** **(Earliest first)**, **Due date (latest first)**, **Name**, or **Status**.
   3. **Hide achieved** (to hide achieved milestones from the list).

![Milestones filtering options](/cms_trial/assets/10b4518e-97fa-4213-a2cd-02f5a9f5a23a.png)

## API

You can fetch OKR milestones via the API.

Visit the [BigPicture Developer Portal](https://developer.bigpicture.one/reference/whatisbigpicture) for more details.

## Track OKR milestones

Milestone health is indicated by the following statuses:

- **Upcoming**: The due date is in the future, and OKR actual progress is below the milestone target.
- **Achieved**: The due date has passed, or OKR progress is >= milestone target.
- **Missed**: The due date has passed, and OKR progress is < milestone target.
- **Invalid**: The milestone date lands outside the OKR's start or end dates. A common example is updating the OKR start/end dates and leaving an existing milestone due date out of range.

A warning indicator is shown in the status column for OKRs with a missed latest milestone.

You can track milestones' health and progress on the progress chart and in the dedicated **Milestones** section.

### Progress chart

OKR milestones are mapped along the timeline in the Progress chart in the OKR module.

- *OKR Details* page > Progress tab
- *Overview* page > [OKR Details side panel](/cms_trial/space/SPM/1918865686/OKR+Details+side+panel/)

Mouse over a milestone to see more details.

![OKR milestones on the progress chart.](/cms_trial/assets/8ce4d67e-6cb9-49a0-be50-67e9a5d51b41.png)

### Milestones (section)

The *OKR Details* page > **Milestones** section lists all milestones created for the OKR you are currently viewing (the list may be affected by the active filters).

Here, you can check milestone progress, due dates, and status, and manage your milestones.

### Overview (page)

On the [*Overview*](/cms_trial/space/SPM/1918834317/OKR+Overview/) page, you can filter all visible OKRs by the **Has latest milestone missed** status to let you surface OKRs with missed milestones.

![Has latest milestone missed filter in the Status column.](/cms_trial/assets/a32a16af-80f4-4551-9d9c-e1572582789e.png)

### Progress dashboard (page)

The [*Progress Dashboard*](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918801225) page features an **OKRs with most recent milestone missed** section, letting you to review OKRs with overdue milestones and inspect them individually on their respective *OKR Details* pages.

![OKRs with most recent milestone missed section on the Progress Dashboard page.](/cms_trial/assets/e39e6c03-cd84-4ba4-aa4d-fc7a9bb65596.png)

## Import/Export OKR milestones

OKR milestones are included in the [CSV export](/cms_trial/space/SPM/1918668919/Export+OKRs/). You can also add them to your [import file](/cms_trial/space/SPM/1918406659/Import+OKRs/).