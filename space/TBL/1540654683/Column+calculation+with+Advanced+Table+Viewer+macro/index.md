# Column calculation with Advanced Table Viewer macro

The Advanced Table Viewer macro enables you to perform simple and conditional column calculations and display summarized values at each column level.

## **Column calculation**

The **Column calculation** feature supports the following calculation types: **Sum**, **Average**, **Minimum**, **Maximum**, **Count**, and **Distinct**. You can configure the Sum-up type for each column independently.

- You can configure column calculations only in macro setup mode and cannot change them in Confluence page view and edit mode.
- You can summarize specific rows with conditions (**SUMIF** and **COUNTIF**).
- - For **Sum** and **Count,** the macro provides **conditional calculations** to summarize only the values in rows that match the condition. This works like SUMIF and COUNTIF in spreadsheets. The condition can use any column in the table, not only the column you are calculating.
- The macro adds a summarized row below the table header.
- The macro displays the configured Sum-up values in the Confluence page view and edit mode.

  ![Edit column calculation dialog showing the available Sum-up types for the Story Points column.](/cms_trial/assets/697cfcca-7797-4afc-840e-b204bac6beb0.png)

## Manage column calculations

[Unmapped macro: refined-tab — no content to fall back on]

You can perform the following column calculations

| **Type** | **Description** | **Column type** | **Indicator on the Confluence page** |
| --- | --- | --- | --- |
| None | Disables the Sum-up calculation - no value is displayed for the column | Any | Not applicable |
| Sum | Calculates the total of all values in the column | Numeric | Total of all values: **Sum** |
| Add a condition to sum only the values in rows that match the condition. | Numeric | Total of values with an applied condition: **SUMIF** |
| Average | Calculates the average of all values in the column | Numeric | **Avg** |
| Minimum | Returns the lowest numerical value in the column | Numeric | **Min** |
| Maximum | Returns the highest numerical value in the column | Numeric | **Max** |
| Count | Counts the total number of non-empty cells in the column. | Numeric, String, Date | Count of non-empty cells: Cnt |
| Add a condition to count only the rows that match the condition. | Numeric, String, Date | Count of non-empty cells with an applied condition: **COUNTIF** |
| Distinct | Counts unique values only, ignoring duplicates and empty cells | Numeric, String, Date | Disct |

[Unmapped macro: refined-tab — no content to fall back on]

You need edit permissions to access the macro setup mode.

1. To configure **column calculation**, edit the macro to open the setup mode. Refer to [Set up the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/). Each column in the table has an *Edit column* ( ▢) option.
2. To set up the column calculation for any column, navigate to **Edit column** > **Edit column calculation**. For example, for the **Story Points** column, click **Edit column calculation**.

   ![To setup column calculation, click Edit column calculation](/cms_trial/assets/28431b79-af9a-4d77-ac77-9b690d0dce0d.png)
3. The *Edit column calculation* dialog opens. Select the required Sum-up type, and click **Save**. For example, for the **Story Points** column, the Sum-up type is set to **Sum**.

   ![Edit column calculation dialog with Sum selected for the Story Points column.](/cms_trial/assets/f122557b-3421-43d8-bd80-23ac02181115.png)

- For the String and Date column types, the *Edit* *column calculation* dialog displays *None*, *Count*, and *Distinct*.

  ![Edit column calculation dialog for string and date type](/cms_trial/assets/0869c270-1555-4829-8e21-1a98b0c57179.png)

1. The summarized row appears as the first row below the table header and displays the configured sum-up values. For example: **Issue Key** - Count, **Assignee** - Distinct, **Story Points** - Sum, **Hours Estimated** - Max.

   ![Advanced Table Viewer_Edit mode_summarized row](/cms_trial/assets/de6ec5e2-ff8e-4b92-99aa-c6159d34104a.png)
2. Click **Save** and **Publish** the page. You can view the configured summary values in the Confluence page view and edit mode.

   ![Summarized row in Confluence page view mode.](/cms_trial/assets/ce832c3a-4161-4e2c-993a-6dd8f1031179.png)

[Unmapped macro: refined-tab — no content to fall back on]

You need edit permissions to access the macro setup mode.

For **Sum** and **Count** calculation types, you can **add a condition** to summarize only the values in rows that match the condition.

**Apply conditional column calculation to numeric columns**

**Example - Sum the budget allocated for work items with status In progress:** In the **Budget Allocated** column, select **Sum** and apply conditional calculation on the **Status** columnforvalue *In progress*. The summarized row shows the total budget allocated for *In progress* work items.

- To configure **column calculation**, edit the macro to open the setup mode. Refer to [Set up the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/). Each column in the table has an *Edit column* (▢ ) option.

- To set up the column calculation for any numeric column, navigate to **Edit column** > **Edit column calculation**. For example, for the **Budget Allocated** column, click **Edit column calculation**.

  ![Budget Allocated column menu with the Edit column calculation option highlighted.](/cms_trial/assets/fcae2934-3012-4302-91e6-b54090f4d33c.png)
- The *Edit column calculation* dialog opens. To perform a conditional calculation on the **Budget Allocated** column, select the **Sum-up type** as **Sum**.
- The **Add condition** toggle is off by default, and the macro calculates the total of all values in the column.

  - To add a condition to the **Budget Allocated** column calculation, enable the **Add condition** toggle.

    ![Edit column calculation dialog with Sum selected and the Add condition toggle enabled.](/cms_trial/assets/44a6b837-0182-4081-9d1d-356216f0e5e3.png)
  - When the Sum-up type is set to Sum and **Add condition** is enabled**,** you can sum only the values of rows that match a specific condition.

    - The first dropdown selector lists the table column names.
    - The second dropdown selector lists the conditions available for the column type selected in the first dropdown.
    - The third dropdown selector lists the values for the column selected in the first dropdown. For numeric column types, it displays an input field for numeric column values.
    - For example, the condition for the **Budget Allocated** column sums all **Budget Allocated** column values where the **Status** column value is *In Progress.*
    - To apply the condition, click **Save**.

      ![Conditional Sum settings with Status, equals, and In Progress selected.](/cms_trial/assets/136b1ce5-c2cc-4aed-91e1-6d52ef953698.png)
    - The macro setup mode displays the sum-up value just below the table header for the **Budget Allocated** column. The sum-up indicator (for example, SUMIF) displays the condition type. Hover over the indicator to view the applied condition.

      ![Budget Allocated column showing the SUMIF indicator and a tooltip describing the applied condition.](/cms_trial/assets/0c82091b-7c33-4601-8a96-3743f344f49a.png)
    - Click **Save** and then **Publish** the page. You can view the summarized values in the Confluence page view mode.

      ![Advanced Table Viewer_SUMIF value_in page view mode](/cms_trial/assets/3f4b9d97-352c-4a16-8787-eee6ddecd330.png)

### Apply column calculation to string column type

For the **String** and **Date** column types, the *Edit* *column calculation* dialog displays *None*, *Count*, and *Distinct*.

**Example** - **Count work items with highest priority**:In the **Status** column, use **Count** with a condition on the ***Priority*** *column* where the value is Highest. The summarized row shows how many work items have the highest priority.

1. 1. For the **Status** column, navigate to **Edit column** > **Edit column calculation**.

      ![Status column menu with the Edit column calculation option highlighted.](/cms_trial/assets/6a29bef7-8903-4546-933d-95b53bbea454.png)
   2. Select the required Sum-up type; for example, for the **Status** column, select **Count**. The **Add condition** toggle is off by default, and the macro returns the total number of non-empty cells in the column.
   3. To add a condition to the **Status** column calculation, enable the **Add condition** toggle.
   4. In the condition dropdowns, select the column, condition, and value in sequence. For example, select *Priority*, *equals*, and *Highest*.
   5. The applied condition for the **Status** column counts non-empty rows where the **Priority** column value equals *Highest*.
   6. To apply the condition, click **Save**.

      ![Edit column calculation dialog with Count selected and a condition where Priority equals Highest.](/cms_trial/assets/89c712f7-7680-4a05-972c-4901893093c6.png)
   7. The macro setup mode displays the summarized value just below the **Status** column header. The sum-up indicator (for example, COUNTIF) indicates that a condition is applied. Hover over the indicator to view the applied condition.

      ![Status column showing the COUNTIF indicator and a tooltip describing the applied condition.](/cms_trial/assets/4a159fe8-59d8-41b6-a480-f49633e1ca72.png)

- Click **Save** and **Publish** the page. You can view the summarized values in the Confluence page view mode.

  ![Advanced Table Viewer table showing the COUNTIF result in the Status column summary row.](/cms_trial/assets/6dbb2e24-86da-4ead-b50e-5bd705e0110e.png)

[unmapped inline: placeholder]

[Unmapped macro: refined-tab — no content to fall back on]

To disable the configured Sum-up type for any column, navigate to the *Edit column calculation* dialog and select **None**.

For example, to disable the column calculation:

- For the **Status** column, navigate to **Edit column** (▢ ) > **Edit column calculation**. The *Edit column calculation* dialog opens.
- Select **None**, and click **Save**.

  ![Edit column calculation dialog with None selected for the Status column.](/cms_trial/assets/dd841295-eb75-48ae-b6aa-52e458fe7066.png)