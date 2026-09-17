# Column calculation with Advanced Table Viewer macro

The Advanced Table Viewer macro enables you to perform column calculations and display summarized values at each column level.

## **Column calculation**

The **Column calculation** feature supports the following calculation types: Sum, Average, Minimum, Maximum, Count, and Distinct. You can configure the Sum-up type for each column independently.

- You can configure column calculations only in macro setup mode and cannot change them in Confluence page view and edit mode.
- For Sum and Count, you can also add a condition to summarize only the values in rows that match the condition.
- The feature adds a summarized row below the table header.
- The macro displays the configured Sum-up values in the Confluence page view and edit mode.

  ![Edit column calculation.png](/cms_trial/assets/697cfcca-7797-4afc-840e-b204bac6beb0.png)

## Manage column calculations

[Unmapped macro: refined-tab — no content to fall back on]

You can perform the following column calculations.

| **Type** | **Description** | **Column type** | **Indicator on the Confluence page** |
| --- | --- | --- | --- |
| None | Disables the Sum-up calculation - no value is displayed for the column | Any | Not applicable |
| Sum | Calculates the total of all values in the column  You can also add a condition to sum only the values in rows that match the condition. | Numeric | Total of all values: Sum  Total of values with an applied condition: SUMIF |
| Average | Calculates the average of all values in the column | Numeric | Avg |
| Minimum | Returns the lowest numerical value in the column | Numeric | Min |
| Maximum | Returns the highest numerical value in the column | Numeric | Max |
| Count | Counts the total number of non-empty cells in the column  You can also add a condition to count only the rows that match the condition. | Numeric, String, Date | Count of non-empty cells: Cnt  Count of non-empty cells with an applied condition: COUNTIF |
| Distinct | Counts unique values only, ignoring duplicates and empty cells | Numeric, String, Date | Disct |

[Unmapped macro: refined-tab — no content to fall back on]

You need edit permissions to access the macro setup mode.

To configure **column calculation**, edit the macro to open the setup mode. Refer to [Set up the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/). Each column in the table has an *Edit column* (▢ ) option.

### Apply column calculation to numeric column type

- To set up the column calculation for any column, navigate to **Edit column** > **Edit column calculation**. For example, for the **Budget Allocated** column, click **Edit column calculation**.

  ![Edit column calculation_Budget allocated.png](/cms_trial/assets/bbb5c354-35cf-4903-92de-e03110b4d202.png)
- The *Edit column calculation* dialog opens.
- Select the required Sum-up type; for example, for the **Budget Allocated** column, select **Sum**.
- The **Add condition** toggle is off by default, and the macro calculates the total of all values in the column.

  - To add a condition to the **Budget Allocated** column calculation, enable the **Add condition** toggle.

    ![Edit column calculation_Sum_Add condition.png](/cms_trial/assets/a15b8bb2-677c-422c-bc55-1fd961039606.png)
  - When the Sum-up type is set to Sum, the **Add condition** lets you sum only the values of rows that match a specific condition.

    - The first dropdown selector lists the table column names.
    - The second dropdown selector lists the conditions available for the column type selected in the first dropdown.
    - The third dropdown selector lists the values for the column selected in the first dropdown. For numeric column types, it displays an input field for numeric column values.
    - For example, the condition for the **Budget Allocated** column sums all **Budget Allocated** column values where the **Status** column value is *In Progress.*
    - To apply the condition, click **Save**.

      ![Add condition_for budget allocated for in progress issues.png](/cms_trial/assets/e6d7372b-b542-4940-a455-58873139ac99.png)
    - The macro setup mode displays the sum-up value just below the table header for the **Budget Allocated** column. The sum-up indicator (for example, SUMIF) displays the condition type. Hover over the indicator to view the applied condition.

      ![Macro config shows the conditional sumup value.png](/cms_trial/assets/8a43642b-4e92-40bb-bec0-8d9b87375928.png)

### Apply column calculation to string column type

- For the String and Date column types, the *Edit* *column calculation* dialog displays *None*, *Count*, and *Distinct*.

  1. For the **Status** column, navigate to **Edit column** > **Edit column calculation**.

     ![Add condition_status column.png](/cms_trial/assets/ff95a895-a6ad-4217-b41b-1a7247d5a6c1.png)
  2. Select the required Sum-up type; for example, for the **Status** column, select **Count**. The **Add condition** toggle is off by default, and the macro returns the total number of non-empty cells in the column.
  3. To add a condition to the **Status** column calculation, enable the **Add condition** toggle.
  4. The applied condition for the **Status** column counts non-empty rows where the **Status** column value equals *In Progress*.

     ![Add condition for Status column.png](/cms_trial/assets/992a25d8-21ff-422d-bcf3-ce6ec0f47289.png)
  5. To apply the condition, click **Save**. The macro setup mode displays the sum-up value just below the table header for the **Status** column. The sum-up indicator (for example, COUNTIF) displays the condition type. Hover over the indicator to view the applied condition.

     ![Sum-value for Status column.png](/cms_trial/assets/f567f8e5-ca77-45f6-bf17-e5cde7bf3f6b.png)

- You can configure the Sum-up type for any other columns as needed. The summarized row appears as the first row below the table header and displays all the configured sum-up values and the sum-up indicator. For example: **Status** and **Priority** - COUNTIF, **Story Points** - SUMIF, **Hours Estimated** - SUMIF, **Hours Logged** - Sum, **Hourly Rate** - Avg, and **Budget Allocated** - SUMIF.

  ![SUM-UP row displaying the sum-up values.png](/cms_trial/assets/f2790680-5f9b-4e47-a478-985d91a027fd.png)

- Click **Save** and **Publish** the page. You can view the configured summary values in both view and edit modes of the Confluence page.

  ![Column calculation sum-up row in page view mode.png](/cms_trial/assets/e538088b-4c51-47ac-8b7c-a85af86522e9.png)

[Unmapped macro: refined-tab — no content to fall back on]

To disable the configured Sum-up type for any column, navigate to the *Edit column calculation* dialog and select **None**.

For example, to disable the column calculation:

- For the **Status** column, navigate to **Edit column** (▢ ) > **Edit column calculation**. The *Edit column calculation* dialog opens.
- Select **None**, and click **Save**.

  ![Disable column calculation for Status column.png](/cms_trial/assets/dd841295-eb75-48ae-b6aa-52e458fe7066.png)