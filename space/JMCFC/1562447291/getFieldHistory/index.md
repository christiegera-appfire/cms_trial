# getFieldHistory

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | api.issue.getFieldHistory(issue, fieldName) | **Category** | issue |

## Description

Retrieve the change history for a particular field of an issue.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | Object | Yes | Issue object  The issue of interest. For the current issue, use `issue`. For related issues, see [getParentIssue](/cms_trial/space/JMCFC/1326022692/getParentIssue/), [getChildIssue](/cms_trial/space/JMCFC/1325072483/getChildIssues/), or [getLinkedIssues](/cms_trial/space/JMCFC/1798209737/getLinkedIssues/). |
| fieldName | String | Yes | Use double quotes (for example, “summary”). For custom fields, see **Determining custom field IDs**, below. |

## Returns

Returns a Promise to the value; you must use `await`.

Returns an array of zero or more `IssueChange` objects; each `IssueChange` object includes an array of zero or more `IssueChangeItems`.

**Note**: When an issue is updated from the issue screen (or other Jira screens), it will usually only include a single `IssueChangeItem`. However, when an issue is updated programmatically, multiple fields or attributes can be updated at once, resulting in several `IssueChangeItems` included.

```text
interface IssueChange {
  id: string
  author: {
    displayName: string
    accountId: string
    accountType: string
  }
  created: string
  items: IssueChangeItem[]
}

interface IssueChangeItem {
  field: string
  fieldId: string
  fieldtype: 'jira' | 'custom'
  from: string
  fromString: string
  to: string
  toString: string
}
```

## Examples

Return a list of all recent changelog entries for the **Status** field.

```text
const statusChanges = await api.issue.getFieldHistory(issue, 'status'')
return statusChanges.map((change)=>change.items.map((item)=>`status changed from ${item.fromString} to ${item.toString} by ${change.author.displayName}`)).flat()
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