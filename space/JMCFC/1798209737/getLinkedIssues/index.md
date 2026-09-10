# getLinkedIssues

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | api.issue.getLinkedIssue(issue, linkFilterFunction?) | **Category** | issue |

**Note**: Access to fields on related issues is now possible through the [getParentIssue](/cms_trial/space/JMCFC/1326022692/getParentIssue/), [getChildIssues](/cms_trial/space/JMCFC/1325072483/getChildIssues/), and getLinkedIssues APIs. However, updates to any related issue fields will **not** trigger a recalculation of the scripted field!

## Description

Get linked issues for the current issue, either through a specific link type or all linked issues. A filter function can be provided to limit which linked issues should be retrieved.

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| issue | Object | Yes | Issue object  The issue of interest. For the current issue, use `issue`. For related issues, see [getParentIssue](#), [getChildIssue](#), or [getLinkedIssues](#). |
| linkFilterFunction | Function | No | See **Link Filter Functions**, below. |

## Returns

Returns a Promise to the value; you must use `await`.

Returns an issue object that can be used in subsequent issue API calls.

## Examples

Return all issues linked to the current issue.

```text
const linkedIssues = await api.issue.getLinkedIssues(issue)
return linkedIssues.map(li=>li.key) // Returns an array of issue objects
```

Return the total number of issues linked to the current issue.

```text
const linkedIssues = await api.issue.getLinkedIssues(issue)
return linkedIssues.length // Number of linked issues
```

Return any issues that are blocking the current issue. Uses the **Link Filter Function** (see below).

```text
function blockingUs(link) {
  return link.type.name==='Blocks' && link.inwardIssue
} 

// using the filter function
const issuesBlockingUs = await api.issue.getLinkedIssues(issue, blockingUs)

return issuesBlockingUs.map(li=>li.key) //Returns an array of issue objects
```

You are viewing the documentation for **Jira Cloud**.

| **On this page**   - [Syntax](#syntax) - [api.issue.getLinkedIssue(issue, linkFilterFunction?)](#api-issue-getlinkedissue-issue-linkfilterfunction) - [Category](#category) - [issue](#issue) - [Description](#description) - [Parameters](#parameters) - [Returns](#returns) - [Examples](#examples) - [Link Filter Functions](#link-filter-functions) - [Finding the link data shape](#finding-the-link-data-shape) - [Link direction](#link-direction) |
| --- |

## Link Filter Functions

**Note**: Using link filter functions can lead to significant performance improvements, particularly for larger instances with many linked issues. The link filter function guarantees that only issues linked using specified link types will be fetched by `getLinkedIssues`.

In order to limit the types of linked issues this API will return, you can use a link filter function. Link filter functions are functions that describe which links should be used to retrieve issues; they are called for every link present in the issue and return `true` or `false` for each link that exists. It is important to note that a link filter function does not return issues, or even references to issues - it only returns an indicator of which link types should subsequently be fetched and returned by the `getLinkedIssue` call. When you call `getLinkedIssues`, the API runs the filter function for every issue connected to the issue provided in the first argument. The `getLinkedIssues`API only returns those issues for which the filter function returns `true`.

To demonstrate how a link filter function works, consider the following example. The example below demonstrates a scripted string collection field that will return an array of strings that include the issue key and description of every issue that is currently **blocked by** the issue where the custom field is calculated. The full script of the custom field is:

```text
function blocksUs(link) {
  return link.type.name==='Blocks' && link.inwardIssue
}

const linkedIssues = await api.issue.getLinkedIssues(issue,blockedByUs) //get only issues blocked by the current issue

//Get the description value from each issue and return a string
const linkedIssueDescriptions = await Promise.all(linkedIssues.map(async(li) => {
  const description = await api.issue.getField(li, 'description')
  return `${li.key} - ${description}`
}))

return linkedIssueDescriptions //Returns a collection of strings
```

Looking at a specific example, we have an issue that has three linked issues (pictured right). Each of the linked issues uses a different link type - ‘duplicates,’ ‘is blocked by,’ and ‘relates to.’ The code for our scripted field includes a link filter function **blocksUs** that details which links should be used to retrieve linked issues.

In this custom field, only issues that block the current issue should be fetched by getLinkedIssues. You can see this in the function itself on line 2:

`return link.type.name==='Blocks' && link.inwardIssue`

### Finding the link data shape

To create this function, you need to know the shape of the link data. To determine this, we can add the following to the link filter function:

```text
function blocksUs(link) {
  //Output the shape of any links to the console
  console.log(JSON.stringify(link, null, 2)) 
  return link.type.name==='Blocks' && link.inwardIssue
}
```

![customFields-ScriptedFieldExampleIssue.png](/cms_trial/assets/8a16a9f8-0af9-4cd2-8c00-6276767de355.png)

When testing the custom field script against the issue with the three links, we get the full shape of all links. The full shape of the link of interest - a link for issues that are blocked by our test issue - is detailed on the right. (When running the above script, all links that exist on the issue will be returned.)

Using the full link shape, creating the function is a matter of determining which data points to use in your link filter function to return the needed linked issues.

In our example, two data points are relevant:

- **Name** - Line 6, right. The name of the link type.
- **inwardIssue** - Line 11, right. The direction of the link.

### Link direction

Link direction is an important factor in filtering issues fetched by `getLinkedIssues`. In the link data to the right, note that the name of the link type does not correspond to how the link is detailed in the Jira issue; the **name** of the link type is **Blocks**, but on the Jira issue view, it’s described as **is blocked by**. You can determine the direction of the link by checking the data immediately after `type`; the array will either be named `inwardIssue` or `outwardIssue`, detailing the direction of the link.

Alternately, by matching the description in the issue view to the link data, you can see that the link is an inward **Blocks** link.

**Link data**

```text
{
  "id": "10118",
  "self": "https://api.atlassian.com/ex/jira/.../rest/api/2/issueLink/10118",
  "type": {
    "id": "10000",
    "name": "Blocks",
    "inward": "is blocked by",
    "outward": "blocks",
    "self": "https://api.atlassian.com/ex/jira/../rest/api/2/issueLinkType/10000"
  },
  "inwardIssue": {
    "id": "10404",
    "key": "DEV-42",
    "self": "https://api.atlassian.com/ex/jira/.../rest/api/2/issue/10404",
    "fields": {
      "summary": "Login allows blank spaces in username",
      "status": {
        "self": "https://api.atlassian.com/ex/jira/.../rest/api/2/status/10001",
        "description": "",
        "iconUrl": "https://api.atlassian.com/ex/jira/.../",
        "name": "Done",
        "id": "10001",
        "statusCategory": {
          "self": "https://api.atlassian.com/ex/jira/../rest/api/2/statuscategory/3",
          "id": 3,
          "key": "done",
          "colorName": "green",
          "name": "Done"
        }
      },
      "priority": {
        "self": "https://api.atlassian.com/ex/jira/.../rest/api/2/priority/3",
        "iconUrl": "https://danappfire.atlassian.net/images/icons/priorities/medium.svg",
        "name": "Medium",
        "id": "3"
      },
      "issuetype": {
        "self": "https://api.atlassian.com/ex/jira/.../rest/api/2/issuetype/10004",
        "id": "10004",
        "description": "A problem or error.",
        "iconUrl": "https://api.atlassian.com/ex/jira/.../rest/api/2/universal_avatar/view/type/issuetype/avatar/10303?size=medium",
        "name": "Bug",
        "subtask": false,
        "avatarId": 10303,
        "hierarchyLevel": 0
      }
    }
  }
}
```