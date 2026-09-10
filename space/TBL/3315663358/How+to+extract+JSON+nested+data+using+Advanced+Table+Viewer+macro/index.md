# How to extract JSON nested data using Advanced Table Viewer macro

## Overview

This page guides you through using the **Advanced Table Viewer** macro to connect a JSON data source and extract nested inventory data into a simple table on your Confluence page.

## Insert the macro and configure the JSON data source

1. Insert the macro in a Confluence page using the macro shortcut (/).
2. Type `/Advanced` and select **Advanced Table Viewer**.

   ![image-20260603-132615.png](/cms_trial/assets/aaa1b57d-bf50-41ac-80e8-891b0ea2ad97.png)
3. Click **Connect Data Source**.

   ![ATV_Connect data source.jpg](/cms_trial/assets/07f0e2cd-9bdb-4b03-997c-8f440362634b.jpg)
4. From the **Select data connector** dropdown, select *JSON*. Under the **Choose data source type**, select **Upload file**.

   ![ATV_JSON upload.jpg](/cms_trial/assets/d9cf5414-b171-4e16-a496-3d826c827bb6.jpg)
5. Click **Browse** and select the JSON inventory file.

   ![ATV_JSON_browse and upload file.jpg](/cms_trial/assets/fdfd4dc7-fd76-449a-a15f-4e386c71d27d.jpg)
6. Once you choose the file, the **Row data path** field appears.

**Row data path**: Enter the JSON data path to import data and generate a table.

- The path can be a dot-separated path to the target field in the JSON string. The path is case sensitive.
- If fields along the specified row data path contain multiple values (arrays or objects), the macro cannot parse or display the data. To successfully extract data, the Row data path must navigate strictly through single-value parent objects or explicit array indexes (e.g., `[0]`) until it reaches the final target array.
- For more information, refer to [JSON path syntax](https://goessner.net/articles/JsonPath/).

Fields with multiple values (arrays or objects) are not supported to keep the table simple and sortable.

### Configure the Row data path

Expand to view the JSON path architecture of the Inventory source file used for the scenarios below.

The Inventory file JSON path architecture

▲ Root Object: inventory  
 └── 📄 Field: sheet ("Product Inventory")  
 └── 📂 Array: categories (Cannot pass as a wildcard!)  
 ├── 📦 Object: categories[0] (Hardware)  
 │ └── 📂 Array: subcategories  
 │ ├── 📦 Object: subcategories[0] (Processors\_and\_Memory)  
 │ └── 📋 Array: products ◄── [TARGET SCALAR DATA]  
 │ └── 📦 Object: subcategories[1] (Storage)  
 │ └── 📋 Array: products  
 └── 📦 Object: categories[1] (Networking)  
 └── 📂 Array: subcategories  
 └── 📦 Object: subcategories[0] (Infrastructure)  
 └── 📋 Array: products

Download the JSON file used for the scenarios![contentId-3315663358](/cms_trial/assets/191148b7-6c3d-403f-9593-9aadb31d752d.json)

## Scenarios

[Unmapped macro: refined-tab — no content to fall back on]

This scenario demonstrates how to use the recursive descent operator (`..`) to generate a table with grouped row nesting.

- **Row data path**: inventory.categories..
- **Select columns**: Once you specify the **Row data path**, the **Select columns** field displays the list of field names available at the specified path. You can remove, select, and reorder the column names as needed.

  ![ATV_JSON Source_grouped category.jpg](/cms_trial/assets/80337ae5-faa3-44a9-b078-1089a3914e5d.jpg)
- Click **Save**. The macro opens in setup mode, displaying the table with the selected column names and data.

  ![ATV_JSON Source_Extract group inventory category.jpg](/cms_trial/assets/916e77d4-f1e7-4128-9b2c-ef5e7cacaded.jpg)
- To configure various features in setup mode, refer to [Set up the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/).
- To apply the configurations, click **Save,** and the configured table appears on the Confluence page in edit and view mode.

[Unmapped macro: refined-tab — no content to fall back on]

This scenario demonstrates how to fetch a high-level list of all primary categories from the root of your JSON.

- **Row data path**: inventory.categories
- **Select columns**: Once you specify the **Row data path**, the **Select columns** field displays the list of field names available at the specified path. You can remove, select, and reorder the column names as needed.

  ![ATV_JSON_Row data path for primary categories.jpg](/cms_trial/assets/bab4ccca-f3eb-4beb-a9ba-7d36337e5da0.jpg)

- Click **Save**. The macro opens in setup mode, displaying the table with the selected column names and data.

  ![ATV_JSON Source_primary category names.jpg](/cms_trial/assets/b7ba9963-a14f-4249-abe5-fa44dca49379.jpg)
- To configure various features in setup mode, refer to [Set up the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/).
- To apply the configurations, click **Save,** and the configured table appears on the Confluence page in edit and view mode.

[Unmapped macro: refined-tab — no content to fall back on]

This scenario demonstrates how to use bracket-index notation to extract core hardware component data.

- **Row data path**: inventory.categories[0].subcategories[0].products
- **Select columns**: Once you specify the **Row data path**, the **Select columns** field displays the list of field names available at the specified path. You can remove, select, and reorder the column names as needed.

  ![ATV_JSON source_Row data path_Extract core hardware components.jpg](/cms_trial/assets/3992342f-d183-4ddd-8976-adb68f2daeb3.jpg)

- Click **Save**. The macro opens in setup mode, displaying the table with the selected column names and data.

  ![ATV_JSON Source_Extract core hardware.jpg](/cms_trial/assets/45e06848-93cf-4c25-a945-2a8cdbc52227.jpg)
- To configure various features in setup mode, refer to [Set up the Advanced Table Viewer macro features](/cms_trial/space/TBL/1765147138/Set+up+the+Advanced+Table+Viewer+macro+features/).
- To apply the configurations, click **Save**, and the configured table appears on the Confluence page in edit and view mode.

## More examples

Similarly, you can extract the data for specific categories. The table below lists the specific category scenarios.

| **Specific category scenarios** | **Row data path syntax** | **Output screen in setup mode** |
| --- | --- | --- |
| Network Infrastructure | inventory.categories[1].subcategories[0].products | ATV_JSON_Network Infrastructure.jpg |
| Displays and Audio | inventory.categories[2].subcategories[1].products | ATV_JSON_Displays and Audio.jpg |
| Software Security | inventory.categories[3].subcategories[1].products | ATV_JSON Source_Software security.jpg |
| Wireless and cabling | inventory.categories[1].subcategories[1].products | ATV_JSON Source_Extract wireless and cabling products.jpg |