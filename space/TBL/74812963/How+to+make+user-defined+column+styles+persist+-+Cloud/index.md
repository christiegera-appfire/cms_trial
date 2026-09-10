# How to make user-defined column styles persist - Cloud

This page provides an example to enforce user-defined styles in columns. For this example, let's consider the [Monthly Temperatures Table](https://appfire.atlassian.net/wiki/spaces/TBL/pages/74812593), for which you want to set background colors and borders of various columns and auto-number all the rows.

### Select this macro

|  |  |
| --- | --- |
| **Macro name** | *Table Plus* |
| **Macro syntax (Old editor)** | *{table-plus}* |
| **Macro syntax (New editor - case insensitive)** | */Table Plus* |

### Define these parameters/values

|  |  |
| --- | --- |
| ***Auto number on each row*** | On |
| ***Column styles***  (Comma separated styles) | *border:5px solid #c1c7d0;background:lightgrey;padding:15px, background:lightgreen;color:red;font-size: 160%, background:lightyellow;border: 3px dotted green, 2* |
| ***Apply Column styles to data column cells*** | On |

### Parameters set in the macro editor

![Advanced Tables Table Plus macro settings for column styles](/cms_trial/assets/0fe6e6f4-fabb-46aa-98ad-20b21fba61fb.png)![Specify the column Styles ](/cms_trial/assets/d3727d41-6bc2-4b9c-b940-99d9dfc7bb18.png)

### Example result

When the *Apply Column styles to data column cells* is disabled, certain styles like padding and text color are not applied due to the existing default Confluence styles as shown:

![Advanced Tables table before userdefined column styles](/cms_trial/assets/cb564c0b-c2e3-4a68-a852-7d5e635075b5.png)

When the *Apply Column styles to data column cells* is enabled, the table is displayed with all the specified styles after overriding the default Confluence styles as shown:

![Advanced Tables table after userdefined column styles persist](/cms_trial/assets/a71edcdd-102f-4444-a71f-bad628b6bd9c.png)