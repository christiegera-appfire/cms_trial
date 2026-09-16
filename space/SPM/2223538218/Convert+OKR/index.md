# Convert OKR

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

You can convert a manual OKR to an auto-OKR and other way around.

## Convert an OKR

You can change the OKR mode on the [*OKR Details*](/cms_trial/space/SPM/1918536390/OKR+details+page/) page.

1. Click **More actions** (**…**) in the top-right corner.
2. From the menu:

   1. For a Strategic theme/Objective:

      1. If the OKR is in manual mode, select **Convert to auto progress tracking**.
      2. If the OKR is in auto mode, select **Convert to manual progress tracking**.

         ![Context menu on the OKR details page.](/cms_trial/assets/0b69f97d-c994-4dc0-8ca7-d0c6aac5a1a0.png)
   2. For a Key Result:

      1. If the KR is in manual mode, select **Convert to auto KR**.
      2. If the KR is in auto mode, select **Convert to manual KR**.
3. A confirmation modal displays. Click **Convert** to finish.

## After OKR conversion

Changing an OKR's mode can directly impact its progress calculation.

### Manual OKR --> Auto-OKR

You can [link work items](/cms_trial/space/SPM/1918507296/Link+work+items+to+Key+Results/) and [boxes](/cms_trial/space/SPM/2229665803/Link+boxes+to+Key+Results/) to a manual KR. Linked issues and boxes do not affect manual KR progress, but they add visibility and context.

Converting a manual OKR to an automatic OKR allows the [progress of an OKR](/cms_trial/space/SPM/2325021322/OKR+progress/) to be updated automatically based on the progress of the linked items.

After the conversion:

- Strategic theme/Objective:

  - Progress is calculated based on the progress of all associated items: sub-themes, sub-objectives, and Key Results.
- Key Result:

  - Progress is calculated based on the linked boxes and work items. Updates happen automatically when linked issues change status (synced every 5 minutes). You can manually trigger a refresh by clicking **Trigger refresh** in the **Linked Issues** section on the OKR details page.
  - When you mark a work item as **Done** in the Scope, Gantt, Board, Resources, or Calendar modules, the linked issue in the OKR module automatically reflects this progress.
  - If you move an issue back to **To Do**, OKR progress decreases. Issues marked **In Progress** don't affect OKR progress, but their status still updates in the OKR module.
  - If issues are linked through JQL, they will be integrated into the JQL used to sync matching issues. To include more issues, modify the query in the **Linked Issues** section on the OKR details page.
  - If no issues were previously linked, you will need to link them to see progress.

### Auto-KR -> Manual KR

Converting from an auto-OKR to a manual OKR means your KR's progress will no longer update automatically based on the linked items.

Upon conversion, the OKRs, boxes, and linked issues will remain connected but will no longer affect progress. Your current progress will remain unchanged, and the app will not delete OKRs’ previous updates.