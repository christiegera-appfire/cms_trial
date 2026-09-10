# Release notes 30 April 2026

**Release date**: April 30, 2026

This page outlines the updates included in the latest release of Advanced Tables for Confluence.

Version: 7.1.0

---

## New features

## Advanced Table Viewer macro

### Column grouping

The Advanced Table Viewer macro now supports column grouping. You can group and organize table data interactively on the Confluence page.

- Once you enable column grouping, hover over any column header to display the grouping icon, and click it to group table data by that column.
- Nest grouping across multiple columns, up to one less than the total number of columns.
- For more information, refer to [Group columns with Advanced Table Viewer macro](/cms_trial/space/TBL/3211755580/Group+columns+with+Advanced+Table+Viewer+macro/).

  ![Advanced Table Viewer showing grouped columns with expandable rows and a grouping icon in the column header.](/cms_trial/assets/8c33c8db-17df-4dde-9c5e-0b3aaa316e7a.jpg)

### Pagination

The Advanced Table Viewer macro now includes pagination, enabling you to navigate large datasets efficiently on the Confluence page.

- Display the current row range and total row count (for example, showing 1–10 of 55 rows).
- Navigate across pages using the previous, next, and direct page number controls.
- Set the number of rows displayed per page using the **Rows per page** option.

  ![Table with pagination controls showing row range, page numbers, and a Rows per page dropdown at the bottom.](/cms_trial/assets/4e426bf4-d4d1-42c7-85a8-a850db5104de.jpg)

---

## Enhancements

## Advanced Table Viewer macro

### Summarize column calculations

The Sum-up type feature now includes new calculation types in addition to the existing **Sum** and **Average** types. For more information, refer to [Summarize column values with Advanced Table Viewer macro](/cms_trial/space/TBL/1540654683/Column+calculation+with+Advanced+Table+Viewer+macro/).

- **Minimum** - Returns the lowest numerical value in the column.
- **Maximum** - Returns the highest numerical value in the column.
- **Count** - Counts the total number of non-empty cells in the column.
- **Distinct** - Counts unique values only, ignoring duplicates and empty cells.

![Advanced Table Viewer displaying column summary options including Sum, Average, Minimum, Maximum, Count, and Distinct.](/cms_trial/assets/5b61aaf8-07af-414d-9f0a-b3c41b5894ce.jpg)

---

## Bug fixes

The following bugs are fixed in this release:

- Existing **JSON Table macros** on older pages using JSON URL failed to render data and returned an error.

  - This issue is resolved, and the JSON Table macro using JSON URL now renders data correctly as expected.
- Emojis were not rendering inside the **Table Plus macro**.

  - This issue is resolved, and emojis now render as expected.
- The simple date format link in the **Attachment Table macro** was pointing to an incorrect URL.

  - The link has been updated to reference the correct page.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/197/advanced-tables-for-confluence?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/197/advanced-tables-for-confluence?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Advanced Tables for Confluence!