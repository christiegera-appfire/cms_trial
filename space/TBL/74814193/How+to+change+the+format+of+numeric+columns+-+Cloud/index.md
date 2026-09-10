# How to change the format of numeric columns - Cloud

## Overview

Numeric values within total rows (of numeric table columns) can be formatted to look like currency, percentages, times, or plain numbers with decimal places, thousands, and abbreviations. The app provides the ability to change the format of data using *FF* and *M* column types, without changing the actual data itself. This helps to keep the format consistent even if the format of the provided data is not. The [*Column types*](https://appfire.atlassian.net/wiki/x/EZN1B) parameter is used to specify what type of formatting is done.

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

## Screenshot

![Advanced Tables numeric column formatting settings](/cms_trial/assets/ed96a95b-0db9-46b9-af06-c63dc7c30092.jpg)

## Formatting options

### Acknowledgement

Advanced numeric formatting support is provided using Javascript with the help of the Numerals.js library (open source, MIT license). A summary of the relevant parts of the [Numerals.js documentation](http://numeraljs.com/) is repeated here.

## Numbers

| **Value (Original)** | **Format definition** | **Value (Formatted)** |
| --- | --- | --- |
| 10000 | '0,0.0000' | 10,000.0000 |
| 10000.23 | '0,0' | 10,000 |
| 10000.23 | '+0,0' | +10,000 |
| -10000 | '0,0.0' | -10,000.0 |
| 10000.1234 | '0.000' | 10000.123 |
| 10000.1234 | '0[.]00000' | 10000.12340 |
| -10000 | '(0,0.0000)' | (10,000.0000) |
| -0.23 | '.00' | -.23 |
| -0.23 | '(.00)' | (.23) |
| 0.23 | '0.00000' | 0.23000 |
| 0.23 | '0.0[0000]' | 0.23 |
| 1230974 | '0.0a' | 1.2m |
| 1460 | '0 a' | 1 k |
| -104000 | '0a' | -104k |
| 1 | '0o' | 1st |
| 52 | '0o' | 52nd |
| 23 | '0o' | 23rd |
| 100 | '0o' | 100th |

## Currency

| **Value (Original)** | **Format definition** | **Value (Formatted)** |
| --- | --- | --- |
| 1000.234 | '$0,0.00' | $1,000.23 |
| 1000.2 | '0,0[.]00 $' | 1,000.20 $ |
| 1001 | '$ 0,0[.]00' | $ 1,001 |
| -1000.234 | '($0,0)' | ($1,000) |
| -1000.234 | '$0.00' | -$1000.23 |
| 1230974 | '($ 0.00 a)' | $ 1.23 m |

## Bytes

| **Value (Original)** | **Format definition** | **Value (Formatted)** |
| --- | --- | --- |
| 100 | '0b' | 100B |
| 2048 | '0 b' | 2 KB |
| 7884486213 | '0.0b' | 7.3GB |
| 3467479682787 | '0.000 b' | 3.154 TB |

## Percentages

| **Value (Original)** | **Format definition** | **Value (Formatted)** |
| --- | --- | --- |
| 1 | '0%' | 100% |
| 0.974878234 | '0.000%' | 97.488% |
| -0.43 | '0 %' | -43 % |
| 0.43 | '(0.000 %)' | 43.000 % |

## Time

| **Value (Original)** | **Format definition** | **Value (Formatted)** |
| --- | --- | --- |
| 25 | '00:00:00' | 0:00:25 |
| 238 | '00:00:00' | 0:03:58 |
| 63846 | '00:00:00' | 17:44:06 |

## Examples

The following example shows how numeric values can be formatted in total rows:

- [Formatting the auto total row for numeric columns](https://appfire.atlassian.net/wiki/spaces/TBL/pages/74815084)

## Internationalization

The format can be automatically switch to support various international differences by adding a *language* parameter to the format.

A list of the languages available and their specification is available [here](https://github.com/adamwdraper/Numeral-js/tree/master/locales).

## Example

| **Column type** | **Value** | **Formatted value** |
| --- | --- | --- |
| FF"(de)0,0.00 $" | 1.234,5 | 1 234,50 € |
| FF"(fr)$0,0.00" | 1 234,5 | €1 234,50 |