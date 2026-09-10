# Attachment Table macro - Cloud

## Overview

The *Attachment Table* macro produces a table of attachments based on various selection criteria, including space and page selection.

Further customization is possible by specifying filters to select attachments by name, comments, and labels. You can select and indicate the order of the columns in the table to be displayed based on column name or number. Refer to the [Columns available to display](/cms_trial/space/TBL/74812217/Attachment+Table+macro+-+Cloud/) section for details.

The resulting table can be customized and supports most [common table capabilities](https://appfire.atlassian.net/wiki/x/06B1B).

Depending on the selection criteria used and a number of attachments, pages, and spaces that need to be processed, this could be a long running process. Choose your selection criteria carefully and consider using the *Limit number of attachments to retrieve* parameter described below to limit processing.

## Basic use

This macro can be added to a page using any of the following methods:

|  |  |
| --- | --- |
| **Select from the macro browser (Insert elements)** | *Attachment Table* Insert Attachment Table macro using Insert elements |
| **Markup shortcut (New editor - case insensitive)** | */Attachment Table* Insert Attachment Table macro using macro shortcut |

### Screenshot

### See a live site creatively using the attachment-table macro

From [vxvista.org](http://vxvista.org): [Recorded Webinars](https://www.vxvista.org/display/vx4Learn/Recorded+Webinars)

![Advanced Tables Attachment Table macro showing attachment table output](/cms_trial/assets/dcac274d-f18f-4223-ade9-0db060bd44b9.png)

## Parameters

The macro parameters are categorized into various tabs, such as **Structure and Data**, **Sort** **and Filter**, **Style**, and **Export**.

![Attachment Table macro configuration.jpg](/cms_trial/assets/4043a0c5-763c-46fa-b1d2-2f71199c10ec.jpg)

Refer to [How to use regex expressions to select attachments](https://appfire.atlassian.net/wiki/x/6Ip1B) to learn how to form the regular expressions with the parameters.

## Macro specific parameters

| Tab | Macro Editor Label | Default | Description | Macro Parameter |
| --- | --- | --- | --- | --- |
| Structure and Data | Page to list attachments from | Most recent attachment uploaded to the current page | Enter the location where the attachments are available. The following locations are supported:   - *page* - Data is read from an attachment to the page specified here; provided that *page* is in the same space as the macro. - *space:page* - Data is read from an attachment to the specified *page* that is in the specified *space*. |  |
| Include personal spaces | false | Enable to control whether personal spaces matching *Space key or space name regex* are to be included or not, to process and render attachments from the specified spaces. | includePersonalSpaces |
| Retrieve attachments from child pages | false | Enable this option to list the child page attachments of the specified page in *Space* and *Page* parameters in the *Page filtering*tab. By default, only the attachments on the specified page are displayed.  This option works only if *Single page* is selected in ***Page filtering > Source***. | fromAllChildPages |
| Limit number of attachments to retrieve | *1000* | Enter the number of attachments that the macro must retrieve in total. Processing stops after the number of attachments found matching the selection criteria reaches the limit value. Space, page, and attachment processing is ordered by attachment name. | limit |
| Space key or space name regex |  | Enter a [regular expression (regex)](https://appfire.atlassian.net/wiki/spaces/info/pages/86082100) pattern to match with space keys or space names. Used in combination with the *Page name regex* parameter to select pages from which attachments are to be chosen. If left blank, the *Page to list attachments from* parameter is required.  The following options indicate:   - *@self* - current space or page - *@home* - home page of current space - *@parent* - parent page of current page or space   It is possible that in page preview, before publishing for the first time, the result for *@self* and *@parent* are not displayed as expected. Once you save the document, you can view the result as expected. | spaceRegex |
| Page name regex |  | Enter a [regular expression (regex)](https://appfire.atlassian.net/wiki/spaces/info/pages/86082100) pattern to match on page names (titles). Used in combination with the *Space key or space name regex* parameter to select pages from which attachments are to be chosen. | pageRegex |
| Page label regex |  | Enter a [regular expression (regex)](https://appfire.atlassian.net/wiki/spaces/info/pages/86082100) pattern to match on page labels. Used in combination with the *Page name regex* and *Space key or space name regex* parameters to select pages from which attachments are to be chosen. Pages must match with every selection criteria. | pageLabelRegex |
| Attachment name regex |  | Enter a [regular expression (regex)](https://appfire.atlassian.net/wiki/spaces/info/pages/86082100) pattern to match on attachment names. Used in combination with the *Attachment comment regex* and *Attachment label regex* parameters to select attachments. Attachment must match with every selection criteria. | attachmentRegex |
| Attachment comment regex |  | Enter a [regular expression (regex)](https://appfire.atlassian.net/wiki/spaces/info/pages/86082100) pattern to match on attachment comments. Used in combination with the *Attachment name regex* and *Attachment label regex* parameters to select attachments. Attachment must match with every selection criteria. | commentRegex |
| Attachment label regex |  | Enter a [regular expression (regex)](https://appfire.atlassian.net/wiki/spaces/info/pages/86082100) pattern to match on attachment labels. Used in combination with the *Attachment name regex* and *Attachment comment regex* parameters to select attachments. Attachment must match with every selection criteria. Matching technique is determined using the *Label match option* parameter. | labelRegex |
| Label match option | *single* | Specify the manner in which to apply the *Attachment label regex* parameter (for attachments) and the *Page label regex* parameter (for pages) when looking for matching labels. The options are:   - *single*: An attachment, that has at least one label that matches the *Page label regex* or *Attachment label regex* pattern, is considered as selected. - *all*: *Page label regex* and *Attachment label regex* are used to match a blank separated list of all labels. | labelMatchOption |
| Date format | Confluence default | Enter a date format to format the dates in the *created* and *modified* columns. Use a simple date format string. | dateFormat |
| Style | Text to display when no attachments match |  | Enter the text to be displayed when no attachments are found that match the given search criteria. If left blank, no text is displayed if no attachments are found. | textForNone |

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

## Columns available for display

The *Attachment Table* macro allows the user to select the columns to be displayed as well as the order in which the columns are to be displayed. A default set of columns is displayed unless an explicit list is provided. You can select and indicate the order in which columns are to be displayed based on their column name or number. Use the *columns* parameter to specify a comma separated list of column names or numbers.

The column names are case insensitive.

In most cases, the column heading can be used instead of the column name, but there are a few cases where that is ambiguous. In such a case, the first column matching the heading is used.

|  |  |
| --- | --- |
| Default columns for single page attachments | **file, size, creator, created, comment** |
| Default columns for multiple page attachments | **page, file, size, creator, created, comment** |

| Column Number | Column Name | Column Heading | Description |
| --- | --- | --- | --- |
| 1 | page | Page | Link to page the attachment is on |
| 2 | file | File | File link to download or view |
| 3 | size | Size | Size of attachment in bytes |
| 4 | creator | Creator | User link to who added the attachment |
| 5 | created | Created | When the attachment was added |
| 6 | comment | Comment | Descriptive comment about the attachment |
| 7 | labels | Labels | Attachment labels |
| 8 | version | Version | Version number |
| 9 | type | Type | Type of attachment - simple name |
| 10 | mimetype | Mime Type | Technical mime type name |
| 11 | size2 | Size | Size of attachment in KB or MB |
| 12 | modifier | Modifier | User link to who modified attachment properties |
| 13 | modified | Modified | When attachment properties were modified |
| 14 | id | Id | Confluence content id |
| 15 | space | Space | Key of the space containing the attachment |
| 16 | spacename | Space | Name of the space containing the attachment |
| 17 | pagetitle | Page | Title of the page containing the attachment |
| 18 | filename | File | File name of the attachment (not a link) |
| 19 | thumbnail | Thumbnail | Thumbnail image when the attachment is an image |
| 20 | image | Image | Image when the attachment is an image |
| 21 | location | Location | Link to the location on the page attachments list for the attachment |
| 22 | properties | Properties | Link to the attachment properties display for the attachment |

## Examples

## Other macros

Below is a list of all other macros available within this app:

- [Table Plus macro](https://appfire.atlassian.net/wiki/x/fox1B)
- [CSV (Comma Separated Values) macro](https://appfire.atlassian.net/wiki/x/4It1B)
- [JSON Table macro](https://appfire.atlassian.net/wiki/x/nIt1B)