# How to format the Auto Total row for numeric columns - Cloud

## Overview

This page outlines an example of how to style the row with totals of numeric columns using the [Table Plus macro](/cms_trial/space/TBL/74812542/Table+Plus+macro+-+Cloud/), [CSV (Comma Separated Values) macro](/cms_trial/space/TBL/74812384/CSV+(Comma+Separated+Values)+macro+-+Cloud/), or [Attachment Table macro](/cms_trial/space/TBL/74812217/Attachment+Table+macro+-+Cloud/), which are part of the [Advanced Tables for Confluence](https://appfire.atlassian.net/wiki/spaces/TBL) app. This example assumes your data itself contains the formatting you want, such as comma separators and dollar signs. The instructions given on this page ensure that when you choose to have a row with totals of numeric columns, it too is similarly styled.

Watch this video for details on configuring the Table Plus to perform the most common functions, including adding up columns and filtering.

## Macro browser input

### Select any of the macros

|  |  |
| --- | --- |
| **Macro name** | - *Advanced Tables - CSV Table* - *Advanced Tables - Table Plus* - *Advanced Tables - Attachment Table* |
| **Macro syntax (Old editor)** | - *{csv}* - *{table-plus}* - {attachment-table} |
| **Macro syntax (New editor - case insensitive)** | - */Table Plus* - */CSV (Comma Separated Values)* - */Attachment Table* |

### Define these parameters/values

|  |  |
| --- | --- |
| ***Auto total numeric columns*** | On |
| ***Column types*** | *s,f"0,0",f"$0,0.00"* |

- Due to the values set in the [Column types](/cms_trial/space/TBL/74814225/Column+types+-+Cloud/) parameter, the Auto Total row also follows the same column types.
- See [Formatting options for numeric rows](/cms_trial/space/TBL/74814193/How+to+change+the+format+of+numeric+columns+-+Cloud/) for a full list of available formatting options.

### Parameters set in the macro editor

![Advanced Tables Table Plus macro auto total row settings](/cms_trial/assets/b1999305-75c0-404a-853b-787e9a4f3cf5.png)![Advanced Tables Table Plus macro numeric column settings for auto total row](/cms_trial/assets/3f778d7d-7a3b-46c3-95f7-835e96145887.png)

## Wiki markup input (Old editor)

For a table built using the [CSV (Comma Separated Values) macro](/cms_trial/space/TBL/74812384/CSV+(Comma+Separated+Values)+macro+-+Cloud/):

```plaintext
{csv:output=wiki|autoTotal=true|columnTypes=s,f"0,0",f"$0,0.00"}
"Item","Units","Revenue"
"Kazoos","1,368","$4,074.25"
"Accordions","445","$222,500.63"
"Mandolins","2,296","$1,033,200.00"
{csv}
```

## Example result

![Advanced Tables auto total row example result](/cms_trial/assets/9a674188-58fa-4a93-80bc-605b8ceaddec.png)

## Other examples

Visit our [full list of product examples](/cms_trial/space/TBL/74814716/Use+cases+-+cloud/) for additional inspiration!