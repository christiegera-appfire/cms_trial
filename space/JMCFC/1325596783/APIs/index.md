# APIs

## Accessing Jira Fields

You can access the values of other fields and properties within JMCF [Scripted Fields](/cms_trial/space/JMCFC/731676729/Scripted+Field/) - both for the current issue and related issues - by using the APIs detailed in this section.

**Note**: It is not possible to access values directly within your scripts. This method, while once possible, is no longer supported. You must use the [getField](/cms_trial/space/JMCFC/1325137936/getField/) or [getFields](/cms_trial/space/JMCFC/1326317598/getFields/) APIs to access field values. This includes when using [getLinkedIssues](/cms_trial/space/JMCFC/1798209737/getLinkedIssues/), [getChildIssues](/cms_trial/space/JMCFC/1325072483/getChildIssues/), and [getParentIssue](/cms_trial/space/JMCFC/1326022692/getParentIssue/). To access field values of work items returned by these APIs, you must also use `getField` or `getFields` after fetching the related work items. See each page for details on how to update your scripts.

Additionally, you must always get fields using the ID or key, and not the field name or label (some Jira system fields have the same ID as their name, but this does not affect the requirement). See **Determining custom field IDs**, below, for more information.

## The script editor

The script editor window includes standard code editing features, including syntax colorization, error highlighting, code formatting, and code completion. Additionally, the script editor will provide prompts when it detects you are implementing API calls in your code.

The editor also includes three shortcut buttons to the right side of the window:

- [contract icon] **Expand/Contract** - Expand the editor to full height, or shrink it back to its original height.
- [templates icon] **Snippets** - Pre-written script examples.
- [help icon] **Help** - Links to JMCF for Jira Cloud documentation, scripted field documentation, and the Appfire support portal.

Image — asset pipeline pending  
Jira Misc Custom Fields (JMCF) Cloud scripted field editor interface

## Scripted Field Hints

Image — asset pipeline pending  
Jira Misc Custom Fields (JMCF) Cloud scripted field code hints display

Similar to many code editors, the scripted field editor includes syntax highlighting, error highlighting, cursor navigation, and code completion. The editor has access to all **JMCF for Jira Cloud** APIs and provides prompts as you type, as well as function references.

You are viewing the documentation for **Jira Cloud**.

| **In This Section**   - [issue APIs](/cms_trial/space/JMCFC/1325301787/issue+APIs/)   - [getChildIssues](/cms_trial/space/JMCFC/1325072483/getChildIssues/)   - [getField](/cms_trial/space/JMCFC/1325137936/getField/)   - [getFields](/cms_trial/space/JMCFC/1326317598/getFields/)   - [getFieldHistory](/cms_trial/space/JMCFC/1562447291/getFieldHistory/)   - [getIssueHistory](/cms_trial/space/JMCFC/1563854403/getIssueHistory/)   - [getLinkedIssues](/cms_trial/space/JMCFC/1798209737/getLinkedIssues/)   - [getParentIssue](/cms_trial/space/JMCFC/1326022692/getParentIssue/)   - [getProperty](/cms_trial/space/JMCFC/1326120998/getProperty/)   - [getProperties](/cms_trial/space/JMCFC/1324974093/getProperties/) - [jira APIs](/cms_trial/space/JMCFC/1741390022/jira+APIs/)   - [getGroup](/cms_trial/space/JMCFC/1741226042/getGroup/)   - [getGroupUsers](/cms_trial/space/JMCFC/1740963918/getGroupUsers/)   - [getAllPermissions](/cms_trial/space/JMCFC/1742045213/getAllPermissions/)   - [getPermissions](/cms_trial/space/JMCFC/1741750369/getPermissions/)   - [getProject](/cms_trial/space/JMCFC/1741815887/getProject/)   - [getProjects](/cms_trial/space/JMCFC/1741390062/getProjects/)   - [getStatuses](/cms_trial/space/JMCFC/1741488202/getStatuses/)   - [getUser](/cms_trial/space/JMCFC/1740898448/getUser/) |
| --- |

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