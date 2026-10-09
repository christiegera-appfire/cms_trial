# Column calculation with Native Table Enhancer [Beta] macro

The Native Table Enhancer macro enables you to perform simple and conditional column calculations and display summarized values at each column level.

The Native Table Enhancer macro is currently in beta. [Learn more](/cms_trial/space/TBL/3520037211/Native+Table+Enhancer+%5BBeta%5D+macro/).

## **Column calculation**

The **Column calculation** feature supports the following calculation types: **Sum**, **Average**, **Minimum**, **Maximum**, **Count**, and **Distinct**. You can configure the Sum-up type for each column independently.

- You can configure column calculations only in macro setup mode and cannot change them in Confluence page view mode.
- You can summarize specific rows with conditions (**SUMIF** and **COUNTIF**)
- - For **Sum** and **Count,** the macro provides **conditional calculations** to summarize only the values in rows that match the condition. This works like SUMIF and COUNTIF in spreadsheets. The condition can use any column in the table, not only the column you are calculating.
- The macro adds a summarized row below the table header.
- The macro displays the configured Sum-up values in the Confluence page view mode.

  ![Native Table Enhancer_Edit Column calculation dialog](/cms_trial/assets/df939309-f6ea-47bb-956d-5bee71a8c226.png)

## Manage column calculations

[Unmapped macro: refined-tab — no content to fall back on]

You can perform the following column calculations.

| **Type** | **Description** | **Column type** | **Indicator on the Confluence page** |
| --- | --- | --- | --- |
| None | Disables the column calculation: no value is displayed for the column | Any | Not applicable |
| Sum | Calculates the total of all values in the column | Numeric | Total of all values: **Sum** |
| Add a condition to sum only the values in rows that match the condition. | Numeric | Total of values with an applied condition: **SUMIF** |
| Average | Calculates the average of all values in the column | Numeric | **Avg** |
| Minimum | Returns the lowest numerical value in the column | Numeric | **Min** |
| Maximum | Returns the highest numerical value in the column | Numeric | **Max** |
| Count | Counts the total number of non-empty cells in the column | Numeric, String, Date | Count of non-empty cells: **Cnt** |
| Add a condition to count only rows that match the condition. | Numeric, String, Date | Counts only the cells that match the condition*:* **COUNTIF** |
| Distinct | Counts unique values only, ignoring duplicates and empty cells | Numeric, String, Date | **Disct** |

[Unmapped macro: refined-tab — no content to fall back on]

You need edit permissions to access the macro setup mode.

1. To configure **column calculation**, edit the macro to open the setup mode. Refer to [Set up the Native Table Enhancer macro features](/cms_trial/space/TBL/3568173057/Set+up+the+Native+Table+Enhancer+%5BBeta%5D+macro+features/). Each column in the table has an *Edit column* (▢ ) option.
2. To set up the column calculation for any column, navigate to **Edit column** > **Edit column calculation**. For example, for the **Stock Qty** column, click **Edit column calculation**.

   ![To set up the column calculation for any column navigate to Edit column and then Edit column calculation](/cms_trial/assets/094945df-12d5-45bb-a305-e0cbea9e626e.png)
3. The *Edit column calculation* dialog opens. Select the required Sum-up type, and click **Save**. For example, for the **Stock Qty** column, **Sum** is selected.

   ![Select the required column calculation type](/cms_trial/assets/eeda2a5a-6d80-4c85-b16c-6256e8dc699a.png)

- For the String and Date column types, the *Edit* *column calculation* dialog displays *None*, *Count*, and *Distinct*.

  ![Column calculation types for the String and Date column types](/cms_trial/assets/479c7805-7aae-47d7-a5c7-958e1d5e94de.png)

1. The summarized row appears as the first row below the table header and displays the configured sum-up values. For example: **Category** - Distinct, **Product ID** - Count, **Unit Price** - Max, **Stock Qty** - Sum, **Reorder Level** - Average.

   ![Summarized row appears as first row below the table header](/cms_trial/assets/fad5e56c-c448-44b7-ac39-a7eec2827e0f.png)

1. Click **Save** and **Publish** the page. You can view the configured summary values in the Confluence page view mode.

   ![Summarized value in Page view mode](/cms_trial/assets/2c4dba87-5d60-4588-9b4b-3a861f4146b0.png)

[Unmapped macro: refined-tab — no content to fall back on]

You need edit permissions to access the macro setup mode.

For **Sum** and **Count** calculation types, you can **add a condition** to summarize only the values in rows that match the condition.

**Apply conditional column calculation to numeric column type**

**Example 1 - Sum values for one specific category:** In the **Annual Maintenance** column, use **Sum** with a conditional calculation on the **Category** columnvalue *Hardware*. The summarized row shows the total maintenance cost for Hardware items only.

- To configure a conditional column calculation, edit the macro to open the setup mode. Refer to [Set up the Native Table Enhancer macro features](/cms_trial/space/TBL/3568173057/Set+up+the+Native+Table+Enhancer+%5BBeta%5D+macro+features/). Each column in the table has an *Edit column* (▢ ) option.
- To set up the conditional column calculation for any numeric column, navigate to **Edit column** > **Edit column calculation**. For example, for the **Annual Maintenance($)** column, click **Edit column calculation**.

  ![To set up the conditional column calculation for any numeric column, navigate to Edit column and then Edit column calculation](/cms_trial/assets/701c9e73-70b2-49d9-9df1-2eb7d74c5e75.png)
- The *Edit column calculation* dialog opens. To perform a conditional calculation on the **Annual Maintenance** column, select the required **Sum-up type** as **Sum**.
- The **Add condition** toggle is off by default, and the macro calculates the total of all values in the column.

  - To add a condition to the **Annual Maintenance** column calculation, enable the **Add condition** toggle.

    ![Native Table Enhancer_Enable Add condition](/cms_trial/assets/6ffc3a49-1923-4750-8bcc-38e4d4ceb957.png)
  - When the Sum-up type is set to Sum, the **Add condition** lets you sum only the values of rows that match a specific condition.

    - The first dropdown selector lists the table column names.
    - The second dropdown selector lists the conditions available for the column type selected in the first dropdown.
    - The third dropdown selector lists the values for the column selected in the first dropdown. For numeric column types, it displays an input field for numeric column values.
    - For example, the condition for the **Annual Maintenance** column sums all **Annual Maintenance** column values where the **Category** column value is *Hardware.*
    - To apply the condition, click **Save**.

      ![Native Table Enhancer_Add condition for SUM](/cms_trial/assets/0d9e0cda-28aa-4147-8567-8c14950138dc.png)
    - The macro setup mode displays the summarized value just below the **Annual Maintenance** column header. The Sum-up indicator (for example, SUMIF) displays the condition type. Hover over the indicator to view the applied condition.

      ![The Sum-up indicator (for example, SUMIF) displays the condition type. Hover over the indicator to view the applied condition.](/cms_trial/assets/cf6d41b3-ac7f-431a-9b46-2c7f29e12f02.png)
    - Click **Save** and then **Publish** the page. You can view the summarized values in the Confluence page view mode.

      ![View the summarized values in the Confluence page view mode](/cms_trial/assets/ce133774-ebbe-45ca-bb85-2fb5295cb27a.png)

**Apply conditional column calculation to string column type**

For the **String** and **Date** column types, the *Edit* *column calculation* dialog displays *None*, *Count*, and *Distinct*.

**Example 2**- **Count items with low stock**:In the **Stock Status** column, use **Count** with a condition on the ***Stock Qty*** *column* where the value***is less than or equal to 5***. The summarized row shows how many items are low on stock.

- For the **Stock** **Status** column, navigate to **Edit column** > **Edit column calculation**.

  ![For any column, navigate to Edit column and then Edit column calculation](/cms_trial/assets/ff6420f7-1174-42d3-b011-4174881ff3d8.png)
- Select the required Sum-up type; for example, for the **Stock** **Status** column, select **Count**. The **Add condition** toggle is off by default, and the macro returns the total number of non-empty cells in the column.
- To add a condition to the **Stock** **Status** column calculation, enable the **Add condition** toggle.
- In the condition dropdowns, select **Stock Qty**, select **less than or equal to**, and enter **5**.
- The applied condition for the **Stock** **Status** column counts non-empty rows where the **Stock Qty** column value is *less than or equal to* 5.
- To apply the condition, click **Save**.

  ![Apply conditional calculation for Count](/cms_trial/assets/0ba64ca2-2b4e-46e7-8e81-fd74c46b3661.png)
- The macro setup mode displays the summarized value just below the **Stock** **Status** column header. The Sum-up indicator (for example, COUNTIF) indicates that a condition is applied. Hover over the indicator to view the applied condition.

  ![The Sum-up indicator (for example, COUNTIF) indicates that a condition is applied. Hover over the indicator to view the applied condition](/cms_trial/assets/17cb6d57-d220-4aa2-ab7a-eff809e88c8c.png)
- Click **Save** and then **Publish** the page. You can view the summarized values in the Confluence page view mode.

  ![View the summarized values in the Confluence page view mode](/cms_trial/assets/fdb905f5-bb54-49ae-903c-316e453ceb1d.png)

[Unmapped macro: refined-tab — no content to fall back on]

To disable the configured Sum-up value for any column, navigate to the *Edit column calculation* dialog and select **None**.

For example, to disable the column calculation for the **Stock** **Status** column:

1. For the **Stock Status** column, navigate to **Edit column** > **Edit column calculation**.
2. Select **None**, and click **Save**.

   ![To disable the configured sum-up value for any column select None](/cms_trial/assets/01908523-2c64-4458-87fa-e269d3aed303.png)