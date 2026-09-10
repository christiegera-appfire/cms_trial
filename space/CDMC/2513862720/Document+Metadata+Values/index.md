# Document Metadata Values

## Overview

The **Document Metadata Values** macro displays a table containing all metadata key–value pairs associated with a page. It provides a quick way to view all metadata information defined on a page, including metadata set using the following macros or actions:

- Document Metadata Set macro
- Document Metadata List macro
- Page Parameters
- Set-metadata workflow action

## Parameters

| **Parameter** | **Description** |
| --- | --- |
| **Space** *(required)* | The space where the target page is located. Defaults to **@self**, which points to the current space. |
| **Page** *(required)* | The page from which to retrieve all associated metadata keys and values. The default value `@self` points to the current page. |
| **Orientation of the table** | Defines how the metadata table is displayed horizontally or vertically within the page content. |

## Add the macro

The macro displays all metadata key–value pairs from the specified page in a table format. If no page is specified, it defaults to the current page (`@self`). Add this macro to a page to display all metadata associated with that page or with another specified page.

To add the Document Metadata List macro,

1. On a draft page, type **/document metadata values**

   ![The document metadata values macro.](/cms_trial/assets/19ec38fe-1f25-412c-9a84-59c366678685.png)
2. Choose the **Document Metadata Values** macro. Click the macro to edit and choose the orientation of the table.

   ![The Insert Metadata Values window showing the Space, Page, and Orientation fields.](/cms_trial/assets/78d2fa83-dcd5-4b54-956a-e67843756a37.png)
3. Click **Insert**. This displays the metadata names and their corresponding values on the current page.