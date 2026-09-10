# How to improve the Jira Issues macro with the Table Plus macro - Cloud

## Overview

This page demonstrates how to use the [Table Plus macro](/cms_trial/space/TBL/74812542/Table+Plus+macro+-+Cloud/), which is part of the [Advanced Tables for Confluence](https://appfire.atlassian.net/wiki/spaces/TBL) app, to enhance the *Jira Issues* macro. Simply insert a *Table Plus* macro onto your page, configure its parameters, and then insert a *Jira Issues* macro inside of the *Table Plus* macro.

Though nested macros are generally not supported in Confluence Cloud, some macros like the *Jira Issues* macro can be inserted into the *Table Plus* macro.

The *Table Plus* macro can add sorting and other features to the [Jira Issues macro](https://confluence.atlassian.com/display/DOC/JIRA+Issues+Macro) including styling the table differently. The key to doing this successfully can sometimes be dependent on the Confluence release (or more specifically, the release of the plugin containing *Jira Issues* macro).

### Limitations

Sorting is only done on the visible issues.

## Macro browser input

## Select this macro

|  |  |
| --- | --- |
| **Macro name** | *Advanced Tables - Table Plus* |
| **Macro syntax (Old editor)** | *{table-plus}* |
| **Macro syntax (New editor - case insensitive)** | */Table Plus* |

## Define these parameters/values

|  |  |
| --- | --- |
| ***Heading rows*** | *2* |
| ***Column types*** | *S,S,X,M,M,S,S,S,F,F,S* |

- The *Column types* parameter is required for sorting. It should contain a comma separated list of values for handling each column.
- Click *Display Options* from within the [Jira Issues macro](https://confluence.atlassian.com/display/DOC/JIRA+Issues+Macro) to review and optionally, customize the columns to display, and thus, determine how to set the *Table Plus* macro's *Column types* parameter.

### Column types parameter values

| Use | For |
| --- | --- |
| **String (*****S*****)** | Columns with string values. |
| **Exclude this column from user selectable sorting (*****X*****)** | Exclude column from sorting. For example, using *Type* column as that sorts by key, which is confusing. |
| **Date (*****M*****)** | Columns with date values. |
| **Complex HTML elements (*****E*****)** | Columns with images or emoticons. |
| **Numeric and float values** ***(F)*** | Columns with numeric or float values. |

### Parameters set in the macro editor

![Advanced Tables Table Plus macro settings for Jira Issues macro data](/cms_trial/assets/c6f86e73-275b-43f5-977d-b285d77fb692.png)![Advanced Tables Jira Issues macro column type settings](/cms_trial/assets/4531a7bc-493e-4add-b698-44736b01bc0a.jpg)

After the relevant parameters are set in the *Table Plus* and *Jira Issues* macros, the macros are shown on the page (before it is published) as:

![Advanced Tables Jira Issues macro input table example](/cms_trial/assets/37271841-a955-4da8-9614-e5d334b3cddd.jpg)

## Wiki markup input (Old editor)

```plaintext
{table-plus:heading=2|autoTotal=true|columnTypes=S,S,X,M,M,S,S,S,F,F,S}
{jiraissues:url=[https://xxxxxxxx.atlassian.net/sr/jira.issueviews:searchrequest-rss/temp/SearchRequest.xml?jqlQuery=project+%3D+TBL+AND+fixVersion+%3D+%226.1.0%22+ORDER+BY+priority+DESC}
{table-plus}
```

## Example result

[Unmapped block: blockCard]

## Other examples

Visit our [full list of product examples](/cms_trial/space/TBL/74814716/Use+cases+-+cloud/) for additional inspiration!