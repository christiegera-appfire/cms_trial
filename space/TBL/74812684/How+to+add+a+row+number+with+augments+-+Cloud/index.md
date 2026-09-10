# How to add a row number with augments - Cloud

## Overview

This page shows how you can use augments to add a column of row numbers in a CSV table, except for the header row.

## Macro browser input

### Select this macro

|  |  |
| --- | --- |
| **Macro name** | *Advanced Table - CSV Table* |
| **Macro syntax (Old editor)** | {csv} |
| **Macro syntax (New editor - case insensitive)** | */CSV (Comma Separated Values)* |

### Define these parameters/values

|  |  |
| --- | --- |
| ***Output format*** | *wiki* |
| ***Columns to display*** | *,Product,Sales* |
| ***Augments to data row values*** | *%#%* |

### Screenshot

![Advanced Tables CSV data used to add row numbers](/cms_trial/assets/9ca2374c-c8c3-4844-b13b-ca2499a40f88.jpg)

## Wiki markup input (Old editor)

```plaintext
{csv:columns=,Product, Sales|augments=%#%}
Product, Sales
ABC, 1000
XYZ, 2000
{csv}
```

## Example result

![Advanced Tables row number augment output in a table](/cms_trial/assets/9fc13172-a62d-4a8d-a524-f9e0b961162d.png)

### Persistent row number

This row number is added to the macro generated HTML table just as if it was in the original CSV data. This is different from the *Auto number each row* option in the macro editor for the table which is a browser display option only. If the augment is specified, the row numbers are also exported along with the table.

## Other examples

Visit our [full list of product examples](/cms_trial/space/TBL/74814716/Use+cases+-+cloud/) for additional inspiration!