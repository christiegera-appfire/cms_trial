# CSV (Comma Separated Values) macro - Cloud

Try our new Advanced Table Viewer macro for your CSV data. [Learn more](/cms_trial/space/TBL/2112356514/Advanced+Table+Viewer+for+your+CSV+data/).

## Overview

The *CSV (Comma Separated Values)* macro can import, format, and display comma-separated values (CSV) data from anywhere, by:

- Reading the CSV data from either of these sources:

  - Within your Confluence page
  - From a page attachment in the same or different space
- Allowing customizable delimiters, quote characters, and character encoding.
- Supporting inclusion of wiki markup macros within the CSV data.
- Leveraging the same table styling capabilities as the *Table Plus* macro.

CSV is not a formal standard, but the best reference is [The Comma Separated Value (CSV) File Format](http://www.creativyst.com/Doc/Articles/CSV/CSV01.htm). The support in this macro comes close to mirroring this pseudo-standard. This macro supports certain [common table capabilities](/cms_trial/space/TBL/74817747/Common+table+capabilities+-+Cloud/) with the other macros in this app and also other Bob Swift Atlassian apps.

By default, the CSV macro preserves extra spaces in CSV data between delimiters as valid column values.

## Basic use

This macro can be added to a page using any of the following methods:

|  |  |
| --- | --- |
| **Select from the macro browser (Insert elements)** | *CSV* click Insert elements and select CSV macro |
| **Markup shortcut (New editor - case insensitive)** | */CSV* Insert CSV macro using macro shortcut |

## Parameters

The macro parameters are categorized into various tabs, such as **Content**, **Source**, **Structure and Data**, **Sort** **and Filter**, **Style**, and **Export**.

![CSV macro configuration dialog](/cms_trial/assets/1946d1a5-613e-49a3-b879-ea543ed73e90.jpg)

**Parameters removed**

- The ***URL user*** and ***URL user password*** parameters have been removed from the ***CSV*** ***Table*** macro.
- Use a [*profile*](/cms_trial/space/TBL/74812041/Configuration+-+Cloud/) to access the data from a remote location.

## Macro specific parameters

| **Tab** | **Macro Editor Label** | **Default** | **Description** | **Macro Parameter** |
| --- | --- | --- | --- | --- |
| Content | Show wiki | false | Enable this option to show a non-formatted version of the wiki table following the formatted table. This is used to help resolve formatting issues. It can also be used to convert CSV to Confluence markup by cut and paste. | showWiki |
| Escape special characters in wiki markup | false | Enable this option to allow few special characters to be escaped so that the formatting is unaffected. When wiki output is requested (O*utput format* is set to *wiki*), some special characters (like '**|**', '**[**', '**]**', '**{**', '**}**') in data can cause undesirable formatting of the table. By default, data that has wiki markup is  rendered correctly. | escape |
| Render wiki markup macros in body | false | Enable this option to render wiki markup macros found in the body prior to processing as CSV. This is useful to run macros from apps such as *Scripting for Confluence*, *Run CLI Actions in Confluence*, *SQL for Confluence*, or similar, that can produce CSV output. | macros |
| Source | Location of CSV data | macro body | Specifies the list of options where CSV data is located. The included data follows the body data based on the location selected. The options are:   - *blank* - Data is read from the contents in the macro body. - *^attachment* - Data is read from an attachment that is available on the current page. - *page^attachment* - Data is read from an attachment available on the specified page in the current space. - *space:page^attachment* - Data is read from an attachment available on the specified page in a different space. | location |
| Profile |  | Enter the profile name from the list of pre-configured profiles. Contact your administrator to know about the profiles available for your use. Refer to the [Configuration documentation](/cms_trial/space/TBL/74812041/Configuration+-+Cloud/) to learn more about profile configuration. | profile |
| URL to CSV data |  | Enter the URL containing the required CSV files that are to be rendered. If specified, the included data follows the body and script data. | url |
| URL connection timeout (milliseconds) |  | Enter time in milliseconds such that URL connections do not timeout before getting data. Use this to increase time needed for slow connections. Note that if a zero is given the connection may wait infinitely. | timeout |
| Structure and Data | Output format | *html* | Specify how the output is formatted. The options are as follows:   - *html* - data is entered as standard HTML directly in the macro body. - *wiki* - data in the table rendered using the wiki renderer. | output |
| File encoding | System default | Specify the encoding for an external file, if different from the Confluence default (like Windows-1252, UTF-8, MacRoman). Refer to [this article](http://en.wikipedia.org/wiki/Character_encoding) for more information. Example: UTF-8. | encoding |
| Delimiter that separates columns | **,** (Comma) | Enter a delimiter to be used to separate column values when the table is downloaded or exported. The characters that can be used as delimiters are:   - *, or "," (comma)* - Default column separator. - *whitespace* - Blanks, tabs, and other white space are used to separate columns. - *tab* - A single tab character is used to separate columns. - *blanks* - Blank or blanks only. - *pipe* - A single pipe (**|**) character is used to separate columns. - *other single character delimiter* - can be within double quotes with some restrictions. Examples: "**;**", "**=**". | delimiter |
| Quote character | double | Specify the character used to represent quoted data. Quoted data may contain delimiters or new lines. Quote character data must be doubled inside a quoted string.   - double - Double quote character: **"** - single - Single quote character: **'** | quote |
| Ignore trailing blank rows | true | Disable this option to show blank rows. A row is considered blank if all the columns selected by the *Columns to show* parameter are blank. | ignoreTrailingBlankRows |
| Augments to data row values |  | Enter a comma separated list of augments to the data row values, one for each column. Specify double quotes for values with a comma. See [Augments](/cms_trial/space/TBL/74815166/Augments+-+Cloud/) for details. | augments |
| Augments to heading row values |  | Enter a comma separated list of augments to heading row values, one for each column. See [Augments](/cms_trial/space/TBL/74815166/Augments+-+Cloud/) for details. | headingAugments |
| Augments to footing row values |  | Enter a comma separated list of augments to footing row values, one for each column. See [Augments](/cms_trial/space/TBL/74815166/Augments+-+Cloud/) for details. | footingAugments |

### Common parameters

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

- [Format CSV data with CSV (Comma Separated Values) macro - Cloud](/cms_trial/space/TBL/74817820/How+to+format+CSV+data+with+CSV+(Comma+Separated+Values)+macro+-+Cloud/)

## Other macros

Below is a list of all other macros available within this app:

- [Table Plus macro](/cms_trial/space/TBL/74812542/Table+Plus+macro+-+Cloud/)
- [JSON Table macro](/cms_trial/space/TBL/74812316/JSON+Table+macro+-+Cloud/)
- [Attachment Table macro](/cms_trial/space/TBL/74812217/Attachment+Table+macro+-+Cloud/)

## Additional references

- [Augments](/cms_trial/space/TBL/74815166/Augments+-+Cloud/)
- [The Comma Separated Value (CSV) File Format](http://www.creativyst.com/Doc/Articles/CSV/CSV01.htm)
- [Scripting for Confluence](https://appfire.atlassian.net/wiki/spaces/SCRP)
- [Run CLI Actions in Confluence](https://appfire.atlassian.net/wiki/spaces/CCLI)