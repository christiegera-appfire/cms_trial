# Column group calculation with Native Table Enhancer [Beta] macro

The Native Table Enhancer macro enables you to perform simple and conditional column group calculations and display summarized values at each level of the nested group.

The Native Table Enhancer macro is currently in beta. [Learn more](/cms_trial/space/TBL/3520037211/Native+Table+Enhancer+%5BBeta%5D+macro/).

## Group calculation overview

Group calculation supports the following calculation types: Sum, Average, Minimum, Maximum, Count, and Distinct. For Sum and Count,the macro also provides conditional calculations. For each group, the macro calculates a summarized value from the rows in that group and displays it in each grouped row.

**Prerequisite**: To apply a group calculation, first group the required columns. Refer to [Group columns with Native Table Enhancer macro](/cms_trial/space/TBL/3559129118/Group+columns+with+Native+Table+Enhancer+%5BBeta%5D+macro/).

- You can configure only one group calculation type for each ungrouped column.
- For grouped columns, only column-level calculations apply.
- You can configure group calculations only in macro setup mode. You cannot change it in Confluence page view mode.
- You can also summarize grouped rows with conditions (**SUMIF** and **COUNTIF**)

  - For **Sum** and **Count,** the macro provides [conditional calculations](#Configure-conditional-group-calculation) to summarize only the values in rows that match the specified condition. This works like SUMIF and COUNTIF in spreadsheets. The condition can use any column in the table, not only the column you are calculating.
- The macro displays the configured values in the Confluence page view mode.

  ![Native Table Enhancer_Group calculation dialog](/cms_trial/assets/bca40961-f79b-4d5d-9933-78b91b22009d.png)

## Manage group calculations

### **Calculation type**

You can perform the following group calculations.

| **Type** | **Description** | **Column type** | **Indicator on the Confluence page** |
| --- | --- | --- | --- |
| None | Disables the group calculation: no value is displayed for the column | Any | Not applicable |
| Sum | Calculates the total of all values in the column | Numeric | Total of all values: **Sum** |
| Add a condition to sum only the values in rows that match the condition. | Numeric | Total of values with an applied condition: **SUMIF** |
| Average | Calculates the average of all values in the column | Numeric | **Avg** |
| Minimum | Returns the lowest numerical value in the column | Numeric | **Min** |
| Maximum | Returns the highest numerical value in the column | Numeric | **Max** |
| Count | Counts the total number of non-empty cells in the column | Numeric, String, Date | Count of non-empty cells: **Cnt** |
| Add a condition to count only the rows that match the condition. | Numeric, String, Date | Count of non-empty cells with an applied condition: **COUNTIF** |
| Distinct | Counts unique values only, ignoring duplicates and empty cells | Numeric, String, Date | **Disct** |

### **Configure group calculation**

Follow the steps to configure group calculation for any column.

You need edit permissions to access the macro setup mode.

1. Edit the macro to open setup mode. Refer to [Set up the Native Table Enhancer macro features](/cms_trial/space/TBL/3568173057/Set+up+the+Native+Table+Enhancer+%5BBeta%5D+macro+features/).
2. Each column displays an *Edit column* ( ▢ ) option. To set up the group calculation for any column, navigate to **Edit column** > **Edit group calculation**.

   ![To set up the group calculation for any column, navigate to Edit column and then Edit group calculation](/cms_trial/assets/f393aea5-d42b-4f09-95c3-5bc245046944.png)
3. For example, to apply group calculation to the **Unit Price** column at the **Category** level:

   1. First, group the **Category** column. Refer to [Group columns with Native Table Enhancer macro](/cms_trial/space/TBL/3559129118/Group+columns+with+Native+Table+Enhancer+%5BBeta%5D+macro/).
   2. Then, navigate to column **Unit Price** > **Edit column** > **Edit group calculation** and select **Average**.

      ![Select the required Sum-up type in Edit group calculation dialog](/cms_trial/assets/d9dec48b-5572-4340-9dee-efce066c920e.png)
   3. The macro calculates the average of product rows within each group and displays the result on each category group row.

      ![Summarized values at each group level](/cms_trial/assets/20cc03c5-6785-488f-a940-c1a4507c53e1.png)
   4. You can further group by the required columns and nest groups. The average unit price rolls up and displays at all group levels.

      ![Group column calculation at nested levels](/cms_trial/assets/a1499135-94f6-4eca-b137-de1dea799bd7.png)
   5. You can configure group calculation for multiple columns. For example, applying **Minimum** to the **Stock Qty** column displays the minimum stock quantity at all group levels.

      ![Apply group calculation for multiple columns](/cms_trial/assets/b4bef3bf-b47a-489e-8084-786b871788f1.png)

- Group calculation does not affect the configured column-level calculation type. For example, if you set **Maximum** as the column-level calculation for Unit Price and **Minimum** for Stock Qty, these values remain unchanged when you apply or remove group calculation.

  ![Group calculation does not affect the configured column-level calculation type](/cms_trial/assets/b98bf181-97cc-4b58-b3a1-ca0a011fbed3.png)

### Configure conditional group calculation

For **Sum** and **Count** calculation types, you can **add a condition** to summarize only the values in rows that match the condition.

#### **Apply conditional group calculation to the SUM calculation type**

**Example 1- Sum the Unit Shipping Cost of products whose reorder level is less than or equal to ten**

Follow the steps below for Example 1:

**Prerequisite**: To apply a conditional group calculation, first group the required columns. For example, the **Category** column is grouped here. Refer to [Group columns with Native Table Enhancer macro](/cms_trial/space/TBL/3559129118/Group+columns+with+Native+Table+Enhancer+%5BBeta%5D+macro/).

1. To configure **conditional** **group calculation**, edit the macro to open the setup mode. Refer to [Set up the Native Table Enhancer macro features](/cms_trial/space/TBL/3568173057/Set+up+the+Native+Table+Enhancer+%5BBeta%5D+macro+features/).
2. Each column in the table has an *Edit column* ( ▢ ) option. To set up the group calculation for any column, navigate to **Edit column** > **Edit group calculation**. For example, for the **Est. Unit Shipping Cost** column, click **Edit group calculation**.

   ![To set up the group calculation for any column, navigate to Edit column and then Edit group calculation](/cms_trial/assets/735d33f2-3335-47f6-b86c-bc4a05cf4ade.png)
3. The *Edit group calculation* dialog opens. To perform a conditional group calculation on the **Est. Unit Shipping Cost** column, select the **Sum-up type** as **Sum**.
4. The **Add condition** toggle is off by default, and the macro calculates the total of all values in the column.

   - To add a condition to the **Est. Unit Shipping Cost** group calculation, enable the **Add condition** toggle.

     ![To add a condition for group calculation, enable the Add condition toggle](/cms_trial/assets/88c1294b-a463-411c-8dcb-f21f5eae1955.png)
   - When the Sum-up type is set to **Sum** and **Add condition** is enabled**,** you can sum only the values of rows that match a specific condition.

     - The first dropdown selector lists the table column names.
     - The second dropdown selector lists the conditional operators available for the column type selected in the first dropdown.

       - For a numeric column type, the dropdown displays the condition operators *equals*, *more than*, *less than*, *more than or equal to*, and *less than or equal to*.
       - For string and date columns, the dropdown displays only the *equals* operator.
     - The third field displays either a dropdown selector list or an input field based on the column type selected in the first dropdown.

       - For numeric column types, it displays an input field for numeric values.
       - For string and date column types, it displays the dropdown with values to choose from.
     - To specify a condition, select the column name and conditional operator, and then select or enter a value.

       - For example, select *Reorder Level*, *less than or equal to*, and *enter* *10*. The condition applied to the **Est. Unit Shipping Cost** column totals the unit shipping cost for products whose reorder level is less than or equal to 10.
     - To apply the condition, click **Save**.

       ![To specify a condition, select the column name and conditional operator, and then select or enter a value](/cms_trial/assets/20d0f119-f5d3-43ae-bd93-c661c96c1f49.png)
5. The macro setup mode displays the summarized value for the **Est. Unit Shipping Cost** column at each group level. The sum-up indicator (for example, SUMIF) displays the condition type. Hover over the indicator to view the applied condition.

   ![Summarized values at each group level](/cms_trial/assets/32e67eb6-305e-4f05-baab-9268e0f6acb4.png)
6. Click **Save** and then **Publish** the page. You can view the summarized values at the group level in the Confluence page view mode.

   ![Summarized values at the group level in the Confluence page view mode](/cms_trial/assets/a856bae9-e722-41e7-b78e-5e06064c9eed.png)

#### **Apply conditional group calculation to the COUNT calculation type**

**Example 2** - Under each product category, count products with reorder level less than or equal to 10.

Follow the steps below for Example 2:

**Prerequisite**: To apply a conditional group calculation, first group the required columns. For example, the **Category** column is grouped here. Refer to [Group columns with Native Table Enhancer macro](/cms_trial/space/TBL/3559129118/Group+columns+with+Native+Table+Enhancer+%5BBeta%5D+macro/).

1. To configure **conditional** **group calculation**, edit the macro to open the setup mode. Refer to [Set up the Native Table Enhancer macro features](/cms_trial/space/TBL/3568173057/Set+up+the+Native+Table+Enhancer+%5BBeta%5D+macro+features/).
2. For the **Reorder Level** column, navigate to **Edit column** > **Edit group calculation**.

   ![To setup conditional group calculation, navigate to Edit group calculation dialog](/cms_trial/assets/05bd193a-4a43-4ad6-aff5-f7241eb5e2f1.png)
3. Select the required **Sum-up type**; for example, for the **Reorder Level** column, select **Count**. The **Add condition** toggle is off by default, and the macro returns the total number of non-empty cells in the column.
4. To add a condition to the **Reorder Level** group calculation, enable the **Add condition** toggle.
5. In the condition dropdowns, select the column, condition, and value in order. For example, select *Reorder Level*, *less than or equal to*, and enter *10*.

   - The applied condition for the **Reorder Level** column counts non-empty rows where the **Reorder Level** column value is *less than or equal to* 10.
6. To apply the condition, click **Save**.

   ![In the condition dropdown, select the column, condition, and value in order](/cms_trial/assets/e61b799b-245c-44c8-9a29-e431f8392fd3.png)
7. The macro setup mode displays the summarized value for the **Reorder Level** column at each group level. The sum-up indicator (for example, COUNTIF) indicates that a condition is applied. Hover over the indicator to view the applied condition.

   ![Summarized value with applied condition at each group level](/cms_trial/assets/9122aaf8-d91e-4a95-82b5-f10ac7efd99a.png)
8. Click **Save** and **Publish** the page. You can view the summarized values in the Confluence page view mode.

   ![Summarized value with applied condition at each group level in Confluence page view mode](/cms_trial/assets/1c8b18d7-956b-49b3-8837-e05cd9d883dc.png)

**Disable group calculation**

1. To disable group calculation for any column, navigate to **Edit column** > **Edit group calculation** and select **None.**

   - For example, to disable the group calculation for the **Stock Qty** column:

     1. Click the **Stock Qty** Edit column. The **Edit group calculation** dialog opens.
     2. Select **None**, and click **Save**.

        ![To disable group calculation for any column, select None](/cms_trial/assets/79be7561-2f3e-4e1f-b103-ea46fd2f96f2.png)
2. When you click **Disable grouping** (▢), the macro hides the grouped view and saves the group calculation set for each column. When you enable grouping again and group columns, the macro displays the saved group calculations.

   ![Disable grouping - hides the grouped view and saves the group calculation set for each column](/cms_trial/assets/ac41b235-7584-45b9-9847-e418f99e7d5b.png)