# How to make user-defined row styles persist - Cloud

This page provides an example to enforce user-defined styles for rows. For this example, let's consider [Monthly Temperatures table](https://appfire.atlassian.net/wiki/spaces/TBL/pages/74812593) for which you want to set styles of various rows, including the header row.

### Select this macro

|  |  |
| --- | --- |
| **Macro name** | *Table Plus* |
| **Macro syntax (Old editor)** | *{table-plus}* |
| **Macro syntax (New editor - case insensitive)** | */Table Plus* |

### Define these parameters/values

|  |  |
| --- | --- |
| ***Row styles***  (Comma separated styles) | *font-size:160%;padding:20px;border: 5px solid #c1c7d0, color:green;font-size:125%;padding-top:25px, background:lightblue;color:red;border: 2.5px dotted black, font-style:italic;font-size:175%;padding-left:35px* |
| ***Apply row style to individual cell*** | On |

### Parameters set in the macro editor

![Advanced Tables Table Plus macro settings for row styles](/cms_trial/assets/8c85b1d9-7378-4edf-9584-f65ce079170c.png)

### Example result

When the *Apply row style to individual cell* is off, certain styles for cell padding or borders are not applied due to the existing default Confluence styles as shown:

![Advanced Tables table before userdefined row styles](/cms_trial/assets/802e2594-e6b1-48d0-a373-13a665e8ae66.png)

When the *Apply row style to individual cell* is toggled on, the table is displayed with all the specified styles are applied after overriding the default Confluence styles as shown:

![Advanced Tables table after userdefined row styles persist](/cms_trial/assets/4c439335-fe0e-469b-9475-b5b8cb690fcd.png)