# Column calculation with Advanced Table Viewer macro

The Advanced Table Viewer macro enables you to perform column calculations and display summarized values at each column level.

## **Column calculation**

The **Column calculation** feature supports the following calculation types: Sum, Average, Minimum, Maximum, Count, and Distinct. You can configure the Sum-up type for each column independently.

- You can configure the column calculation only in macro setup mode and cannot change it in Confluence page view and edit mode.
- The feature adds a row below the table header.
- The macro displays the configured Sum-up values in the Confluence page view and edit mode.

  ![Advanced Table Viewer macro configuration showing available sum-up type options for table columns.](/cms_trial/assets/2261b37f-95d8-4ec7-87b3-1273f5083da8.png)

## Manage column calculations

[Unmapped macro: refined-tab — no content to fall back on]

You can perform the following column calculations.

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

You need edit permissions to access the macro setup mode.

1. To configure **column calculation**, edit the macro to open the setup mode. Refer to [Set up the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/). Each column in the table has an *Edit column* (▢ ) option.
2. To set up the column calculation for any column, navigate to **Edit column** > **Edit column calculation**. For example, for the **Tax** column, click **Edit column calculation**.

   ![Edit column menu showing the Edit column calculation option selected for the Tax column.](/cms_trial/assets/9e6ce8bf-bc9f-4af1-9f3b-b4087aa8fcf2.png)
3. The *Edit column calculation* dialog opens. Select the required Sum-up type, and click **Save**. For example, for the **Tax** column, **Average** is selected.

   ![Edit column calculation dialog with Average selected for the Tax column.](/cms_trial/assets/feda288c-a019-4a6c-8297-081ee5ac49f1.png)

- For the String and Date column type, the *Edit* *column calculation* dialog displays *None*, *Count*, and *Distinct*.

  ![Edit column calculation dialog for a string column showing None, Count, and Distinct options.](/cms_trial/assets/a40fee5e-c981-49a5-b3e7-06aa2df0a090.png)

1. The summarized row appears as the first row below the table header and displays the configured sum-up values. For example: **Index** - Count, **Item** - Distinct, **Cost** - Max, **Tax** - Avg, **Total** - Sum.

   ![First row displaying configured sum-up values.](/cms_trial/assets/114a3910-6338-48f6-b708-f66638b3a4e5.png)

1. Click **Save** and **Publish** the page. You can view the configured summary values in both view and edit modes of the Confluence page.

   ![Table displaying summarized column values in the Advanced Table Viewer macro.](/cms_trial/assets/446d5ced-d6c1-4a43-a8ef-f0e22c50d61c.png)

[Unmapped macro: refined-tab — no content to fall back on]

To disable the configured sum-up value for any column, navigate to the *Edit column calculation* dialog and select **None**.

For example, to disable the column calculation for the **Tax** column:

1. Click the **Tax** *Edit column*. The *Edit column calculation* dialog opens.
2. Select **None**, and click **Save**.

   ![Edit column calculation dialog with None selected to disable summary values for a column.](/cms_trial/assets/ee6db992-67ef-488e-a8d6-d12ca2153990.png)