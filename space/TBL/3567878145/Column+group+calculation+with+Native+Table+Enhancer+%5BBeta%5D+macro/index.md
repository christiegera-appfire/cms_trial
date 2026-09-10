# Column group calculation with Native Table Enhancer [Beta] macro

The Native Table Enhancer macro enables you to perform column calculations and display summarized values at each level of the nested group.

The Native Table Enhancer macro is currently in beta. [Learn more](/cms_trial/space/TBL/3520037211/Native+Table+Enhancer+%5BBeta%5D+macro/).

## Group calculation overview

Group calculation supports the following calculation types: Sum, Average, Minimum, Maximum, Count, and Distinct. For each group, the macro calculates a summarized value from its nested groups and displays it in each grouped row.

- To apply group calculation, you must first group the required columns. Refer to [Group columns with Native Table Enhancer macro](/cms_trial/space/TBL/3559129118/Group+columns+with+Native+Table+Enhancer+%5BBeta%5D+macro/).
- You can configure only one group calculation type for each ungrouped column.
- For grouped columns, only column-level calculations apply.
- You can configure group calculations only in macro setup mode. You cannot change it in Confluence page view mode.
- The macro displays the configured values in the Confluence page view mode.

  ![Edit group calculation dialog](/cms_trial/assets/e73542a3-4365-44cc-b141-91245abfe978.png)

## Manage group calculations

[Unmapped macro: refined-tab — no content to fall back on]

You can perform the following group calculations.

| **Type** | **Description** | **Column type** | **Indicator on the Confluence page** |
| --- | --- | --- | --- |
| None | Disables the group calculation: no value is displayed for the column | Any | Not applicable |
| Sum | Calculates the total of all values in the column | Numeric | Sum |
| Average | Calculates the average of all values in the column | Numeric | Avg |
| Minimum | Returns the lowest numerical value in the column | Numeric | Min |
| Maximum | Returns the highest numerical value in the column | Numeric | Max |
| Count | Counts the total number of non-empty cells in the column | Numeric, String, Date | Cnt |
| Distinct | Counts unique values only, ignoring duplicates and empty cells | Numeric, String, Date | Disct |

[Unmapped macro: refined-tab — no content to fall back on]

Follow the steps to configure group calculation for any column.

You need edit permissions to access the macro setup mode.

1. Edit the macro to open setup mode. Refer to [Set up the Native Table Enhancer macro features](/cms_trial/space/TBL/3568173057/Set+up+the+Native+Table+Enhancer+%5BBeta%5D+macro+features/).   
   Each column displays an *Edit column* ( ▢ ) option.
2. To set up the group calculation for any column, navigate to **Edit column** > **Edit group calculation**.

   ![To set up the group calculation for any column, click Edit group calculation](/cms_trial/assets/d3569c9c-9955-41ce-80f6-5814e97f67af.png)
3. For example, to apply group calculation to the **Unit Price** column at the **Category** level:

   1. First, group the **Category** column. To start grouping, click **Enable grouping**, then hover over the Category column header, and click the grouping icon to group table data by that column. For more information, refer to [Group columns with Native Table Enhancer macro](/cms_trial/space/TBL/3559129118/Group+columns+with+Native+Table+Enhancer+%5BBeta%5D+macro/).
   2. Then, navigate to column **Unit Price** > **Edit column** > **Edit group calculation** and select **Average**.

      ![Select the required Sum-up type in Edit group calculation dialog](/cms_trial/assets/b726b818-4994-466e-9626-3453975e4fd3.png)
   3. The macro calculates the average of product rows within each group and displays the result on each category group row.

      ![Summarized values at each group level](/cms_trial/assets/c92d51b7-3555-4731-9556-7fb01c677413.png)
   4. You can further apply grouping on the required columns and nest groups. The average unit price rolls up and displays at all group levels.

      ![Group column calculation at nested levels](/cms_trial/assets/05377cd1-c31d-4548-901b-f3c4097247cb.png)
   5. You can configure group calculation for multiple columns. For example, applying **Minimum** to the **Stock Qty** column displays the minimum stock quantity at all group levels.

      ![Apply group calculation for multiple columns](/cms_trial/assets/af6154b9-0cb2-4d6d-9661-3a4f6e6f8a04.png)

- Group calculation does not affect the configured column-level calculation type. For example, if you set **Maximum** as the column-level calculation for Unit Price and **Minimum** for Stock Qty, these values remain unchanged when you apply or remove group calculation.

  ![Group calculation does not affect the configured column-level calculation type](/cms_trial/assets/d5d8fd86-a028-48c7-b466-6069dd244192.png)

[Unmapped macro: refined-tab — no content to fall back on]

1. To disable group calculation for any column, navigate to **Edit column** > **Edit group calculation** and select **None.**

   - For example, to disable the group calculation for the **Stock Qty** column:

     1. Click the **Stock Qty** Edit column. The **Edit group calculation** dialog opens.
     2. Select **None**, and click **Save**.

        ![To disable group calculation for any column, select None](/cms_trial/assets/a2066379-a999-420e-ba0c-8e8cd5fe0e0a.png)
2. To disable group calculation for all columns in the table, edit the macro and click **Disable grouping** (▢ ).

   ![Disable grouping](/cms_trial/assets/9a04d62c-210c-4f81-8726-5f6fbd4b834b.png)