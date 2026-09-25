# Release notes September 2026

**Release date**: September 17, 2026

This page outlines the updates included in the latest release of Advanced Tables for Confluence.

Version: 8.1.0

---

## New features

The **Advanced Table Viewer** and **Native Table Enhancer** macros now let you manage columns to control **column visibility** and **add calculated columns**.

For the Sum-up type Sum and Count, under Edit column calculation, you can add a condition so only matching rows are included in the summary.

## Advanced Table Viewer macro

### Manage columns

#### Manage column visibility

1. To configure column visibility in macro setup mode, enable **Manage columns**.
2. Under **Columns**, you can select or clear the checkbox and click **Save**. For more information, refer to [Manage column visibility with Advanced Table Viewer macro](/cms_trial/space/TBL/3637706822/Manage+column+visibility+with+Advanced+Table+Viewer+macro/).

   ![ATV_deselect columns copy.png](/cms_trial/assets/fa0a8c1c-f7e4-490b-92bf-b6bb024926a1.png)

#### Manage calculated columns

The macro now lets you create new calculated columns using values from other columns.

- To add and configure a new calculated column, either click **Add calculated column** under **Calculated columns**, or click **+** at the end of the column headers in the left panel.

  ![image-20260916-134118.png](/cms_trial/assets/1ba44db2-7999-4040-b21e-e925aa3f787f.png)

- The *Add calculated column* dialog lets you calculate and derive a new column using the **Builder** or **Formula** tab. For more information, refer to [Manage calculated columns with Advanced Table Viewer macro](/cms_trial/space/TBL/3643965558/Manage+calculated+columns+with+Advanced+Table+Viewer+macro/).

  - **Builder**: The **Builder** tab provides a user-friendly interface to configure simple mathematical operations without writing custom syntax.

    ![ATV_calculated column_total cost.png](/cms_trial/assets/5f5629f2-8709-4fcb-b012-db5094a2aeae.png)

- - **Formula**: The **Formula** tab lets you write custom formulas using a formula editor.

    ![ATV_calculated column_Formula.png](/cms_trial/assets/4a99168c-1b7e-46f6-af56-b0012a3f225e.png)
  - After you add calculated columns, you can manage them under **Calculated columns** in the right panel.

    ![image-20260916-135247.png](/cms_trial/assets/d37b3bec-6015-4c16-af32-93905e2d4a9b.png)

## Conditional column calculation

- For the Sum-up types **Sum** and **Count**, under **Edit column calculation**, you can now add a condition to include only rows matching that condition. For more information, refer to [Column calculation with Advanced Table Viewer macro](/cms_trial/space/TBL/1540654683/Column+calculation+with+Advanced+Table+Viewer+macro/).

  ![image-20260916-135810.png](/cms_trial/assets/0c05f81e-b570-4c81-a8a9-26cb385ae370.png)

## Native Table Enhancer macro

### Manage columns

#### Manage column visibility

1. To configure column visibility in macro setup mode, enable **Manage columns**.
2. Under **Columns**, you can select or clear the checkbox and click **Save**. For more information, refer to [Manage column visibility with Native Table Enhancer macro](/cms_trial/space/TBL/3639115855/Manage+column+visibility+with+Native+Table+Enhancer+%5BBeta%5D+macro/).

   ![Native Table_column visibility_deselect columns copy.png](/cms_trial/assets/5d2e9528-48bb-41f4-a84c-f37140ff7c65.png)

#### Manage calculated columns

The macro now lets you create new calculated columns using values from other columns.

- To add and configure a new calculated column, either click **Add calculated column** under **Calculated columns**, or click **+** at the end of the column headers in the left panel.

  ![NTE_Add calculated column.png](/cms_trial/assets/2b1ea710-051e-4316-bff1-ab43497342e0.png)
- The *Add calculated column* dialog lets you calculate and derive a new column using the **Builder** or **Formula** tab. For more information, refer to [Manage calculated columns with Native Table Enhancer macro](/cms_trial/space/TBL/3676897293/Manage+calculated+columns+with+Native+Table+Enhancer+macro/).
- **Builder**: The **Builder** tab provides a user-friendly interface to configure simple mathematical operations without writing custom syntax.

  ![NTE_Builder tab.png](/cms_trial/assets/0a82ba04-89c0-48e2-8e6e-1c218984ab52.png)
- **Formula**: The **Formula** tab lets you write custom formulas using a formula editor.

  ![NTE_calculated column_Formula.png](/cms_trial/assets/da862c0e-ae0d-4065-bc6e-b79652786136.png)
- After you add calculated columns, you can manage them in the right panel.

  ![NTE_manage calculated columns.png](/cms_trial/assets/a3bc2632-f1a7-4a78-a821-b88047c7d6f9.png)

### Conditional column calculation

- For the Sum-up types **Sum** and **Count**, under **Edit column calculation**, you can now add a condition to include only rows matching that condition. For more information, refer to [Column calculation with Advanced Table Viewer macro](/cms_trial/space/TBL/1540654683/Column+calculation+with+Advanced+Table+Viewer+macro/).

  ![NTE_conditional sum.png](/cms_trial/assets/1f7ff238-7579-4649-9288-99f2c294c0e9.png)

---

## Bug fixes

The following bugs are fixed in this release:

**JSON Table macro**

- Resolved the issue wherein the JSON Table macro failed to load data from JSON URLs with internal redirects. Now, the macro processes internal redirects correctly so data loads as expected.
- Resolved the issue wherein the JSON Table macro failed to load data from JSON URLs with responses exceeding 5 MB. The macro now loads the data as expected.

---

**Questions and feedback**

- Explore exciting features, pricing updates, reviews, and more on the [Marketplace](https://marketplace.atlassian.com/apps/197/advanced-tables-for-confluence?hosting=cloud&tab=overview).
- Stuck with something? Raise a ticket through our [support portal](https://appf.re/support).
- Do you love using our app? Let us know what you think [here](https://marketplace.atlassian.com/apps/197/advanced-tables-for-confluence?hosting=cloud&tab=reviews).

**Credits**

Thank you to our valued customers! Your incredible support and feedback inspire us to improve continuously. We appreciate your trust in Advanced Tables for Confluence!