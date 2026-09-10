# getFields

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | api.issue.getField(issue, fieldNames) | **Category** | issue |

## Description

Get the value of a a set of fields for the given Jira issue.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | Object | Yes | Issue object  The issue of interest. For the current issue, use `issue`. For related issues, see [getParentIssue](/cms_trial/space/JMCFC/1326022692/getParentIssue/), [getChildIssue](/cms_trial/space/JMCFC/1325072483/getChildIssues/), or [getLinkedIssues](/cms_trial/space/JMCFC/1798209737/getLinkedIssues/). |
| fieldNames | Array | Yes | Include an array of field names. Use double quotes around field names (for example, [“summary”,”description”]).  For custom fields, see **Determining custom field IDs**, below. |

## Returns

Returns a Promise to the value; you must use `await`.

Returns an array of values, each of their own data type.

## Examples

Get the **Affects versions** and **Fix versions** of the issue.

```text
const vers = await api.issue.getFields(issue, ["versions","fixVersions"])
return JSON.stringify(vers)
```

Returns:

```text
{"versions":
  [
    {
      "self":"https://api.atlassian.com/ex/jira/<id>/rest/api/2/version/10001",
      "id":"10001",
      "description":"",
      "name":"2.0",
      "archived":false,
      "released":false
    },
    {
      "self":"https://api.atlassian.com/ex/jira/<id>/rest/api/2/version/10002",
      "id":"10002",
      "description":"",
      "name":"1.9",
      "archived":false,
      "released":true,
      "releaseDate":"2024-09-24"
    }
  ],
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

Get the **Labels** and **Components** of the issue’s Parent.

```text
const parentIssue = await api.issue.getParentIssue(issue)
const assignedTo = await api.issue.getFields(parentIssue, ["labels","components"]) 
return JSON.stringify(assignedTo)
```

Returns:

```text
{"labels":
  ["leadApproved","needsDocs"],
"components":
  [
    {
      "self":"https://api.atlassian.com/ex/jira/<id>/rest/api/2/component/10032",
      "id":"10032",
      "name":"Authentication"
    },
    {
      "self":"https://api.atlassian.com/ex/jira/<id>/rest/api/2/component/10033",
      "id":"10033",
      "name":"Infrastructure"
    }
  ]
}
```

You are viewing the documentation for **Jira Cloud**.

## Determining custom field IDs

There are several ways to determine the field ID of a custom field; the most straightforward is to check the URL of the custom field when editing its details through the Jira **Custom fields** screen. To find the ID of a custom field:

1. Log into Jira as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Issues**.
3. In the left-hand sidebar, click **Custom fields**.
4. Locate your custom field in the list; use the filter at the top of the list to search.
5. Click the action button at the far right ( [actionmenu icon] ) and select **Edit details**.
6. Check the URL for the page that opens - the final argument of the URL is the field ID (Figure 1, right).
7. Append this value to “customfield\_” to get the full ID of the field. For example, `customfield_10130` is the field ID of Projected Due Date, shown in the figure immediately right.

Image — asset pipeline pending  
Jira Misc Custom Fields (JMCF) Cloud custom field ID determination guide