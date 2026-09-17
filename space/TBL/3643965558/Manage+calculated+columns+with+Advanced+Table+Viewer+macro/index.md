# Manage calculated columns with Advanced Table Viewer macro

The Advanced Table Viewer macro enables you to create calculated columns using values from other columns.

- You can configure the calculated columns in the macro setup mode.
- The macro displays the calculated columns in Confluence page edit and view mode.

## Manage calculated columns

[Unmapped macro: refined-tab — no content to fall back on]

You need edit permissions to access the setup mode.

- To add a calculated column, edit the macro to open setup mode. Refer to [Set up the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/).

  ![ATV_Edit macro.png](/cms_trial/assets/1df1b22f-a8da-4e59-a39c-d9abc3391c4b.png)
- Click **Manage** **columns** (▢). The **Manage columns** feature configuration panel appears on the right side of the screen.
- To add a new calculated column, either click **Add calculated column** under **Calculated columns**, or click **+** at the end of the column headers in the left panel.

  ![ATV_Manage columns_panel.png](/cms_trial/assets/e4f3cb40-1e64-43dc-81c1-760565c0f295.png)

- The *Add calculated column* dialog opens. It lets you derive new column data from existing column values on a row-by-row basis.

  - **Column name**: Enter the name for the new calculated column.
  - To perform calculations, you can use either **Builder** or **Formula** mode.

    - To use Builder, refer to the **Builder** section on this page.
    - To use Formula, refer to the **Formula** section on this page.

      ![ATV_Add calculated column](/cms_trial/assets/cff86676-ded3-41ff-90e3-71ff5e9dd16b.png)

## **Builder**

- The **Builder** tab provides a user-friendly interface to configure simple mathematical operations without writing custom syntax. For more information, refer to **Supported formulas** section on this page.

  - **Operation:** Select the mathematical function from the dropdown, such as Sum, Minus, Multiply, or Divide, to execute across your chosen columns.
  - **Columns to calculate**: The columns dropdown displays only the numeric columns from the table.

    - Choose columns from the dropdown selectors to include in the calculation. As you select a column, the next dropdown selector shows the remaining numeric columns.
    - For example, to calculate the *Total cost*, choose **Operation** as *Sum and* **Columns to calculate** as *Budget Allocated (USD)* and Contingency Budget (USD).
    - To add an additional column in the **Sum** operation, click **Add column**.

      ![ATV_Builder_two columns.png](/cms_trial/assets/b4e7f620-31fd-4a7e-a88d-3176f07ea4d9.png)
    - The builder adds another column dropdown selector. Select the required column, for example, *Overhead Cost (USD)*.

      ![ATV_Builder_three columns.png](/cms_trial/assets/f52763e9-831e-4306-af2c-27e73a6c9dc2.png)
  - As you choose the operation and select columns, the builder displays the saved formula and a preview of three table rows with the chosen columns and the new calculated column.
  - In the preview, the macro displays the new calculated column with a blue highlight and the prefix *fx.*
  - To add the configured column to the table, click **Save**.

    ![ATV_Builder_Sum_Operation.png](/cms_trial/assets/d6a9792f-7a2f-4d34-a040-d478d7036373.png)

- Click the delete (▢ )icon next to a column name to remove it from the calculation.
- To include additional columns in the operation, click **Add column**. If all columns have been selected for the operation, then you cannot add more columns and the **Add column** button is disabled.

  ![ATV_No numeric column left.png](/cms_trial/assets/702466be-3136-4e95-9d2e-25d44f4bee90.png)
- The macro displays an error message if you try to save the calculated column with a column name that already exists or without selecting columns to calculate.

- The macro setup mode displays the new calculated column in the left panel.
- You can manage the calculated columns in the right panel. To edit and delete the calculated columns, refer to the **Edit or delete calculated columns** section on the page.

  ![ATV_macro setup_calculated column added.png](/cms_trial/assets/3e1d7d4c-3608-4b95-b66b-bb6784a7d3da.png)
- Click **Save** and publish the changes. Both the page edit and view modes display the table with the newly added calculated column without the *fx* prefix.

  ![ATV_Page view mode_calculated columns.png](/cms_trial/assets/cd4e2124-286d-4273-becd-09638a883277.png)

## **Formula**

The **Formula** tab lets you write custom formulas using a formula editor. You can write simple or conditional formulas, similar to spreadsheet-like expressions. For more information, refer to the **Supported formulas** section on this page.

![ATV_Formula tab.png](/cms_trial/assets/e5164fc4-2433-4cc5-8772-23024ff6e6cf.png)

- **Enter formula**: Enter the formula to calculate using values from the table columns. Type '[' and the macro displays the list of column names. You can reference any source column type.

  - Type the formula using operators (such as +, -, \*, /, or conditional functions) and insert columns by typing `[` to select them from the list.
  - The macro displays a preview of three table rows with the chosen columns and the new calculated column.
  - In the preview, the macro displays the new calculated column with a blue highlight and the prefix *fx.*
  - For example, the formula checks for **Budget risk** and returns *True* or *False* values for the Budget risk column.

    ![ATV_Formula_If condition.png](/cms_trial/assets/608493cc-9f50-4810-a778-c5cb3d273ce9.png)

The macro displays an error message if you try to save the calculated column with a column name that already exists or if the syntax is invalid.

- - To add the configured column to the table, click **Save**.
  - The macro setup mode displays the new calculated column in the left panel.
  - You can manage the calculated columns in the right panel. To edit and delete the calculated columns, refer to the **Edit or delete calculated columns** section on the page.

![ATV_Formula_column in setup mode.png](/cms_trial/assets/6849d072-5070-4768-bbc9-324d9d89917a.png)

- Click **Save** and publish the changes. Both the page edit and view modes display the table with the newly added calculated column without the *fx* prefix.

![ATV_Formula_Page view.png](/cms_trial/assets/4d227200-2993-47d4-a11f-e5fc3ad8be9f.png)

[Unmapped macro: refined-tab — no content to fall back on]

After you create a calculated column, you can manage it under **Manage columns**.

The **Calculated columns** section displays the list of created calculated columns. You can edit or delete the calculated column.

**Edit calculated column**

- To edit a calculated column, click **Edit**.

  ![ATV_Calculated column_click Edit.png](/cms_trial/assets/9aa56a99-26bf-44ec-9783-c882b5e1a440.png)

- After you add a new calculated column, you can also edit it from the **Edit column** option in the column header.

  ![ATV_Edit column.png](/cms_trial/assets/532e6b79-c230-4fe0-8e34-393b6edeb449.png)

- The *Edit calculated column* dialog opens. You can make the required changes and save the calculated column. The configuration remains similar to adding a calculated column. For more information, refer to the **Add calculated column** section.

  ![ATV_Edit_calculated column_dialog.png](/cms_trial/assets/c3393f83-6362-4022-ad90-c151d74bfcbb.png)

**Delete calculated column**

- To delete a calculated column, click **Delete,** and the column is removed from the list. To apply the change, click **Save**.

  ![ATV_calculated column_click Delete.png](/cms_trial/assets/7154c91a-b3b8-48c1-91d4-922ea43a19e4.png)

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