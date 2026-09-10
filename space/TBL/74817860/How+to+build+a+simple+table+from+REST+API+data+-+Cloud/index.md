# How to build a simple table from REST API data - Cloud

## Overview

This page shows how to bring REST API data from a Jira query directly into a Confluence table using the [JSON Table macro](/cms_trial/space/TBL/74812316/JSON+Table+macro+-+Cloud/), which is part of the [Advanced Tables for Confluence](https://appfire.atlassian.net/wiki/spaces/TBL) app.

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
| ***Paths to fields*** | *issues* |
| ***Paths to fields to be included*** | *key,fields.summary,fields.issuetype.name,fields.issuetype.id,fields.fixVersions[\*].name* |
| ***URL to JSON data*** | *https://xxxxxxxx.atlassian.net/rest/api/latest/search?jql=key%20in%20(TBL-174%2C%20TBL-300)%20order%20by%20key* |
| ***Auto number on each row*** | On |

### JSON data

Click the URL link above to view the live JSON data.

## Parameters set in the macro editor

![Advanced Tables JSON Table macro settings for simple REST API data](/cms_trial/assets/119f967b-701a-4f3e-a461-299f6320c8d4.png)![Advanced Tables simple REST API JSON table rendered on a page](/cms_trial/assets/3d86f915-14d7-4fd1-baa6-36d691957c04.png)

## Wiki markup input (Old editor)

```plaintext
{json-table:
paths=issues|
fieldPaths=key,fields.summary,fields.issuetype.name,fields.issuetype.id,fields.fixVersions[*].name|
url=https://xxxxxxxx.atlassian.net/rest/api/latest/search?jql=key%20in%20(TBL-174%2C%20TBL-300)%20order%20by%20key|
autoNumber=true}
{json-table}
```

## Example result

![Advanced Tables JSON data sample for simple REST API table](/cms_trial/assets/cf320ff4-d810-44bf-ac2a-97271b3d30f3.png)

## Other examples

Visit our [full list of product examples](/cms_trial/space/TBL/74814716/Use+cases+-+cloud/) for additional inspiration!