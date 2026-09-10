# Group tasks

## Group tasks (old navigation)

Click to expand the guide

## About grouping tasks

The **Group tasks**option allows you to sort and organize data using different field values with just a few clicks. To simplify data analysis, the created groups will be marked in colors, both on the task list and on the timeline indicating the earliest start and the latest date of the tasks in a particular group.

Grouping doesn't permanently alter the WBS (task structure) - data is temporarily reorganized. As a result, the task hierarchy is not displayed when data is grouped.

The video presents how to group data in the Scope module.

### Security and access

- Box admins, box editors, and box viewers can group tasks.
- For box viewers, the **Data** drop-down menu has only the **Group tasks** feature.

## Preconditions

Grouping is based on visible columns - if the new column view doesn't contain columns that were used for grouping, grouping is cleared.

## Activate grouping

To activate grouping:

1. Expand the **Data**drop-down menu.
2. Select the **Group tasks**option.
3. Activate grouping elements to create groups.
4. Define the order of grouping elements.
5. Specify the color of grouping elements.

![Screenshot of grouping data in the Scope module.](/cms_trial/assets/88787329-dcbd-49ab-ade7-c7f35f117858.png)

### Color groups

The color is reflected:

- on the task structure
- on the timeline

![contentId-1918830289](/cms_trial/assets/3439a475-ffd0-4619-a200-52eb6055908d.png)

To select a color, click on the icon in the Color column:

[Unmapped macro: multimedia — no content to fall back on]

## Deactivate grouping

**Method 1**

To deactivate grouping:

1. Hover the mouse cursor over a group heading.
2. Click **X**to deactivate a particular grouping.

![Screenshot of deactivating grouping in the Scope module.](/cms_trial/assets/0f937b04-498a-4741-8b42-f4d16fa7abb7.png)

**Method 2**

To deactivate grouping:

1. Go to **Data > Group tasks**.
2. Deactivate grouping by:

   1. Adjusting toggle switches.
   2. Using the **Deactivate all**button.
3. Click **Apply**.

![Screenshot of deactivating grouping in the Scope module.](/cms_trial/assets/73c0f04b-8113-4a0a-bfb1-3be70af8fd8a.png)

## Available grouping options

To group using a specific field, make sure it is added as a column first. To learn more, see the Column Views page.

#### Multi-level grouping

With the multi-level grouping method, tasks will be counted in each group. The group structure will be based on the active grouping elements. The order of grouping elements (fields) defines the group hierarchy.

A task **cannot** be duplicated, which means that a task can belong to a single group only.

## Filter grouped tasks

The grouping functionality can be combined with other filters (such as Search and Quick filters).

![Screenshot of applying filters on grouped data in the Scope module.](/cms_trial/assets/ef2a4aaf-fdca-4680-8312-a02fa8981bb4.png)

## Sort grouped tasks

Once the tasks are grouped, the **Organize taska A/Z** and **Organize taska Z/A** options are **unavailable**. You can sort rows ascending by clicking the column header. The second click sets descending order.

## Inline edit fields

When the grouping option is enabled, you can inline edit fields. To see changes, refresh the page.

See more on the Inline edit page.

![Screenshot of editing inline the Status field in the Scope module.](/cms_trial/assets/8c1525c2-ca89-4b02-aa86-4f6d52387b80.png)

## Limitations

- The **Key** and **Summary** columns cannot be used for grouping.
- All WBS (task structure operations) are disabled - when task grouping is active, the WBS structure is ignored and can't be modified.
- **Grouping task limit = 50000 tasks**. If you have more than 50000 tasks in a box, use filters (search, quick filters, date filters etc.) to narrow the scope of the operation. Then, perform grouping.

To set a task limit on how many tasks a box can have to allow grouping, go to **App settings > App Configuration > Advanced > Technical Info**.

![contentId-1918830289](/cms_trial/assets/04b0df70-ed02-4d89-b608-7cf193cb54b7.png)

## Sorting grouped tasks

The below applies to a situation when [task grouping](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298354243) is active.

**Sorting is initiated by clicking on the column header**

- Only tasks in groups are sorted (groups themselves are not sorted)
- Sorting is possible only for the fields that can be "organized by."

Sorting by clicking the header is **disabled when**:

- the sorted column is removed
- grouping mode is disabled (when grouping is inactive, use the "Data" option in the menu at the top > "Organize tasks")

  ![contentId-1918830289](/cms_trial/assets/79c12718-e0e0-4d14-9e6c-da7aa8b7dca4.png)

When tasks are grouped, a **sorting action is triggered**:

- By clicking the column header (the first click sorts the task in ascending order, the next one descending)
- grouping conditions are changed
- page is refreshed

Sorting does not reflect field value changes (when tasks are already sorted, changing a value won't trigger an automatic recalculation)

## Group tasks (new navigation)

Click to expand the guide

## About grouping tasks

The **Group tasks**option allows you to sort and organize data using different field values with just a few clicks. To simplify data analysis, the created groups will be marked in colors, both on the task list and on the timeline, indicating the earliest start and the latest date of the tasks in a particular group.

Grouping doesn't permanently alter the WBS (task structure) - data is temporarily reorganized. As a result, the task hierarchy is not displayed when data is grouped.

See the interactive demo on how to group data in the Scope module.

<https://app.arcade.software/share/G3y942beK4POljq5Efu2>

### Security and access

Box admins, box editors, and box viewers can group tasks.

## Preconditions

Grouping is based on visible columns - if the new column view doesn't contain columns that were used for grouping, grouping is cleared.

## Activate grouping

To activate grouping:

1. Expand the **View**drop-down menu.
2. Select the **Group tasks**option.
3. Activate grouping elements to create groups.
4. Define the order of grouping elements.
5. Specify the color of grouping elements.

![Screenshot of grouping tasks in the Scope module.](/cms_trial/assets/98063d56-ba54-4038-9fc0-208ebc4eada9.png)

### Color groups

When grouping tasks in the Gantt module, the color is reflected:

- on the task structure
- on the timeline

![Screenshot of grouping tasks in the Gantt module.](/cms_trial/assets/6b55b6d9-9765-47a6-bdc9-aea64d7e14e6.png)

## Deactivate grouping

**Method 1**

To deactivate grouping:

1. Hover the mouse cursor over a group heading.
2. To deactivate one grouping element, click **X**.
3. To deactivate all grouping elements, click **Disable grouping**.

![Screenshot of deactivating grouping in the Gantt module.](/cms_trial/assets/66360048-54e0-4bf7-a4a1-885c675291ed.png)

**Method 2**

To deactivate grouping:

1. Go to **View** > **Group tasks**.
2. Deactivate grouping by:

   1. Adjusting toggle switches.
   2. Using the **Deactivate all**button.
3. Click **Apply**.

![Screenshot of deactivating grouping in the Gantt module.](/cms_trial/assets/49806f2c-5e7c-4ba7-84fa-a01fd00e769b.png)

## Available grouping options

To group using a specific field, make sure it is added as a column first.

#### Multi-level grouping

With the multi-level grouping method, tasks will be counted in each group. The group structure will be based on the active grouping elements. The order of grouping elements (fields) defines the group hierarchy.

A task **cannot** be duplicated, which means that a task can belong to a single group only.

## Filter grouped tasks

The grouping functionality can be combined with other filters (such as search and quick filters).

![Screenshot of filtering grouped tasks in the Gantt module.](/cms_trial/assets/43306140-0691-42a8-a380-98db5db4a06e.png)

## Inline edit fields

When the grouping option is enabled, you can inline edit fields. To see changes, refresh the page.

See more on the [Inline edit](/cms_trial/space/SPM/1918637324/Inline+edit/) page.

## Limitations

- The **Key** and **Summary** columns cannot be used for grouping.
- All WBS (task structure operations) are disabled - when task grouping is active, the WBS structure is ignored and can't be modified.
- **Grouping task limit = 50000 tasks**. If you have more than 50000 tasks in a box, use filters (search, quick filters, date filters etc.) to narrow the scope of the operation. Then, perform grouping.

To set a task limit on how many tasks a box can have to allow grouping, go to **App settings > App Configuration > Advanced > Technical Info**.

![contentId-1918830289](/cms_trial/assets/04b0df70-ed02-4d89-b608-7cf193cb54b7.png)

## Sort grouped tasks

The following applies to a situation when task grouping is active.

When tasks are grouped, a **sorting action is triggered**:

- By clicking the column header (the first click sorts the task in ascending order, the next one descending).
- Grouping conditions are changed.
- The page is refreshed.

Sorting does not reflect field value changes (when tasks are already sorted, changing a value won't trigger an automatic recalculation).