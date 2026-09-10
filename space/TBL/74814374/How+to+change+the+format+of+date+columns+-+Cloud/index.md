# How to change the format of date columns - Cloud

## Overview

This example explains how to format the display of date columns without changing the actual data. This helps to keep the format consistent even if the format of the provided data is not. To do this, configure the appropriate columns with the *M* column type in the [*Column types*](/cms_trial/space/TBL/74814225/Column+types+-+Cloud/) parameter. [Advanced date sorting](/cms_trial/space/TBL/74814618/How+to+perform+advanced+date+sorting+with+M+column+type-+Cloud/) specifies how to use the *M* column type to customize how the column data is interpreted as data.

In this page, two formats that support both interpreting the data and formatting the display (output) of the data are explained.

- Input format - This is the current format specified on the *M* column type; if nothing is specified, the default format is used. See [Advanced date sorting](/cms_trial/space/TBL/74814618/How+to+perform+advanced+date+sorting+with+M+column+type-+Cloud/) for more details.
- Display format - This is how you want the date to be displayed and sorted. If not specified, the column is displayed in the same format as the input format. The display format is similar but, necessarily, more complex than the input format. The **~** character is used to separate the input and display formats to avoid most conflicts with characters used in formats. This is summarized in the succeeding sections.

### Examples

| **Column type** | **Input format** | **Display format** |
| --- | --- | --- |
| M~YYYY.MM.DD | <default> | YYYY.MM.DD |
| MDDMMMYYYY~YYYY.MM.DD | DDMMMYYYY | YYYY.MM.DD |
| M(de)DDMMMYYYY~YYYY.MM.DD | (de)DDMMMYYYY | YYYY.MM.DD |
| MX~DD.MM.YY | Unix timestamp | DD.MM.YY |
| MDD MMM YYYY~YYYY.MM.DD | DD MMM YYYY  Default Confluence Date Picker (US) | YYYY.MM.DD |

## Usage

The formatting options listed on this page can be defined through the *Column types*parameter within the following macros:

- [Table Plus macro](/cms_trial/space/TBL/74812542/Table+Plus+macro+-+Cloud/)
- [CSV (Comma Separated Values) macro](/cms_trial/space/TBL/74812384/CSV+(Comma+Separated+Values)+macro+-+Cloud/)
- [JSON Table Macro](/cms_trial/space/TBL/74812316/JSON+Table+macro+-+Cloud/)
- [Attachment Table macro](/cms_trial/space/TBL/74812217/Attachment+Table+macro+-+Cloud/)
- [SQL macro](https://appfire.atlassian.net/wiki/spaces/SQL/pages/172458339)
- [SQL File macro](https://appfire.atlassian.net/wiki/spaces/SQL/pages/172458378)
- [SQL Query macro](https://appfire.atlassian.net/wiki/spaces/SQL/pages/172458423)
- [Excel macro](https://appfire.atlassian.net/wiki/spaces/XL/pages/76613631)

### Screenshot

![Advanced Tables date column type format settings](/cms_trial/assets/b51ccd24-712b-45f2-88b1-7db53592fbba.png)

## Formatting options

### Acknowledgement

Advanced date sorting support with the *M* column type is provided using Javascript with the help of the [Moment.js](http://momentjs.com/) library (open source, MIT license). A summary of the relevant parts of the [Moment.js documentation](http://momentjs.com/docs/#/displaying/format/) is repeated here.

|  | **Token** | **Output** |
| --- | --- | --- |
| **Month** | M | 1 2 ... 11 12 |
|  | Mo | 1st 2nd ... 11th 12th |
|  | MM | 01 02 ... 11 12 |
|  | MMM | Jan Feb ... Nov Dec |
|  | MMMM | January February ... November December |
| Quarter | Q | 1 2 3 4 |
| **Day of Month** | D | 1 2 ... 30 31 |
|  | Do | 1st 2nd ... 30th 31st |
|  | DD | 01 02 ... 30 31 |
| **Day of Year** | DDD | 1 2 ... 364 365 |
|  | DDDo | 1st 2nd ... 364th 365th |
|  | DDDD | 001 002 ... 364 365 |
| **Day of Week** | d | 0 1 ... 5 6 |
|  | do | 0th 1st ... 5th 6th |
|  | dd | Su Mo ... Fr Sa |
|  | ddd | Sun Mon ... Fri Sat |
|  | dddd | Sunday Monday ... Friday Saturday |
| **Day of Week (Locale)** | e | 0 1 ... 5 6 |
| **Day of Week (ISO)** | E | 1 2 ... 6 7 |
| **Week of Year** | w | 1 2 ... 52 53 |
|  | wo | 1st 2nd ... 52nd 53rd |
|  | ww | 01 02 ... 52 53 |
| **Week of Year (ISO)** | W | 1 2 ... 52 53 |
|  | Wo | 1st 2nd ... 52nd 53rd |
|  | WW | 01 02 ... 52 53 |
| **Year** | YY | 70 71 ... 29 30 |
|  | YYYY | 1970 1971 ... 2029 2030 |
| **Week Year** | gg | 70 71 ... 29 30 |
|  | gggg | 1970 1971 ... 2029 2030 |
| **Week Year (ISO)** | GG | 70 71 ... 29 30 |
|  | GGGG | 1970 1971 ... 2029 2030 |
| **AM/PM** | A | AM PM |
|  | a | am pm |
| **Hour** | H | 0 1 ... 22 23 |
|  | HH | 00 01 ... 22 23 |
|  | h | 1 2 ... 11 12 |
|  | hh | 01 02 ... 11 12 |
| **Minute** | m | 0 1 ... 58 59 |
|  | mm | 00 01 ... 58 59 |
| **Second** | s | 0 1 ... 58 59 |
|  | ss | 00 01 ... 58 59 |
| **Fractional Second** | S | 0 1 ... 8 9 |
|  | SS | 0 1 ... 98 99 |
|  | SSS | 0 1 ... 998 999 |
| **Timezone** | z or zz | EST CST ... MST PST  **Note:** as of **1.6.0**, the z/zz format tokens have been deprecated. [Read more about it here](https://github.com/moment/moment/issues/162). |
|  | Z | -07:00 -06:00 ... +06:00 +07:00 |
|  | ZZ | -0700 -0600 ... +0600 +0700 |
| **Unix Timestamp** | X | 1360013296 |

## Internationalization

See [language support (i18n)](https://appfire.atlassian.net/wiki/display/TBL/Advanced+Date+Sorting#AdvancedDateSorting-Languagesupport(i18n)).