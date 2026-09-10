# How to build a Jira version list with JSON Table - Cloud

## Overview

This page shows how you create a simple table from JSON data using the [JSON Table macro](/cms_trial/space/TBL/74812316/JSON+Table+macro+-+Cloud/), which is part of the [Advanced Tables for Confluence](https://appfire.atlassian.net/wiki/spaces/TBL) app.

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
| ***Paths to fields*** | *values* |
| ***Paths to fields to be included*** | *name,description,id,releaseDate* |
| ***URL to JSON data*** | *https://xxxxxxxx.atlassian.net/rest/api/latest/project/TBL/version* |
| ***Sort descending*** | On |
| ***Auto sort column*** | *Name* |

## Parameters set in the macro editor

![Advanced Tables JSON Table macro settings for Jira version list](/cms_trial/assets/aba6315f-20ae-4f28-ae27-ac401277b992.png)![Advanced Tables Jira version list rendered from JSON data](/cms_trial/assets/2a9d6e3d-5bc3-4cf2-88d3-d51e7bc36bb8.png)

## Wiki markup input (Old editor)

```plaintext
{json-table:
paths=values|
fieldPaths=name,description,id,releaseDate|
url=https://xxxxxxxx.atlassian.net/rest/api/latest/project/TBL/version?maxResults=100|
sortDescending=true|
sortColumn=Name}
{json-table}
```

## Live example

[Unmapped macro: json-table — no content to fall back on]

## Other examples

Visit our [full list of product examples](/cms_trial/space/TBL/74814716/Use+cases+-+cloud/) for additional inspiration!