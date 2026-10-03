# Link work items to Key Results

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

Linking specific tasks to Key Results (KRs) is an effective way to ensure alignment and clarity that every effort contributes meaningfully to achieving Objectives. It also lets you track KR progress based on the status of linked work items/tasks.

In the OKR module, you can associate Key Results with Jira work items and boxes.

Visit the [Auto-KR](/cms_trial/space/SPM/1918670238/Auto-KR/) page to learn how linked work items and linked boxes affect auto-KR’s progress.

- Linked work items help you visualize and track the work contributing to your Key Results. However, they do not directly affect the Key Result's progress (unless you convert your KR to auto-KR).
- You can add multiple work items to one Key Result and one work item to multiple Key Results. However, the task hierarchy in the Gantt module built using the [Objective & Key Result structure builder](/cms_trial/space/SPM/1918863661/OKRs+as+task+structure+builders/) works correctly only when your work item is linked to one Key Result. Work items assigned to multiple Key Results appear only once.

## Permissions

- To link a work item to a particular KR, a user needs to be permitted to view or manage the item they want to link. They also need the **Link items to KRs** permission.
- Users who are not permitted to view or manage a linked work item will not see it under the respective KR on the OKR Overview page.

## Link work items to KRs

You can add, change, and remove work items you have already linked to a Key Result at any point by editing them on the [*Overview*](/cms_trial/space/SPM/1918834317/OKR+Overview/) page (OKR details panel, context menu) and on the [*OKR Details*](/cms_trial/space/SPM/1918536390/OKR+details+page/) page.

1. Open the **Edit linked work items** modal on one of the following:

   1. *OKR Details* page:

      1. Go to the **Linked work** tab.
      2. In the **Jira work items** section, click the **Link work item** (**+**) button or **+Add** if the KR has no items linked yet.

         ![The Linked work tab on the Strategic theme details page.](/cms_trial/assets/2b144a2d-496d-435e-ad3b-1cd0aa289e10.png)
   2. *Overview* page > OKR Details side panel:

      1. Click **More actions** (…).
      2. Select **Edit linked work items** from the dropdown.

         ![A dropdown on the OKR Details side panel.](/cms_trial/assets/24a14f24-c3df-4533-8959-6d02bc52c169.png)

1. 1. *Overview* page > context menu:

      1. Click **More actions** (…) next to the KR you want to add or edit work items for.
      2. From the context menu, select **Edit linked work items**.

         ![Edit linked work items on the Overview page.](/cms_trial/assets/3e08e635-9003-44f2-93cb-0b15be9129c5.png)
2. The **Edit linked work items** modal displays. Select a work item you want to link to a KR in the following ways:

   1. **Select manually** from the filtered list:

      1. Search for a work item manually using the search bar and Jira dropdowns/filters (**Project**, **Work item Type**, **Parent**). Click **+More** to access more filters.
      2. From the list, check/uncheck the items you want to link/unlink.
      3. Click **Save**.

         ![Edit linked work items window.](/cms_trial/assets/6d32c2e4-63ff-4b9d-99ca-9e5aa40e1958.png)
   2. **Select manually** from the list returned by JQL:

      1. Switch to **JQL** mode and type your JQL clause to pinpoint a specific item or items.
      2. Click **Search**.
      3. From the list, check/uncheck the items you want to link/unlink.
      4. Click **Save**.

         ![Select manually in the JQL mode.](/cms_trial/assets/7f3e9460-3f87-4482-9062-665c86b0662c.png)
   3. **Automated linking** of items from the filtered list:

      1. Set up automation rules to link related work items to OKRs automatically when specific conditions are met. For example, you can link a specific work item type (e.g., an Epic) from a specific space or spaces. Any new Epics added to that space/spaces will also be automatically linked to the KR.

         ![auto-link-list.png](/cms_trial/assets/134d23f3-9995-4b9b-83e0-981b6d6d7bea.png)
   4. **Automated linking** of items based on JQL:

      1. Switch to **JQL** mode and type your JQL clause to pinpoint a specific item or items. When a new work item meets the JQL criteria, the app automatically adds it to the KR.

         ![Automated linking in JQL mode.](/cms_trial/assets/b05e7d5f-3a61-406b-befc-ed36b547bb7b.png)
3. Click **Save** to finish.

For the same Key Result, you can use manual and automated work item linking. This applies to Key Results with either automatic or manual progress tracking.

Cannot see your work items on the Overview?

Check if you have the **View** > **Connected boxes** option enabled.

## Link new work items to Key Results

On the **Edit linked work items** screen, you can additionally create new Jira work items using the **Create work item** button. When you create an item, it becomes automatically linked to the KR you are currently viewing.

![The Create work item button in the Edit linked work items window.](/cms_trial/assets/3825c556-ecdf-4510-85b9-0bf26f262172.png)

## Limitations

- You can link either Jira work items or boxes to one KR.
- The app displays up to 50 work items per KR.