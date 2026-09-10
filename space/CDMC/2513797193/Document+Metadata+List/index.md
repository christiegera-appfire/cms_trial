# Document Metadata List

## Overview

The **Document** **Metadata List** macro stores and displays multiple metadata key–value pairs in a table format. It helps organize and present related metadata values, such as document details, reviewer information, or workflow data, in a clear and structured way.

Metadata values defined with this macro can also be accessed in workflow definitions or retrieved using other metadata macros.

## Syntax

You can define multiple key–value pairs using the following format:

```text
||job|cook|
||salary|1000|
||city|Boston|
```

Each row represents a metadata key and its corresponding value.

## Parameters

| **Parameter** | **Description** |
| --- | --- |
| **Orientation of the table** | Defines how the metadata table is displayed horizontally or vertically. |
| **Hidden** | When selected, the metadata table is stored but not displayed as part of the page content. |
| **Content** | The list of metadata keys and values, written using the syntax shown above. |

## Add the macro

To add the Document Metadata List macro:

1. On a draft page, type `/document metadata List`.

   ![Comala Document Metadata List macro output on a page](/cms_trial/assets/b6bd2873-6e83-4bc3-97fe-0d7d97c77979.png)
2. Choose the **Document Metadata List** macro. Click the macro to edit and choose the orientation of the table.

   ![Comala Document Metadata List macro with metadata entries displayed](/cms_trial/assets/4cdf612f-e09e-4d7e-b012-6ab2a3acfbf6.png)

1. **Publish** or **update** the page to retrieve and render the metadata value on the page.

   ![Comala Document Metadata List macro configuration settings](/cms_trial/assets/febfe1d4-1617-4a91-923c-292501624214.png)