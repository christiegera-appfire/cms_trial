# Native Table Enhancer [Beta] macro

## Overview

The Native Table Enhancer macro transforms your native Confluence tables with advanced formatting and calculations for custom views and data analysis.

- The macro setup mode includes features such as sorting, searching, column filters, row styles, row numbering, grouping, column and group calculations, downloading, and pagination.
- The macro currently reads only the first native Confluence table content from the macro body on the Confluence page.
- The macro supports only plain text in table cells and converts the content of each cell to plain text if other attributes are present.
- Other content in the macro body, such as paragraphs, headings, lists, etc., is rendered as normal Confluence content.

**Beta release notice:** The Native Table Enhancer macro is currently in beta.

While we strive to deliver a seamless experience, minor issues can arise. We encourage you to explore the macro and share your [feedback](https://appf.re/support) to help us improve the final release. Thank you for your support and understanding!

## **What is in the beta release**?

In the beta release, you can enhance the first native Confluence table in the Native Table Enhancer macro body for custom views and data analysis.

### **Beta limitations**

- The Native Table Enhancer macro does not support:

  - Attachments
  - Data profiles
  - External URLs
  - Multiple tables:

    - If the macro body contains more than one top-level Confluence table, the first table is used for configuration and enhanced rendering.
    - Additional tables in the macro are not enhanced and are not rendered when the Confluence page is published. We recommend including only one native Confluence table in the Native Table Enhancer macro.
- The macro supports only plain text. It converts each cell's content to plain text, and during conversion, the following attributes are not preserved:

  - Links
  - Images
  - Nested macros
  - Nested tables
  - @mentions

If you want to import data from other sources such as CSV, Excel, JSON, and Jira work items, use the [**Advanced Table Viewer**](/cms_trial/space/TBL/1531117698/Advanced+Table+Viewer+macro/)[**macro**](/cms_trial/space/TBL/1531117698/Advanced+Table+Viewer+macro/) instead.

## **Enhance your native Confluence table with Native Table Enhancer macro features**

|  |  |  |
| --- | --- | --- |
| [Unmapped macro: refined-button — no content to fall back on] | [Unmapped macro: refined-button — no content to fall back on] | [Unmapped macro: refined-button — no content to fall back on] |
| [Unmapped macro: refined-button — no content to fall back on] | [Unmapped macro: refined-button — no content to fall back on] | [Unmapped macro: refined-button — no content to fall back on] |
| [Unmapped macro: refined-button — no content to fall back on] | [Unmapped macro: refined-button — no content to fall back on] | [Unmapped macro: refined-button — no content to fall back on] |
| [Unmapped macro: refined-button — no content to fall back on] | [Unmapped macro: refined-button — no content to fall back on] |  |

## Insert and configure the macro

[Unmapped macro: refined-tab — no content to fall back on]

**Macro basic use**

You can add the macro to a Confluence page using one of the following methods:

|  |  |
| --- | --- |
| **Select from the macro browser** | **Insert elements** > Native Table Enhancer Insert Native Table Enhancer macro from Insert elements |
| **Macro shortcut (New editor)** | **Confluence page** > /Native Table Enhancer Insert Native Table Enhancer macro using macro shortcut |

**Insert or paste a Confluence table**

- Once you insert the macro, you can either insert or paste the Confluence table.

  ![Insert Native Table Enhancer macro on Confluence page](/cms_trial/assets/24026680-b334-43c9-a2a7-c9f62c711934.png)

- Add the table data, and to configure the macro, click **Edit**.

  ![Native Table Enhancer_Add or paste table data and edit to configure](/cms_trial/assets/0da0f8cf-6d7e-4bf4-9d86-0e9df9559bf1.png)

- The macro opens in setup mode, displaying the table with the column names and data. Refer to the **Set up the macro** section on this page.

[Unmapped macro: refined-tab — no content to fall back on]

- The Native Table Enhancer macro setup mode lets you configure the macro features and make them accessible in Confluence page view mode.
- You need edit permissions to configure the macro features.
- For reference, the table displays download, row styling, and dropdown column filters. For more information, refer to [Set up the Native Table Enhancer macro features](/cms_trial/space/TBL/3568173057/Set+up+the+Native+Table+Enhancer+%5BBeta%5D+macro+features/).
- To apply the configurations, click **Save**.

  ![Native Table Enhancer_configure features in setup mode](/cms_trial/assets/58b877ec-0f9f-4056-9ff4-df3685e90476.png)
- Once you save the macro, the table appears in Confluence page edit mode. The Confluence page edit mode does not show the applied feature configurations, and the native table is displayed as is.

  ![Table enhancer_Page edit mode does not display the configured features](/cms_trial/assets/54998bb2-85ee-4e45-8c70-4b83f9a77014.png)
- **Publish** the page to view the table with all applied feature configurations.

  ![Table enhancer_publish changes and the page view mode displays the features configured](/cms_trial/assets/4735b4ae-2b04-42de-9cb3-5518916e5a50.png)

Your native Confluence table data is now ready to view and analyze directly within Confluence. To analyze the table data, refer to the page [Analyze Native Table Enhancer data with Atlassian Rovo](/cms_trial/space/TBL/3568173411/Analyze+Native+Table+Enhancer+%5BBeta%5D+macro+data+with+Atlassian+Rovo/).

## References

- [Set up the Native Table Enhancer macro features](/cms_trial/space/TBL/3568173057/Set+up+the+Native+Table+Enhancer+%5BBeta%5D+macro+features/)
- [Analyze Native Table Enhancer data with Atlassian Rovo](/cms_trial/space/TBL/3568173411/Analyze+Native+Table+Enhancer+%5BBeta%5D+macro+data+with+Atlassian+Rovo/)