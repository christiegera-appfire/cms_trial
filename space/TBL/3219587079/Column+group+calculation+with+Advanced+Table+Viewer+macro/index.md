# Column group calculation with Advanced Table Viewer macro

The Advanced Table Viewer macro enables you to perform column calculations and display summarized values at each level of the nested group.

## Group calculation overview

Group calculation supports the following calculation types: Sum, Average, Minimum, Maximum, Count, and Distinct. For each group, the macro calculates a summarized value from its nested groups and displays it in each grouped row.

- To apply group calculation, you must first group the required columns. Refer to [Group columns with Advanced Table Viewer macro](/cms_trial/space/TBL/3211755580/Group+columns+with+Advanced+Table+Viewer+macro/).
- You can configure only one group calculation type for each ungrouped column.
- For grouped columns, only column-level calculations apply.
- You can configure group calculation only in macro setup mode. You cannot change it in Confluence page view and edit mode.
- The macro displays the configured values in the Confluence page view and edit mode.

![Edit group calculation dialog showing Sum-up type options.](/cms_trial/assets/b99d6a72-b454-4355-bd4a-a64a3877f888.jpg)

## Manage group calculations

[Unmapped macro: refined-tab — no content to fall back on]

You can perform the following group calculation.

| **Type** | **Description** | **Column type** | **Indicator on the Confluence page** |
| --- | --- | --- | --- |
| None | Disables the sum-up calculation - no value is displayed for the column | Any | Not applicable |
| Sum | Calculates the total of all values in the column | Numeric | Sum |
| Average | Calculates the average of all values in the column | Numeric | Avg |
| Minimum | Returns the lowest numerical value in the column | Numeric | Min |
| Maximum | Returns the highest numerical value in the column | Numeric | Max |
| Count | Counts the total number of non-empty cells in the column | Numeric, String, Date | Cnt |
| Distinct | Counts unique values only, ignoring duplicates and empty cells | Numeric, String, Date | Disct |

[Unmapped macro: refined-tab — no content to fall back on]

Follow the steps to configure group calculation for any column.

You need edit permissions to access the macro setup mode.

1. Edit the macro to open setup mode. Refer to [Set up the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/).   
   Each column displays an *Edit column* ( ▢ ) option.
2. To set up the group calculation for any column, navigate to **Edit column** > **Edit group calculation**.

   ![Edit column with Edit group calculation selected. ](/cms_trial/assets/6c149a73-f936-4ee8-a901-94181051a2df.jpg)
3. For example, to apply group calculation to the **Unit Price** column at the **Category** level:

   1. First, group the **Category** column. Refer to [Group columns with Advanced Table Viewer macro](/cms_trial/space/TBL/3211755580/Group+columns+with+Advanced+Table+Viewer+macro/).
   2. Then, navigate to column **Unit Price** > **Edit column** > **Edit group calculation** and select **Average**.

      ![Edit group calculation dialog with the Average option selected.](/cms_trial/assets/287ef199-1a3c-4e60-b032-2d1d5bf1dbdd.jpg)
   3. The macro calculates the average from the product rows within each group and displays it on every category group row.

      ![Group calculation at category level](/cms_trial/assets/f6bdbc66-b806-485a-b2d3-fb9606795c90.jpg)
   4. You can further apply grouping on the required columns and nest groups. The average unit price rolls up and displays at all group levels.

      ![Nested group column calculation](/cms_trial/assets/576fb0fa-ffa3-46e6-af0a-2c7f78b36e45.jpg)
   5. You can configure group calculation for multiple columns. For example, applying **Minimum** to the **Stock Qty** column displays the minimum stock quantity at all group levels.

      ![Group calculation for multiple columns](/cms_trial/assets/c717d7f7-4e27-4f53-983e-a9ed6d60707e.jpg)

- Group calculation do not affect the configured column-level calculation type. For example, if you set **Maximum** as the column-level calculation for Unit Price and **Minimum** for Stock Qty, these values remain unchanged when you apply or remove group calculation.

  ![Columnlevel_calculation](/cms_trial/assets/d2ad45ad-b497-42a0-8896-d5079c26e980.jpg)

[Unmapped macro: refined-tab — no content to fall back on]

1. To disable group calculation for any column, navigate to the **Edit column** > **Edit group calculation** and select **None.**

   - For example, to disable the group calculation for the **Stock Qty** column:

     1. Click the **Stock Qty** Edit column. The **Edit group calculation** dialog opens.
     2. Select **None**, and click **Save**.![Edit group calculation](/cms_trial/assets/8aac92dc-f0c9-4e7e-94b2-eb45a642ed65.jpg)
2. To disable group calculation for all columns in the table, edit the macro and click **Disable grouping** (▢ ).

   ![Group calculation_disable grouping](/cms_trial/assets/8b427edc-6bca-449c-8b61-632819c7d0ed.jpg)