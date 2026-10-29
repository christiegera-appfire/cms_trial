# Column group calculation with Advanced Table Viewer macro

The Advanced Table Viewer macro enables you to perform simple and conditional column group calculations and display summarized values at each level of the nested group.

## Group calculation overview

Group calculation supports the following calculation types: Sum, Average, Minimum, Maximum, Count, and Distinct. For Sum and Count,the macro also provides conditional calculations. For each group, the macro calculates a summarized value from the rows in that group and displays it in each grouped row.

**Prerequisite**: To apply a group calculation, first group the required columns. Refer to [Group columns with Advanced Table Viewer macro](/cms_trial/space/TBL/3211755580/Group+columns+with+Advanced+Table+Viewer+macro/).

- You can configure only one group calculation type for each ungrouped column.
- For grouped columns, only column-level calculations apply.
- You can configure group calculations only in macro setup mode and cannot change it in Confluence page view and edit mode.
- You can also summarize grouped rows with conditions (**SUMIF** and **COUNTIF**)

  - For **Sum** and **Count,** the macro provides **conditional calculations** to summarize only the values in rows that match the specified condition. This works like SUMIF and COUNTIF in spreadsheets. The condition can use any column in the table, not only the column you are calculating.
- The macro displays the configured values in the Confluence page view and edit mode.

![Edit group calculation dialog showing Sum-up type options.](/cms_trial/assets/659dfdeb-f1a4-4e5c-b2a3-aaef1e696b0e.jpg)

## Manage group calculations

### Calculation type

You can perform the following group calculations.

| **Type** | **Description** | **Column type** | **Indicator on the Confluence page** |
| --- | --- | --- | --- |
| None | Disables the sum-up calculation - no value is displayed for the column | Any | Not applicable |
| Sum | Calculates the total of all values in the column | Numeric | Total of all values: **Sum** |
| Add a condition to sum only the values in rows that match the condition. | Numeric | Total of values with an applied condition: **SUMIF** |
| Average | Calculates the average of all values in the column | Numeric | **Avg** |
| Minimum | Returns the lowest numerical value in the column | Numeric | **Min** |
| Maximum | Returns the highest numerical value in the column | Numeric | **Max** |
| Count | Counts the total number of non-empty cells in the column | Numeric, String, Date | Count of non-empty cells: **Cnt** |
| Add a condition to count only the rows that match the condition. | Numeric, String, Date | Count of non-empty cells with an applied condition: **COUNTIF** |
| Distinct | Counts unique values only, ignoring duplicates and empty cells | Numeric, String, Date | **Disct** |

### Configure group calculation

Follow the steps to configure group calculation for any column.

You need edit permissions to access the macro setup mode.

1. Edit the macro to open setup mode. Refer to [Set up the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/).
2. Each column displays an Edit column (▢) option. To set up the group calculation for any column, navigate to **Edit column** > **Edit group calculation**.

   ![Edit column with Edit group calculation selected. ](/cms_trial/assets/534b630d-bd1f-4a07-9aaf-972abe7e30ac.jpg)
3. For example, to apply group calculation to the **Unit Price** column at the **Category** level:

   1. First, group the **Category** column. Refer to [Group columns with Advanced Table Viewer macro](/cms_trial/space/TBL/3211755580/Group+columns+with+Advanced+Table+Viewer+macro/).
   2. Then, navigate to column **Unit Price** > **Edit column** > **Edit group calculation** and select **Average**.

      ![Edit group calculation dialog with the Average option selected.](/cms_trial/assets/543e62fd-b3b0-4f12-9d2a-eb59f9af7424.jpg)
   3. The macro calculates the average from the product rows within each group and displays it on every category group row.

      ![Group calculation at category level](/cms_trial/assets/8ce9f2db-5735-46ce-a83c-835d4cec2479.jpg)
   4. You can further group by the required columns and nest groups. The average unit price rolls up and displays at all group levels.

      ![Nested group column calculation](/cms_trial/assets/bff7e430-0fa8-41d4-8fc5-9472cc729797.jpg)
   5. You can configure group calculation for multiple columns. For example, applying **Minimum** to the **Stock Qty** column displays the minimum stock quantity at all group levels.

      ![Group calculation for multiple columns](/cms_trial/assets/7ab1850e-07c9-4cbe-8e69-b243a9d29fd7.jpg)

- Group calculations do not affect the configured column-level calculation type. For example, if you set **Maximum** as the column-level calculation for Unit Price and **Minimum** for Stock Qty, these values remain unchanged when you apply or remove group calculation.

  ![ATV_Columnlevel_sum.jpg](/cms_trial/assets/df8ba48f-c8be-41d0-9ec0-683848a4092d.jpg)

### Configure conditional group calculation

For **Sum** and **Count** calculation types, you can **add a condition** to summarize only the values in rows that match the condition.

#### **Apply conditional group calculation to SUM calculation type**

**Example 1- Sum the Unit Shipping Cost of products whose reorder level is less than or equal to ten**

Follow the steps below for Example 1:

1. To configure **conditional** **group calculation**, edit the macro to open the setup mode. Refer to [Set up the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/).
2. Each column in the table has an *Edit column* (▢) option. To set up the group calculation for any column, navigate to **Edit column** > **Edit group calculation**. For example, for the **Est. Unit Shipping Cost** column, click **Edit group calculation**.

   ![ATV_Edit Group Calculation.png](/cms_trial/assets/94dffc8a-ac11-446e-8213-8b86a9ef7038.png)
3. The *Edit group calculation* dialog opens. To perform a conditional group calculation on the **Est. Unit Shipping Cost** column, select the **Sum-up type** as **Sum**.
4. The **Add condition** toggle is off by default, and the macro calculates the total of all values in the column.

   - To add a condition to the **Est. Unit Shipping Cost** group calculation, enable the **Add condition** toggle.

     ![ATV_Enable Add Condition toggle.png](/cms_trial/assets/3c195d6d-051a-42de-a0e9-64f64f546d3f.png)
   - When the Sum-up type is set to Sum and **Add condition** is enabled**,** you can sum only the values of rows that match a specific condition.

     - The first dropdown selector lists the table column names.
     - The second dropdown selector lists the conditional operators available for the column type selected in the first dropdown.

       - For a numeric column type, the dropdown displays the conditional operators *equals*, *more than*, *less than*, *more than or equal to*, and *less than or equal to*.
       - For string and date columns, the dropdown displays only the *equals* operator.
     - The third field displays either a dropdown selector list or an input field based on the column type selected in the first dropdown.

       - For numeric column types, it displays an input field for numeric values.
       - For string and date column types, it displays the dropdown with values to choose from.
     - To specify a condition, select the column name and conditional operator, and then select or enter a value.

       - For example, select *Reorder Level*, *less than or equal to*, and *10*. The condition applied to the **Est. Unit Shipping Cost** column totals the unit shipping cost for products whose reorder level is less than or equal to 10.
     - To apply the condition, click **Save**.

       ![ATV_apply_numeric group calculation.png](/cms_trial/assets/41b2da30-ab57-4925-889f-5676c3ab0f49.png)
5. The macro setup mode displays the summarized value for the **Est. Unit Shipping Cost** column at each group level. The sum-up indicator (for example, SUMIF) displays the condition type. Hover over the indicator to view the applied condition.

   ![ATV_group calculation_Edit mode_sum up row.png](/cms_trial/assets/c4fc8c79-fa6b-4d37-9090-0f2768714af7.png)
6. Click **Save** and then **Publish** the page. You can view the summarized values at group level in the Confluence page view mode.

   ![ATV_SUMIF_Group calculation_View mode.png](/cms_trial/assets/9c098bc7-b3fd-4dbf-809d-65a13aafa778.png)

#### **Apply conditional group calculation to COUNT calculation type**

**Example 2** - Under each product category, count products with reorder level less than or equal to 10.

Follow the steps below for Example 2:

1. For the **Reorder Level** column, navigate to **Edit column** > **Edit group calculation**.

   ![ATV_Reorder Level_Edit group calculation.png](/cms_trial/assets/575cf8a6-f805-4da6-8dd2-538ebbf179f6.png)
2. Select the required **Sum-up type**; for example, for the **Reorder Level** column, select **Count**. The **Add condition** toggle is off by default, and the macro returns the total number of non-empty cells in the column.
3. To add a condition to the **Reorder Level** group calculation, enable the **Add condition** toggle.
4. In the condition dropdowns, select the column, condition, and value in order. For example, select *Reorder Level*, *less than or equal to*, and *10*.

   - The applied condition for the **Reorder Level** column counts non-empty rows where the **Reorder Level** column value is *less than or equal to* 10.
5. To apply the condition, click **Save**.

   ![ATV_Reorder level_Count condition.png](/cms_trial/assets/9fc49a4d-5aa2-4bb8-86b5-faebdb0c86b3.png)
6. The macro setup mode displays the summarized value for the **Reorder Level** column at each group level. The sum-up indicator (for example, COUNTIF) indicates that a condition is applied. Hover over the indicator to view the applied condition.

   ![ATV_summarized row in edit mode_for count condition.png](/cms_trial/assets/77d3563e-b39a-4100-9f36-380b579816c1.png)
7. Click **Save** and **Publish** the page. You can view the summarized values in the Confluence page view mode.

   ![ATV_page view mode with group calculation applied.png](/cms_trial/assets/5c5774ae-5ad4-4178-8c6e-ce4111162e5d.png)

### Disable group calculation

- To disable group calculation for any column, navigate to **Edit column** > **Edit group calculation** and select **None.**

  - For example, to disable the group calculation for the **Stock Qty** column:

    1. Click the **Stock Qty** Edit column. The **Edit group calculation** dialog opens.
    2. Select **None**, and click **Save**.

       ![ATV_Select None to disable column group calculation.png](/cms_trial/assets/fa219b52-a813-423a-aea9-10411b62d295.png)
- When you click **Disable grouping** (▢ ), the macro hides the grouped view and saves the group calculation set for each column. When you enable grouping again and group columns, the macro displays the saved group calculations.

  ![ATV_Disable Grouping.png](/cms_trial/assets/38d1c2b1-ff2b-4250-8e9e-7c494948fa6e.png)