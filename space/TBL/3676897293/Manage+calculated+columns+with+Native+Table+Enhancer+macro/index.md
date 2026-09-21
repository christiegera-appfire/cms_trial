# Manage calculated columns with Native Table Enhancer macro

The Native Table Enhancer macro enables you to create custom calculated columns using values from other columns.

- You can configure the calculated columns in the macro setup mode.
- The macro displays the calculated columns in Confluence page edit and view mode.

## Manage calculated columns

[Unmapped macro: refined-tab — no content to fall back on]

You need edit permissions to access the setup mode.

- To add a calculated column, edit the macro to open setup mode. Refer to [Set up the Native Table Enhancer macro features](/cms_trial/space/TBL/3568173057/Set+up+the+Native+Table+Enhancer+%5BBeta%5D+macro+features/).

  ![Native Table enhancer_edit macro.png](/cms_trial/assets/05094c3d-0192-41fd-b989-78c1dc3c875e.png)
- Click **Manage** **columns** (▢). The **Manage columns** feature configuration panel appears on the right side of the screen.
- To add a new calculated column, either click **Add calculated column** under **Calculated columns**, or click **+** at the end of the column headers in the left panel.

  ![Native Table Enhancer_Manage columns.png](/cms_trial/assets/902be5b6-2c3f-41cc-abcb-10851986a82b.png)

- The *Add calculated column* dialog opens. It lets you derive new column data from existing column values on a row-by-row basis.

  - **Column name**: Enter the name for the new calculated column.
  - To perform calculations, you can use either **Builder** or **Formula** mode.

    - To use Builder, refer to the **Builder** section on this page.
    - To use Formula, refer to the **Formula** section on this page.

      ![Native Table Enhancer_Add calculated column.png](/cms_trial/assets/97ea98d0-421f-47d3-b3a4-7507a95e4d45.png)

## **Builder**

- The **Builder** tab provides a user-friendly interface to configure simple mathematical operations without writing custom syntax. For more information, refer to **Supported formulas** section on this page.

  - **Operation:** Select the mathematical function from the dropdown, such as Sum, Minus, Multiply, or Divide, to execute across your chosen columns.
  - **Columns to calculate**: The columns dropdown displays only the numeric columns from the table.

    - Choose columns from the dropdown selectors to include in the calculation. As you select a column, the next dropdown selector shows the remaining numeric columns.
    - For example, to calculate the *Total cost*, choose **Operation** as *Sum and* **Columns to calculate** as *Unit price ($)* and Annual Maintenance ($).
    - To add an additional column in the **Sum** operation, click **Add column**.

      ![Native Table Enhancer_Add column.png](/cms_trial/assets/66492259-c27a-48ab-ad5a-d02bc76f7e44.png)
    - The builder adds another column dropdown selector. Select the required column, for example, *Shipping Cost ($)*.

      ![Native Table Enhancer_Add another column.png](/cms_trial/assets/17c84deb-1bef-4cf6-8a6f-c690125e3433.png)
  - As you choose the operation and select columns, the builder displays the saved formula and a preview of three table rows with the chosen columns and the new calculated column.
  - In the preview, the macro displays the new calculated column with a blue highlight and the prefix *fx.*
  - To add the configured column to the table, click **Save**.

    ![Native Table Enhancer_Builder_Sum.png](/cms_trial/assets/5aade846-2f5a-4efb-91eb-46b76cd57d90.png)

- Click the delete (▢ )icon next to a column name to remove it from the calculation.
- To include additional columns in the operation, click **Add column**. If all columns have been selected for the operation, then you cannot add more columns and the **Add column** button is disabled.

  ![ATV_No numeric column left.png](/cms_trial/assets/05ac040d-fece-4c49-88ac-5cfa305696f9.png)
- The macro displays an error message if you try to save the calculated column with a column name that already exists or without selecting columns to calculate.

- The macro setup mode displays the new calculated column in the left panel.
- You can manage the calculated columns in the right panel. To edit and delete the calculated columns, refer to the **Edit or delete calculated columns** section on the page.

  ![NTE_column added from builder tab.png](/cms_trial/assets/6daff666-fc9c-48ef-ba3a-ece1df54f107.png)
- Click **Save** and publish the changes. Both the page edit and view modes display the table with the newly added calculated column without the *fx* prefix.

  ![Native table_Page view mode with new column.png](/cms_trial/assets/e1bf8126-0301-46dd-9cca-c6ba6fc554e7.png)

## **Formula**

The **Formula** tab lets you write custom formulas using a formula editor. You can write simple or conditional formulas, similar to spreadsheet-like expressions. For more information, refer to the **Supported formulas** section on this page.

![Native Table_Add calculated column_Formula.png](/cms_trial/assets/8e1acee7-cad9-4c18-b85c-40ee319a73cc.png)

- **Enter formula**: Enter the formula to calculate using values from the table columns. Type '[' and the macro displays the list of column names. You can reference any source column type.

  - Type the formula using operators (such as +, -, \*, /, or conditional functions) and insert columns by typing `[` to select them from the list.
  - The macro displays a preview of three table rows with the chosen columns and the new calculated column.
  - In the preview, the macro displays the new calculated column with a blue highlight and the prefix *fx.*
  - For example, the formula checks for **Stock Qty** and returns *1* or *0* values for the Needs Reorder (Flag) column.

    ![Native table_custom column_If condition.png](/cms_trial/assets/9f6fb75b-3b6e-4772-a309-a671515311bf.png)

The macro displays an error message if you try to save the calculated column with a column name that already exists or if the syntax is invalid.

- - To add the configured column to the table, click **Save**.
  - The macro setup mode displays the new calculated column in the left panel.
  - You can manage the calculated columns in the right panel. To edit and delete the calculated columns, refer to the **Edit or delete calculated columns** section on the page.

    ![Native Table_column added from Formula tab.png](/cms_trial/assets/2535412f-4908-4cc4-b5c5-ab4cdaeab000.png)

- Click **Save** and publish the changes. Both the page edit and view modes display the table with the newly added calculated column without the *fx* prefix.

  ![Native Table enhancer_new calc column in page view mode.png](/cms_trial/assets/13a15d0d-0ab0-48a6-aaa2-631a91669c75.png)

[Unmapped macro: refined-tab — no content to fall back on]

After you create a calculated column, you can manage it under **Manage columns**.

The **Calculated columns** section displays the list of created calculated columns. You can edit or delete the calculated column.

**Edit calculated column**

- To edit a calculated column, click **Edit**.

  ![Native Table Enhancer_column_Edit.png](/cms_trial/assets/9cd5f5f9-a9c4-45ce-9e17-d7383f245e6c.png)

- After you add a new calculated column, you can also edit it from the **Edit column** option in the column header.

  ![Native Table_setup mode_Edit calculated column.png](/cms_trial/assets/6ccd0385-cf4d-4943-9d5a-53ecbe644edb.png)

- The *Edit calculated column* dialog opens. You can make the required changes and save the calculated column. The configuration remains similar to adding a calculated column. For more information, refer to the **Add calculated column** section.

  ![Native table_Edit calculated column.png](/cms_trial/assets/23cfc5b4-ec57-4339-ac8d-64d0648bb3f9.png)

**Delete calculated column**

- To delete a calculated column, click **Delete,** and the column is removed from the list. To apply the change, click **Save**.

  ![Native table enhancer_Delete calc column.png](/cms_trial/assets/0ebfc5d3-8f67-4eba-93dd-0de197ee5895.png)

[Unmapped macro: refined-tab — no content to fall back on]

The Builder tab supports simple, single-operation math on numeric columns with no syntax to write. The Formula tab supports full spreadsheet-like expressions — operators, functions, conditionals, and any source column type.

## Operators and functions

| **Capability** | **Builder tab** | **Formula tab** |
| --- | --- | --- |
| **Column references** | Numeric source columns only (`[Column Name]`) | Any source column by name (`[Column Name]`) |
| **Sum (**`+`**)** | Yes, supports 3+ columns | Yes |
| **Minus (**`-`**)** | Yes, 2 columns only | Yes |
| **Multiply (**`*`**)** | Yes, supports 3+ columns | Yes |
| **Divide (**`/`**)** | Yes, 2 columns only | Yes |
| **Mixed operators in one expression** | No — one operator per calculated column | Yes, with standard precedence (`[A] + [B] * [C]`) |
| **Parentheses** | No | Yes (`([A] + [B]) * [C]`) |
| **Numeric / string / boolean literals** | No | Yes (`100`, `10.5`)  Yes (`"Done"`, `'Open'`)  Yes (`TRUE`, `FALSE`) |
| **Comparisons** (`>`, `<`, `>=`, `<=`, `=`, `<>`) | No | Yes |
| **Row-wise functions** — `SUM()`, `AVERAGE()`, `MIN()`, `MAX()`, `ABS()`, `ROUND()`, `IF()` | No | Yes, evaluated across the arguments in the current row |
| **Unary minus** | No | Yes (`-[A] + [B]`) |
| `SUMIF` **/** `COUNTIF` **/** `AVERAGEIF` | No | No — these are column-level aggregates, not per-row calculations |

## Examples

| Tab | Expression | Result |
| --- | --- | --- |
| Builder | SUM: Budget, Spend, Tax →  `[Budget] + [Spend] + [Tax]` | Sum |
| Builder | Minus: Budget, Spend →  `[Budget] - [Spend]` | Difference |
| Builder | Multiply: Qty, Rate →  `[Qty] * [Rate]` | Product |
| Builder | Divide: Total, Count →  `[Total] / [Count]` | Quotient |
| Formula | `[Budget] - [Spend]` | Difference |
| Formula | `[A] + [B] * [C]` | A + (B × C), respecting operator precedence |
| Formula | `IF([Status] = "Done", 1, 0)` | Conditional value |
| Formula | `SUM([A], [B], [C])` | Sum of three cells in the same row |
| Formula | `ROUND([Total] / [Qty], 2)` | Rounded ratio |