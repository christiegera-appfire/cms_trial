# getParentIssue

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | api.issue.getParentIssue(issue) | **Category** | issue |

**Note**: Access to fields on related issues is now possible through the getParentIssue, [getChildIssues](/cms_trial/space/JMCFC/1325072483/getChildIssues/), and [getLinkedIssues](/cms_trial/space/JMCFC/1798209737/getLinkedIssues/) APIs. However, updates to any related issue fields will **not** trigger a recalculation of the scripted field!

## Description

Get the Parent issue for a given issue.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | Object | Yes | Issue object  The issue of interest. For the current issue, use `issue`. For related issues, see [getParentIssue](/cms_trial/space/JMCFC/1326022692/getParentIssue/), [getChildIssue](/cms_trial/space/JMCFC/1325072483/getChildIssues/), or [getLinkedIssues](/cms_trial/space/JMCFC/1798209737/getLinkedIssues/). |

## Returns

Returns a Promise to the value; you must use `await`.

Returns an issue object that can be used in subsequent issue API calls.

## Examples

Return the **Affects versions** and **Fix versions** of the Parent issue.

```text
const parentIssue = await api.issue.getParentIssue(issue)
const parentVers = await api.issue.getFields(parentIssue,["versions","fixVersions"])
return JSON.stringify(parentVers)
```

Returns:

```text
 {
  "versions":[],
  "fixVersions":
  [
    {
      "self":"https://api.atlassian.com/ex/jira/<id>/rest/api/2/version/10000",
      "id":"10000",
      "description":"",
      "name":"2.1",
      "archived":false,
      "released":false
    }
  ]
}
```

You are viewing the documentation for **Jira Cloud**.