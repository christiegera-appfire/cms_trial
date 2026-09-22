# Get started with Advanced Tables for Confluence for Cloud

**Connect End of Support**: Atlassian has [announced](https://www.atlassian.com/blog/developer/announcing-connect-end-of-support-timeline-and-next-steps) the end of support for the Connect framework in late 2026.

- At Appfire, we are committed to maintaining the highest standards of security, reliability, and performance across our solutions.
- As part of this commitment, the **Advanced Tables for Confluence** cloud app has been developed and deployed on **Atlassian Forge**, Atlassian’s most advanced cloud development platform. For more information about the upgrade, refer to the [Release notes February 2026](/cms_trial/space/TBL/2766798931/Release+notes+February+2026/).
- The Advanced Tables for Confluence app on Forge Remote now **offers an improved macro editor experience**.
- The **Connect version** of Advanced Tables for Confluence is out of date and will no longer receive updates. **Contact your Confluence administrator** to **update** the app.
- Contact our [support team](https://appf.re/support) if you have any questions.

**Why Forge Remote?**

- Moving to Forge ensures that your data is protected within Atlassian’s trusted infrastructure, leveraging its built-in security, compliance, and scalability capabilities.
- This advancement represents our ongoing dedication to delivering solutions that meet Level 3 (Forge) and Level 4 (Runs on Atlassian – RoA) technical and security standards.
- By embracing Forge, Appfire continues to deliver on its promise to offer secure, enterprise-grade apps that evolve with Atlassian’s platform, giving you confidence that your workflows are supported by the strongest foundation available.

## Communicate information that matters — with tables built for limitless potential.

Advanced Tables for Confluence extends Confluence's native table capabilities with a set of powerful macros — letting you import, display, and manage data as structured, customizable tables.

Whatever your data source — CSV files, Excel spreadsheets, JSON data, page attachments, or native Confluence tables — Advanced Tables has the right macro for you.

Additionally, the Advanced Table Viewer and Native Table Enhancer macros bring Atlassian Rovo integration — turning your table data into instant AI-driven insights, all within Confluence.

---

## Get started with a real use case

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

   ![Insert ATV macro.png](/cms_trial/assets/55724c6c-6bff-4089-8e5a-6bb3e1dff1a3.png)
2. **Connect Data Source:** On the initial macro setup screen, click **Connect Data Source**.

   ![Connect Data Source.png](/cms_trial/assets/e3a96329-f049-4f76-98d6-fd4f7add2e37.png)
3. **Select Data Connector:** From the *Select data connector* dropdown, select **Excel**.

   ![Select data connector as Excel.png](/cms_trial/assets/36eded93-001d-46c0-ab34-6724e9a67585.png)
4. **Upload sample Excel file:** Click **Browse** and select `Employee_Directory.xlsx` from your computer, and upload it.

   ![Browse and select Excel file.png](/cms_trial/assets/6d60b826-c9e2-492b-b77e-b25e5eb91528.png)
5. **Save the changes**:The macro will automatically display the first sheet name (`Employees`) and its columns. Click **Save** to enter setup mode.

   ![ATV_macro displays sheet name and columns.png](/cms_trial/assets/60361c00-0e4e-49bf-91b2-1fa12794588f.png)

#### 🔸 **Macro setup mode: Customize filters, grouping, and calculations**

1. **Enable and set column filter**: In the right panel, enable **Column filtering** (▢ ) and then enable **Column filters**.For the **Status** column, select the *dropdown* filter.

   ![ATV_macro_Column filters.png](/cms_trial/assets/078167db-b5f5-4e5d-b835-14cbef47e3f0.png)
2. **Enable Column Grouping:**  In the right panel, enable **Grouping**.
3. **Group by Department**: Hover over the **Department** column header and click the grouping icon you see on the **Department** column header to group by this column.

   ![ATV_grouping.png](/cms_trial/assets/15cd7ae6-1047-4656-9f74-2bbb63ca9860.png)
4. **Configure group calculation:** In the **Salary ($)** column header, click **Edit Column** (▢ ) and select **Edit group calculation**.

   ![ATV_Edit group calculation.png](/cms_trial/assets/2b5347ad-7ccd-4cd5-93db-701918ee559e.png)
5. **Select** **Sum-up type**: Select the **Sum** checkbox and click **Save**.

   ![Edit group calculation_Sum.png](/cms_trial/assets/eed1cc46-1da8-4ba7-9e64-951a7378cfbf.png)
6. **Save the macro**: The macro displays the Sum of salaries at each department level. To save the macro configuration, click **Save**.

   ![ATV_Department column grouped.png](/cms_trial/assets/04d23c86-9a80-420f-880a-4eb7c4be0930.png)
7. **Publish**: Click **Publish (**or **Update)** to save the page.

   ![ATV_page view mode.png](/cms_trial/assets/f2e2cce1-2cc4-4778-a5d0-a42a67980fab.png)

#### ✅ Outcome: Publish and analyze table data

Your Confluence page now features an interactive employee directory table where you can expand/collapse departments to view grouped salary totals and quickly filter records by employee status.

Image — asset pipeline pending  
Analyze table data in Confluence page.gif

## 📚 **What’s next?**

- To import Excel data using other data source types such as Attachment or URL, refer to [Configure Excel data source in Advanced Table Viewer macro](/cms_trial/space/TBL/3122888898/Configure+Excel+data+source+in+Advanced+Table+Viewer+macro/).
- To analyze your table data using Atlassian Rovo, refer to [Analyze Advanced Table Viewer data with Atlassian Rovo](/cms_trial/space/TBL/3429499007/Analyze+Advanced+Table+Viewer+data+with+Atlassian+Rovo/).

### **Quick-start videos**

Get onboarded quickly — watch the [quick-start videos](/cms_trial/space/TBL/3647963421/Quick+start+guide+to+Advanced+Tables+for+Confluence/) for Advanced Tables for Confluence macros.

### Migrate to cloud

Are you planning to migrate from Data Center to cloud? Refer to the [Migration guide](/cms_trial/space/TBL/3131703327/Migrate+to+cloud/).

### Use cases

Refer to macro-specific [Use cases](/cms_trial/space/TBL/74814716/Use+cases+-+cloud/) to take full advantage of the app's capabilities.

Advanced Tables for Confluence - Data Center documentation has moved to a dedicated space. Visit [Advanced Tables for Confluence - Data Center.](https://appfire.atlassian.net/wiki/spaces/atdc)