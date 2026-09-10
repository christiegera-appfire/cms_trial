# How to add links and images with augments - Cloud

## Overview

This example shows how to add wiki links and images to CSV data produced by other processes. This highlights the real advantages of augments especially for data produced by other processes. In this example, the data is produced using the [Confluence Command Line Interface (CLI)](https://appfire.atlassian.net/wiki/spaces/CSOAP) app's**getSpacePermissionList** action.

## Macro browser input

### Select this macro

|  |  |
| --- | --- |
| **Macro name** | *Advanced Tables - CSV Table* |
| **Macro syntax (Old editor)** | *{csv}* |
| **Macro syntax (New editor - case insensitive)** | */CSV (Comma Separated Values)* |

### Define these parameters/values

|  |  |
| --- | --- |
| ***Output format*** | *wiki* |
| ***Columns to display*** | *Space, Id Type, Id, Viewspace* |
| ***Augments to data row values*** | [%Space%:],,,!images^%viewspace%.png! |
| ***Augments to heading row values*** | *,,,View* |
| ***Column type*** | *S,S,S,E* |

### Screenshot

![Advanced Tables CSV data with links and image paths](/cms_trial/assets/789d7664-fd00-4b85-9f7e-785469d420e9.jpg)

## Wiki markup input (Old editor)

```plaintext
{csv:output=wiki
  |columns=Space, Id Type, Id, viewspace
  |augments=[%Space%:],,,!images^%viewspace%.png!
  |headingAugments=,,,View
  |columnTypes=S,S,S,E}
...
{csv}
```

## Example result

![Advanced Tables space permissions for links and images augments](/cms_trial/assets/86dbce11-b73b-4a43-89bc-dd9a7c98aa24.png)

## Other examples

Visit our [full list of product examples](/cms_trial/space/TBL/74814716/Use+cases+-+cloud/) for additional inspiration!