# Fields

## Fields (old navigation)

This section changes the task field synchronization settings and enables additional features, such as comments and notifications, which facilitate team communication.

Modify the mapping of this section to synchronize task attributes with appropriate external tool fields. When enabled, task synchronization is bi-directional and instant. For example, if you move a task using the Gantt module, the **Start Date** and **End Date** fields will be updated. Conversely, if you edit the Start Date or End Date fields via the Jira card of a task, the task changes will be updated and visible in the Gantt module.

General mapping affects all tasks unless you add custom mapping for specific projects.

For boxes based on a single Jira project, field mapping can be easily changed:

- From the level of an individual box
- Directly from a box context and a Jira project context

For boxes based on multiple Jira projects, the field mapping is configured on the **App configuration > General > Fields** page.

Synchronization of the app values with a task source:

- Values stored in a connected integration (such as Jira) can be synchronized with the app. For example, the **Original Estimate** Jira field can be synchronized with the app’s **End Date** field.
- Values that aren't being synchronized are stored exclusively in the app’s database.

## Conditions

The scope definition of a box must be simple, meaning limited to a single Jira project.

If a box is based on multiple Jira projects and you click the **Field mapping** button, you are redirected to theApp configuration > General > Fields page.

![image2022-3-23_8-40-39.png](/cms_trial/assets/bfdbd987-311f-4445-af84-3d51ba0bcbb6.png)

## Security and access

To change the field mapping, you must have sufficient permissions in the app and Jira.

Acceptable app permissions:

- Box Admin
- App Admin
- App Resource Admin

Acceptable Jira permissions:

- Jira project Admin
- Jira Admin

If there is more than one project in a box, you need Jira admin permission to preview or edit field mapping.

![image-20240209-093351.png](/cms_trial/assets/1ad54b8b-6456-4708-982e-175c9225f828.png)

1. Click the **wrench** icon at the top right and select**General** from the drop-down list.

   ![contentId-1918635376](/cms_trial/assets/4187fe10-447d-4627-853e-d7b5e649d54f.png)
2. Next, go to the **Fields** tab.

## General mapping

You **can’t** use the same field more than once. For example, If the **Due Date** field is mapped as the **End Date** of your task, you cannot select this field for any other mapping within a configuration of the same Jira Project. This applies to the following filed mappings:

- Start Date
- End Date
- Baseline Start Date
- Baseline End Date

Every connection has separate settings used for mapping. That includes each Jira instance, Trello workspace, etc.

Each instance connection can be expanded. Upon expanding, you can see the field mapping settings of the particular instance.

![Screenshot of the Fields page in BigPicture App Configuration.](/cms_trial/assets/6c77ebb9-fab2-49ec-ba5c-736a1b610958.png)

### Platform differences

Field mapping possibilities depend on the product (Jira vs. Trello).

**Jira:**

![Screenshot of defining Jira mapping in BigPicture App Configuration.](/cms_trial/assets/c959b781-8ffd-4f82-a365-fab2a9bc82f6.png)

**Trello:**

![Screenshot of defining Tello mapping in BigPicture App Configuration.](/cms_trial/assets/adecef0b-a24f-46e3-a1e1-25e43cf36b6c.png)

## Custom mapping (per Jira project)

Customize your synchronization settings by creating a separate configuration scheme for a Jira project. When you do that, general settings will no longer apply to this project.

Custom synchronization is created per Jira project - not per box. This means you can have tasks from different projects with different mappings in the same box.

To add custom mapping for a selected project:

1. Switch to the **Custom mapping** tab.
2. Click **Add Project**.
3. Select a project from the drop-down menu.
4. Click **Add and configure**.
5. Customize synchronization settings for a project.
6. Click **Save** to confirm.
7. The list of projects with custom synchronization is displayed once the new synchronization is saved.

![Screenshot of defining custom mapping in BigPicture App Configuration.](/cms_trial/assets/492a28bd-7bf9-403e-88c3-ba423325100f.png)

When you map a new Trello instance connection, its **Start Date** and **End Date** fields are set to **Not Synchronized** by default.

This means that when you change the dates of your Trello tasks in BigPicture, the changes will not be transferred to Trello (and vice versa).

The mappings need to be set manually when connecting with Trello.

You can leave the **Not Synchronized** status if you don't want to set dates from the BigPicture level.

## How to access the field mapping?

### From a box context

**Method 1:**

1. Click the **wrench icon** at the top right.
2. Select **Field mapping** from the list.

   ![image-20240207-084333.png](/cms_trial/assets/4f23d04b-e6b3-4e90-8a74-ff013c4944e4.png)

**Method 2:**

1. Click the **cog** icon.
2. Click the **Field mapping** button.

   ![image-20240207-084636.png](/cms_trial/assets/d934afcb-5d57-484e-a8c0-d7ba8a1ec99f.png)
3. Now, you can:

   1. Restore default settings
   2. Reset to defaults
   3. Make changes
4. When ready, click **Save**.

   ![image-20240207-083009.png](/cms_trial/assets/a0fcca6e-8e5f-4836-9348-893812211153.png)

### From a Jira project context

Go to a **Jira project:**

1. On the left, select the **BigPicture widget**.
2. Click the **wrench icon** at the top right.
3. Select **Field mapping** from the list.

![image-20240207-090141.png](/cms_trial/assets/b5179b09-2193-4379-be3c-94fa10e3ae12.png)

## Field mapping

### Current setup info

In the dialog, you can see the current field mapping of a project:

![contentId-1918635376](/cms_trial/assets/2cbf8454-e66f-4d58-bf83-6bc793dfc6c7.png)

At the top, you can see info regarding the current setup. The message lets you know if a **custom configuration** (custom mapping) exists for a project.

If a project uses the **default configuration** settings, it means a custom configuration doesn't exist for a project yet. The project is using the default mapping.

![contentId-1918635376](/cms_trial/assets/f54c713c-c108-4ea9-ad92-6618d535b349.png)

If a project uses the **custom configuration** settings, it means a separate, independent mapping exists.

![contentId-1918635376](/cms_trial/assets/5b7ea605-52a0-4e58-a9f3-f404f547e73e.png)

### Make changes

When you modify the mapping and save changes:

- The custom configuration is created, **OR**
- The existing custom configuration is updated.

![image-20240207-090410.png](/cms_trial/assets/9d051e17-e933-435d-813c-fcf0729c9043.png)

### Available fields

In some cases correct fields are still missing on Jira instances created after **Jan 1, 2026**, due to changes to Atlassian API behaviour. We are currently working on a fix that will be provided shortly.

A Jira field has to have a specific type to be available to be chosen for synchronization:

![image-20260206-103258.png](/cms_trial/assets/d3f91c6c-4048-4a38-8ff4-1451edaa161a.png)

|  |  |  |
| --- | --- | --- |
| **BigPicture Field** | **Compatible Jira Field Type(s)** | **Technical Specification & Sync Logic** |
| **Start date** | `Date Picker`, `Date Time Picker`, `Original Estimate` | **Date types:** Standard sync.  **Original Estimate:** BP calculates start based on task position/duration. |
| **End date** | `Date Picker`, `Date Time Picker`, `Remaining Estimate`, `Due Date` | **Date types:** Standard sync.  **Remaining Estimate:** BP uses this to calculate the task bar’s end point. |
| **Baseline start/end** | `Date Picker`, `Date Time Picker` | **Strict requirement:** Must be a date type to store a static schedule "snapshot." |
| **Team Code** | `Labels` **(Recommended)**  `Select List (single choice)`, | **Labels (Recommended):** Syncs as `team#Code`.  **Select List:** Jira option names must match BP Team IDs exactly. |
| **Milestone field** | `Labels` **(Recommended)**, `Checkbox` | **Checkbox:** Requires a single-option checkbox (e.g., "Yes"). |
| **Story Points** | `Number Field`, `Time Tracking` | **Number:** Standard Story Point sync.  **Time Tracking:** BP converts time to "points" based on Task Resource settings. |
| **Required Skills** | `Labels`, `Select List (multiple choice)`, `Text (single line)` | **Labels:** Syncs as `skill#Name`.  **Note:** Spaces are replaced by underscores (e.g., `skill#Java_Dev`). |
| **Actual / Est. Cost** | `Number Field` | Used for financials modules; requires numeric custom fields. |
| **Progress** | `Number Field`, `Time Tracking` | **Number:** Uses 0–100 values.  **Time Tracking:** Syncs based on "Time Spent" vs. "Original Estimate." |
| **Scheduling mode** | `Task mode` **(Recommended)**  `Select List (single choice)` | Jira options must be exactly: `Auto`, `Manual`, and `Locked` (or `Lock`). |

- **The API Filter:** BigPicture identifies available fields by combining results from `/field` (classic) and `/field/search` (modern/team-managed). If a field doesn't appear, ensure it matches the types in the table above.
- **The Sync Prefixes:** When using **Labels** for Teams or Skills, BigPicture uses the `#` delimiter (`team#` and `skill#`). This allows it to coexist with other Jira labels without overwriting them.
- **Time Tracking Fields:** You may see Jira's `Time Tracking` or `Original Estimate` fields available in several dropdowns (like Start Date or Story Points). This is because BigPicture can automatically convert "Time" into "Dates" or "Points" based on your project's working calendar. While supported, we recommend using standard **Date Picker** and **Number** fields for the most predictable results.

### Restore default settings

You can always remove the custom configuration and return to the default configuration.

![image-20240207-090505.png](/cms_trial/assets/f4ab3ab4-898c-4f43-80e2-f5ad5acb88cc.png)

### Reset to defaults

If you click **Reset to defaults**, all custom settings will be overwritten with default settings.

The action **CANNOT** be undone.

![image-20240207-090608.png](/cms_trial/assets/baa3e261-53c1-4007-9930-3cf9d0c68706.png)

### Field mapping (App configuration)

An App Admin can access and modify the default configuration in the **App Configuration** > **General** > **Fields** section.

![contentId-1918635376](/cms_trial/assets/f35d9b32-c83c-40ba-a442-2f9fdaf8e001.png)

### Field mapping reminders

The app prompts you to check the field mapping:

- when you add or remove projects in the scope

- when you make an edit to a built-in field that does not have mapping.

## Limitations

- **Box editors** and **box viewers** have read-only access to the field mapping of a box. The field mapping option is greyed out for them.

## Fields (new navigation)

This section changes the task field synchronization settings and enables additional features, such as comments and notifications, which facilitate team communication.

Modify the mapping of this section to synchronize task attributes with appropriate external tool fields. When enabled, task synchronization is bi-directional and instant. For example, if you move a task using the Gantt module, the **Start Date** and **End Date** fields will be updated. Conversely, if you edit the Start Date or End Date fields via the Jira card of a task, the task changes will be updated and visible in the Gantt module.

General mapping affects all tasks unless you add custom mapping for specific projects.

For boxes based on a single Jira project, field mapping can be easily changed:

- From the level of an individual box
- Directly from a box context and a Jira project context

For boxes based on multiple Jira projects, the field mapping is configured on the **App configuration > General > Fields** page.

Synchronization of the app values with a task source:

- Values stored in a connected integration (such as Jira) can be synchronized with the app. For example, the **Original Estimate** Jira field can be synchronized with the app’s **End Date** field.
- Values that aren't being synchronized are stored exclusively in the app’s database.

## Conditions

The Add work items from Jira settings of a box must be simple, meaning limited to a single Jira space.

![work-items-from-jira-spaces.png](/cms_trial/assets/bee392ce-2a9c-4f69-8b5f-846277d538bf.png)

If a box is based on multiple Jira projects and you click the **Field mapping** button, you are redirected to theApp configuration > General > Fields page.

## Security and access

To change the field mapping, you must have sufficient permissions in the app and Jira.

Acceptable app permissions:

- Box Admin
- App Admin
- App Resource Admin

Acceptable Jira permissions:

- Jira project Admin
- Jira Admin

If there is more than one project in a box, you need Jira admin permission to preview or edit field mapping.

![image-20240209-093351.png](/cms_trial/assets/1ad54b8b-6456-4708-982e-175c9225f828.png)

1. Click the **wrench** icon at the top right and select**General** from the drop-down list.

   ![contentId-1918635376](/cms_trial/assets/4187fe10-447d-4627-853e-d7b5e649d54f.png)
2. Next, go to the **Fields** tab.

## General mapping

You **can’t** use the same field more than once. For example, If the **Due Date** field is mapped as the **End Date** of your task, you cannot select this field for any other mapping within a configuration of the same Jira Project. This applies to the following filed mappings:

- Start Date
- End Date
- Baseline Start Date
- Baseline End Date

Every connection has separate settings used for mapping. That includes each Jira instance, Trello workspace, etc.

Each instance connection can be expanded. Upon expanding, you can see the field mapping settings of the particular instance.

![Screenshot of the Fields page in BigPicture App Configuration.](/cms_trial/assets/6c77ebb9-fab2-49ec-ba5c-736a1b610958.png)

### Platform differences

Field mapping possibilities depend on the product (Jira vs. Trello).

**Jira:**

![Screenshot of defining Jira mapping in BigPicture App Configuration.](/cms_trial/assets/c959b781-8ffd-4f82-a365-fab2a9bc82f6.png)

**Trello:**

![Screenshot of defining Tello mapping in BigPicture App Configuration.](/cms_trial/assets/adecef0b-a24f-46e3-a1e1-25e43cf36b6c.png)

## Custom mapping (per Jira project)

Customize your synchronization settings by creating a separate configuration scheme for a Jira project. When you do that, general settings will no longer apply to this project.

Custom synchronization is created per Jira project - not per box. This means you can have tasks from different projects with different mappings in the same box.

To add custom mapping for a selected project:

1. Switch to the **Custom mapping** tab.
2. Click **Add Project**.
3. Select a project from the drop-down menu.
4. Click **Add and configure**.
5. Customize synchronization settings for a project.
6. Click **Save** to confirm.
7. The list of projects with custom synchronization is displayed once the new synchronization is saved.

![Screenshot of defining custom mapping in BigPicture App Configuration.](/cms_trial/assets/492a28bd-7bf9-403e-88c3-ba423325100f.png)

When you map a new Trello instance connection, its **Start Date** and **End Date** fields are set to **Not Synchronized** by default.

This means that when you change the dates of your Trello tasks in BigPicture, the changes will not be transferred to Trello (and vice versa).

The mappings need to be set manually when connecting with Trello.

You can leave the **Not Synchronized** status if you don't want to set dates from the BigPicture level.

## How to access the field mapping?

### From a box context

**Method 1:**

1. Click the **wrench icon** at the top right.
2. Select **Field mapping** from the list.

   ![image-20240207-084333.png](/cms_trial/assets/4f23d04b-e6b3-4e90-8a74-ff013c4944e4.png)

**Method 2:**

1. Click the **cog** icon.
2. Click the **Field mapping** button.

   ![image-20240207-084636.png](/cms_trial/assets/d934afcb-5d57-484e-a8c0-d7ba8a1ec99f.png)
3. Now, you can:

   1. Restore default settings
   2. Reset to defaults
   3. Make changes
4. When ready, click **Save**.

   ![image-20240207-083009.png](/cms_trial/assets/a0fcca6e-8e5f-4836-9348-893812211153.png)

### From a Jira project context

Go to a **Jira project:**

1. On the left, select the **BigPicture widget**.
2. Click the **wrench icon** at the top right.
3. Select **Field mapping** from the list.

![image-20240207-090141.png](/cms_trial/assets/b5179b09-2193-4379-be3c-94fa10e3ae12.png)

## Field mapping

### Current setup info

In the dialog, you can see the current field mapping of a project:

![contentId-1918635376](/cms_trial/assets/2cbf8454-e66f-4d58-bf83-6bc793dfc6c7.png)

At the top, you can see info regarding the current setup. The message lets you know if a **custom configuration** (custom mapping) exists for a project.

If a project uses the **default configuration** settings, it means a custom configuration doesn't exist for a project yet. The project is using the default mapping.

![contentId-1918635376](/cms_trial/assets/f54c713c-c108-4ea9-ad92-6618d535b349.png)

If a project uses the **custom configuration** settings, it means a separate, independent mapping exists.

![contentId-1918635376](/cms_trial/assets/5b7ea605-52a0-4e58-a9f3-f404f547e73e.png)

### Make changes

When you modify the mapping and save changes:

- The custom configuration is created, **OR**
- The existing custom configuration is updated.

![image-20240207-090410.png](/cms_trial/assets/9d051e17-e933-435d-813c-fcf0729c9043.png)

### Available fields

In some cases correct fields are still missing on Jira instances created after **Jan 1, 2026**, due to changes to Atlassian API behaviour. We are currently working on a fix that will be provided shortly.

A Jira field has to have a specific type to be available to be chosen for synchronization:

![image-20260206-103258.png](/cms_trial/assets/d3f91c6c-4048-4a38-8ff4-1451edaa161a.png)

|  |  |  |
| --- | --- | --- |
| **BigPicture Field** | **Compatible Jira Field Type(s)** | **Technical Specification & Sync Logic** |
| **Start date** | `Date Picker`, `Date Time Picker`, `Original Estimate` | **Date types:** Standard sync.  **Original Estimate:** BP calculates start based on task position/duration. |
| **End date** | `Date Picker`, `Date Time Picker`, `Remaining Estimate`, `Due Date` | **Date types:** Standard sync.  **Remaining Estimate:** BP uses this to calculate the task bar’s end point. |
| **Baseline start/end** | `Date Picker`, `Date Time Picker` | **Strict requirement:** Must be a date type to store a static schedule "snapshot." |
| **Team Code** | `Labels` **(Recommended)**  `Select List (single choice)`, | **Labels (Recommended):** Syncs as `team#Code`.  **Select List:** Jira option names must match BP Team IDs exactly. |
| **Milestone field** | `Labels` **(Recommended)**, `Checkbox` | **Checkbox:** Requires a single-option checkbox (e.g., "Yes"). |
| **Story Points** | `Number Field`, `Time Tracking` | **Number:** Standard Story Point sync.  **Time Tracking:** BP converts time to "points" based on Task Resource settings. |
| **Required Skills** | `Labels`, `Select List (multiple choice)`, `Text (single line)` | **Labels:** Syncs as `skill#Name`.  **Note:** Spaces are replaced by underscores (e.g., `skill#Java_Dev`). |
| **Actual / Est. Cost** | `Number Field` | Used for financials modules; requires numeric custom fields. |
| **Progress** | `Number Field`, `Time Tracking` | **Number:** Uses 0–100 values.  **Time Tracking:** Syncs based on "Time Spent" vs. "Original Estimate." |
| **Scheduling mode** | `Task mode` **(Recommended)**  `Select List (single choice)` | Jira options must be exactly: `Auto`, `Manual`, and `Locked` (or `Lock`). |

- **The API Filter:** BigPicture identifies available fields by combining results from `/field` (classic) and `/field/search` (modern/team-managed). If a field doesn't appear, ensure it matches the types in the table above.
- **The Sync Prefixes:** When using **Labels** for Teams or Skills, BigPicture uses the `#` delimiter (`team#` and `skill#`). This allows it to coexist with other Jira labels without overwriting them.
- **Time Tracking Fields:** You may see Jira's `Time Tracking` or `Original Estimate` fields available in several dropdowns (like Start Date or Story Points). This is because BigPicture can automatically convert "Time" into "Dates" or "Points" based on your project's working calendar. While supported, we recommend using standard **Date Picker** and **Number** fields for the most predictable results.

### Restore default settings

You can always remove the custom configuration and return to the default configuration.

![image-20240207-090505.png](/cms_trial/assets/f4ab3ab4-898c-4f43-80e2-f5ad5acb88cc.png)

### Reset to defaults

If you click **Reset to defaults**, all custom settings will be overwritten with default settings.

The action **CANNOT** be undone.

![image-20240207-090608.png](/cms_trial/assets/baa3e261-53c1-4007-9930-3cf9d0c68706.png)

### Field mapping (App configuration)

An App Admin can access and modify the default configuration in the **App Configuration** > **General** > **Fields** section.

![contentId-1918635376](/cms_trial/assets/f35d9b32-c83c-40ba-a442-2f9fdaf8e001.png)

### Field mapping reminders

The app prompts you to check the field mapping:

- when you add or remove projects in the scope

- when you make an edit to a built-in field that does not have mapping.

## Limitations

- **Box editors** and **box viewers** have read-only access to the field mapping of a box. The field mapping option is greyed out for them.