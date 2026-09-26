# Move box in box hierarchy

## BMove a box in a box hierarchy (old navigation)

Click to expand the guide

You can move a project box and place it under another one. This action changes the box’s position in the hierarchy and gives it a new parent.

## Move a box

1. Go to the Overview module on the root, program, or portfolio level (depending on the location of the box you want to move)
2. Grab a box you want to move and drop it under a new parent. If you select a parent box, all its sub-boxes will be highlighted to indicate the boxes that will be moved together with a parent.

![Nesting one box under another.](/cms_trial/assets/17600610-059c-44c2-87b9-fe8cb8b844cb.mp4)

## Change in the hierarchy - validation error

If a selected box cannot be moved under a specific parent box, you will see a validation error.

The app verifies if the new parent box's current scope settings are compatible with the sub-box and checks the box type parent settings. You must have sufficient permissions in both boxes (parent and child) to move a box.

## Validation rules

The box-moving operation depends on:

- Security roles
- Box type configuration, you decide the possible parents of each box type. [Parent box types](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298289300) determine how to build the box hierarchy (nest boxes) and prevent users from making mistakes and mixing methodologies.
- Each box type has scope type settings (None, Own scope, Sub-scope).
- Sequentiality (box type settings)
- [box period mode](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297636248)
- Box status (under a "closed" box, you can place only other "closed" boxes)

### Security and access

You need sufficient security role permissions in both the box that is being moved and the box that will become the new parent in the hierarchy.

- You have to be an Admin of the box being moved (remember, since roles are inherited, if you are an Admin in an upper-level box, you are automatically an Admin of all sub-boxes lower in the hierarchy).
- The App admin has full permissions in all boxes and can perform the action.
- In the new upper-level (parent) box, you must be an Admin or a sub-box creator (once again, the Admin role can be inherited from an upper-level box; the sub-box creator role is not inherited).

For example, Paul is an Admin of "ALFA" but only an Editor of "OMEGA." He will not be able to move "ALFA" and nest it under "OMEGA" - his current set of permissions is insufficient.

![A home screen showing that some boxes are not visible, indicating the lack of security access.](/cms_trial/assets/5dd30a35-eaef-4c86-b2b5-791440384bfc.png)

### Parent Types

Remember to adjust [possible parents](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spmdraft&title=Basics%20%28box%20types%29&linkCreation=true&fromPageId=1811022333) for each box type. If the list of possible parents doesn't allow the change, you won't be able to move a box. Settings of a box type have to allow for a new parent relationship.

![Box type configuration page.](/cms_trial/assets/44f08a0c-4fde-497b-97b7-34f3f64f4554.png)

For example, Drew is an App admin, so he has full Admin access to all boxes. However, when he tries to place the "ALFA" box in "OMEGA," he can't do it. "ALFA" is an "Agile Project" box type and can't be placed under "OMEGA" (the "Program" box type).

![Box type column on the home screen.](/cms_trial/assets/6e3cab8c-6ae9-40a0-84f4-4a151e74bf8a.png)

For this move to be possible, a new parent would have to be added for the "Agile Project" box type.

![Adding a new parent box type on the box type configuration page.](/cms_trial/assets/6036a247-bb18-46e1-801e-9b6c6a79a70e.png)

### Box status

Under a "Closed" parent box, you can place only other "Closed" boxes.

|  | **parent "Not started"** | **parent "In progress"** | **parent "Closed"** |
| --- | --- | --- | --- |
| child "Not started" | YES | YES | NO |
| child "In progress" | YES | YES | NO |
| child "Closed" | YES | YES | YES |

### Scope Types

In general, if moving a box would drastically impact its scope, the change will not be permitted. This means that boxes with the "Sub-scope" cannot be moved in the hierarchy, as their scope depends entirely on their parent; all work done in boxes with "Sub-scope" is intrinsically tied to the upper-level box. boxes that utilize the "Sub-scope" have to be created directly where you intend to use them.

Under boxes with "None" scope, you can place:

- other boxes with "None" scope
- boxes with "Own" scope

Under boxes with "Own" scope, you can place:

- boxes with "None" scope
- other boxes with "Own scope"

Take a look at the matrix below to see what kinds of changes are possible:

![child-parent.png](/cms_trial/assets/8baac1f6-b11f-4d0f-8f19-c7118a62bd9f.png)

The scope type is set during box creation. It is based on the box type settings and can't be changed afterward.

![Scope definition page on the box type configuration page.](/cms_trial/assets/be8070a0-bbc5-4d49-a2a9-3ac92d77a35a.png)

For example, the "Program Increment" box type is set to have a "Sub-scope." If Jessica tries to move a "Program Increment 4" from one box to another, she will receive an error.

![Moving a sub-box validation error.](/cms_trial/assets/55b67f7e-cfb8-4f9a-a9ac-809c5844b5ff.png)

## Sequentiality

Sequentiality settings affect same-level boxes (can potentially prevent box periods from overlapping).

**Auto bottom-up** and **auto scope-based** boxes are never sequential - they can always overlap.

Only "**manual**" and "**auto top-down**" boxes can be sequential—if set to 'sequential,' sequential boxes at the same level can't overlap.

![Box sequentiality validation error.](/cms_trial/assets/a3541ade-08a3-41da-8c4d-e05b5e420193.png)

### Period mode

[Box type period mode](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spmdraft&title=Advanced%20%28Box%20types%29&linkCreation=true&fromPageId=1811022333) can affect if a new child box can be created with a specified start/date.

#### Period of a box vs period mode of its sub-boxes

boxes in an "auto bottom-up" period mode are affected by the period of their sub-boxes (regardless of a sub-box period mode).

#### Period of a box vs period mode of its parent

- **An "auto top-down" parent** →

  - **limits the period of an "auto top-down" child box**
  - child boxes in "manual"/ "auto scope-based" period mode are not affected
  - "auto bottom-up" child overrides an "auto top-down" parent

Effects of the parent box period mode on a child box period are outlined in the table below.

| **Parent box →** | **box period** |
| --- | --- |
| auto bottom-up | unaffected (regardless of child period mode) |
| auto scope-based | unaffected (regardless of child period mode) |
| auto top-down | **An "auto top-down" parent limits the period of an "auto top-down" child**  Period of an "auto bottom-up" child unaffected ("auto bottom-up" child has priority over an auto "top-down parent")  Periods of "manual" and "auto scope-based" boxes unaffected |
| manual | unaffected (regardless of child period mode) |

#### Bulk Move

You can use the multi-select function to move multiple boxes simultaneously. Validation is performed for each box - if any of the boxes can't be moved, the entire operation fails, and no boxes are moved. In other words, the system will either successfully move all the boxes or none at all.

![Bulk moving boxes on the home screen.](/cms_trial/assets/c486640c-5311-49d4-bb3a-5565c6e2796b.png)

[Unmapped block: nestedExpand]

If any of the boxes can't be moved, the entire operation fails (no boxes will be moved), regardless of which validation check failed.

For example, the "CUSTOM" box type can't be placed under "Portfolio."

![custom-basics.png](/cms_trial/assets/9c22d72a-47e3-41a4-922d-79d112f1eceb.png)![portfolio-types.png](/cms_trial/assets/b7f3a10c-070e-46ff-8209-bf75f7b9e6e8.png)![id-validation-error.png](/cms_trial/assets/c2367aa3-01ab-4c53-894f-a5cd6d179302.png)

## Move a box in a box hierarchy (new navigation)

Click to expand the guide

You can move a project box and place it under another one. This action changes the box’s position in the hierarchy and gives it a new parent.

## Move a box

1. Go to the Overview module and open the Main box.
2. Grab a box you want to move and drop it under a new parent. If you select a parent box, all its sub-boxes will be highlighted to indicate the boxes that will be moved together with a parent.

![Nesting one box under another.](/cms_trial/assets/f45f76b9-de5f-4d16-bd44-38333d7f3c74.mp4)

## Change in the hierarchy - validation error

If a selected box cannot be moved under a specific parent box, you will see a validation error.

The app verifies whether the new parent box's current scope settings are compatible with the sub-box and checks the parent settings for the box type. You must have sufficient permissions in both boxes (parent and child) to move a box.

## Validation rules

The box-moving operation depends on:

- Security roles
- Box type configuration, you decide the possible parents of each box type. [Parent box types](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298289300) determine how to build the box hierarchy (nest boxes) and prevent users from making mistakes and mixing methodologies.
- Each box type has scope type settings (None, Own scope, Sub-scope).
- Sequentiality (box type settings)
- [Box period mode](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297636248)
- Box status (see the **Box status** section on this page)

### Security and access

You need sufficient security role permissions in both the box that is being moved and the box that will become the new parent in the hierarchy.

- You have to be a Box Admin of the box you want to move (because roles are inherited, being an Admin in an upper-level box automatically grants you Admin status for all sub-boxes lower in the hierarchy).
- The App Admin has full permissions in all boxes and can perform the action.
- In the new upper-level (parent) box, you also must be a Box Admin or a Sub-box Creator (again, the Admin role can be inherited from an upper-level box; the Sub-box Creator role is not inherited).

### Parent Types

Remember to adjust [possible parents](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spmdraft&title=Basics%20%28box%20types%29&linkCreation=true&fromPageId=1811022333) for each box type. If the list of possible parents doesn't allow the change, you won't be able to move a box. You need to allow for a new parent relationship in the box type settings.

For example, say you are a Box Admin of the “New mobile app” Agile project box. However, when you attempt to move that Agile box under the “New program” Program box, you receive a validation error.

![Validation error.](/cms_trial/assets/26799216-d9b6-4504-8647-ba58c81270cd.png)

For this move to be possible, you need to add **Program** as the new parent type in the Agile Project box type.

![Agile project box type settings.](/cms_trial/assets/79b5cda6-5145-40b0-a40a-81fdc061070a.png)

### Box status

|  | parent box status: **Not started** | parent status: **In progress** | parent status: **Closed** |
| --- | --- | --- | --- |
| child box status: **Not started** | YES | YES | NO |
| child box status: **In progress** | YES | YES | NO |
| child box status: **Closed** | YES | YES | YES |

### Scope types

In general, if moving a box would drastically impact its scope, the change will not be permitted. This means that boxes with the **Sub-scope** cannot be moved in the hierarchy, as their scope depends entirely on their parent; all work done in boxes with **Sub-scope** is intrinsically tied to the upper-level box. boxes that utilize the **Sub-scope** have to be created directly where you intend to use them.

You can place the following box scope types under boxes with the **None** scope:

- other boxes with the **None** scope
- boxes with the **Own** scope

You can place the following box scope types under boxes with the **Own** scope:

- boxes with the **None** scope
- other boxes with the **Own** scope

Take a look at the matrix below to see what kinds of changes are possible:

![child-parent.png](/cms_trial/assets/8baac1f6-b11f-4d0f-8f19-c7118a62bd9f.png)

The scope type is set during box creation. It is based on the box type settings and can't be changed afterward.

![Scope types for the Program Increment box type.](/cms_trial/assets/109a707e-6b76-4ca1-be25-6deb6d387247.png)

For example, say you have set the Program Increment box type to a **Sub-scope**. If you then try to move a Program Increment box from one parent box to another, you will receive an error.

## Sequentiality

Sequentiality settings affect same-level boxes (which can potentially prevent box periods from overlapping).

- **Auto bottom-up** and **auto scope-based** boxes are never sequential; they can overlap.
- Only **manual** and **auto top-down** boxes can be sequential
- **Sequential** boxes at the same level cannot overlap.

![Box sequentiality validation error.](/cms_trial/assets/a3541ade-08a3-41da-8c4d-e05b5e420193.png)

### Period mode

[Box type period mode](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spmdraft&title=Advanced%20%28Box%20types%29&linkCreation=true&fromPageId=1811022333) can affect whether a new child box can be created with a specified start/date.

#### Period of a box vs period mode of its sub-boxes

Boxes in the **auto bottom-up** period mode are affected by the period of their sub-boxes (regardless of the sub-box period mode).

#### Period of a box vs period mode of its parent

- An **auto top-down** parent →

  - limits the period of the **auto top-down** child box
  - the **manual** or **auto scope-based** child boxes are not affected
  - an **auto bottom-up** child box overrides an **auto top-down** parent

The effects of the parent box period mode on the child box period are outlined in the table below.

| **Parent Box →** | **New Box (child)** |
| --- | --- |
| Auto bottom-up | Unaffected (regardless of the child's period mode) |
| Auto scope-based | Unaffected (regardless of the child’s period mode) |
| Auto top-down | - An **auto top-down** parent limits the period of an **auto top-down** child. - The period of an **auto bottom-up** child is unaffected (an **auto bottom-up** child has priority over an **auto top-down parent**). - Periods of the **manual** and **auto scope-based** boxes are unaffected. |
| Manual | Unaffected (regardless of child period mode) |

#### Bulk move

Just like with tasks, you can use the [multi-select](/cms_trial/space/SPM/1918832779/Multiselect+tasks/) feature to move multiple boxes at once. Validation is performed for each box; if any box can't be moved, the entire operation fails, and no boxes are moved. In other words, the system will either successfully move all the boxes or none at all.

For example, say you created a Portfolio box using the Portfolio box type. If you want to move an Agile Project and Program boxes under a Portfolio box, you will be able to do it. That’s because the Portfolio box is the None scope box type, while the Agile and Program boxes were created with the Own scope. In such a case, you can select both and place them under the portfolio.

If you want to move multiple boxes and at least one of those boxes cannot be moved, the entire operation fails (no boxes will be moved), regardless of which validation check has failed.