# Quick start guide to Advanced Tables for Confluence

## Transform your Excel data into an interactive Confluence report

Get started with the Advanced Tables for Confluence app by completing this quick 12-step walkthrough of the Advanced Table Viewer macro.

### 🚀 What will you do?

In this 12-step walkthrough, you will configure the Advanced Table Viewer macro to import sample Excel data and apply real-time filtering, grouping, and column calculations.

### 📌 Prerequisites and sample file

- Install the latest version of the Advanced Tables for Confluence app on your cloud instance.
- ⬇️ **Download** and save the Employee\_Directory.xlsx sample file to your desktop before beginning. ▢

### 🔢 Step-by-step walkthrough

⏱️ 6–8 minutes

#### 🔹 **Insert macro and connect data source**

1. **Insert the macro**: Type `/Advanced Table Viewer` in the Confluence page editor and press **Enter**.

   ![Insert ATV macro.png](/cms_trial/assets/66bcf60a-10ed-4d3a-97f2-4ab9dc765cab.png)
2. **Connect Data Source:** On the initial macro setup screen, click **Connect Data Source**.

   ![Connect Data Source.png](/cms_trial/assets/1f01013f-0094-46f3-b58b-40843bcdf468.png)
3. **Select Data Connector:** From the *Select data connector* dropdown, select **Excel**.

   ![Select data connector as Excel.png](/cms_trial/assets/1eeef363-2868-4bdf-99c5-41eaf272cc4b.png)
4. **Upload sample Excel file:** Click **Browse** and select `Employee_Directory.xlsx` from your computer, and upload it.

   ![Browse and select Excel file.png](/cms_trial/assets/151fd47b-519a-45d0-9ae2-7237fc0da506.png)
5. **Save the changes**:The macro will automatically display the first sheet name (`Employees`) and its columns. Click **Save** to enter setup mode.

   ![ATV_macro displays sheet name and columns.png](/cms_trial/assets/af083632-4200-40fe-9ccb-8aefc2a8fb49.png)

#### 🔸 **Macro setup mode: Customize filters, grouping, and calculations**

1. **Enable and set column filter**: In the right panel, enable **Column filtering** (▢ ) and then enable **Column filters**.For the **Status** column, select the *dropdown* filter.

   ![ATV_macro_Column filters.png](/cms_trial/assets/288532ec-a9c3-4384-8f4a-5155d5371040.png)
2. **Enable Column Grouping:**  In the right panel, enable **Grouping**.
3. **Group by Department**: Hover over the **Department** column header and click the grouping icon you see on the **Department** column header to group by this column.

   ![ATV_grouping.png](/cms_trial/assets/f097ff66-f0f6-4120-8b30-2fd7ee9f4f44.png)
4. **Configure group calculation:** In the **Salary ($)** column header, click **Edit Column** (▢ ) and select **Edit group calculation**.

   ![ATV_Edit group calculation.png](/cms_trial/assets/6ed5c33e-92bd-455c-8111-23df7d49594d.png)
5. **Select** **Sum-up type**: Select the **Sum** checkbox and click **Save**.

   ![Edit group calculation_Sum.png](/cms_trial/assets/a3cec581-3883-4585-a20b-fcb19680d47f.png)
6. **Save the macro**: The macro displays the Sum of salaries at each department level. To save the macro configuration, click **Save**.

   ![ATV_Department column grouped.png](/cms_trial/assets/f5e03bf3-8b98-41a3-9622-f6ce74314505.png)
7. **Publish**: Click **Publish (**or **Update)** to save the page.

   ![ATV_page view mode.png](/cms_trial/assets/0e6e5d3b-a540-49b2-8ac4-7c640a1100ff.png)

#### ✅ Outcome: Publish and analyze table data

Your Confluence page now features an interactive employee directory table where you can expand/collapse departments to view grouped salary totals and quickly filter records by employee status.

Image — asset pipeline pending  
Analyze table data in Confluence page.gif

## 📚 **What’s next?**

- To import Excel data using other data source types such as Attachment or URL, refer to [Configure Excel data source in Advanced Table Viewer macro](/cms_trial/space/TBL/3122888898/Configure+Excel+data+source+in+Advanced+Table+Viewer+macro/).
- To analyze your table data using Atlassian Rovo, refer to [Analyze Advanced Table Viewer data with Atlassian Rovo](/cms_trial/space/TBL/3429499007/Analyze+Advanced+Table+Viewer+data+with+Atlassian+Rovo/).
- To get onboarded quickly with other Advanced Tables for Confluence macros, [watch the quick-start videos](/cms_trial/space/TBL/74813990/Get+started+with+Advanced+Tables+for+Confluence+for+Cloud/).