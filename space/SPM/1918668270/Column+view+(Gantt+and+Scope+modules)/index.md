# Column view (Gantt and Scope modules)

## Column view - Gantt and Scope modules (old navigation)

Click to expand the guide

## About the column view

Column Views allow you to add different fields and configure their display and aggregation settings which determine how data is presented.

Each Box type has a predefined list of Column Views, which you can edit or create new ones.

The column view works the same for both the Gantt and Scope modules.

## Configuration

- To configure Column Views go to Box configuration > Gantt type module (Gantt is the default module name used) > Column Views.
- To configure the  default views and the inheritance mode go to App's administration > Box types > select a Box type > Gantt > Gantt is the default module name used) > Column Views.
- Only a user with a minimum Box admin security role can access and manage the Box configuration.
- Only a user with a minimum App admin security role can access and manage the Administration.

The Card View configuration page will not be visible if the Gantt module is not active or the Inheritance mode is set to 'inherited only'.

![contentId-1918668270](/cms_trial/assets/00de5ecd-cdc9-44ae-ac28-3f0dee23a909.png)

## Active column view

Expand the drop-down menu to see the list of available column views. When you select one of them, it becomes active and is applied whenever a user opens the module or returns to it.

![image-20240205-125322.png](/cms_trial/assets/ae9bcf95-6765-4190-ab6b-f01372ac6f90.png)

## [Inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/)

The Column Views can be inherited by the sub-level Boxes when the Inheritance mode is set to "Inherited only" or "Own with inherited" in the Box type configuration of the upper-level Box. This way, every time you create new views or edit the existing ones, all available views will also be updated in the sub-level Boxes.

## [Default column views](/cms_trial/space/SPM/1918503715/Manage+column+views/)

When the "Inheritance mode' is set to "Own" or "Own with inherited" App Admins can create the default Column Views, which will be used every time a new Box of a given type is created.

## Change views

The Column View drop-down shows the list of available views. To switch between the views, click on one of the names. The currently used view will be displayed on the Column View button:

![image-20240205-102759.png](/cms_trial/assets/3d665d01-c6f7-41de-bdd3-46164edb5d18.png)

## Edit and create views

You can edit column views:

- In Box configuration > Gantt > Gantt Column Views
- Directly within the Gantt module

**Box Viewers** and **Box Editors** can dynamically modify an active column view but don't have permission to save those changes.

**Box Admins** can additionally save changes made to the active view.

We recommend using the 'Built-in" type of fields which display field values from all synchronized fields in Jira and connected tools. For example, the "Start date" built-in field shows the date values from all fields mapped as the start date in the Fields configuration and from connected tools, such as Trello.

To add a column, click the 'cog' icon on the far right of the task list header. Use the search box to find the fields you want to add:

![contentId-1918668270](/cms_trial/assets/912c6afb-5f40-4011-a1ed-c0eb12f3c47d.png)

Once the view is modified, the Box admin can:

- Save changes to the active view
- Save it as a new one
- Restore the changes

![image-20240205-124620.png](/cms_trial/assets/f26eed6e-c59a-47e9-967f-394f7843edfc.png)

## Column configuration

Click on the **Customize column** icon to:

- Pin column
- Sort tasks
- Customize
- Column info
- Resize all columns to fit
- Remove column

![image-20240801-083658.png](/cms_trial/assets/56caaedf-3c87-4a3d-bb7c-bbf0ba9122c5.png)

### Pin column

To pin a selected column:

1. Click on the **Customize column** icon.
2. Click **Pin column** and select one of the available options:

   1. No pin
   2. Pin left
   3. Pin right

![image-20240801-083829.png](/cms_trial/assets/563bf02c-d9c1-4a8c-82e1-1b36c754f461.png)

### Sort tasks

When you sort tasks, the view is temporarily modified, and the applied changes are visible only to you.

To sort tasks:

1. Click on the **Customize column** icon.
2. Click **Sort tasks** and select one of the available options:

   1. A-Z
   2. Z-A
   3. None

![image-20240801-084101.png](/cms_trial/assets/4054ca98-dd72-4ecf-a70c-c6bdc33fe3b9.png)

### Customize column

Data from various fields can be aggregated at the parent task level, or you can change the way it is presented. For example, the status field has different aggregation options, and one of the most useful is the **Children status categories** which shows the task distribution in status categories:

![image-20240801-084220.png](/cms_trial/assets/aa1903de-b56a-411b-ae58-c21f8f4c2f0f.png)

### Column info

Click **Column info** to check the source of a selected column.

BigPicture built-in field:

![image-20240801-084717.png](/cms_trial/assets/99069d72-ecec-4dce-83fd-02b0c1510f45.png)

Jira field:

![image-20240801-084751.png](/cms_trial/assets/5dd65c29-ecdd-4bbb-bb51-e1fd6630ac8c.png)

### Resize all columns to fit

Use the **Resize all columns to fit** option to automatically adjust the width of all columns added to the current column view to the width of the task list.

![image-20240801-085155.png](/cms_trial/assets/ad4cca79-bee3-424a-a3ff-499197f657f5.png)

If there are too many columns to fit the width of the task list, a horizontal scroll is active.

![contentId-1918668270](/cms_trial/assets/8b3f6662-8262-4175-b3c6-a06b9e6d65ac.png)

### Remove column

To remove the selected column from the column view:

**Method 1:**

1. Click on the **Customize column** icon.
2. Click **Remove**.

**Method 2:**

1. Click the cog icon.
2. Click the bin icon next to a column you want to remove.

![image-20240205-123823.png](/cms_trial/assets/129ec11a-5eaa-453c-bbbe-a53e81e45aae.png)

## Favourite views

You can mark your favorite views using the star, and your views will be displayed in a separate section of the drop-down:

![image-20240205-104324.png](/cms_trial/assets/fb04c7eb-ab4a-404c-8745-13345125421f.png)

## Delete column views

You must access **Box configuration > Gantt/Scope > Column Views** to delete column views.

You can't delete the column view that is in use. At least one View has to exist at all times.

![image-20240205-104427.png](/cms_trial/assets/72a6ec41-69cf-4fd2-ac3e-ef5fd573038e.png)

## [Field mapping](/cms_trial/space/SPM/1918635376/Fields/)

For boxes based on a single Jira project, you can configure the field mapping rules directly from a box context.

## Affects

Switching between column views may clear [the grouping](/cms_trial/space/SPM/1918830289/Group+tasks/). Grouping is based on visible columns - if the new column view doesn't contain columns used for grouping, grouping is cleared. If possible, grouping is maintained.

## Column view - Gantt and Scope modules (new navigation)

Click to expand the guide

## About the column view

Column views allow you to add different fields and configure their display and aggregation settings, which determine how data is presented.

Each box type has a predefined list of column views, which you can edit or create new ones.

The column view works the same for both the Gantt and Scope modules.

## Configuration

- To configure column views go to **Box configuration** > **Gantt type module (Gantt is the default module name used)** > **Column Views**.
- To configure the  default views and the inheritance mode, go to **App's administration** > **Box types** > **select a Box type** > **Gantt** > **Gantt is the default module name used)** > **Column Views**.
- Only a user with a minimum Box admin security role can access and manage the box configuration.
- Only a user with a minimum App admin security role can access and manage the Administration.

The column view configuration page will not be visible if the Gantt module is not active or the Inheritance mode is set to 'inherited only'.

## Active column view

Expand the drop-down menu to see the list of available column views. When you select one of them, it becomes active and is applied whenever a user opens the module or returns to it.

![Screenshot of the column views in the Gantt module.](/cms_trial/assets/1d0c308e-787a-40ac-8252-29d49a9af40e.png)

## [Inheritance mode](/cms_trial/space/SPM/1918700886/Inheritance+mode/)

The column views can be inherited by the sub-level boxes when the Inheritance mode is set to "Inherited only" or "Own with inherited" in the box type configuration of the upper-level box. This way, every time you create new views or edit the existing ones, all available views will also be updated in the sub-level boxes.

## [Default column views](/cms_trial/space/SPM/1918503715/Manage+column+views/)

When the Inheritance mode is set to "Own" or "Own with inherited", App Admins can create the default column views, which will be used every time a new box of a given type is created.

## Change views

The Column View drop-down lists the available views. To switch between the views, click on one of the names. The currently used view will be displayed on the **Column View** button.

![Screenshot of the current column view in the Gantt module.](/cms_trial/assets/74e7d585-412d-4eb7-947a-13e1bf75a8fd.png)

## Edit and create views

You can edit column views:

- In **Box configuration** > **Gantt** > **Gantt Column Views**
- Directly within the Gantt module

**Box Viewers** and **Box Editors** can dynamically modify an active column view, but don't have permission to save those changes.

**Box Admins** can additionally save changes made to the active view.

We recommend using the 'Built-in" type of fields, which display field values from all synchronized fields in Jira and connected tools. For example, the "Start date" built-in field shows the date values from all fields mapped as the start date in the Fields configuration and from connected tools, such as Trello.

To add a column, click the **plus** icon on the far right of the task list header. Use the search box to find the fields you want to add.

![Screenshot of adding a column to the view in the Gantt module.](/cms_trial/assets/7fc24a67-dda6-4a97-8829-fa39ce022c87.png)

Once the view is modified, the Box admin can:

- Save changes to the active view
- Save it as a new one
- Restore the changes

![Screenshot of the available options after modifying the view in the Gantt module (save, save as, restore).](/cms_trial/assets/08a1bb08-f9db-4bef-8c2a-05a1dab18ac9.png)

## Column configuration

Click the **Customize column** icon to:

- Pin column
- Sort tasks
- Customize
- Column info
- Resize all columns to fit
- Remove column

![Screenshot of the Customize column options available for the Start field in the Gantt module.](/cms_trial/assets/dd95066a-a0e3-447f-835e-aedf64a56f2a.png)

### Pin column

To pin a selected column:

1. Click the **Customize column** icon.
2. Click **Pin column** and select one of the available options:

   1. No pin
   2. Pin left
   3. Pin right

![Screenshot of the Pin column option in the Gantt module.](/cms_trial/assets/c25b3b9c-4e0a-4817-b6ee-7a1a663d74f5.png)

### Sort tasks

When you sort tasks, the view is temporarily modified, and the applied changes are visible only to you.

To sort tasks:

1. Click on the **Customize column** icon.
2. Click **Sort tasks** and select one of the available options:

   1. A-Z
   2. Z-A
   3. None

![Screenshot of the Sort task option available in the Gantt module.](/cms_trial/assets/a54851cf-216c-40a9-a5dc-3bf1541f3cd0.png)

### Customize column

Data from various fields can be aggregated at the parent task level, or you can change the way it is presented. For example, the status field has different aggregation options, and one of the most useful is the **Children status categories** which shows the task distribution in status categories:

![Screenshot of the Customize column options available in the Gantt module.](/cms_trial/assets/aa1903de-b56a-411b-ae58-c21f8f4c2f0f.png)

### Column info

Click **Column info** to check the source of a selected column.

BigPicture built-in field:

![Screenshot of the Column info option available in the Gantt module.](/cms_trial/assets/99069d72-ecec-4dce-83fd-02b0c1510f45.png)

Jira field:

![Screenshot of the Column info option available in the Gantt module.](/cms_trial/assets/5dd65c29-ecdd-4bbb-bb51-e1fd6630ac8c.png)

### Resize all columns to fit

Use the **Resize all columns to fit** option to automatically adjust the width of all columns added to the current column view to the width of the task list.

![Screenshot of the Resize all columns to fit option available in the Gantt module.](/cms_trial/assets/cbf68d88-330d-4e73-ad84-7909148af8c8.png)

If there are too many columns to fit the task list width, a horizontal scroll is enabled.

![Screenshot of the Gantt module after clicking Resize all columns to fit option.](/cms_trial/assets/d58a2795-1618-4a8a-bb98-fa435b8c3219.png)

### Remove column

To remove the selected column from the column view:

**Method 1:**

1. Click on the **Customize column** icon.
2. Click **Remove column**.

**Method 2:**

1. Click the **plus** icon.
2. Click the bin icon next to a column you want to remove.

![Screenshot of removing a column from the view in the Gantt module.](/cms_trial/assets/1967cb3a-7266-4648-aea8-0d4c1a6d5ee3.png)

## Favourite views

You can mark your favorite views using the star, and your views will be displayed in a separate section of the drop-down.

![Screenshot of adding column views to favorite in the Gantt module.](/cms_trial/assets/4f3be89b-25e8-4845-8375-7690f8aa813f.png)

## Delete column views

You must access **box configuration** > **Gantt/Scope** > **Column Views** to delete column views.

You can't delete the column view that is in use. At least one view has to exist at all times.

![Screenshot of deleting the column view in the box configuration.](/cms_trial/assets/f445f211-9c81-4a83-92fa-cb0e64167151.png)

## [Field mapping](/cms_trial/space/SPM/1918635376/Fields/)

For boxes based on a single Jira project, you can configure the field mapping rules directly from a box context.

## Affects

Switching between column views may clear the [grouping](/cms_trial/space/SPM/1918830289/Group+tasks/). Grouping is based on visible columns - if the new column view doesn't contain columns used for grouping, grouping is cleared. If possible, grouping is maintained.