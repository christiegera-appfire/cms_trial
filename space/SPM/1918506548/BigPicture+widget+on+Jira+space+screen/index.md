# BigPicture widget on Jira space screen

## BigPicture widget on Jira project screen (old navigation)

The App widget allows access to the app directly from a Jira project.

![Screenshot of the BigPicture widget from the Jira project's context.](/cms_trial/assets/34ceb294-69f5-41a5-96c5-b654ce130027.png)

## Preconditions

Creating a matching box is allowed when a user meets the combination of the two permission conditions:

- The user must have permission to create boxes under the root box in BigPicture (App admin or sub-box creator).
- The user is a Jira admin or Jira project admin.

You can use BigPicture directly from the Jira project screen when the relationship between a box and a Jira project is simple - the scope of a box is the exact match to a project, and only the project (no other filters, boards, or projects are in scope. The **Narrow down** option is allowed.

![Screenshot of the Scope definition page in the BigPicture widget.](/cms_trial/assets/e8c3e7b7-6f6f-4db1-996f-2d1699614e82.png)

When the **own** scope box is a perfect match, child boxes with **sub-scope** can also be managed directly from Jira.

Boxes that do not meet the preconditions (aren't a match for a project) are not shown in the box switcher (unless they are sub-boxes of a matching box).

A project can potentially be in multiple boxes with this simple matching setup.

![Screenshot of the box switcher in the BigPicture widget.](/cms_trial/assets/ded82eda-4770-4edd-a6eb-7ed5dcad5a0b.png)

## Access existing boxes

To access existing boxes:

1. Go to a Jira project page.
2. Click the App icon on the left.
3. The App view will be displayed if a matching box is found.

A project, or even part of the project, can be in more than one box. Only the simple 1:1 matches are detected; therefore, if some tasks are in a box with a more complex scope definition, you may not be aware of this fact.

A simple match will be shown. When no simple direct matches are found, you are presented with a screen to create a box.

![Screenshot of the BigPicture widget from the Jira project's context.](/cms_trial/assets/34ceb294-69f5-41a5-96c5-b654ce130027.png)

### Context

The Box switcher is at the top. It lets you navigate the box structure, including sub-boxes.

![Screenshot of the box switcher in the BigPicture widget.](/cms_trial/assets/805109da-1695-48e3-ad49-a78090b85d51.png)

### Modules and operations

You can access the full module directly from a Jira project page. Use the module dropdown to switch between modules.

![Screenshot of the module switcher in the BigPicture widget.](/cms_trial/assets/caafb18c-0905-4527-8faf-cdb27a5d7af1.png)

## Create a box

To create a box, you must have sufficient permissions within the App.

If a perfect match box already exists, you won't be allowed to create one.

If no perfect match box has been detected for a project, you are given the possibility to create it:

- New box name = project name.
- Nested directly under the home (root) box in the App (you can later move it if needed).

![Screenshot of the box creation window in the BigPicture widget.](/cms_trial/assets/b98e2659-32aa-4022-953c-2561a2b0d994.png)

Select a box type - available options depend on your box type setup (read more about [box types](/cms_trial/space/SPM/1918830000/Box+types/)).

When you click a box type, you will see the list of modules that will be automatically active (you can change those settings later).

Click **Start working**to create a perfect match box.

![Screenshot of the chosen template in the BigPicture widget.](/cms_trial/assets/fe888d0c-c307-441b-b61f-53ee0848cf18.png)

The box is ready. You can create timeboxes to subdivide the scope further and change the box configuration to best suit your needs.

![Screenshot of the newly-created box in the BigPicture widget.](/cms_trial/assets/96cf6f63-a862-41fa-86bd-a08c47dfcc95.png)

### Conditions

Requirements for box types used to create a matching box in the context of a Jira Project:

- **Own scope box** - Sub-scope and "none" scope boxes can't be created using this method.
- It can be created under the root (parent box set as root) - Box type settings > General > Basics related to **parent types** have to allow for a **main** box type to be a parent.
- Sequentiality set as **overlapping allowed**. See more on the Advanced (Box types) page.

## Go to BigPicture

To go to BigPicture:

1. Click the BigPicture icon at the top left to be taken to the App. You will be taken to the Home Box (Root Box).

   ![Screenshot of the App icon in the BigPicture widget.](/cms_trial/assets/8579aa17-57e8-49a0-b9cd-b9fa16d8c180.png)
2. Use the box switcher to go directly to a selected box (right-clicking an item opens a box link in a new tab, for example).

   ![Screenshot of opening the box from the BigPicture widget in a new tab.](/cms_trial/assets/b7d72498-4ecf-4a0d-a158-def876f0dc45.png)

## Troubleshooting

### A new box can't be created

If you want to create a box using a particular box type and can't find it on the list of available options, box type settings don't meet one or more of the conditions outlined above.

### Missing permissions

Make sure to verify the App and box permissions and roles.

## BigPicture widget on Jira space screen (new navigation)

The App widget provides direct access to the app from a Jira space screen.

![Screenshot of the BigPicture widget from the Jira space context.](/cms_trial/assets/df2fed81-22b3-4695-9843-63e32f70392f.png)

## Preconditions

Creating a matching box is allowed when a user meets the combination of the two permission conditions:

- The user must have permission to create boxes under the root box in BigPicture (App Admin or sub-box creator).
- The user is a Jira admin or Jira project admin.

You can use BigPicture directly from the Jira project screen when the relationship between a box and a Jira project is simple - the scope of a box is the exact match to a project, and only the project (no other filters, boards, or projects are in scope. The **Narrow down** option is allowed.

When the **own** scope box is a perfect match, child boxes with **sub-scope** can also be managed directly from Jira.

Boxes that do not meet the preconditions (aren't a match for a project) are not shown in the box switcher (unless they are sub-boxes of a matching box).

## Access existing boxes

To access existing boxes:

1. Go to a Jira space page.
2. Click the BigPicture icon (**BigPicture App entry**) under **More**.
3. The App view will be displayed if a matching box is found.

A Jira space, or even part of the space, can be in more than one box. Only the simple 1:1 matches are detected; therefore, if some tasks are in a box with a more complex scope definition, you may not be aware of this fact.

A simple match will be shown. When no simple direct matches are found, you are presented with a screen to create a box.

![Acessing app widget in Jira.](/cms_trial/assets/c31e58ce-0c20-4f6d-beac-f5e0e57203ee.png)

### Context

The Box switcher is at the top. It lets you navigate the box structure, including sub-boxes.

![Box switcher in thr app widget.](/cms_trial/assets/8df9e1c5-d351-4a52-8764-4a63052294fc.png)

### Modules and operations

You can access the full module directly from a Jira space page. Use the module dropdown to switch between modules.

![Modules menu in the App widget in Jira.](/cms_trial/assets/b6235375-fa2d-4cf5-929e-7c87a7c067e2.png)

## Create a box

To create a box, you must have sufficient permissions within the App.

If a perfect match box already exists, you won't be allowed to create one.

If no perfect match box has been detected for a project, you are given the possibility to create it:

- New box name = project name.
- Nested directly under the home (root) box in the App (you can later move it if needed).

![App widget displays a screen where a user can create a matching box.](/cms_trial/assets/5b59ca47-7fcc-4f75-9a0a-c8c04b474307.png)

Select a box type - available options depend on your box type setup. Only own scope boxes can be selected.

When you click a box type, you will see the list of modules that will be automatically active (module settings can be changed after a box has been created).

Click **Start working**to create a perfect match box.

The box is ready. You can create timeboxes to subdivide the scope further and change the box configuration to best suit your needs.

### Conditions

Requirements for box types used to create a matching box in the context of a Jira space:

- **Own scope box** - The sub-scope and the none-scope boxes can't be created using this method.
- It can be created under the root (parent box set as root) - **Box type settings** > **General** > **Basics** related to **parent types** have to allow for a **main** box type to be a parent.
- Sequentiality is set as **overlapping allowed**.

## Go to BigPicture

To go to BigPicture:

1. Click the BigPicture icon at the top left to be taken to the app. You will be taken to the Home box.

   ![BigPicture logo in the app widget.](/cms_trial/assets/7811cbef-8b28-48dc-95cd-83e0e966dd3e.png)
2. Use the box switcher to go directly to a selected box; right-click a box name link and open it in a new browser tab.

## Troubleshooting

### A new box can't be created

If you want to create a box using a particular box type and can't find it on the list of available options, box type settings don't meet one or more of the conditions outlined above.

### Missing permissions

Make sure to verify the app and box permissions and roles.