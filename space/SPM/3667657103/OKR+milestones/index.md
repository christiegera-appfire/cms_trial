# OKR milestones

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

OKR Milestones break down long-term goals into time-bound checkpoints between your start and target values. They let teams measure incremental progress, flag trajectory risks early with automated status updates (Upcoming, Achieved, or Missed), and keep OKRs on track well before the final deadline.

You can create and manage OKR milestones only in the OKR module.

See the video to learn more.

## Permissions

Adding and managing OKR milestones requires **Edit OKR** permission.

## Create a new OKR milestone

You can define milestones between a start value and a specific target value for any OKR (Strategic theme, Objective, Key Result).

You can create up to 12 milestones per OKR.

1. On the [*OKR details*](/cms_trial/space/SPM/1918536390/OKR+details+page/) page, go to the *Progress* tab.
2. In the **Milestones** section, click **Add milestone** (plus icon).
3. The **Add milestone** modal displays. On this modal, add:

   ![Add milestone dialog with fields for name, description, target value, and due date.](/cms_trial/assets/11da9f0c-4b05-4b1e-8df6-583988eeba08.png)
   1. **Name**.
   2. **Description** (optional).
   3. **Target value**: (Milestones use the same measurement unit as the parent OKR. See: [OKR progress](/cms_trial/space/SPM/2325021322/OKR+progress/)).
   4. **Due date**: (Must be between the OKR expected start date and expected end date).
4. Click **Add milestone**.
5. The milestone is now shown on the Progress chart and in the **Milestones** section.

## Delete and Edit OKR milestones

After you create it, you can edit and delete it.

1. On the *OKR Details* page, go to the **Progress** > **Milestones** section.
2. Click **More actions** (**…**) next to the milestone and select from the menu:

   1. **Edit**.
   2. **Delete**.

### Edit

1. The **Edit milestone** modal displays. Change the milestone name, description, target value, or due date as you see fit.
2. Click **Save changes**.

![Edit milestone dialog showing the fields available for updating a milestone.](/cms_trial/assets/4b33766b-4821-4483-8f16-48ed60f61520.png)

### Delete

A confirmation modal displays. Click **Delete** to confirm deleting the OKR milestone. This action cannot be undone.

![Delete milestone confirmation dialog with the option to confirm or cancel deletion.](/cms_trial/assets/b75be217-0798-447e-b2e0-90c6ed9e167f.png)

## Filter and sort OKR milestones

1. On the *OKR Details* page, go to the **Progress** > **Milestones** section.
2. Click **Filter** and select:

   1. Filter by status: **All**, **Upcoming**, **Achieved**, or **Missed**.
   2. Sort by: **Due date** **(Earliest first)**, **Due date (latest first)**, **Name**, or **Status**.
   3. **Hide achieved** (to hide achieved milestones from the list).

![Milestones filter menu showing status filters, sorting options, and the Hide achieved option.](/cms_trial/assets/a8e21990-1b5d-48dd-875e-ef0f128c0845.png)

*Progress*

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

- *OKR Details* page > *Progress* tab
- *Overview* page > [OKR Details side panel](/cms_trial/space/SPM/1918865686/OKR+Details+side+panel/)

Mouse over a milestone to see more details.

![OKR progress chart showing milestones along the timeline and their relationship to OKR progress.](/cms_trial/assets/cbdb51ef-7596-4d63-a1f8-68b6799ba6ad.png)

### Milestones (section)

The *OKR Details* page > **Milestones** section lists all milestones created for the OKR you are currently viewing (the list may be affected by the active filters).

Here, you can check milestone progress, due dates, and status, and manage your milestones.

### Overview (page)

On the [*Overview*](/cms_trial/space/SPM/1918834317/OKR+Overview/) page, you can filter all visible OKRs by the **Has latest milestone missed** status to let you surface OKRs with missed milestones.

![Has latest milestone missed filter in the Status column.](/cms_trial/assets/e500d317-67f2-4bdb-be8e-ef2b97124f3b.png)

### Progress dashboard (page)

The [*Progress Dashboard*](/cms_trial/space/SPM/1918801225/Progress+Dashboard/) page features an **OKRs with most recent milestone missed** section, letting you review OKRs with overdue milestones and inspect them individually on their respective *OKR Details* pages.

![OKRs with most recent milestone missed section on the Progress Dashboard page.](/cms_trial/assets/0ab6d064-04aa-4589-a43a-2f868cbb676d.png)

## Import and Export OKR milestones

OKR milestones are included in the [CSV export](/cms_trial/space/SPM/1918668919/Export+OKRs/). You can also add them to your [import file](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918406659).