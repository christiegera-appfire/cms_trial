# Link boxes to Key Results

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

Instead of linking multiple Jira work items to a Key Result individually, you can now organize them into a single box and link the entire box to the KR. As you add or remove tasks from the box, the KR’s progress will update automatically (for auto-KRs only) without the need to manually manage individual links.

Visit the [Auto-KR](/cms_trial/space/SPM/1918670238/Auto-KR/) page to learn how linked work items and linked boxes affect auto-KR’s progress.

- You can link boxes of any [box scope type](/cms_trial/space/SPM/1918766536/Scope+types/).
- If the task appears in multiple linked boxes, each duplicate task contributes to the Key Result's progress.
- Linked boxes help you visualize and track the work contributing to your Key Results. However, they can only affect the Key Result's progress when you convert a manual Key Result to an auto-KR.
- Linking a box to a Key Result is not the same as [linking an OKR to a box](/cms_trial/space/SPM/1918834116/Link+OKR+to+box/).

Below, you can find a video about linking boxes to a Key Result.

## Permissions

- To link a box to a particular KR, a user must be permitted to view or manage the box they want to link to and have the **Link items to KRs** permission.

  ![No permission or box not found on the Edit linked boxes screen.](/cms_trial/assets/0c0c7691-8be2-45df-8b42-2189b960407b.png)
- Users who are not permitted to view or manage a linked box will not see it under the respective KR on the OKR Overview page.

## Link boxes to a new Key Result

1. Click the **Link boxes** button on the Key Result creation modal.
2. On the **Edit linked boxes** modal, use the available filters to find the boxes you want to link:

   ![Edit linked boxes screen.](/cms_trial/assets/22d45f03-cc4e-4df5-a5ee-e3156ceac5cf.png)

- **Search bar** - Use the search bar to search for a Jira space name.
- **Parent box** - Select a specific box from the list of available boxes.
- **Box type** - Narrow down the list of boxes by their box type.
- **Box status** - Narrow down the list of boxes by their status.

1. Check a box or boxes you want to link.
2. Click **Save** to finish the process.

The linked boxes appear under their respective Key Result.

![A list of boxes under a KR on the OKR overview page.](/cms_trial/assets/8086c328-ae15-410b-a402-ae4db4de77b6.png)

Cannot see your boxes on the Overview?

Check if you have the **View** > **Connected boxes** option enabled.

## Add and manage boxes linked to an existing Key Result

You can add, change, and remove boxes you have already linked to a Key Result at any point by editing them on the [*Overview*](/cms_trial/space/SPM/1918834317/OKR+Overview/) page (OKR details panel, context menu) and on the [*OKR Details*](/cms_trial/space/SPM/1918536390/OKR+details+page/) page.

1. Open the **Edit linked boxes** modal on one of the following:

   1. *Overview* page > context menu:

      1. Click **More actions** (**…**) next to the Key Result whose box links you want to edit.
      2. From the context menu, select **Edit linked boxes**.

         ![Prompting context menu for a Key Result. An arrow points at the Edit linked boxes option in the context menu.](/cms_trial/assets/11f6d5b5-030d-4611-ae64-6cb3f558398b.png)
   2. *Overview* page > KR Details side panel:

      1. Select the Key Result to open its details side panel.
      2. Click **More actions** (**…**) and select **Edit linked boxes**.

         ![OKR details panel. The menu is expanded and the arrow points at Edit linked boxes option.](/cms_trial/assets/ece8bd05-b210-4441-9c87-7dfa131769e7.png)
   3. *OKR Details* page:

      1. Open details for a KR you want to link a box to.
      2. Open the **Linked work** tab.
      3. In the **BigPicture boxes** section, click the **plus** button (**+**) to link, edit, or unlink a box; click **More actions** (**…**) next to the linked box and select **Unlink** to unlink it.

         ![BigPicture boxes expandable section on the OKR details page. The unlink option is visible.](/cms_trial/assets/fcf28bff-2fd6-43c5-956b-313eda0d7b8b.png)

1. The **Edit linked boxes** modal displays:

   1. To link new boxes: Search for a specific box by its name, check it from the list, or show only the boxes of the specific scope type or box type.
   2. To change the boxes currently linked: Clear the boxes you want to unlink and check the ones you want to link.
   3. To remove all linked boxes: Clear all checked boxes.

      ![A list of linked boxes.](/cms_trial/assets/1c28d569-b128-41fc-a036-a328965b3f66.png)
2. Click **Save** to finish.

## Limitations

- You can link either Jira work items or boxes to one KR.
- Linked boxes are not displayed in the Gantt module (even when the [Objective & Key Result structure builder](/cms_trial/space/SPM/1918863661/OKRs+as+task+structure+builders/) is active).