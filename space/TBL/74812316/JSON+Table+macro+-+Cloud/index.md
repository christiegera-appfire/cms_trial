# JSON Table macro - Cloud

## Overview

JSON (JavaScript Object Notation) has become a highly used interchange format because it is lightweight, simple, and easy to read and write. Many REST APIs, including Atlassian REST APIs, return JSON format which makes it ideal for scripting output.

The *JSON Table* macro can import, format, and display JSON data from anywhere, by:

- Reading the JSON data from either of these sources:

  - Within your Confluence page.
  - From a page attachment in the same or different space.
- Allowing customizable access to fields.
- Supporting inclusion of wiki markup macros within the JSON data.
- Leveraging the same table styling capabilities as the *Table Plus* macro.

This macro supports certain [common table capabilities](https://appfire.atlassian.net/wiki/x/06B1B) with the other macros in this app and also other Bob Swift Atlassian apps.

Watch this video to see how the JSON Table macro imports and displays JSON data from a page attachment — with sorting and data filter enabled.

## Basic use

This macro can be added to a page using any of the following methods:

|  |  |
| --- | --- |
| **Select from the macro browser** **(Insert elements)** | *JSON Table* Insert JSON macro using Insert elements |
| **Markup shortcut (New editor - case insensitive)** | */JSON Table* Insert JSON macro using macro shortcut |

## Parameters

The macro parameters are categorized into various tabs, such as **Content**, **Source**, **Structure and Data**, **Sort** **and Filter**, **Style**, and **Export**.

![JSON macro configuration dialog.jpg](/cms_trial/assets/2461c223-c92c-4314-b541-396f4f986cdf.jpg)

**Parameters removed**

- The ***URL user*** and ***URL user password*** parameters have been removed from the ***JSON*** ***Table*** macro.
- Use a [*profile*](https://appfire.atlassian.net/wiki/x/iYp1B#profiles) to access the data from a remote location.

## Macro specific parameters

| **Tab** | **Macro Editor Label** | **Default** | **Description** | **Macro Parameter** |
| --- | --- | --- | --- | --- |
| Content | Location of JSON data | macro body | Specifies the list of options where JSON data is located. The included data follows the body data based on the location selected. The possible options are:   - *blank* - Data is read from the contents in the macro body. - *^attachment* - Data is read from an attachment that is available on the current page. - *page^attachment* - Data is read from an attachment available on the specified page in the current space. - *space:page^attachment* - Data is read from an attachment available on the specified page in a different space. | location |
| URL to JSON data |  | Enter the URL containing the required JSON that are to be processed and rendered. If specified, the included data follows the body and script data. | url |
| Profile |  | Enter the profile name from the list of pre-configured profiles. Contact your administrator to know about the profiles available for your use. Refer to the [Configuration documentation](https://appfire.atlassian.net/wiki/x/iYp1B#profiles) to learn more about profile configuration. | profile |
| URL connection timeout (milliseconds) |  | Enter time in milliseconds such that URL connections do not timeout before getting data. Use this to increase time needed for slow connections. Note that if a zero is given the connection may wait infinitely. | timeout |
| Structure and Data | Output format | *html* | Specify how the output is formatted. The options are as follows:   - *html* - data is entered as standard HTML directly in the macro body. - *wiki* - data in the table rendered using the wiki renderer. | output |
| File encoding | System default | Specify the encoding for an external file, if different from the Confluence default (like Windows-1252, UTF-8, MacRoman). Refer to [this article](http://en.wikipedia.org/wiki/Character_encoding) for more information. Example: UTF-8. | encoding |
| Paths to fields |  | Specify a single path to generate a single table. Simple form is a dot separated list of field names to reach the specific field within the JSON string. Example: *total.monthlies*.  When a comma separated list of paths to fields is provided, a table is produced for each valid field identified in the path. No table is produced for references to fields that cannot be found, are empty arrays, or similar.  Paths are expressed in [JSONPath](http://goessner.net/articles/JsonPath/) syntax. | paths |
| Paths to fields to be included | all fields | Enter a comma separated list of paths to fields to be included in the output. Paths are relative to the JSON field specified in the paths parameter. If not specified, all fields found are included.  Example for the *issues* field from the [Jira search REST API](https://docs.atlassian.com/jira/REST/latest/#d2e417):  *key, fields.summary,* *fields.issuetype.name*, *fields.issuetype.id*, *fields.fixVersions[\*].name* | fieldPaths |
| Regex patterns for ordering fields |  | Enter a comma separated list of [regular expression (regex)](https://appfire.atlassian.net/wiki/display/info/How+to+use+regular+expressions) patterns.  This parameter is used only when the *Paths to fields to be included* field defaults to all fields; otherwise, the order specified in *Paths to fields to be included* is used.  Useful when multiple tables are generated and column ordering is not ideal. Field order is not specific in JSON strings so when field order is important, these regex patterns can be used to control the order.  A field found by an earlier pattern is processed before fields not found or fields found by a later pattern. | fieldOrderRegexPatterns |
| Paths to be used to determine sort order |  | Enter a comma separated list of path references to fields (simple only) to be used to determine how rows are initially sorted.  Paths are relative to the JSON field specified in the *Paths to fields* parameter. If specified, JSON array elements are sorted based on the comparison of field values represented by the paths. The first path is the primary sort value. Subsequent paths are used only if the first comparison is equal. The sort direction is ascending unless *Sort descending* is selected. This sorting is done before the HTML is generated for display. | sortPaths |
| Strip leading qualifiers from generated headings | false | Enable to make table heading columns look better by stripping leading qualifiers (using a dot separator (.)) for names generated as a result of *Paths to fields to be included*. For example, *field.type* would be converted to *type*. | stripQualifiers |
| Capitalize first character of generated headings | true | Enable to make table heading columns look better by capitalizing leading character of names generated as a result of *Paths to fields to be included*. | capitalize |
| Augments to data row values |  | Enter a comma separated list of augments to the data row values, one for each column. Specify double quotes for values with a comma. See [Augments](https://appfire.atlassian.net/wiki/x/vpZ1B) for details. | augments |
| Augments to heading row values |  | Enter a comma separated list of augments to heading row values, one for each column. See [Augments](https://appfire.atlassian.net/wiki/x/vpZ1B) for details. | headingAugments |
| Augments to footing row values |  | Enter a comma separated list of augments to footing row values, one for each column. See [Augments](https://appfire.atlassian.net/wiki/x/vpZ1B) for details. | footingAugments |
| Show wiki | false | Enable this option to show a non-formatted version of the wiki table following the formatted table. This is used to help resolve formatting issues. It can also be used to convert CSV to Confluence markup by cut and paste. | showWiki |
| Escape special characters in wiki markup | false | Enable this option to allow few special characters to be escaped so that the formatting is unaffected. When wiki output is requested (O*utput format* is set to *wiki*), some special characters (like '**|**', '**[**', '**]**', '**{**', '**}**') in data can cause undesirable formatting of the table. By default, data that has wiki markup is  rendered correctly. | escape |
| Render wiki markup macros in body | false | Enable this option to render wiki markup macros found in the body prior to processing as CSV. This is useful to run macros from apps such as *Scripting for Confluence*, *Run CLI Actions in Confluence*, *SQL for Confluence*, or similar, that can produce CSV output. | macros |

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

- [Table Plus macro](https://appfire.atlassian.net/wiki/x/fox1B)
- [CSV (Comma Separated Values) macro](https://appfire.atlassian.net/wiki/x/4It1B)
- [Attachment Table macro](https://appfire.atlassian.net/wiki/x/OYt1B)

## Additional references

- [JSON.org home](http://www.json.org/)
- [JSONPath](http://goessner.net/articles/JsonPath/)
- [Jira REST API Example - Query issues](https://developer.atlassian.com/display/JIRADEV/JIRA+REST+API+Example+-+Query+issues)
- [Confluence Remote API Content examples](https://developer.atlassian.com/display/CONFDEV/Remote+API+Content+Examples)
- [Scripting for Confluence](https://appfire.atlassian.net/wiki/spaces/SCRP)
- [Run CLI Actions in Confluence](https://appfire.atlassian.net/wiki/spaces/CCLI)
- [How to deal with templates on Confluence 4.3 and later](https://appfire.atlassian.net/wiki/spaces/info/pages/86120194)