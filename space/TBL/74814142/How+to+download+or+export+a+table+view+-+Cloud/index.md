# How to download or export a table view - Cloud

## Overview

This page demonstrates how to use the [Table Plus macro](/cms_trial/space/TBL/74812542/Table+Plus+macro+-+Cloud/), which is part of the [Advanced Tables for Confluence](https://appfire.atlassian.net/wiki/spaces/TBL) app, to download or export (as an attachment) a CSV representation of the table view. By specifying the *Allow download and export*parameter on the macro, users are given two icons (

[Unmapped macro: inline-media-image — no content to fall back on]

) that can be clicked to download or export the current table view to a CSV file. Download places the file on the users local system, and export creates an attachment.

Though a comma (,) is used as a delimiter for the table contents by default, you can specify a different character in the *Export file delimiter*. Enter any single character to act as a delimiter in the text box. For this example, let's use the default delimiter to download the current table view.

![Advanced Tables Table Plus macro Allow export setting](/cms_trial/assets/3a851881-587a-4cd6-a221-811c5d7f0e44.png)

### Message

![Advanced Tables table export confirmation message](/cms_trial/assets/1f16f490-f94c-4462-b125-c29ebfc17dbf.png)

## Macro browser input

## Select this macro

|  |  |
| --- | --- |
| **Macro name** | *Advanced Tables - Table Plus* |
| **Macro syntax (Old editor)** | *{table-plus}* |
| **Macro syntax (New editor - case insensitive)** | */Table Plus* |

## Define these parameters/values

|  |  |
| --- | --- |
| ***Auto number on each row*** | On |
| ***Auto total row*** | On |
| ***Allow download and export*** | On |
| **Export file delimiter** | *,* |
| ***Sort descending*** | On |
| ***Auto sort this column*** | 3 |
| ***Column types*** | *S,E,I* |
| ***Table id*** | *Product Revenue* |

## Parameters set in the macro editor

![Advanced Tables Table Plus macro export settings](/cms_trial/assets/90adcb38-7d4a-4b66-92ad-a5e6431b82c9.png)![Advanced Tables Table Plus macro export output settings](/cms_trial/assets/fed8b6b1-5574-476b-aa0b-0cb9bd8fbeaf.png)

## Wiki markup input (Old editor)

```plaintext
{table-plus:allowExport=true|id=Product Revenue|autoNumber=true|autoTotal=true|sortDescending=true|sortColumn=3|columnTypes=S,E,FF"$0,0"}
|| Product || On Plan || Revenue ||
| A | (/) | 325100 |
| D | (/) | 315850 |
| C | (x) | 250420 |
| B | (/) | 98650  |
| E | (x) | 79010  |
{table-plus}
```

## Exported CSV file

The exported attachment, *Product Revenue.csv*, can be imported back to a Confluence page using the [CSV (Comma Separated Values) macro](/cms_trial/space/TBL/74812384/CSV+(Comma+Separated+Values)+macro+-+Cloud/). This could be used for showing snapshots of tables that have been archived for a historical view. The exported CSV file is added to a *CSV (Comma Separated Values)* macro as an attachment on this page:

### As text

#### **Product Revenue.csv**

```text
"","Product","On Plan","Revenue"
"1","A","https://examplegear.com/s/en_GB/6214/6860359b26f1e8cc7164bebdad0e2f04c128c291.1/_/images/icons/emoticons/check.png","$325,100"
"2","D","https://examplegear.com/s/en_GB/6214/6860359b26f1e8cc7164bebdad0e2f04c128c291.1/_/images/icons/emoticons/check.png","$315,850"
"3","C","https://examplegear.com/s/en_GB/6214/6860359b26f1e8cc7164bebdad0e2f04c128c291.1/_/images/icons/emoticons/error.png","$250,420"
"4","B","https://examplegear.com/s/en_GB/6214/6860359b26f1e8cc7164bebdad0e2f04c128c291.1/_/images/icons/emoticons/check.png","$98,650"
"5","E","https://examplegear.com/s/en_GB/6214/6860359b26f1e8cc7164bebdad0e2f04c128c291.1/_/images/icons/emoticons/error.png","$79,010"
"","","","$1,069,030"
```

### As-is

![Advanced Tables CSV table macro output before export](/cms_trial/assets/61739598-564a-4955-9c66-2603d1f2e2b9.jpg)

### With a few parameters to make it look more like the original

![Advanced Tables product revenue CSV sample table](/cms_trial/assets/ed4a4e54-9caf-4172-86aa-5063414253a3.jpg)

The following parameters were used in the *CSV (Comma Separated Values)* macro:

## Select this macro

|  |  |
| --- | --- |
| **Macro name** | *Advanced Tables - CSV Table* |
| **Macro syntax (Old editor)** | *{csv}* |
| **Macro syntax (New editor - case insensitive)** | */CSV (Comma Separated Values)* |

## Define these parameters/values

|  |  |
| --- | --- |
| ***Output format*** | *wiki* |
| ***Header rows*** | 1 |
| ***Augments to data row values*** | , , !%3%! |
| ***Augments to footing row values*** | *, , Total* |
| ***Location of CSV data*** | *^Product Revenue.csv* |
| ***Column types*** | *I,S,E,C* |

## Other examples

Visit our [full list of product examples](/cms_trial/space/TBL/74814716/Use+cases+-+cloud/) for additional inspiration!