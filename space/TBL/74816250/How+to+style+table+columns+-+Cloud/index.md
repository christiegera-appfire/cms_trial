# How to style table columns - Cloud

## Overview

This page outlines an example of how to style table columns using any of the [Advanced Tables for Confluence](https://appfire.atlassian.net/wiki/spaces/TBL) macros.

You can apply styles to columns with the *Column styles* parameter. It defines column level CSS at the HTML column level, where as the *Column attributes* parameter works at the element level and provides more than CSS styling capabilities. *Column styles* can be easier to use and is recommended for most use cases. However, it does not cover every use case that is available with the *Column attributes*parameter.

Look at the [Helpful resources](/cms_trial/space/TBL/74816250/How+to+style+table+columns+-+Cloud/) section for other styles related documentation.

**Watch this video to enhance your Confluence tables with custom row and column styles**.

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

- Due to the values set in the [*Column types*](/cms_trial/space/TBL/74814225/Column+types+-+Cloud/) parameter, the Auto Total row also follows the same column types.
- See [Formatting options for numeric rows](/cms_trial/space/TBL/74814193/How+to+change+the+format+of+numeric+columns+-+Cloud/) for a full list of available formatting options.

### Parameters set in the macro editor

![contentId-74816250](/cms_trial/assets/84a320f9-6e9f-446d-bf1d-755d0e1c618e.png)![contentId-74816250](/cms_trial/assets/151d6678-9b20-4537-9504-1939f942c543.png)

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

![contentId-74816250](/cms_trial/assets/9b7d5bbc-1d27-441e-a85d-4af733bf43f6.png)

## Helpful resources

- [Common table capabilities](/cms_trial/space/TBL/74817747/Common+table+capabilities+-+Cloud/)
- [How to make user defined column styes persist](/cms_trial/space/TBL/74812963/How+to+make+user-defined+column+styles+persist+-+Cloud/)
- [How to make user defined row styles persist](/cms_trial/space/TBL/74813085/How+to+make+user-defined+row+styles+persist+-+Cloud/)

## Other examples

Visit our [full list of product examples](/cms_trial/space/TBL/74814716/Use+cases+-+cloud/) for additional inspiration!