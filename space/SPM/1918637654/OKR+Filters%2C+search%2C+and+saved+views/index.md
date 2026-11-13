# OKR Filters, search, and saved views

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

In the OKR module, you can customize your current view for greater flexibility and efficiency in OKR management. When you modify your current view, you can save it to switch to it later or share it with other stakeholders.

## Modify the current view

![okr-header-2.png](/cms_trial/assets/f33be9cb-ca4d-4d45-a0e4-2d8f25232706.png)

Your current view can be modified in the following ways:

| **View modifier** | **Page/Location** | **Description** |
| --- | --- | --- |
| OKR Period | Available:   - Overview - Dependencies - Hierarchy - Progress Dashboard   Modifies:   - Overview - Dependencies - Hierarchy - Progress Dashboard | Use the period selector to display OKRs scheduled for a specific period or periods. |
| Filters | Available:   - Overview - Dependencies - Hierarchy - Progress Dashboard   Modify:   - Overview - Dependencies - Hierarchy - Progress Dashboard | Filter OKRs by Owner, Teams, Labels, and more to see only the OKRs you want. |
| Column filters | Available:   - Overview - Dependencies   Modify:   - Overview - Dependencies - Hierarchy - Progress Dashboard | Filter and sort individual Overview columns. |
| Column search bar | Available:   - Overview - Dependencies   Modifies:   - Overview - Dependencies - Hierarchy - Progress Dashboard | Search a specific OKR by its name. |
| Sort a column | Available:   - Overview - Dependencies   Modifies:   - Overview - Dependencies | Sort a column A-Z or Z-A. |

### OKR Period

![Period selector. The Q3 Y2025 is selected.](/cms_trial/assets/e72ba33f-be47-4f34-a7b3-036f5c5bf017.png)

The period selector lets you select a period from the list to display OKRs planned for that period (for example, Q3 Y2025). The selector heading shows the period you select.

The selected period displays matching OKRs on the *Overview*, *Dependencies*, *Hierarchy*, and *Progress Dashboard* pages.

Use **X** on or next to the selected period to clear it. Alternatively, clear the period on the list.

### Filters

By default, three filters are displayed. Click **More filters** to show all available filters and use the scroll bar to view them. The filter you select displays matching OKRs on the *Overview*, *Dependencies*, *Hierarchy*, and *Progress Dashboard* pages.

Use **x** on or next to the selected filter value to clear it. Alternatively, clear or unselect the value from the list.

### Column filters

You can filter each individual column by its respective value. Click the **filter icon** on a column and then, depending on the column type, check or enter a value.

![OKR column filter.](/cms_trial/assets/73a82b39-e9b8-4167-843e-a96432086b9a.png)

Column filters are available on the *Overview* and *Dependencies* pages. Each active column filter is counted, and the total is displayed directly on the column.

#### Filters vs column filters

The **Filters** button and the **column filters** on the *Overview and Dependencies* pages do the exact same thing: they control which OKRs you see across the *Overview*, *Hierarchy*, and *Progress Dashboard* pages.

Any filter you apply, whether through the **Filters** button or a column, will appear in both places (under the **Filters** button and in the relevant column).

The only exception is the **Period** filter. This one only appears as a column filter and is directly linked to the **Period filter**. When you select a period, it automatically applies to the **Period** column filter.

| **Period filter** | **Filters** | **Column filters** |
| --- | --- | --- |
| - Period | - Owner - Teams - Labels (mul - OKR type - Progress - Collaborators - Status - Weight - Latest Update - Days since last update - Date of last update - Expected start date - Expected end date - Start Value - Current Value - Target Value - Grade | - Period - Owner - Teams - Labels - OKR type - Progress - Collaborators - Status    - You can additionally filter OKRs that have missed their latest milestone. - Weight - Latest Update - Days since last update - Date of last update - Expected start date - Expected end date - Start Value - Current Value - Target Value - Grade |

### View

The **View** options control the visibility of OKRs and connected items on the Overview page.

![A dropdown under the View button on the OKR Overview page.](/cms_trial/assets/9dc3d93f-005c-48f6-b59d-c5a0c440ca49.png)

#### Show

The respective checkboxes determine what items will be visible and hidden from your OKR view:

- **Descendants of filtered OKRs** - check to show child OKRs in the filtered results.
- **Ascendants of filtered results** - check to show parent OKRs in the filtered results.
- **Connected Jira work items** - check to show Jira work items that are connected to Key Results.
- **Connected boxes** - check to show boxes that are connected to Key Results.

To see the issues connected to the KRs on the OKR Overview page, make sure you have the e **Displaying connected issues** **in the OKR Overview** option enabled in **Settings** > **General**.

#### Levels

Expand or collapse all sub-items and show only top-level OKRs.

### Column layout

The **plus icon** at the end of the column layout opens a separate panel that displays all columns in the column view. You can customize individual columns:

- Click the **padlock** icon to lock a column (a locked column cannot be repositioned but can be hidden).
- Check or clear to show or hide a column.
- Drag and drop a column to change the column order.

### Column search bar

The **OKR Name** column includes a search bar that lets you find a specific OKR by name. You can search a column only on the Overview page.

![search bar on the okr name column.](/cms_trial/assets/b18578f2-8f42-47dd-9374-c5139b98cd8a.png)

### Sort a column

Each column can be sorted A-Z and Z-A.

1. Click the **Sort** icon to sort it in descending order.
2. Click again to sort it in ascending order.
3. Click one more time to remove sorting.

You can sort one column at a time.

## OKR custom views

If you have dozens of OKRs in your box, you can combine multiple filters, layout display settings, and a search keyword to customize your view to see only the OKRs you need. Once you set up your perfect filtered view, you can save it so you do not have to reapply the filters or search queries.

- You can save views on the **OKR Overview**, **OKR Hierarchy**, and **Progress Dashboard** pages.
- Custom column width and column sorting are not saved.
- Saved views are shared globally, so other users can access and use them too.

### Save as a new view

To save your new view:

1. Click the **Save as new view** button. The button appears once you modify your view.
2. On the **Create New view** modal,enter your new view name.
3. Click **Save** to finish the process.

![Clicking the save button opens a menu with options to overwrite view, save as new view, or discard changes.](/cms_trial/assets/f261f599-94f0-467b-8067-96a1e2b2c067.png)

### Overwrite the view

The saved view can be modified by you or other permitted users. If you apply a change, you can:

- Save the current view as a new view (recommended if the current saved view you modified was created by someone else).
- Overwrite the current view without creating a new one.

Click the arrow next to the **Save as new view** button to save the changes to the current view.

### Switch to the new view (OKR view switcher)

The view switcher lets you navigate between the default and [saved views](https://appfire.atlassian.net/wiki/spaces/SPMDRAFT/pages/1673593469/OKR+Filters+search+and+saved+views#Save-OKR-views) in the OKR module. It also lets you search, star (add to favorites), delete, edit, and share selected views.

![OKR view switcher expanded.](/cms_trial/assets/69a8fade-1392-4e62-b9f3-8b75f3245ef8.png)

The view switcher consists of the following elements:

| **View switcher** |
| --- |
| **Search** | A search bar for saved views. |
| **All** | A list of all saved views (by default, the five newest views are shown) |
| **Favorites** | A list of favorite saved views. Click the star icon next to the saved view name to add it to Favorites. |
| **More actions** (**…**) | Opens a contextual menu to share, edit, and delete a saved view. |

To add a view to your favorites, click the **star icon** next to the view name.

### Manage saved views

You can rename and delete saved views on the **Settings** > **Saved views** page. There, you will see a list of all the views saved on your instance. Alternatively, you can edit and delete saved views directly in the **view switcher**.

Saved views management requires one of the following [permissions](/cms_trial/space/SPM/1918765815/OKR+module+permissions/):

- Jira Admin
- In-module Admin
- **Change company settings** (basic permission)
- **Manage Custom views** (advancedpermission)