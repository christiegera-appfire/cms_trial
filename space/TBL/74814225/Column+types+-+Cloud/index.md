# Column types - Cloud

## Overview

The macros within the [Advanced Tables for Confluence](https://appfire.atlassian.net/wiki/spaces/TBL) app support a C*olumn types* parameter that allows you to control how the data in a given column is treated and formatted.

Column types determine how column data can be sorted and displayed. By default, column data is treated as a text string, and thus, can be sorted automatically when a column heading is clicked. *CSV* macros may automatically generate more precise column types. When the default behavior is less than optimal for your situation, the *Column types* parameter can be set specifically.

Numeric types are right-aligned, by default. To display the totals of any numeric column(s), you must specify the relevant numeric type for the required columns in *Column types*, and enable the *Auto total row* option.

This table describes the behavior of the various types.

| **Type** | **Description** | **Sorting** | **Total Formatting** | **Data Formatting** |
| --- | --- | --- | --- | --- |
| **String (*****S*****)** | Text string. This is a series of one or more alphanumeric characters, possibly including a letter, number, space, punctuation mark or other special characters. | Alphabetic |  |  |
| **Integer (*****I*****)** | Integer. This is a numeric field without a fractional component. | Numeric | ✅ |  |
| **Numeric or float values (*****F*****)** | Numeric or float value and may contain numeric separators including a decimal point and a comma for thousands separator. | Numeric | ✅ |  |
| **Numeric with data formatting (*****FF*****)** | Numeric or float value and may contain numeric separators including a decimal point and a comma for thousands separator. Forced formatting of data columns. | Numeric | ✅ | ✅ |
| **Float with comma as decimal point (*****FC*****)** | Numeric or float value and may contain numeric separators including a comma for decimal separator and a period for thousands separator. | Numeric | ✅ |  |
| **Currency (*****C*****)** | Similar to *F* with more leniency on leading and trailing characters to allow currency and similar symbols to be present and ignored. | Numeric | ✅ |  |
| **Currency with comma as decimal points (*****CC*****)** | Similar to *FC* with more leniency on leading and trailing characters to allow currency and similar symbols to be present and ignored. | Numeric | ✅ |  |
| **Date (*****M*****)** | Date format in many popular formats. See [Advanced date sorting](/cms_trial/space/TBL/74814618/How+to+perform+advanced+date+sorting+with+M+column+type-+Cloud/) for more information. This is the preferred date sorting type. | Date |  | ✅ |
| **Date in the browser date format (*****D*****)** | Date in the browser date format. See [Advanced date sorting](/cms_trial/space/TBL/74814340/How+to+perform+advanced+date+sorting+with+the+D+column+type+-+Cloud/) for more information. The *D* type is available for compatibility with older releases - the *M* type is recommended. | Date |  |  |
| **Complex HTML elements like emotions or similar (*****E*****)** | Emoticons or other HTML elements. | Alphabetic on the inner HTML value |  |  |
| **Exclude this column from user selectable sorting (*****X*****)** | Indicates to exclude this column from user selectable sorting. | Disabled |  |  |
| ***.*** | Separated numbers, like phone numbers or TCP addresses. Valid values are multiple integer numbers separated by '**.**'. | Numeric on each separated value |  |  |
| ***:*** | Separated numbers, like phone numbers or TCP addresses. Valid values are multiple integer numbers separated by '**:**'. | Numeric on each separated value |  |  |
| ***-*** | Separated numbers, like phone numbers or TCP addresses. Valid values are multiple integer numbers separated by '**-**'. | Numeric on each separated value |  |  |
| ***/*** | Separated numbers, like phone numbers or TCP addresses. Valid values are multiple integer numbers separated by '**/**'. | Numeric on each separated value |  |  |
| **Hide the column (H)** | Indicates to hide the column. |  |  |  |

- **Total formatting** - option to format the total row in a user defined way. See [Format the Auto Total row for numeric columns](/cms_trial/space/TBL/74813253/How+to+format+the+Auto+Total+row+for+numeric+columns+-+Cloud/).
- **Numeric data formatting** - option to format the data rows in a user defined way for numeric columns. See [Formatting options for numeric columns](/cms_trial/space/TBL/74814193/How+to+change+the+format+of+numeric+columns+-+Cloud/).
- **Date data formatting** - option to format the data rows in a user defined way for date columns. See [Formatting options for date columns](/cms_trial/space/TBL/74814374/How+to+change+the+format+of+date+columns+-+Cloud/).

## Helpful resources

[Use cases](/cms_trial/space/TBL/74814716/Use+cases+-+cloud/)