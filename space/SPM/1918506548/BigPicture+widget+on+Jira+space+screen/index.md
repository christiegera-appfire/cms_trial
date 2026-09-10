# BigPicture widget on Jira space screen

## BigPicture widget on Jira project screen (old navigation)

The App widget allows access to the app directly from a Jira project.

![Screenshot of the BigPicture widget from the Jira project's context.](/cms_trial/assets/c5e80540-a358-42b2-b67c-ccf0f6441641.png)

## Preconditions

Creating a matching box is allowed when a user meets the combination of the two permission conditions:

- The user must have permission to create boxes under the root box in BigPicture (App admin or sub-box creator).
- The user is a Jira admin or Jira project admin.

You can use BigPicture directly from the Jira project screen when the relationship between a box and a Jira project is simple - the scope of a box is the exact match to a project, and only the project (no other filters, boards, or projects are in scope. The **Narrow down** option is allowed.

![Screenshot of the Scope definition page in the BigPicture widget.](/cms_trial/assets/2a6e6c3e-de2a-491b-8e75-4affe0db99da.png)

When the **own** scope box is a perfect match, child boxes with **sub-scope** can also be managed directly from Jira.

Boxes that do not meet the preconditions (aren't a match for a project) are not shown in the box switcher (unless they are sub-boxes of a matching box).

A project can potentially be in multiple boxes with this simple matching setup.

![Screenshot of the box switcher in the BigPicture widget.](/cms_trial/assets/0628b418-5374-497b-bde5-204d8bf84d32.png)

## Access existing boxes

To access existing boxes:

1. Go to a Jira project page.
2. Click the App icon on the left.
3. The App view will be displayed if a matching box is found.

A project, or even part of the project, can be in more than one box. Only the simple 1:1 matches are detected; therefore, if some tasks are in a box with a more complex scope definition, you may not be aware of this fact.

A simple match will be shown. When no simple direct matches are found, you are presented with a screen to create a box.

![Screenshot of the BigPicture widget from the Jira project's context.](/cms_trial/assets/c5e80540-a358-42b2-b67c-ccf0f6441641.png)

### Context

The Box switcher is at the top. It lets you navigate the box structure, including sub-boxes.

![Screenshot of the box switcher in the BigPicture widget.](/cms_trial/assets/6e078fec-49a2-407c-be35-12cdb4aadb11.png)

### Modules and operations

You can access the full module directly from a Jira project page. Use the module dropdown to switch between modules.

![Screenshot of the module switcher in the BigPicture widget.](/cms_trial/assets/23f54543-d509-48ce-b888-a748267b1ec2.png)

## Create a box

To create a box, you must have sufficient permissions within the App.

If a perfect match box already exists, you won't be allowed to create one.

If no perfect match box has been detected for a project, you are given the possibility to create it:

- New box name = project name.
- Nested directly under the home (root) box in the App (you can later move it if needed).

![Screenshot of the box creation window in the BigPicture widget.](/cms_trial/assets/95d2275c-6344-4370-a5ae-25902aa75bca.png)

Select a box type - available options depend on your box type setup. Only own scope boxes can be selected (BigPicture Enterprise users may see multiple options since they don't have a limit for how many box types can be created).

When you click a box type, you will see the list of modules that will be automatically active (module settings can be changed after a box has been created).

Click **Start working**to create a perfect match box.

![Screenshot of the chosen template in the BigPicture widget.](/cms_trial/assets/61275bea-fa95-4dee-833c-5a8b40f99e64.png)

The box is ready. You can create timeboxes to subdivide the scope further and change the box configuration to best suit your needs.

![Screenshot of the newly-created box in the BigPicture widget.](/cms_trial/assets/c2f63c57-54c8-4053-8849-4d40c25ba58d.png)

### Conditions

Requirements for box types used to create a matching box in the context of a Jira Project:

- **Own scope box** - Sub-scope and "none" scope boxes can't be created using this method.
- It can be created under the root (parent box set as root) - Box type settings > General > Basics related to **parent types** have to allow for a **main** box type to be a parent.
- Sequentiality set as **overlapping allowed**. See more on the Advanced (Box types) page.

## Go to BigPicture

To go to BigPicture:

1. Click the BigPicture icon at the top left to be taken to the App. You will be taken to the Home Box (Root Box).

   ![Screenshot of the App icon in the BigPicture widget.](/cms_trial/assets/88368659-553b-4963-b4b7-e152e1e3ae6d.png)
2. Use the box switcher to go directly to a selected box (right-clicking an item opens a box link in a new tab, for example).

   ![Screenshot of opening the box from the BigPicture widget in a new tab.](/cms_trial/assets/7dcc6815-1553-442d-9b50-4bdd58e4206d.png)

## Troubleshooting

### A new box can't be created

If you want to create a box using a particular box type and can't find it on the list of available options, box type settings don't meet one or more of the conditions outlined above.

### Missing permissions

Make sure to verify the App and box permissions and roles.

## BigPicture widget on Jira space screen (new navigation)

The App widget provides direct access to the app from a Jira space screen.

![Screenshot of the BigPicture widget from the Jira space context.](/cms_trial/assets/1742abef-bc2e-4734-9dbd-c4cdcd459304.png)

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

![Acessing app widget in Jira.](/cms_trial/assets/567855aa-7fd3-4a37-8e87-187145b1a344.png)

### Context

The Box switcher is at the top. It lets you navigate the box structure, including sub-boxes.

![Box switcher in thr app widget.](/cms_trial/assets/d78a07ff-5771-4860-a306-ae43e15b68ea.png)

### Modules and operations

You can access the full module directly from a Jira space page. Use the module dropdown to switch between modules.

![Modules menu in the App widget in Jira.](/cms_trial/assets/d78771ed-5232-412b-848e-4e639c723f79.png)

## Create a box

To create a box, you must have sufficient permissions within the App.

If a perfect match box already exists, you won't be allowed to create one.

If no perfect match box has been detected for a project, you are given the possibility to create it:

- New box name = project name.
- Nested directly under the home (root) box in the App (you can later move it if needed).

![App widget displays a screen where a user can create a matching box.](/cms_trial/assets/a421c13e-82d1-4e87-bc33-c00f36435fb7.png)

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

   ![BigPicture logo in the app widget.](/cms_trial/assets/491694fc-bd3b-408e-82fa-b5b799fed11a.png)
2. Use the box switcher to go directly to a selected box; right-click a box name link and open it in a new browser tab.

## Troubleshooting

### A new box can't be created

If you want to create a box using a particular box type and can't find it on the list of available options, box type settings don't meet one or more of the conditions outlined above.

### Missing permissions

Make sure to verify the app and box permissions and roles.