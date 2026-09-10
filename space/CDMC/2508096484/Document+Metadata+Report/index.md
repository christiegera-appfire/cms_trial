# Document Metadata Report

## Overview

The **Document Metadata Report** macro displays a table of metadata values from multiple pages within a selected Confluence space.

It retrieves metadata set using the following macros or actions:

- Document Metadata Set macro
- Document Metadata List macro
- Page Parameters
- Set-metadata workflow action

## Parameters

| **Parameter** | **Description** |
| --- | --- |
| **Fields** *(required)* | Defines the list of fields (columns) to display in the report. You can include both Confluence internal metadata and custom metadata names. **Reserved keywords** for internal metadata include: `Title`, `Version`, `Author`, `Time Created` |
| **Space key** *(required)* | Specifies the Confluence space to list pages from. Only one space key can be used at a time.  `@self` can be used for the current space. |
| **Label(s)** | Limits the content to pages that contain the specified labels. Accepts a comma-separated list. Any page with one or more of the listed labels will be included in the report. |
| **Root** *(required)* | Defines the root or starting point for the report.  Possible values include:   - `@self` — current page (default) - `@parent` — parent page - *page title* — a specific page name |
| **Pages** | Defines the set of pages to retrieve from the specified root page(s).  It supports the following values:  `@children`, `@ancestors`, `@descendants,` and `@identity`.  For example, `|root=@self|pages=@children` retrieves all child pages of the current page.  This parameter can be combined with the **Labels** option to include only child pages with specific labels. |
| **Maximum number of results** | Sets the limit on the number of results shown in the report (default and maximum value is 10). |
| **Sort order** | Specifies the column to sort the report by (for example, `"Status desc"`).  You can include a hint for the sort method before the sort direction. For example, `"Name as istring asc"` or `"Name as istring"` applies a case-insensitive comparison, treating values as strings. Other available options include `"as date"`, `"as number"`, and `"as string"` (case-sensitive). The default sort method is case-insensitive comparison. |

## Add the macro

Shows metadata from matching pages in a table report.

To add the Document Metadata Report macro:

1. On a draft page, type `/document metadata report`**.** 

   ![The Document mMetadata Report macro.](/cms_trial/assets/55b5abc4-4807-497e-a9c1-6ea0fb11ad0f.png)
2. Click the **Document Metadata Report** macro to edit and enter the required values.

![The Insert Document Metadata Report window.](/cms_trial/assets/5679bde9-d903-4006-b155-a9a764560fb5.png)

1. Click **Insert** to insert the macro in your page.