# getChildIssues

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | api.issue.getChildIssues(issue) | **Category** | issue |

**Note**: Access to fields on related issues is now possible through the [getParentIssue](/cms_trial/space/JMCFC/1326022692/getParentIssue/), getChildIssues, and [getLinkedIssues](/cms_trial/space/JMCFC/1798209737/getLinkedIssues/) APIs. However, updates to any related issue fields will **not** trigger a recalculation of the scripted field!

## Description

Get all Child issues for a given issue.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | Object | Yes | Issue object  The issue of interest. For the current issue, use `issue`. For related issues, see [getParentIssue](/cms_trial/space/JMCFC/1326022692/getParentIssue/), [getChildIssue](/cms_trial/space/JMCFC/1325072483/getChildIssues/), or [getLinkedIssues](/cms_trial/space/JMCFC/1798209737/getLinkedIssues/). |

## Returns

Returns a Promise to the value; you must use `await`.

Returns an array of issue objects that can be used in subsequent issue API calls.

Other issue APIs are not able to access a list of issues; when trying to access the values of Child issues, you must either reference the desired Child issue using its index - `childIssues[0]` for example - or loop through the Child issues object.

You are viewing the documentation for **Jira Cloud**.