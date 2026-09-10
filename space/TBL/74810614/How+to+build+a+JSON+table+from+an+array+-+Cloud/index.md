# How to build a JSON table from an array - Cloud

## Overview

This page shows how you produce a simple table from JSON data using the [JSON Table macro](/cms_trial/space/TBL/74812316/JSON+Table+macro+-+Cloud/), which is part of the [Advanced Tables for Confluence](https://appfire.atlassian.net/wiki/spaces/TBL) app.

## Macro browser input

## Select this macro

|  |  |
| --- | --- |
| **Macro name** | *Advanced Tables - JSON Table* |
| **Macro syntax (Old editor)** | *{json-table}* |
| **Macro syntax (New editor - case insensitive)** | */JSON Table* |

## Define these parameters/values

|  |  |
| --- | --- |
| ***Paths to fields*** | *$* |
| ***Paths to fields to be included*** | *a,b,c* |
| ***Auto number on each row*** | On |
| ***Auto total row*** | On |
| Macro body  Old editor:  New editor: | [{a:10,b:20,c:30,d:40},{a:15,b:6}]  [{"a":10,"b":20,"c":30,"d":40},{"a":15,"b":6}] |

## Parameters set in the macro editor

![Advanced Tables JSON Table macro settings for array data](/cms_trial/assets/548f130a-dd93-4edb-ac25-2e8a0c808472.png)![Advanced Tables JSON Table macro with selected columns from array data](/cms_trial/assets/78165314-9c44-4524-a6c4-2ee9b62a4c49.png)

The macro looks as follows before the page is published:

![Advanced Tables simple JSON table shown in edit mode](/cms_trial/assets/2bd355ad-6984-4149-8886-57e849c8cc53.png)

## Wiki markup input (Old editor)

```plaintext
{json-table:
paths=$|
fieldPaths=a,b,c|
autoNumber=true|
autoTotal=true}
[{a:10,b:20,c:30,d:40},{a:15,b:6}]
{json-table}
```

## Example result

![Advanced Tables simple JSON table output in page view](/cms_trial/assets/692e1559-3432-4a37-ae11-16a16d1040b6.png)

## Other examples

Visit our [full list of product examples](/cms_trial/space/TBL/74814716/Use+cases+-+cloud/) for additional inspiration!