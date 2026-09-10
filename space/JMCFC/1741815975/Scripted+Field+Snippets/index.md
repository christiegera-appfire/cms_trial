# Scripted Field Snippets

JMCF for Jira Cloud provides several code snippets for Scripted Fields; these snippets address many of the most common data access scenarios and are designed so that they can be modified to fit your needs. To access the snippets, click the **Snippets** button on the right side of the script editor; you can scroll through the list of snippets here and insert the code by clicking on the snippet you want to use.

You are viewing the documentation for **Jira Cloud**.

Be sure to review the snippet code you choose! Many of the snippets require you to enter specific values, such as field IDs, project IDs, or user IDs.

**Note**: Snippets are not fully functional scripted fields! They are pieces of code designed to assist in addressing common data access tasks and calculations.

The following snippets are available:

| **Snippet Name** | **Description** | **Related APIs** |
| --- | --- | --- |
| **Get field value** | Get the value of a field (“Description” by default). Update the ID of the field to customize; see [Determining custom field IDs](https://appfire.atlassian.net/wiki/spaces/MCFCS/pages/1696235728/Scripted+Field+Snippets#Determining-custom-field-IDs) below for details on how to find field IDs. | [getField](/cms_trial/space/JMCFC/1325137936/getField/) |
| **Get property value** | Get the value of a property. Update the name of the property to customize. | [getProperty](/cms_trial/space/JMCFC/1326120998/getProperty/) |
| **Get a group** | Get the ID of a group using its name. | [getGroup](/cms_trial/space/JMCFC/1741226042/getGroup/) |
| **Get the members of a group** | Get a collection of User objects. | [getGroupUsers](/cms_trial/space/JMCFC/1740963918/getGroupUsers/) |
| **Get a project** | Get a project object using the project ID. Update the ID to customize. | [getProject](/cms_trial/space/JMCFC/1741815887/getProject/) |
| **Get projects** | Get an array of project objects using an array of project IDs. Update the IDs to customize. | [getProjects](/cms_trial/space/JMCFC/1741390062/getProjects/) |
| **Get a user** | Get a User object with a User ID. Update the ID to customize; see [Determining User IDs](https://appfire.atlassian.net/wiki/spaces/MCFCS/pages/1696235728/Scripted+Field+Snippets#Determining-User-IDs) below for details on how to find Jira User IDs. | [getUser](/cms_trial/space/JMCFC/1740898448/getUser/) |
| **Get statuses** | Get an array of status objects using an array of status ID values. Update the IDs to customize; see [Determining status IDs](https://appfire.atlassian.net/wiki/spaces/MCFCS/pages/1696235728/Scripted+Field+Snippets#Determining-status-IDs) below for details on how to find status ID values. | [getStatuses](/cms_trial/space/JMCFC/1741488202/getStatuses/) |
| **Get all permissions** | Get an array of all permissions as objects. | [getAllPermissions](/cms_trial/space/JMCFC/1742045213/getAllPermissions/) |
| **Get permissions** |  | [getPermissions](/cms_trial/space/JMCFC/1741750369/getPermissions/) |
| **Remaining story points in an epic** | This snippet calculates the total Story points for any unfinished child issues for an Epic. | [getChildIssues](/cms_trial/space/JMCFC/1325072483/getChildIssues/)  [getFields](/cms_trial/space/JMCFC/1326317598/getFields/) |
| **Completed story points in an epic** | This snippet calculates the total Story points for all finished child issues for an Epic. | [getChildIssues](/cms_trial/space/JMCFC/1325072483/getChildIssues/)  [getFields](/cms_trial/space/JMCFC/1326317598/getFields/) |
| **Time in each status - getFieldHistory() example** | This snippet returns a JSON string of all of the changes for an issue’s Status field. | [getField](/cms_trial/space/JMCFC/1325137936/getField/)  [getFieldHistory](/cms_trial/space/JMCFC/1562447291/getFieldHistory/) |
| **Updates per user - getIssueHistory() example** | This snippet returns a JSON string of the number of changes each user made to an issue. | [getIssueHistory](/cms_trial/space/JMCFC/1563854403/getIssueHistory/) |
| **Due date countdown (duration in seconds)** | This snippet calculates the number of seconds remaining until the Due Date. | [getField](/cms_trial/space/JMCFC/1325137936/getField/) |

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

## Determining User IDs

In Jira, there is a distinct difference between a User’s public name and their User ID; a User’s ID is unique identifier associated with their Atlassian account and is unique across all Atlassian products and instances. The best way to find a User’s ID is to check the URL of the User when viewing their details through the User Management tools. To find the ID of a User:

1. Log into Jira as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **User Management**.
3. This will open a new window displaying the Atlassian Administration tools. In the list of **Users**, click the name of the user for whom you need an ID.
4. Check the URL of the page that opens (figure, immediately right). The User’s ID is the last part of the URL, after ‘/users/’.

Image — asset pipeline pending  
Jira Misc Custom Fields (JMCF) Cloud user ID determination guide

## Determining status IDs

Jira Status values - both default and custom statuses - each have a unique identifier that can be used in scripting to retrieve additional information about that status. To find the ID of a status value:

1. Log into Jira as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Issues**.
3. In the left-hand panel, click **Statuses**.
4. The window will display the list of all status values for your instance. Right-click the **Edit** link to the right and select **Copy link address** (or the equivalent for your browser).
5. Paste the link value into a text document and check the **id** parameter of the URL (figure, immediately right).

Image — asset pipeline pending  
Jira Misc Custom Fields (JMCF) Cloud status ID determination guide