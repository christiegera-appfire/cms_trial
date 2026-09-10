# Link boxes to Key Results

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

Instead of linking multiple Jira work items to a Key Result individually, you can now organize them into a single box and link the entire box to the KR. As you add or remove tasks from the box, the KR’s progress will update automatically (for [auto-KRs](/cms_trial/space/SPM/1918670238/Auto-KR/) only) without the need to manually manage individual links.

Visit the Auto-KR page to learn how linked work items and linked boxes affect auto-KR’s progress.

- You can link boxes of any [box scope type](/cms_trial/space/SPM/1918766536/Scope+types/).
- If the task appears in multiple linked boxes, each duplicate task contributes to the Key Result's progress.
- Linked boxes help you visualize and track the work contributing to your Key Results. However, they can only affect the Key Result's progress when you convert a manual Key Result to an auto-KR.
- Linking a box to a Key Result is not the same as [linking an OKR to a box](/cms_trial/space/SPM/1918834116/Link+OKR+to+box/).

Below, you can find a video about linking boxes to a Key Result.

## Permissions

- To link a box to a particular KR, a user must be permitted to view or manage the box they want to link to.

  ![No permission or box not found on the Edit linked boxes screen.](/cms_trial/assets/7d486d4b-6df8-451d-9670-ffe01bfdadf9.png)
- Users who are not permitted to view or manage a linked box will not see it under the respective KR on the OKR Overview page.

## Link boxes to a new Key Result

1. Click the **Link boxes** button on the Key Result creation screen.

   ![Key Result creation screen. The Link boxes option is outlined.](/cms_trial/assets/73e7d6fd-031a-4e5e-bf3a-935736a87ade.png)

1. **Edit linked boxes** screen appears. Search for the boxes you want to link:

   ![Edit linked boxes screen.](/cms_trial/assets/cad85a01-803b-426d-9f2a-0d5cbf74af6c.png)

- **Search bar** - Use the search bar to search for a Jira space name.
- **Parent box** - Select a specific box from the list of available boxes.
- **Box type** - Narrow down the list of boxes by their box type.
- **Box status** - Narrow down the list of boxes by their status.

1. Check a box or boxes you want to link.

![Edit linked boxes screen with a couple of boxes checked.](/cms_trial/assets/4dd835ea-78bb-4953-bbd7-1121f8368052.png)

1. When you are happy with your results, click the **Save** button to finish the process.

The linked boxes appear under their respective Key Result.

To see the linked boxes on the OKR Overview page, you need to have the following options enabled:

- Global option: **Settings** > **General** > **Displaying connected boxes in the OKR Overview**
- Local (personal) option: **View** > **Connected boxes**

![A list of boxes under a KR on the OKR overview page.](/cms_trial/assets/c00bcf50-7efd-4301-bc35-99037a556df1.png)

## Add and manage boxes linked to an existing Key Result

You can add, change, or remove boxes you have already linked to a Key Result at any point by editing them.

1. Open the **Edit linked boxes** screen on one of the following:

   1. KR context menu:

      1. Open the [context menu](/cms_trial/space/SPM/1918407031/Navigation+and+interface+(OKR+module)/) for the KR you want to link a box to.
      2. Select **Edit linked boxes**.

         ![Screenshot of the Edit linked boxes button.](/cms_trial/assets/70a9d1c0-7406-4075-86da-3c04bf32e055.png)
   2. KR Details side panel:

      1. Select the Key Result to open its details side panel.
      2. Click **More actions** (**…**) and select **Edit linked boxes**.

         ![Screenshot of the Edit linked boxes button for an KR.](/cms_trial/assets/0ad9020e-9ac4-4952-ba2d-cb81d063bc0d.png)
   3. KR Details page:

      1. Open details for a KR you want to link a box to.
      2. Scroll to the **Linked work items & boxes** section at the bottom of the page.
      3. Click the **Edit linked boxes** button.

         ![Screenshot of the Edit linked work items and boxes section.](/cms_trial/assets/caf90cb6-fd3f-470a-b504-f49c1e4733f9.png)

1. On the **Edit linked boxes** screen:

   1. To link new boxes: Search for a specific box by its name, check it from the list, or show only the boxes of the specific scope type or box type (see steps 2-3 in the previous section).
   2. To change the boxes currently linked: Clear the boxes you want to unlink and check the ones you want to link.
   3. To remove all linked boxes: Clear all checked boxes.

      ![A list of linked boxes.](/cms_trial/assets/5263da75-4239-425d-b478-af771a9bf13f.png)
2. When you are happy with your results, click the **Save** button to finish the process.
3. The change in linked boxes is reflected in the OKR Overview under the respective Key Result.

## Limitations

- You can link either Jira work items or boxes to one KR.
- Linked boxes are not displayed in the Gantt module (even when the [Objective & Key Result structure builder](/cms_trial/space/SPM/1918863661/OKRs+as+task+structure+builders/) is active).