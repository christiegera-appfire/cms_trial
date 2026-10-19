# OKR progress

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

The app can automatically calculate any OKR's progress, or the user can update it manually.

## How is OKR progress calculated?

- The progress of a Strategic theme, sub-theme, Objective, and sub-Objective is always expressed as a percentage.
- Individual sub-items affect the parent item’s progress based on their contribution ([weight](/cms_trial/space/SPM/1918636591/Add+weight+(contribution)+to+OKR/)).
- The progress of a Key Result can be expressed as a number, a percentage, or a currency unit.

**OKR progress** = The sum of the progress of all direct sub-items divided by the total number of those sub-items.

The formula remains the same, regardless of whether an OKR is in auto or manual progress mode.

The direct supporting sub-items include:

| **Strategic theme/sub-theme** | **Objective/sub-objective** | **Key result** |
| --- | --- | --- |
| - Sub-themes - Sub-objectives - Key Results    - [linked work items](/cms_trial/space/SPM/1918507296/Link+work+items+to+Key+Results/) (they affect the automatic Key Results’ progress)   - [linked boxes](/cms_trial/space/SPM/2229665803/Link+boxes+to+Key+Results/) (the work items in the scope of linked boxes affect the automatic Key Results’ progress) | - Sub-objectives - Key Results    - [linked work items](/cms_trial/space/SPM/1918507296/Link+work+items+to+Key+Results/) (they affect the automatic Key Results’ progress)   - [linked boxes](/cms_trial/space/SPM/2229665803/Link+boxes+to+Key+Results/) (the work items in the scope of linked boxes affect the automatic Key Results’ progress) | - [Linked work items](/cms_trial/space/SPM/1918507296/Link+work+items+to+Key+Results/) (they affect the automatic Key Results’ progress) - [Linked boxes](/cms_trial/space/SPM/2229665803/Link+boxes+to+Key+Results/) (the work items in the scope of linked boxes affect the automatic Key Results’ progress)   NOTE   - When you mark a work item as **Done** in the Scope, Gantt, Board, Resources, or Calendar modules, the linked work item in the OKR module automatically reflects this progress. - If you move a work item back to **To Do**, the OKR progress will decrease. - Work items marked **In Progress** don't affect OKR progress.   Visit the [OKR linked work items data sync](/cms_trial/space/SPM/2173109245/OKR+linked+work+items+data+sync+(and+auto-progress+update)/) page for more details on task data sync between the OKR module and other modules, and how it affects progress auto-update. |

### Strategic theme/sub-theme

A parent Strategic theme is highlighted in blue, and the three direct sub-items are highlighted in yellow. The Strategic theme’s progress is based on these three sub-items and their weight.

![A strategic theme and its child OKRs highlighted.](/cms_trial/assets/bcb0ea0c-1157-41b7-a886-7c49b47200bc.png)

### Objective/sub-Objective

A parent Objective is highlighted in blue, and the three direct sub-items are highlighted in yellow. The Objective’s progress is based on these three sub-items and their weight.

![An objective and its child OKRs highlighted.](/cms_trial/assets/68c9224d-9f6c-4801-ab63-d8f785de59bf.png)Objective's progress: See example![A sumple OKR hierarchy - one objective and three key results.](/cms_trial/assets/4aeaf77f-bc2f-4341-bd9b-4f269ab93ab9.png)

Given:

- Total number of direct sub-items = 3
- Key Result 1progress =66.67% and its weight = 1
- Key Result 2progress = 9.41% and its weight = 1
- Key Result 3progress = 20% and its weight = 1

Therefore:

**Objective progress** = (66.67%x1 + 9.42%x1 + 20%x1)/3 = 32.03%

### Key Result

A parent Key Result is highlighted in blue, and the direct sub-item is highlighted in yellow. Here, the Key Objective’s progress is based on completed Jira work items (status: **Done**) in the linked box.

![The Key Result and a linked box are highlighted.](/cms_trial/assets/edc8e4f3-51ef-46d5-8add-1981bb5fff25.png)

For examples, see:

- [Auto-KR](/cms_trial/space/SPM/1918670238/Auto-KR/)
- [Manual KR](/cms_trial/space/SPM/1918702967/Manual+KR/)

## Auto-OKR

In auto mode, the app calculates the OKR's progress automatically based on the progress of the linked sub-items. As your teams work toward their OKRs and update the status of the associated sub-items, the OKR’s progress automatically updates.

OKRs in the auto progress mode require minimal user intervention to maintain accurate tracking.

## Manual OKR

In manual mode, the user [updates the OKR's progress](/cms_trial/space/SPM/1918507253/Update+OKR+progress/) manually.

## Set an OKR to auto or manual mode

You can set the progress mode for an OKR in two ways:

- On the New Strategic theme/New Objective/New Key Result modal (when you [create a new OKR](/cms_trial/space/SPM/2324726248/Create+OKR/))

  - For a new Strategic theme and Objective: Under **Progress**, select **Child OKRs** to set it in auto mode, or select **Manual** to set it in manual mode.
  - For a new Key Result: Under **Progress tracking**, select **Linked items** to set it in auto mode, or select **Manual** to set it in manual mode.
- You can [convert](/cms_trial/space/SPM/2223538218/Convert+OKR/) an OKR from one progress mode to another on the [*OKR details*](/cms_trial/space/SPM/1918536390/OKR+details+page/) page.