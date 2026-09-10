# Link work items to Key Results

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

Linking specific tasks to Key Results (KRs) is an effective way to ensure alignment and clarity that every effort contributes meaningfully to achieving Objectives. It also lets you track KR progress based on the status of linked work items/tasks.

In the OKR module, you can associate Key Results with Jira work items and boxes.

Visit the [Auto-KR](/cms_trial/space/SPM/1918670238/Auto-KR/) page to learn how linked work items and linked boxes affect auto-KR’s progress.

- Linked work items help you visualize and track the work contributing to your Key Results. However, they do not directly affect the Key Result's progress (unless you convert your KR to auto-KR).
- You can add multiple work items to one Key Result and one work item to multiple Key Results. However, the task hierarchy in the Gantt module built using the [Objective & Key Result structure builder](/cms_trial/space/SPM/1918863661/OKRs+as+task+structure+builders/) works correctly only when you link one work item to each Key Result. Work items assigned to multiple Key Results appear only once.

## Permissions

- To link a work item to a particular KR, a user needs to be permitted to view or manage the item they want to link.
- Users who are not permitted to view or manage a linked work item will not see it under the respective KR on the OKR Overview page.

## Link existing work items to KRs

You can link a work item to a KR on the [*OKR Details*](/cms_trial/space/SPM/1918536390/OKR+details+page/) page and on the [KR creation](/cms_trial/space/SPM/2324726248/Create+OKR/) screen.

### OKR Details page

1. Scroll down to the **Linked work items** section.
2. Click the **Edit linked work items** button.

   ![Screenshot of the Key Result details page.](/cms_trial/assets/579656c3-3f36-4778-a691-2b2eb109b1c6.png)
3. On the **Edit linked work items** screen, select a work item you want to link to a KR in the following ways:

- Search for a work item manually using the search bar and Jira dropdowns (Project, work item Type, etc.).
- Set up automation rules to link related work items to OKRs automatically when specific conditions are met. For example, you can link work items within a specific Epic, and any new work items added to that Epic will also be automatically linked to the KR.

  ![Screenshot of Edit linked work items window.](/cms_trial/assets/365164ca-828f-4e18-84a7-e22b52523aa1.png)
- Type a JQL query to find a specific work item.

1. Click **Save** to complete the process.

For the same Key Result, you can use both specific work item linking and automated linking. This applies to Key Results with either automatic or manual progress tracking.

### Key Result creation screen

1. Click **Link work items**.
2. The **Edit linked work items** screen displays. Select a work item you want to link to a KR in the following ways:

- Search for a work item manually using the search bar and Jira dropdowns (Project, work item Type, etc.).
- Set up automation rules to link related work items to OKRs automatically when specific conditions are met. For example, you can link work items within a specific Epic, and any new work items added to that Epic will also be automatically linked to the KR.
- Type a JQL query to find a specific work item.

1. Click **Link work items**, then **Save** to complete the process.

## Link new work items to Key Results

### On the Key Result details side panel

1. Click **More options** (**…**) and select **Create new work item**.
2. Enter the Jira work item details.
3. Click **Create** tocomplete the process.

### On the Key Result details page

1. Scroll down to the **Linked work items** section.
2. On the **Edit linked work items** screen, click **Create work item**.

   ![Screenshot of the Create work item button in the Edit linked work items window.](/cms_trial/assets/4503c14d-ca5d-44f8-b453-9353aa860b0c.png)
3. Enter Jira work item details.
4. Click **Create**, then **Save** to complete the process.

## Limitations

- You can link either Jira work items or boxes to one KR.

## Edit work items linked to a Key Result

Changing tasks associated with Key Results is often done to ensure the project or portfolio stays on track and continues to move towards its goals as efficiently as possible. There can be several reasons for this:

- If the project or organizational priorities shift, certain tasks may no longer align with the overall goal, so they’d need to be updated to reflect the new focus.
- Tasks that were originally planned might prove to be more difficult or time-consuming than anticipated.
- As the project progresses, new information or insights might surface that suggest a better way to achieve the expected results.
- If available resources change, tasks might need to be adjusted to reflect what is feasible under the new constraints.
- Feedback from team members, clients, or other stakeholders can reveal that certain tasks are not working well or are less impactful than originally thought.
- If there’s a more streamlined way to reach the expected outcome, you might alter tasks accordingly.

## Edit linked work items

You can edit which work items are linked to auto-KRs and manual KRs.

Even though you update manual KRs by editing the linked work items, you still add them to the KR. Consequently, if you want the progress of the manual KR to be calculated based on the work items you just linked, do not forget to [convert it to an auto-KR](/cms_trial/space/SPM/1918670238/Auto-KR/).

You can edit linked work items on the [OKR details side panel](/cms_trial/space/SPM/1918865686/OKR+Details+side+panel/) and the *OKR details* page.

### OKR details panel

1. Select the KR to open its details side panel.
2. Click **More actions** (**…**).
3. From a dropdown, select **Edit linked work items**.

   ![Screenshot of the Edit linked work items button.](/cms_trial/assets/63165404-943c-420b-a81e-6144356bec85.png)

1. The **Edit linked work items** screen displays. Add/remove the linked work items.
2. **Save** to finish the process.

### OKR details page

1. Open the *OKR details* page and go to the **Linked work items** section.
2. Click the **Linked work items** button.

   ![Screenshot of the Edit linked work items button.](/cms_trial/assets/3942a44d-22c9-45da-b8c4-c98be2416ea1.png)

1. The **Edit linked work items** screen displays. Add/remove the linked work items.
2. **Save** to finish the process.