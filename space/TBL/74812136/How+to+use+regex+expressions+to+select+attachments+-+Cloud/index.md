# How to use regex expressions to select attachments - Cloud

## Overview

This page demonstrates how to use the [Attachment Table macro](/cms_trial/space/TBL/74812217/Attachment+Table+macro+-+Cloud/), which is part of the [Advanced Tables for Confluence](https://appfire.atlassian.net/wiki/spaces/TBL) app, to select attachments based on the space or attachment name using a regex expression.

- Use the special *@self* value for the *Space key or space name regex* parameter to match on all attachments in the current space.
- Use *.\*png* to match on attachments whose name ends in PNG.

## Macro browser input

### Select this macro

|  |  |
| --- | --- |
| **Macro name** | *Advanced Tables - Attachment table* |
| **Macro syntax (Old editor)** | *{attachment-table}* |
| **Macro syntax (New editor - case insensitive)** | */Attachment Table* |

### Define these parameters/values

|  |  |
| --- | --- |
| *Space key or space name regex* | *@self* |
| *Attachment name regex* | .\*png |

Confluence is more limited on parameter values. Thus, **|** (pipe - used for regex **or**)is a reserved character and cannot be used.

### Parameters set in the macro editor

![Advanced Tables Attachment Table macro regex selection settings](/cms_trial/assets/79b79f17-7bb7-4330-8f34-4f751e2cf90b.png)![Advanced Tables Attachment Table macro regex output settings](/cms_trial/assets/7b5cc8cf-05d6-4382-8455-24117e9c0971.png)

## Wiki markup input (Old editor)

```plaintext
{attachment-table:spaceRegex=@self|attachmentRegex=.*png}
```

## Example result

![Advanced Tables attachment table example for a space using regex selection](/cms_trial/assets/7457085d-9f40-4c5e-8282-619212c815f4.png)

### Selecting attachments based on matching on more than one label

Constructing a regex to match attachments that have two or more specific labels is a bit more complicated. To do this, you must:

1. Set the *Label match option* to *all*.
2. Use a regex pattern similar to the following using *xxx*, *yyy*, and *zzz* as sample labels:

```text
2 labels:  .*(?:.*\b(?:(?:xxx)|(?:yyy))\b.*){2}.*
3 labels:  .*(?:.*\b(?:(?:xxx)|(?:yyy)|(?:zzz))\b.*){3}.*
```

## Other examples

Visit our [full list of product examples](/cms_trial/space/TBL/74814716/Use+cases+-+cloud/) for additional inspiration!