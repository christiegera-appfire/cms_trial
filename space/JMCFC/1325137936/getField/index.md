# getField

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | api.issue.getField(issue, fieldName) | **Category** | issue |

## Description

Get the value of a field for the given Jira issue.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | Object | Yes | Issue object  The issue of interest. For the current issue, use `issue`. For related issues, see [getParentIssue](/cms_trial/space/JMCFC/1326022692/getParentIssue/), [getChildIssue](/cms_trial/space/JMCFC/1325072483/getChildIssues/), or [getLinkedIssues](/cms_trial/space/JMCFC/1798209737/getLinkedIssues/). |
| fieldName | String | Yes | Use double quotes (for example, “summary”). For custom fields, see **Determining custom field IDs**, below. |

## Returns

Returns a Promise to the value; you must use `await`.

Exact return type matches the field being accessed.

## Examples

Return a string of the **Summary** field value of the current issue.

```text
await api.issue.getField(issue, "summary") // “Implement SSO Login”
```

Return a datetime of the **Actual Start** field of the current issue.

```text
await api.issue.getField(issue, "customfield_10008") // “2024-09-17T04:00:00.000-0400"
```

Return the **Assignee** of the current issue’s Parent.

```text
const parentIssue = await api.issue.getParentIssue(issue)
const assignedTo = await api.issue.getFields(parentIssue, "assignee") // Returns a User Object
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