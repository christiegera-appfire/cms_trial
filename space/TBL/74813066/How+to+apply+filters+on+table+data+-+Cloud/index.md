# How to apply filters on table data - Cloud

Users can now search for some specific data with regular expressions in the tables generated with the *Advanced Tables for Confluence Cloud* macros. If the *Display data filter* option is toggled on in the macro's settings, a filter panel appears on the top of every table inside this macro. This panel contains a text box to enter the required search criteria and buttons: *Filter* to apply the search against the data rows, and, *Clear* to clear the box to start a new search. Refer to [this article](/cms_trial/space/TBL/74814629/How+to+use+regular+expressions+-+Cloud/) to know more about regular expressions.

This page provides an example of how to use filters. Though you can use this feature with any of the macros, for this example, let's work with a *CSV* macro.

To use this feature, users must enable the *Display data filter* option from the macro editor.

### Select this macro

|  |  |
| --- | --- |
| **Macro name** | *CSV* |
| **Macro syntax (Old editor)** | *{csv}* |
| **Macro syntax (New editor - case insensitive)** | */CSV (Comma Separated Values)* |

### Define these parameters/value

|  |  |
| --- | --- |
| ***Display data filter*** | On |

### Parameters set in the macro editor

For this example, the data from the [Monthly temperatures](https://appfire.atlassian.net/wiki/spaces/TBL/pages/74812593) page was entered as a comma separated value list in the macro body itself.

Image — asset pipeline pending  
Advanced Tables Table Plus macro filter parameter settings

### Example result

Image — asset pipeline pending  
Advanced Tables filter panel displayed beside table data

### Sample filters applied to the table

The following table lists certain sample requirements, filters applied, and the resultant data:

| **Requirement** | **Filter applied** | **Result** |
| --- | --- | --- |
| Display temperatures for the months of January, March, and May | **ja|ma** | Image — asset pipeline pending Advanced Tables table filter example with filtered results |
| Display data with temperatures in the 60s | **60** | Image — asset pipeline pending Advanced Tables table filter example with another filter selection |
| Display data with temperatures in the range of 40 to 45 degrees | **4[0-5]** | Image — asset pipeline pending Advanced Tables table filter example with multiple matching rows |
| Display the temperatures for the last quarter of the year | **ber** | Image — asset pipeline pending Advanced Tables table filter example with filtered table output |