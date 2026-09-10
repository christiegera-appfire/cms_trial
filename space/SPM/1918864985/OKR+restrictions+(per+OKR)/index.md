# OKR restrictions (per OKR)

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

OKR restrictions add an extra layer of control for individual Strategic themes, Objectives, and Key Results (OKRs), allowing users to manage who can view and edit specific OKRs. There are two types of restrictions:

- **Visibility restriction** - Limits the visibility of an OKR to a specific group of users or teams.
- **Editing restriction** - Restricts editing capabilities, such as creating sub-items or linking Jira work items, to a selected group of users or teams.

It is important to note that restrictions on specific OKRs take precedence over general in-app and Jira permissions, providing a more granular level of access control.

See the video to learn more.

Video transcript

In a large enterprise, complete openness can quickly turn into operational chaos. When anyone can view or accidentally edit sensitive corporate strategies, you risk data corruption and premature exposure. As an enterprise leader, you don’t just need OKRs—you need governance.

OKR Restrictions in BigPicture help you solve this exact problem.

OKR restrictions serve as the top security layer, overriding all other existing OKR permissions.

They provide granular administrative control over your goal-setting ecosystem, allowing you to open restriction management to everyone or limit it strictly to designated individuals and teams.

Let’s see how it works.

First, you need to enable OKR restrictions in your OKR Settings in the General tab. Toggle the Allow Restricting OKRs option and choose whether you want to completely hide restricted OKRs from unauthorized users or leave them partially visible.

With this configuration active, you can seamlessly restrict both new and existing Strategic Themes, Objectives, and Key Results.

To restrict an existing OKR, open its details page.

Next, click the padlock icon in the upper right-hand corner. This opens a dedicated security configuration modal, where you can apply two distinct governance types based on your business requirements.

The first option is Anyone can view, specific people or teams can edit. Choose this to leave an OKR visible to all users for strategic alignment, while locking down modification rights to a select group.

The second option is Only specific people or teams can view or edit. Choose this to completely hide the OKR from the general directory. Only designated teams and specific users will be able to see or modify it.

In this example, the Objective we restricted has three child items. Because we restricted the parent OKR, the security settings were automatically inherited by all of its children.

Just like in the case of these OKRs.

When you inspect any of the child OKRs on their respective details pages, you will see that their restriction settings perfectly mirror the parent.

To change or remove inheritance restrictions from child OKRs, you must edit or delete them directly from the top-level parent OKR.

Let's go ahead and remove it.

The restrictions are now lifted from the parent... …and automatically cleared from all three children.

While restriction settings flow downwards from the top parent, you can still apply individual, unique restrictions to any specific child item.

Let’s restrict this single Key Result to Anyone can view, specific people or teams can edit.

Next, let's change the parent for this restricted Key Result.

Even though the Key Result is now nested under a different, unrestricted Objective, it securely retains its original individual restriction settings.

Restricting a new OKR works in a very similar way.

Right from the OKR creation screen, click the padlock icon and select your desired restriction type before saving.

Any child OKRs later created under this new Objective or Strategic Theme will automatically inherit these security settings from day one.

With OKR restrictions, you can ensure that your macro strategy remains cleanly insulated, your metric automation stays accurate, and your teams remain aligned to verified, approved targets.

## Allow restricting OKRs

The OKR module’s **Settings** are **global**—any changes you make also apply to the organization's settings.

Permitted users can restrict OKRs only when the **Allow restricting OKRs** feature is enabled on the **Settings** > **General** page. This feature is enabled by default.

You can choose to completely hide or partially show restricted OKRs.

In both cases, the progress of such OKRs will contribute to the completion of the parent OKR, while partial visibility lets you ensure that the progress of all top-level elements is coherent.

![General settings in the OKR module.](/cms_trial/assets/2efb1798-b2e5-47bc-bb5b-34945e5f4d79.png)

## Restrictions inheritance

- All existing and newly created child OKRs inherit the restriction from their parent.
- You can restrict individual child OKRs (considering their parent is not restricted. Otherwise, the child OKR will also be restricted).
- The restriction applies to all hierarchical descendants.
- Restrictions automatically update when you move an OKR to a new parent. If the new parent is unrestricted, the child will be unrestricted as well (unless the child was previously restricted individually). If the new parent is restricted, those same limits will immediately apply to the child.

Let’s say one of your OKRs has the following structure:

**Strategic theme** → **Objective** → **Key Result1**, **Key Result2**

Based on this setup, you can:

- Restrict only **Key Result1** and/or **Key Result2** (if the Strategic theme or Objective is not restricted).
- Restrict only the **Objective** (if the Strategic theme is not restricted). This action will also cause Key Result1 and Key Result2 to be restricted.

  ![A hierarchy of restricted OKRs.](/cms_trial/assets/7b54cce6-82bd-49b6-96ff-5915f0244c08.png)
- Restrict the **Strategic theme**. This action will also cause Objective, Key Result1, and Key Result2 to be restricted.

## Required permissions

OKR restrictions can be allowed and applied only by individuals with the required permissions. The permission configuration can be set on the **Settings** > [**Permissions page**](/cms_trial/space/SPM/1918765815/OKR+module+permissions/).

| **Permission** | **Who can restrict OKRs?** | **Who can restrict OKRs?** |
| --- | --- | --- |
| Full access | Everyone with this permission | Everyone with this permission |
| Global settings control | Selected users (with global settings permission) | Everyone with this permission |
| Editing control | Everyone with this permission | Selected users (with editing permission) |
| Global settings and editing control | Selected users (with global settings permission) | Selected users (with editing permission) |
| [Advanced setup](/cms_trial/space/SPM/1918767695/OKR+module+advanced+permissions/) | Users with admin roles or selected custom roles (with “Settings” permissions) | Selected users (with “Restrict chosen OKRs” permission) |

## Restrict an OKR

- If you want to restrict an existing OKR, go to its [**OKR detail page**](https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/1673724393/OKR+details+page?search_id=6353a544-ff22-4545-8f66-2040d9836863&additional_analytics=queryHash---ea7faa255dec6d7df3c4947162e52221c33182d6e35050a8b5d9e9d6ac4cf439) and click the **padlock icon**.

  ![Restrict OKR modal with all three restriction options listed in the dropdown.](/cms_trial/assets/9f55a2bb-a218-488d-b211-d22d67d1dc8c.png)
- If you want to restrict a new OKR, open the new OKR creation screen and click the **Restrict** button.

  ![Restrict OKR modal with all three restriction options listed in the dropdown.](/cms_trial/assets/fa9266e4-a8ba-4b91-9757-83e8eae3dfda.png)

1. A **Restrict OKR** modal displays. Select the restriction type:

   1. **Anyone can view and edit** (default state). This option does not introduce any restrictions.
   2. **Anyone can view, specific people or teams can edit**. This option allows all users and teams to view an OKR, but only selected users and teams can edit it.

      ![restrict-okr-anyone-view-selected-edit.png](/cms_trial/assets/57c7e537-8534-4c22-adec-c31271c87002.png)
   3. **Only specific people or teams can view or edit**. This option allows only selected users and/or teams to view and edit an OKR. Select users/teams and grant them either a **View** or an Edit permission.

      ![Only specific people or teams can view or edit option.](/cms_trial/assets/defb2f33-2cb5-44d9-acb0-9ec8e82b16ce.png)
2. **Save** to finish the process.

The restricted OKR is now marked with the **closed padlock icon**, indicating that it is restricted to some users.

If you restrict a parent OKR and open the restriction settings for a child OKR, a modal will display a message informing you that the parent OKR is already restricted. To change the child OKR’s restrictions, edit the restriction settings of the parent OKR.

![okr-restrictions-inherited.png](/cms_trial/assets/4d545e8c-0bf9-4ffb-aeef-cab20d4c0e9b.png)

## Permissions precedence

- Only users who were added to the restricted OKRs can see/edit that OKR. The **Administer data of OKRs for Jira** global permission or in-module admin permission **does not grant** the ability to view or edit Restricted OKRs.
- Contextual permissions for Owners and Collaborators do not override OKR restrictions.
- The **Administer data of OKRs for Jira** global permission overrides all in-module permissions, granting full module access (except for Restricted OKRs).