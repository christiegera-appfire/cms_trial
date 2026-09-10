# Work with Jira comments (NextGen) with Lightning Experience

This page explains how to use the Jira Comments (NextGen) component to view and manage comments from Jira and Salesforce in one place. With this component, you can:

- Displays comments added to the associated work items.

  - Work item c omments are tagged with `Jira` and are linked to a work item key.
- Displays comments added to Salesforce record.

  - Record comments are tagged with `Salesforce`.
- Displays Chatter Feed posts:

  - Posts are tagged with `Chatter`.
- Displays comments added to the Chatter Feed post.
- Supports rich text formatting in Salesforce Case Comments, including styles and tables. Comments appear rendered in Jira and in the Salesforce connector panel. Images in rich text comments are displayed inline when hosted on Salesforce domains. Images hosted elsewhere appear as links instead.
- Matches the selected connection:

  - The connection dropdown appears only if there is more than one connection.
  - Selecting a connection in Jira Issues or Jira Comments component reflects the selected relationship in the other component automatically.

## Before you start

Make sure you have:

- Added the Jira Comment component to the record page. [Configured Lightning Experience components](/cms_trial/space/CSFJIRA/1873969162/Configure+Lightning+Experience+components/).
- Set up comment privacy under Connection settings [Configure connection settings](https://support.appfire.com/space/CSFJIRA/1853653945/Configure+connection+settings#Comments-&-Chatter-Settings)

## Display Jira comments

1. Associate a Jira work item to the Salesforce record by following this guide: [Create a Jira work item from Salesforce.](/cms_trial/space/CSFJIRA/3091792703/Create+a+Jira+work+item+from+Salesforce/)
2. In Jira, write a comment on the Jira work item. The comment is synced to Salesforce and shown in the **Jira Comments** component.

   ![screenshot of Jira Comments component](/cms_trial/assets/bc5f98fd-4d87-4b60-a8a4-a1b7155eb7a7.png)

## Add comments in Salesforce (Chatter Feed and Case)

1. For Case comments:

   1. In the Salesforce record page, scroll to **Case Comments** and click **New**.
   2. Write a comment in the **Body** and select **Save**. The comment is included in the Jira Comment component.
2. For Chatter Feed:

   1. In the **Feed** tab, insert the comment in the **Post** section and click **Share**. The comment is included in the Jira Comment component.
   2. Under **All Updates**, write a comment under the Chatter Post and click **Comment**. The comment is included in the Jira Comment component.
3. The **Jira Comment** component tags the comment according to where the comment was made.

   ![screenshot of Jira Comment component tags the comment according to where the comment was made.](/cms_trial/assets/7aed0224-9af1-4a62-a34c-7875f70d0ae7.png)

## Change connections

1. In the Jira Comments component, you can change the selected connection from the dropdown.
2. The newly selected connection will update automatically in the Jira Issues section, ensuring both Jira Comments and Jira Issues always show the same connection.

## Sort comment history by newest or oldest first

You can read a comment starting from the newest or the oldest. The total number of Jira Comments in the Jira Issue is shown by the number in brackets.

To sort comment history by newest or oldest first:

1. Scroll down to the Jira Comments component.
2. Select **Oldest** or **Newest** first.