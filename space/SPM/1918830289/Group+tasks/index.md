# Group tasks

[Unmapped macro: d1a8786a-e4fc-49c5-8b89-103ffd18e3e2/2cc2c77e-5377-42cb-add7-54a9da0f9b1c/static/refined-expand — no content to fall back on]

**About grouping tasks**

The **Group tasks**option allows you to sort and organize data using different field values with just a few clicks. To simplify data analysis, the created groups will be marked in colors, both on the task list and on the timeline, indicating the earliest start and the latest date of the tasks in a particular group.

Grouping doesn't permanently alter the WBS (task structure) - data is temporarily reorganized. As a result, the task hierarchy is not displayed when data is grouped.

The video presents how to group data in the Scope module.

**Security and access**

- Box admins, box editors, and box viewers can group tasks.
- For box viewers, the **Data** drop-down menu has only the **Group tasks** feature.

**Preconditions**

Grouping is based on visible columns - if the new column view doesn't contain columns that were used for grouping, grouping is cleared.

**Activate grouping**

To activate grouping:

1. Expand the **Data**drop-down menu.
2. Select the **Group tasks**option.
3. Activate grouping elements to create groups.
4. Define the order of grouping elements.
5. Specify the color of grouping elements.

![Screenshot of grouping data in the Scope module.](/cms_trial/assets/40ed5463-cabd-4701-b503-cfaf0d97897a.png)

**Color of groups**

The color is reflected:

- on the task structure
- on the timeline

![contentId-1918830289](/cms_trial/assets/96a4b145-d15c-4350-b748-96671872e123.png)

To select a color, click on the icon in the Color column:

[Unmapped macro: multimedia — no content to fall back on]

**Deactivate grouping**

**Method 1**

To deactivate grouping:

1. Hover the mouse cursor over a group heading.
2. Click **X**to deactivate a particular grouping.

![Screenshot of deactivating grouping in the Scope module.](/cms_trial/assets/a0e5cee3-7ad1-4442-aaac-04e2dd9d5fa8.png)

**Method 2**

To deactivate grouping:

1. Go to **Data > Group tasks**.
2. Deactivate grouping by:

   1. Adjusting toggle switches.
   2. Using the **Deactivate all**button.
3. Click **Apply**.

![Screenshot of deactivating grouping in the Scope module.](/cms_trial/assets/0f87127e-7046-4a54-93fd-851e89a81e26.png)

**Available grouping options**

To group using a specific field, make sure it is added as a column first. To learn more, see the Column Views page.

**Multi-level grouping**

With the multi-level grouping method, tasks will be counted in each group. The group structure will be based on the active grouping elements. The order of grouping elements (fields) defines the group hierarchy.

A task **cannot** be duplicated, which means that a task can belong to a single group only.

**Filter grouped tasks**

The grouping functionality can be combined with other filters (such as Search and Quick filters).

![Screenshot of applying filters on grouped data in the Scope module.](/cms_trial/assets/0c2d297e-0069-4cb0-a7d4-5daceebfa592.png)

**Sort grouped tasks**

Once the tasks are grouped, the **Organize taska A/Z** and **Organize taska Z/A** options are **unavailable**. You can sort rows ascending by clicking the column header. The second click sets descending order.

**Inline edit fields**

When the grouping option is enabled, you can inline edit fields. To see changes, refresh the page.

See more on the Inline edit page.

![Screenshot of editing inline the Status field in the Scope module.](/cms_trial/assets/6b3e80d8-1295-4eb8-8b3d-263f645691ce.png)

**Limitations**

- The **Key** and **Summary** columns cannot be used for grouping.
- All WBS (task structure operations) are disabled - when task grouping is active, the WBS structure is ignored and can't be modified.
- **Grouping task limit = 50000 tasks**. If you have more than 50000 tasks in a box, use filters (search, quick filters, date filters etc.) to narrow the scope of the operation. Then, perform grouping.

To set a task limit on how many tasks a box can have to allow grouping, go to **App settings > App Configuration > Advanced > Technical Info**.

![contentId-1918830289](/cms_trial/assets/9b7e5502-cc32-467d-9ca2-1f20995b6651.png)

**Sorting grouped tasks**

The below applies to a situation when [task grouping](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298354243) is active.

**Sorting is initiated by clicking on the column header**

- Only tasks in groups are sorted (groups themselves are not sorted)
- Sorting is possible only for the fields that can be "organized by."

Sorting by clicking the header is **disabled when**:

- the sorted column is removed
- grouping mode is disabled (when grouping is inactive, use the "Data" option in the menu at the top > "Organize tasks")

  ![contentId-1918830289](/cms_trial/assets/af641844-b843-452d-b5c4-88517a1874a9.png)

When tasks are grouped, a **sorting action is triggered**:

- By clicking the column header (the first click sorts the task in ascending order, the next one descending)
- grouping conditions are changed
- page is refreshed

Sorting does not reflect field value changes (when tasks are already sorted, changing a value won't trigger an automatic recalculation)

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

![Screenshot of grouping tasks in the Scope module.](/cms_trial/assets/ce4e6984-d319-4597-8b7a-2db6f2d8eb78.png)

### Confirmation banner

When you activate a grouping, a confirmation banner appears at the top of the page; it tells you what groups are currently active.

Click X to close the banner - this will not deactivate the grouping.

![image-20261119-174843.png](/cms_trial/assets/02d14446-4370-4512-b6e9-fb29fcd59024.png)

### Color of a group

When grouping tasks in the Gantt module, the color is reflected:

- on the task structure
- on the timeline

![coloring-grouping.png](/cms_trial/assets/9024522c-05c1-4d7f-ab12-a03ab449b6b1.png)

## Deactivate grouping

You can click the **X** on the grouping bar to remove it the bar - this does **NOT** deactivate grouping. To deactivate grouping:

**Method 1**

1. Hover the mouse cursor over a group heading.
2. To deactivate one grouping element, click **X**.
3. To deactivate all grouping elements, click **Disable grouping**.

![Screenshot of deactivating grouping in the Gantt module.](/cms_trial/assets/7086e177-7edf-4c63-ae1b-c055d84fbcf1.png)

**Method 2**

1. Go to **View** > **Group tasks**.
2. Deactivate grouping by:

   1. Adjusting toggle switches.
   2. Using the **Deactivate all**button.
3. Click **Apply**.

![Screenshot of deactivating grouping in the Gantt module.](/cms_trial/assets/ba065dc3-cbbc-45f6-94bd-e1cfbe51c8a5.png)

## Available grouping options

To group using a specific field, make sure it is added as a column first.

#### Multi-level grouping

With the multi-level grouping method, tasks will be counted in each group. The group structure will be based on the active grouping elements. The order of grouping elements (fields) defines the group hierarchy.

A task **cannot** be duplicated, which means that a task can belong to a single group only.

### Grouping by status

If the grouping by Status is turned on, the groups are displayed in the following order:

- Open OKRs
- Closed OKRs
- TO DO work items
- IN PROGRESS work items
- DONE work items.

## Filter grouped tasks

The grouping functionality can be combined with other filters (such as search and quick filters).

![Screenshot of filtering grouped tasks in the Gantt module.](/cms_trial/assets/986cf984-24f8-4aa8-82fd-dbc4226283c5.png)

## Inline edit fields

When the grouping option is enabled, you can inline edit fields. To see changes, refresh the page.

See more on the [Inline edit](/cms_trial/space/SPM/1918637324/Inline+edit/) page.

## Limitations

- The **Key** and **Summary** columns cannot be used for grouping.
- All WBS (task structure operations) are disabled - when task grouping is active, the WBS structure is ignored and can't be modified.
- **Grouping task limit = 50000 tasks**. If you have more than 50000 tasks in a box, use filters (search, quick filters, date filters etc.) to narrow the scope of the operation. Then, perform grouping.

To set a task limit on how many tasks a box can have to allow grouping, go to **App settings > App Configuration > Advanced > Technical Info**.

![contentId-1918830289](/cms_trial/assets/9b7e5502-cc32-467d-9ca2-1f20995b6651.png)

## Sort grouped tasks

The following applies to a situation when task grouping is active.

When tasks are grouped, a **sorting action is triggered**:

- By clicking the column header (the first click sorts the task in ascending order, the next one descending).
- Grouping conditions are changed.
- The page is refreshed.

Sorting does not reflect field value changes (when tasks are already sorted, changing a value won't trigger an automatic recalculation).

## 