# Column calculation with Native Table Enhancer [Beta] macro

The Native Table Enhancer macro enables you to perform column calculations and display summarized values at each column level.

The Native Table Enhancer macro is currently in beta. [Learn more](/cms_trial/space/TBL/3520037211/Native+Table+Enhancer+%5BBeta%5D+macro/).

## **Column calculation**

The **Column calculation** feature supports the following calculation types: Sum, Average, Minimum, Maximum, Count, and Distinct. You can configure the Sum-up type for each column independently.

- You can configure the column calculation only in macro setup mode and cannot change it in Confluence page view mode.
- The feature adds a row below the table header.
- The macro displays the configured Sum-up values in the Confluence page view mode.

  ![Edit column calculation dialog](/cms_trial/assets/84118a88-e754-4fd2-aea7-58b015f4a537.png)

## Manage column calculations

[Unmapped macro: refined-tab — no content to fall back on]

You can perform the following column calculations.

| **Type** | **Description** | **Column type** | **Indicator on the Confluence page** |
| --- | --- | --- | --- |
| None | Disables the column calculation: no value is displayed for the column | Any | Not applicable |
| Sum | Calculates the total of all values in the column | Numeric | Sum |
| Average | Calculates the average of all values in the column | Numeric | Avg |
| Minimum | Returns the lowest numerical value in the column | Numeric | Min |
| Maximum | Returns the highest numerical value in the column | Numeric | Max |
| Count | Counts the total number of non-empty cells in the column | Numeric, String, Date | Cnt |
| Distinct | Counts unique values only, ignoring duplicates and empty cells | Numeric, String, Date | Disct |

[Unmapped macro: refined-tab — no content to fall back on]

You need edit permissions to access the macro setup mode.

1. To configure **column calculation**, edit the macro to open the setup mode. Refer to [Set up the Native Table Enhancer macro features](/cms_trial/space/TBL/3568173057/Set+up+the+Native+Table+Enhancer+%5BBeta%5D+macro+features/). Each column in the table has an *Edit column* (▢ ) option.
2. To set up the column calculation for any column, navigate to **Edit column** > **Edit column calculation**. For example, for the **Stock Qty** column, click **Edit column calculation**.

   ![Edit column calculation](/cms_trial/assets/50197bc9-1c1c-43f5-a457-fa35416187c2.png)
3. The *Edit column calculation* dialog opens. Select the required Sum-up type, and click **Save**. For example, for the **Stock Qty** column, **Sum** is selected.

   ![Select sum up type for Column Calculation](/cms_trial/assets/f9bcbb9f-fd58-48b1-ac45-6d995f44667e.png)

- For the String and Date column type, the *Edit* *column calculation* dialog displays *None*, *Count*, and *Distinct*.

  ![Sum up type for String and date column calculation](/cms_trial/assets/9628b961-7e42-4d92-b52e-3a3a683013bc.png)

1. The summarized row appears as the first row below the table header and displays the configured sum-up values. For example: **Category** - Distinct, **Product ID** - Count, **Unit Price** - Max, **Stock Qty** - Sum, **Reorder Level** - Average.

   ![Summarized row appears as first row below the table header](/cms_trial/assets/6b14cfed-a07b-485e-a686-f18fa0f49f72.png)

1. Click **Save** and **Publish** the page. You can view the configured summary values in the Confluence page view mode.

   ![Summarized value in Page view mode](/cms_trial/assets/b54ead76-92fa-4a3e-828a-3b74ee75d3e0.png)

[Unmapped macro: refined-tab — no content to fall back on]

To disable the configured sum-up value for any column, navigate to the *Edit column calculation* dialog and select **None**.

For example, to disable the column calculation for the **Tax** column:

1. Click the **Stock Qty** *Edit column*. The *Edit column calculation* dialog opens.
2. Select **None**, and click **Save**.

   ![To disable the configured sum-up value for any column select None](/cms_trial/assets/d6f388f6-5fce-4175-a46a-080fba66f68d.png)