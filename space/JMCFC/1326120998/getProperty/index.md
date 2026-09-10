# getProperty

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | api.issue.getProperty(issue, propertyName) | **Category** | issue |

## Description

Get the value of a property for the given Jira issue.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | Object | Yes | Issue object  The issue of interest. For the current issue, use `issue`. For related issues, see [getParentIssue](/cms_trial/space/JMCFC/1326022692/getParentIssue/), [getChildIssue](/cms_trial/space/JMCFC/1325072483/getChildIssues/), or [getLinkedIssues](/cms_trial/space/JMCFC/1798209737/getLinkedIssues/). |
| propertyName | String | Yes | Use double quotes (for example, “issueSource”). |

## Returns

Returns a Promise to the value; you must use `await`.

Exact return type matches the property being accessed.

You are viewing the documentation for **Jira Cloud**.