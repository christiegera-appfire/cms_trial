# Link OKR to box

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

## Link OKR to box (old navigation)

Click to expand the guide

OKRs in the OKR module are only shown if they are linked to the box you are viewing.

## Automatically link an existing OKR to a box

OKRs are automatically linked to the box when you:

- [link a Jira work item](/cms_trial/space/SPM/1918507296/Link+work+items+to+Key+Results/) that is within the scope of the current box. In such a case, the Key Result (KR) that is linked to the work item from the current box will also appear in the OKR module, even if that Key Result belongs to a different box.
- [create an Objective](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918702275)/[Key Result](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918538655) in the OKR module. The newly created OKRs appear in the current box and are visible on the *Overview*, *Hierarchy*, and *Progress Dashboard* pages.
- [import OKRs](/cms_trial/space/SPM/1918406659/Import+OKRs/) from another source.

## Manually link an existing OKR to a box

The OKRs you create in the OKR module are global, which means you can link them to any other box in the [box hierarchy](/cms_trial/space/SPM/1918535907/Box+hierarchy/).

Note that you cannot link individual KRs to a box, as they exist only with their respective Objectives. Once you select a Key Result you want to link, the parent Objective will also be selected.

### In the box configuration

You can add OKRs to a box on the box scope definition page. And then, use a structure builder to arrange those OKRs into a hierarchy.

1. Define the OKRs to link. Go to **box configuration** > **Tasks** > box [**Scope definition**](/cms_trial/space/SPM/1918765868/Own-scope/) page > **OKR linked work** section.

   1. The **Direct links only** option lets you select individual Strategic themes/Objectives added to BigPicture. If any of those Strategic Themes or Objectives have Key Results, they will also be added to the box.
   2. The **All child items** option lets you select individual Key Results. Since KRs cannot exist without their parent, the Strategic themes/Objectives to which they belong will also be added to the box.
2. Click **Save**.

![OKR linked work section on the scope definition page. In the new navigation, the scope definition page is called Work items from Jira.](/cms_trial/assets/0344cb51-ff49-4216-9873-9a4bec642d43.png)

1. Build a structure. Go to **box configuration** > **Tasks** > **Task structure** > select [**Objective & Key Result**](/cms_trial/space/SPM/1918863661/OKRs+as+task+structure+builders/) [structure builder](/cms_trial/space/SPM/1918863661/OKRs+as+task+structure+builders/).

![Task structure builder templates.](/cms_trial/assets/5842f717-748a-471d-a2a4-b4ace6945c65.png)

1. Click **Save**.
2. Go to the Gantt or Scope module. Your OKRs are now displayed in the task list. If any of the OKRs you have defined in the box scope are linked to Jira work items, they will also be displayed and nested under their respective Key Result.

![okr-scope-and-structure-builders.png](/cms_trial/assets/37831429-b113-4b72-b44b-eca773101878.png)

### In the OKR module

You can add an existing OKR to your current box directly in the OKR module.

#### Box with no OKRs

By default, no OKRs are linked to the box. If you land in a box where no OKRs were ever created or manually linked:

1. On the splash screen, click the **Connect existing OKRs** button to add OKRs to the scope of a box.
2. A screen with the available OKRs appears. Check the OKRs from the list you want to add to a box.
3. Click **Connect** to finish the process.

#### Box with OKRs

If someone has already created OKRs or linked work items from that box to some KRs, you can manually add more OKRs to it.

1. On the [*Overview*](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918408551) page, click the **Link to box** button.
2. A screen with the available OKRs appears. Check the OKRs from the list you want to add to a box.
3. Click **Save** to finish the process.

## Unlink OKRs from a box

### In the box configuration

1. Go to **box configuration** > **Tasks** > box **Scope definition** page > **OKR linked work** section.
2. In the **OKR linked work** section, click **X** on the OKR to remove it from the list.
3. Click **Save**.

### In the OKR module

- Unlinking OKRs from a current box does not affect their progress (unless you unlink work items from the auto-KR or convert it to a manual KR).
- Unlinking an OKR is not the same as [deleting](/cms_trial/space/SPM/1918408286/Delete+OKR/) it. If you unlink an OKR, you can link it again to the current or another box.

If there is an OKR in your box that is no longer relevant to your current work, you can hide it. Note that you can unlink only:

- OKRs that were created directly in the box
- OKRs that were linked manually
- KRs that are not linked to any work items ([unlink the work items](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918670410) or convert the [auto-KR](/cms_trial/space/SPM/1918670238/Auto-KR/) to a [manual KR](/cms_trial/space/SPM/1918702967/Manual+KR/) to unlink it from the box)

To unlink an OKR from a box:

1. On the [*Overview*](/cms_trial/space/SPM/1918834317/OKR+Overview/) page, click the **Link to box** button.
2. A screen with the available OKRs appears. Uncheck the OKRs from the list you want to remove from the box.
3. Click **Save** to finish the process.

![unselect the box next to the OKR to have it unlinked.](/cms_trial/assets/416b3cd4-be56-4e72-ae48-77d89428d7cf.png)

## Link OKR to box (new navigation)

Click to expand the guide

OKRs in the OKR module are only shown if they are linked to the box you are viewing.

## Automatically link an existing OKR to a box

OKRs are automatically linked to the box when you:

- [link a Jira work item](/cms_trial/space/SPM/1918507296/Link+work+items+to+Key+Results/) that is within the scope of the current box. In such a case, the Key Result (KR) that is linked to the work item from the current box will also appear in the OKR module, even if that Key Result belongs to a different box.
- [create an Objective](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918702275)/[Key Result](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918538655) in the OKR module. The newly created OKRs appear in the current box and are visible on the *Overview*, *Hierarchy*, and *Progress Dashboard* pages.
- [import OKRs](/cms_trial/space/SPM/1918406659/Import+OKRs/) from another source.

## Manually link an existing OKR to a box

The OKRs you create in the OKR module are global, which means you can link them to any other box in the [box hierarchy](/cms_trial/space/SPM/1918535907/Box+hierarchy/).

You cannot link individual KRs to a box, as they exist only within their respective Objectives. Once you select a Key Result you want to link, the parent Objective will also be selected.

### Box configuration

You can add OKRs to a box on the Add work items from Jira page. And then, use a structure builder to arrange those OKRs into a hierarchy.

1. Define the OKRs to link. Go to **box configuration** > **Tasks** > box [**Add work items from Jira**](/cms_trial/space/SPM/1918765868/Own-scope/) page > **OKR linked work** section.

   1. The **Direct links only** option lets you select individual Strategic themes/Objectives added to BigPicture. If any of those Strategic Themes or Objectives have Key Results, they will also be added to the box.
   2. The **All child items** option lets you select individual Key Results. Since KRs cannot exist without their parent, the Strategic themes/Objectives which they belong to will also be added to the box.
2. Click **Save**.

![OKR linked work section on the scope definition page. In the new navigation, the scope definition page is called Work items from Jira.](/cms_trial/assets/0344cb51-ff49-4216-9873-9a4bec642d43.png)

1. Build a structure. Go to **box configuration** > **Tasks** > **Task structure** > select [**Objective & Key Result**](/cms_trial/space/SPM/1918863661/OKRs+as+task+structure+builders/) [structure builder](/cms_trial/space/SPM/1918863661/OKRs+as+task+structure+builders/).

![Task structure builder templates.](/cms_trial/assets/5842f717-748a-471d-a2a4-b4ace6945c65.png)

1. Click **Save**.
2. Go to the Gantt or Scope module. Your OKRs are now displayed in the task list. If any of the OKRs you defined in the box scope are linked to Jira work items, they will also display and nest under their respective Key Result.

![okr-list.png](/cms_trial/assets/0c280dfd-cba9-4f2b-b178-ebc7517d8863.png)

### OKR module

You can add an existing OKR to your current box directly in the OKR module.

#### Box with no OKRs

By default, no OKRs are linked to the box. If you land in a box where no OKRs were ever created or manually linked:

1. On the splash screen, click the **Connect existing OKRs** button to add OKRs to the scope of a box.
2. A screen with the available OKRs appears. Select the OKRs you want to add to a box.
3. Click **Connect** to finish the process.

#### Box with OKRs

If someone has already created OKRs or linked work items from that box to some KRs, you can manually add more OKRs to it.

1. On the [*Overview*](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918408551) page, click the **Link to box** button.
2. A screen with the available OKRs appears. Select the OKRs you want to add to a box.
3. Click **Save** to finish the process.

## Unlink OKRs from a box

### Box configuration

1. Go to **box configuration** > **Tasks** > box **Add work items from Jira** page > **OKR linked work** section.
2. In the **OKR linked work** section, click **X** on the OKR to remove it from the list.
3. Click **Save**.

### OKR module

- Unlinking OKRs from a current box does not affect their progress (unless you unlink work items from the auto-KR or convert it to a manual KR).
- Unlinking an OKR is not the same as [deleting](/cms_trial/space/SPM/1918408286/Delete+OKR/) it. If you unlink an OKR, you can link it again to the current or another box.

If there is an OKR in your box that is no longer relevant to your current work, you can hide it. Note that you can unlink only:

- OKRs that were created directly in the box
- OKRs that were linked manually
- KRs that are not linked to any work items ([unlink the work items](https://appfire.atlassian.net/wiki/spaces/SPM/pages/1918670410) or convert the [auto-KR](/cms_trial/space/SPM/1918670238/Auto-KR/) to a [manual KR](/cms_trial/space/SPM/1918702967/Manual+KR/) to unlink it from the box)

To unlink an OKR from a box:

1. On the [*Overview*](/cms_trial/space/SPM/1918834317/OKR+Overview/) page, click the **Link to box** button.
2. A screen with the available OKRs appears. Uncheck the OKRs you want to remove from the box.
3. Click **Save** to finish the process.