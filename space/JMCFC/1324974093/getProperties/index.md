# getProperties

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | api.issue.getProperties(issue, propertyNames) | **Category** | issue |

## Description

Get the value of a a set of properties for the given Jira issue.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | Object | Yes | Issue object  The issue of interest. For the current issue, use `issue`. For related issues, see [getParentIssue](/cms_trial/space/JMCFC/1326022692/getParentIssue/), [getChildIssue](/cms_trial/space/JMCFC/1325072483/getChildIssues/), or [getLinkedIssues](/cms_trial/space/JMCFC/1798209737/getLinkedIssues/). |
| propertyNames | Array | Yes | Include an array of property names. Use double quotes around property names (for example, [“issueSource”,”issueSynced”]). |

## Returns

Returns a Promise to the value; you must use `await`.

Returns an array of values, each of their own data type.

You are viewing the documentation for **Jira Cloud**.