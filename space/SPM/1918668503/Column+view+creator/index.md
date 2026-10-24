# Column view creator

The column view creator allows you to select and configure fields displayed as columns by the Gantt and Scope modules.

The list of available fields includes native Jira fields and custom fields added by Jira administrators and installed apps. When you connect other tools, fields used by these tools will also appear on that list. Such information will be displayed in the 'Origin column' of the available field list.

## Security and access

The column view creator works exactly the same at the box type and box levels. See the [Manage column views](/cms_trial/space/SPM/1918503715/Manage+column+views/) page.

| **Area** | **Security and access** |
| --- | --- |
| Box type configuration | Gantt / Scope column views:  Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Gantt / Scope** > **Column views**. |
| Hierarchy or timeline column views available in the Overview module:  Go to the **App Administration** > **Box type** > **choose the box type you want to edit** > **Overview > Hierarchy / Timeline column views**. |
| Box configuration | Gantt / Scope column views:  Go to **box configuration** > **Gantt / Scope** > **Column views**. |
| Hierarchy or timeline column views available in the Overview module:  Go to Go to **box configuration** > **Overview > Hierarchy / Timeline column views**. |

## Column views

You can add, edit, duplicate, and delete default column views in the box type configuration and column views available in the box configuration. The instructions apply to the Gantt and Scope modules.

### Available options

The table presents available features to configure for column views.

| **Feature** | **Description** |
| --- | --- |
| Columns preview | Preview your column setup. |
| Column configuration - Display | Select how to display the available data. The most common options include:   - Text - Lozenge - Date - Date with time   Fields such as Time Tracking have additional options:   - Progress - Progress with % - Reported/expected progress - Reported/expected progress %  contentId-1918668503contentId-1918668503 |
| Column configuration -Aggregation | Select how the data will be aggregated on the parent level of WBS:   - None - Minimum - Maximum - Sum - Sum without parent - Average - Average without parent - Children by status category (Sum without parent aggregation is used) - Children by status category % (Sum without parent aggregation is used)  contentId-1918668503 |
| Tree root | Select the field to display the WBS tree (task hierarchy). Screenshot of the Tree root column in the Columns View page of box configuration. For the field selected as the tree root, the [Expand / collapse levels](/cms_trial/space/SPM/1918536207/Layout/) feature is available. image-20250422-075902.png |
| Remove column | Remove the field column from the task list. contentId-1918668503 |
| Field name | List of available fields which can be added as a column to the task list. contentId-1918668503 |
| Field type | Type of available fields - depending on the type, different display and aggregation options will be available. |
| Add field | Add a field as a column. image2021-5-12_11-57-23.png |
| Column configuration | Select the display and aggregation settings. image2021-5-12_11-58-4.png |
| Field search box | Search the list of available fields. image2021-5-12_11-58-48.png |

### Add new column views

1. To add:

   1. Default column views (box type configuration) - go to **App Administration** > **Box type** > **choose the box type you want to edit** > **Gantt / Scope** > **Column views**.
   2. Column views (box configuration) - go to **box configuration** > **Gantt / Scope** > **Column views**.
2. Click the **Add new Column View** button.
3. On the **New Column View** modal, provide a summary of the new view, set the visibility to public or private, and (optionally) write some description.

   ![New column view modal on the box configuration page.](/cms_trial/assets/4809619b-f53d-4a89-8c6a-b22c2d963573.png)
4. Click **Create** to enter the column view creator.
5. In the **column view creator**, add the fields from the field list on the right to the column view area on the left using the **+** (**plus**) icon next to the field name. Alternatively, drag and drop the selected field (the area on the left will be highlighted with a green color).

   ![Column view creator on the box configuration page.](/cms_trial/assets/64549ad2-eb5e-460e-a207-d5ef9b331c98.png)

We recommend using the 'Built-in" type of fields which display field values from all synchronized fields in Jira and connected tools. For example, the "Start date" built-in field shows the date values from all fields mapped as the start date in the [Field configuration](/cms_trial/space/SPM/1918635376/Fields/) and from connected tools, such as Trello.

1. These fields correspond to the columns you will see on your task list in the Gantt or Scope module.  
   When you add or drag a selected field, you can rearrange its order by dragging it again. You can also delete it from the column view. Additionally, if the field supports data aggregation, you can set the aggregation method for the fields you added.

   ![Field data aggregation.](/cms_trial/assets/489e1e62-22e3-4165-a8c1-0f96aed42ece.png)
2. If you want to check how your new column view will look, click the **Preview** panel at the bottom of the column view creator.

   ![Column view preview.](/cms_trial/assets/fbd13919-bb65-42f9-8754-72cdee9dd869.png)
3. When you are happy with your new column view, click the **Save** button and return to the column view list. Your new column view is at the bottom of the list by default, but you can rearrange the order of the views.

   ![New column view on the column view list.](/cms_trial/assets/19abd73e-1424-4c1d-9045-a1749e9e6a11.png)
4. A new column view does not automatically become active (current). To activate it, you need to select it from the current view drop-down menu in the Gantt or Scope module.

   ![Drop-donw menu under the current view in the Gantt module.](/cms_trial/assets/84af6ad9-69a6-4409-a667-12951085b78c.png)

### Edit column views

1. To edit:

   1. Default column views (box type configuration) - go to **App Administration** > **Box type** > **choose the box type you want to edit** > **Gantt / Scope** > **Column views**.
   2. Column views (box configuration) - go to **box configuration** > **Gantt / Scope** > **Column views**.
2. Click the **Details** button to modify details.

   ![A list of column views on the box configuration page. On the right-hand side, you can find the Details button that allows you to rename your column view.](/cms_trial/assets/7e08c761-6234-4ad1-8bc5-3124d53ab355.png)
3. To edit and rearrange fields (columns) within a particular column view, click the column view name. You’ll be redirected to the column view creator.

   ![2025-02-10_10-12-12.mp4](/cms_trial/assets/bf8e5f1f-13ef-4132-9b0c-a0b912087063.mp4)
4. Alternatively, if you are a box admin, you can add and remove columns (and change their aggregation) directly on the task list side. When you modify the current view, click the **Save changes** button (floppy disk icon) next to the current view box.

   ![Save changes button i nthe Gantt module.](/cms_trial/assets/270b4d5f-31ee-48ed-b546-9bdd4ba57e10.png)

### Duplicate column views

You can duplicate an existing view and adjust it to your needs. Click the **Duplicate** button to create a copy of the selected column view. A copy of the column will appear at the bottom of the list.

![A list of column views on the box configuration page. On the right-hand side, you can find the Duplicate button that allows you to duplicate your column view.](/cms_trial/assets/7808c6fc-e65c-4359-8b7f-a4d25f8c758c.png)

### Delete column views

To delete a column view, click the **Delete** button and confirm your action.

You can’t delete the active view. Your list must also have at least one column view defined.

![Use the Delete button to delete any of your column view but the active one.](/cms_trial/assets/9c0bac58-9bc0-4bbe-9061-be23e60c9217.png)

## Active column view

When you apply one of the available views in the Gantt / Scope module, the view becomes active. On the box configuration page, a green check mark will appear next to its name. This active view means that it will be applied whenever a user opens or returns to the Gantt / Scope module.

|  |  |
| --- | --- |
| Active column view in the Gantt module view. | Active column view on the box configuration page. |

## Filters' effect on aggregations

Active filters (Quick filters, search, date range filter) don't impact aggregation results. All tasks are taken into account during a calculation, even if they have been filtered out and are hidden.

![image2021-12-6_1-47-3.png](/cms_trial/assets/0f62df5c-9a81-4180-b186-231cc7292077.png)

## Ordering of column views

Default Box Types have default views set to their default order. If non-default views are present, they are put in alphabetical order after all the default ones.

Boxes created from default Box Types have views set to their default order. If non-default views are present, they are put in alphabetical order after all the default ones.

All views in non-default Box types are in alphabetical order.

## Column views options

Users have consistent column view permissions for different elements (WBS widget, Risks, Board backlog, Gantt module).

They can:

- modify a column view (changes are not visible to other users)
- restore column view settings to the default one set by the box admin.