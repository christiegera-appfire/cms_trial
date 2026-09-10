# Table Plus macro - Cloud

## Overview

The *Table Plus* macro adds advanced functions and formatting to Confluence tables. Users can perform the following functions on tables with this macro:

- Dynamically totalling numeric data
- Dynamically numbering each table row
- Defining the default sort order for the table
- Highlighting a row when the user hovers the pointer over it
- Using CSS to style the entire table or individual columns and rows

Watch this video for details on configuring Table Plus to perform the most common functions, including adding up columns and filtering.

This macro supports certain [common table capabilities](/cms_trial/space/TBL/74817747/Common+table+capabilities+-+Cloud/). You can perform column sorting and add other attributes to one or more tables found in the body of the macro. The tables can be produced by wiki markup or other means. Click a column heading to sort the column and click again to reverse the order.

## Insert macro

This macro can be added to a page using one of the following methods:

|  |  |
| --- | --- |
| **Select from the macro browser (Insert elements)** | *Table Plus* Insert Table plus macro from the macro browser |
| **Markup shortcut (New editor -** **case insensitive)** | */Table Plus* Insert Table Plus macro using the macro shortcut |

In the body of the macro, insert a Confluence table as you normally would and edit the row and columns as needed. You can just simply copy the relevant table(s) from other Confluence spaces or pages, and paste the table(s) directly into the macro body. On rendering or preview, the *Table Plus* macro processes the table to add the advanced capabilities according to the parameters specified in the macro editor.

## Parameters

The macro parameters are categorized into various tabs, such as **Structure and Data**, **Sort** **and Filter**, **Style**, and **Export**.

![Table plus macro configuration ](/cms_trial/assets/0f3b0e49-f2e1-4739-a19a-b47c4109e744.jpg)

## Macro specific parameters

| **Tab** | **Macro Editor Label** | **Default** | **Description** | **Macro Parameter** |
| --- | --- | --- | --- | --- |
| Structure and Data | Multiple table processing | true | Disable this option to process only the first table found in the macro body. By default, all tables that are present in the macro body are processed and rendered to the Confluence page. | multiple |

## Common parameters

These parameters are common table capabilities available across Advanced Tables macros.

[Unmapped macro: refined-tab — no content to fall back on]

| **Macro Editor Label** | **Default** | **Description** | **Macro Parameter** |
| --- | --- | --- | --- |
| Heading rows | 1 | Enter the number of rows that act as heading rows. Heading rows are not included when columns are sorted.  This parameter is not available for the *Attachment Table* macro. | heading |
| Footing rows | 0 | Enter the number of rows that act as footing rows. Footing rows are not included when columns are sorted.  This parameter is not available for the *Attachment Table* macro. | footing |
| Auto total row | false | Enable this option to append a row at the end of the table that contain the totals of all numeric columns.  Specify the relevant numeric types in *Column types* to render the totals. See ***Column types*** section for more information. | autoTotal |
| Columns to show  (Not available for the*Table Plus* macro) |  | Enter a comma-separated list of column names or numbers in any order. By default, all columns are displayed in their existing order. Note that columns are indexed beginning at "1" and exclude any auto-numbered columns.  This parameter is not available for the*Table Plus* macro. | columns |
| Column types |  | Column types determine how column data can be sorted and displayed. Refer to the **Column types** section on this page. | columnTypes |
| Column calculations |  | Refer to the **Column calculations** section on this page. | columnCalculations |

---

## Column types

---

## Column calculations

[Unmapped macro: refined-tab — no content to fall back on]

| **Macro Editor Label** | **Default** | **Description** | **Macro Parameter** |
| --- | --- | --- | --- |
| Enable column sorting | true | Deselect this option to disable sorting of columns. By default, all columns are sorted automatically based on their column types. | enableSorting |
| Sort auto number column | false | Select this option to enable the auto number column to be sortable. This retains the original data row count even after row sorting.  This parameter is not available for the *Attachment Table* macro. | autoNumberSort |
| Sort descending | false | Enable this option to sort in the descending order, to be done automatically, before display. This works only if *Auto sort column* is specified. | sortDescending |
| Show sort icon | false | Enable this option to include a sort icon in the first heading row for sortable columns. An icon is displayed for the last column sorted indicating the direction in which the column was sorted. | sortIcon |
| Auto sort column |  | Enter a valid column name or number to automatically sort the table before it is displayed. No automatic sorting is done if this value is not provided or is invalid. A column number is indexed beginning at "1" and excludes any auto-numbered columns. | sortColumn |
| Sort tip on mouse over |  | Enter the text to be displayed when the mouse is over a sortable column.  Example: **Click to sort** or an equivalent translation. | sortTip |
| Display data filter | false | Enable this option to see filter panel above the table to filter the data. Panel contains a text box to enter the required search criteria and buttons: *Filter* to proceed with the search, and *Clear* to clear the box to start a new search. Can use regular expressions. To know more about regular expressions, refer to [this article](/cms_trial/space/TBL/74814629/How+to+use+regular+expressions+-+Cloud/).  This parameter is not available for the *Attachment Table* macro. | displayDataFilter |
| Retain row style order after sorting | true | Enable this option to make the row styles correspond to the order in which the rows are displayed on the screen. If not selected, the original style given to a row is retained regardless of where the row lands after sorting. | retainRowStyleOrder |

[Unmapped macro: refined-tab — no content to fall back on]

| **Macro Editor Label** | **Default** | **Description** | **Macro Parameter** |
| --- | --- | --- | --- |
| Row styles |  | Enter a comma-separated list of styles to be applied to the specified rows. Each style is made up of one or more properties. The first style is applied to all heading rows determined by the *Number of heading rows* parameter. The remaining styles are applied to the remaining rows in order with repetition as necessary. A style can be reused for subsequent rows by referring to it using a 1-based numeric reference. A column number is indexed beginning at "1" and excludes any auto-numbered columns.  Row styles are applied to the table row and participate with other CSS properties to determine the look of an element. In particular, some properties can be overridden by table or element styles or classes.  Example: `background:lightyellow, background:lightblue` | rowStyles |
| Column styles |  | Enter a comma-separated list of styles to be applied to the columns in the specified sequence. Each style is made up of one or more CSS properties (semi-colon separated). If a column is skipped, supply a comma before adding the next columns style. A style can be reused for subsequent columns by referring to it using a 1-based numeric reference. A column number is indexed beginning at "1" and excludes any auto-numbered columns.  Column styles are applied to the table column and participate with other CSS properties to determine the look of an element. In particular, some properties may be overridden by table, row, or element styles or classes.  Example: `background:lightyellow, background:lightblue,1,2,1,2` | columnStyles |
| Column attributes |  | Enter a comma-separated list of values used to modify cell HTML attributes for all cells in a column. The position in the comma-separated list corresponds to the column that the values apply to. Each value is a double semi-colon list of *attributeNam*e=*value* pairs to be applied to the column cells. See [HTML attributes](https://www.w3schools.com/tags/ref_standardattributes.asp) for more information. | columnAttributes |
| Apply row style to individual cell | false | Enable this option to apply the styles mentioned in *Row styles* to each cell of the specified row(s). This option is used to override the default Confluence styles and make the user-defined styles persist for the specified table rows. Available since version 2.8. |  |
| Enable row highlighting on mouse over | true | Disable this option to stop row highlighting as the mouse moves over a table row. By default, the row is highlighted as the mouse moves. | enableHighlighting |
| Enable heading attributes | true | Disable this option to apply the column attributes only to data rows. By default, any column attributes provided are applied to the all column rows including heading rows. | enableHeadingAttributes |
| Auto number on each row | false | Enable this option to show an additional column that displays the row number for each row. By default, the table rows are not numbered. | autoNumber |
| Apply row style to individual cell | false | Enable this option to apply the styles mentioned in *Row styles* to each cell of the specified row(s). This option is used to override the default Confluence styles and make the user-defined styles persist for the specified table rows. Available since version 2.8. |  |
| Column styles |  | Enter a comma-separated list of styles to be applied to the columns in the specified sequence. Each style is made up of one or more CSS properties (semi-colon separated). If a column is skipped, supply a comma before adding the next columns style. A style can be reused for subsequent columns by referring to it using a 1-based numeric reference. A column number is indexed beginning at "1" and excludes any auto-numbered columns.  Column styles are applied to the table column and participate with other CSS properties to determine the look of an element. In particular, some properties may be overridden by table, row, or element styles or classes.  Example: `background:lightyellow, background:lightblue,1,2,1,2` | columnStyles |
| Apply Column styles to data column cells |  | Enable this option to apply the styles mentioned in *Row styles* to each cell of the specified row(s). This option is used to override the default Confluence styles and make the user-defined styles persist for the specified table rows. Available since version 2.8. |  |
| Highlight color | *lightgoldenrodyellow* | Enter a color to highlight when the mouse is over a row element. See [Web Colors](http://www.answers.com/topic/web-colors) for instructions on how to specify this. | highlightColor |
| Table id | Auto generated | Displays the table ID that can be referenced for use in other macros (like the *Chart* macro) or Javascript. | id |
| Table class | *@default* | Specify the table class (CSS) to apply to render tables.   - *@default* - Apply the default Confluence table class to rendered tables. - *@none* - Do not apply any style to rendered tables.   Currently, Confluence Cloud does not support the use of custom user-defined styles. | class |
| Table style |  | Specify style attributes for the table.  Example: `font-style:italic; background:lightblue;`. | style |
| Table width |  | Enter width for the table border in pixels or as a percentage (%). It is recommended to use *Table style* instead.  This parameter is not available for the *Attachment Table* macro. | width |
| Table border width |  | Enter width for the table border in pixels. Set *Table class* to blank if the width specified here is to be applied to the table. It is recommended to use *Table style* instead.  This parameter is not available for the *Attachment Table* macro. | border |

[Unmapped macro: refined-tab — no content to fall back on]

| **Macro Editor Label** | **Default** | **Description** | **Macro Parameter** |
| --- | --- | --- | --- |
| Allow download and export | false | Enable this option to allow download or export of the current table view as a CSV file. When enabled, download and export icons ( [Unmapped macro: inline-media-image — no content to fall back on] ) are displayed to the right of the table. File is downloaded to the user's local file system, or is exported as an attachment to the current page. Note that only those users that have the permission to add attachments to the page are allowed to export tables. | allowExport |
| Export file delimiter | *,* (Comma) | Enter a single character to be used as a delimiter for the table to be downloaded or exported. By default, a comma (,) is used as the delimiter. Valid only if *Allow download and export* is enabled. Available since 2.9.0.  - Any character can be used as a delimiter for the table contents. - If multiple characters are entered in the text box, an error is displayed. Specify a single character in the macro editor to be used as a delimiter to complete the export process. - After the export is complete, the file contains the table data interspersed with the specified delimiter. |  |

## Examples

## Other macros

Below is a list of all other macros available within this app:

- [CSV (Comma Separated Values) macro](/cms_trial/space/TBL/74812519/CSV+(Comma+Separated+Values)+macro+examples+-+Cloud/)
- [JSON Table macro](/cms_trial/space/TBL/74812316/JSON+Table+macro+-+Cloud/)
- [Attachment Table macro](/cms_trial/space/TBL/74812217/Attachment+Table+macro+-+Cloud/)