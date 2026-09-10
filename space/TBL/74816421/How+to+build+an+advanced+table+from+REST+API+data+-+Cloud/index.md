# How to build an advanced table from REST API data - Cloud

## Overview

This page shows how to use the [JSON Table macro](/cms_trial/space/TBL/74812316/JSON+Table+macro+-+Cloud/), which is part of the [Advanced Tables for Confluence](https://appfire.atlassian.net/wiki/spaces/TBL) app, to create a table that contains version information retrieved directly from Jira. This example uses a number of the advanced capabilities of the *JSON Table* macro, including [augments](/cms_trial/space/TBL/74815166/Augments+-+Cloud/), to transform data into links and a particular emoticon such that the data is presented in a succinct, informative manner. The columns can be customized to meet your specific needs.

## Macro browser input

### Select this macro

|  |  |
| --- | --- |
| **Macro name** | *Advanced Tables - JSON Table* |
| **Macro syntax (Old editor)** | *{json-table}* |
| **Macro syntax (New editor - case insensitive)** | */JSON Table* |

### Define these parameters/values

|  |  |
| --- | --- |
| ***Paths to fields*** | *$* |
| ***Paths to fields to be included*** | *name,description,releaseDate,released,archived,userReleaseDate,self* |
| ***Paths to be used to determine sort order*** | *name* |
| ***Output format*** | *wiki* |
| ***URL to JSON data*** | *https://xxxxxxxx.atlassian.net/rest/api/2/project/TBL/versions* |
| ***Columns to show*** | *name,description,releaseDate,released,archived* |
| ***Augments to data row values*** | *%name%|https://xxxxxxxx.atlassian.net/browse/TBL/fixforversion/%id%],,,!%released%.png!,!%archived%.png!* |
| ***Augments to heading row values*** | *Name,Description,Release Date, Released, Archived* |
| ***Auto number on each row*** | On |
| ***Sort descending*** | On |

### Screenshots

![Advanced Tables JSON Table macro settings for REST API data](/cms_trial/assets/59cac3de-ba6b-4ab5-acb3-9c5bf04fa9eb.png)![Advanced Tables advanced REST API JSON Table macro column settings](/cms_trial/assets/5a833814-2804-444e-9926-63b533530a8f.png)![Advanced Tables JSON macro editor for REST API data](/cms_trial/assets/8c738201-d648-4d96-8c6c-edb3f272c34d.png)

## Wiki markup input (Old editor)

```plaintext
{json-table:
paths=$|
fieldPaths=name,description,releaseDate,released,archived,userReleaseDate,self|
sortPaths=name|
url=https://xxxxxxxx.atlassian.net/rest/api/2/project/TBL/versions|
output=wiki|
columns=name,description,releaseDate,released,archived| 
augments=[%name%%!%https://xxxxxxxx.atlassian.net/browse/TBL/fixforversion/%id%],,,!%released%.png!,!%archived%.png!,|
headingAugments=Name,Description,Release Date, Released, Archived|
sortDescending=true|
autoNumber=true}
{json-table}
```

### Emoticons

- For this example, we used [augments](/cms_trial/space/TBL/74815166/Augments+-+Cloud/) to show an emoticon instead of the true and false values of the released and archived fields. This is a general technique that can be used to make tables look better.
- For this case, it is simply having emoticon images named true and false, attached to this page (or some other page), and referenced in wiki markup notation by *!true.png!* and *!false.png!*. On your site, you will need to add those two images and reference them accordingly.
- They can be named differently, but must have true and false in the name somewhere so the released and archived values determine which emoticon is shown. Wiki markup notation for images in the most general way is: *!SPACE:my page^myimg.jpg!*.

## Example result

![Advanced Tables Jira versions table rendered from JSON REST data](/cms_trial/assets/19f46549-ab4e-4e3b-a421-c8681707b9e3.png)

## Other examples

Visit our [full list of product examples](/cms_trial/space/TBL/74814716/Use+cases+-+cloud/) for additional inspiration!