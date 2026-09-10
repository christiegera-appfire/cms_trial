# Convert OKR

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

You can convert a manual OKR to an auto-OKR and other way around.

## Convert a manual OKR to an auto-OKR

Converting a manual OKR to an automatic OKR allows the [progress of an OKR](/cms_trial/space/SPM/2325021322/OKR+progress/) to be updated automatically based on the progress of the linked items.

After the conversion:

- Strategic theme/Objective:

  - Progress is calculated based on the progress of all associated items: sub-themes, sub-objectives, and Key Results.
- Key Result:

  - Progress is calculated based on the linked boxes and work items. Updates happen automatically when linked issues change status (synced every 5 minutes). You can manually trigger a refresh by clicking **Trigger refresh** in the **Linked Issues** section on the OKR details page.
  - When you mark a work item as **Done** in the Scope, Gantt, Board, Resources, or Calendar modules, the linked issue in the OKR module automatically reflects this progress.
  - If you move an issue back to **To Do**, the OKR progress will decrease. Issues marked **In Progress** don't affect OKR progress, but their status still updates in the OKR module.
  - If issues are linked through JQL, they will be integrated into the JQL used to sync matching issues. To include more issues, modify the query in the **Linked Issues** section on the OKR details page.
  - If no issues were previously linked, you will need to link them to see progress.

You can [link issues](/cms_trial/space/SPM/1918507296/Link+work+items+to+Key+Results/) and boxes to a manual KR. Linked issues an[d boxes](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spmdraft&title=OLD%20Link%20boxes%20to%20Key%20Results&linkCreation=true&fromPageId=2223669291) do not affect manual KR progress, but they add visibility and context.

You can change the OKR mode on the OKR details page.

1. On the [*OKR details*](/cms_trial/space/SPM/1918536390/OKR+details+page/)page, click **More actions** (**…**).
2. For a Strategic theme and Objective, select **Convert to auto progress tracking**; for a Key Result, select **Convert to auto KR**.

![Convert to auto KR option on the menu on the kr details page.](/cms_trial/assets/49f0c024-f2aa-44bb-9f44-14abc40b59eb.png)

1. A modal displays. Click the **Convert** button to finish the process.

## Convert an auto-KR to a manual KR

Converting from an auto-OKR to a manual OKR means your KR's progress will no longer update automatically based on the linked items.

Upon conversion, the OKRs, boxes, and linked issues will remain connected but will no longer affect progress. Your current progress will remain unchanged, and no previous updates will be deleted.

1. On the [*OKR details*](/cms_trial/space/SPM/1918536390/OKR+details+page/)page, click **More actions** (**…**).
2. For a Strategic theme and Objective, select **Convert to manual progress tracking**; for a Key Result, select **Convert to manual KR**.

![Convert to manual KR option on the menu on the kr details page.](/cms_trial/assets/be33fef6-dfd5-4b52-8f7e-9c73425cc935.png)

1. A modal displays. Click the **Convert** button to finish the process.