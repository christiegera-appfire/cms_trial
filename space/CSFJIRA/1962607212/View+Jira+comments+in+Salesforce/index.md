# View Jira comments in Salesforce

You can view Jira Issue comments in Salesforce through a dedicated Visualforce panel and Chatter. This allows a Salesforce agent to view or exchange comments with the Jira team.

At the moment, these features are only supported by the Case Object.

By default, Connector for Salesforce & Jira does not currently work with the Jira Service Management comment visibility setting.

However, Jira Issue comments can be viewed in Salesforce through a dedicated Visualforce panel and Chatter. More details about this configuration are available below.

## Before you start

- Make sure you have enabled the comment visibility in the Salesforce package. Only comments that meet the configured visibility setting are displayed in Salesforce. To learn more, see [Comment Configuration](/cms_trial/space/CSFJIRA/1873445530/Configure+settings+in+the+Salesforce+package/).

Comments restricted to a Jira project role are excluded entirely, ensuring that role-restricted content is not disclosed to unauthorized users.

## View Jira comments with Lightning Experience

The panel is an aggregated view of comments from all associated Jira issues and the comments from the record itself. The comments displayed on this panel are bound to any [comment filter](/cms_trial/space/CSFJIRA/1873413366/Filter+Jira+comments+in+Salesforce+Cases/) set by your administrator.

Your administrator must have also [set up the Jira Comments panel for Lightning Experience](/cms_trial/space/CSFJIRA/1873969162/Configure+Lightning+Experience+components/).

The Jira Issues and Jira Comments Lightning components are visible when added to the records, even though the case might not have any associations. These two components are not displayed once we have an association. We are tracking this as a feature request.

View a Salesforce Case that has an [association](/cms_trial/space/CSFJIRA/3091760268/Work+with+associations/). Depending on how your administrator configured the view, the Jira Issue comments will be displayed in their own section within the Case.

## View Jira comments in a Visualforce panel

The panel is an aggregated view of comments from all associated Jira issues and the comments from the record itself. The comments displayed on this panel are bound to any [comment filter](/cms_trial/space/CSFJIRA/1873413366/Filter+Jira+comments+in+Salesforce+Cases/) set by your administrator.

Your administrator must have also [set up the Jira Comments panel with Visualforce](/cms_trial/space/CSFJIRA/1873445794/Configure+Visualforce+components/).

1. View a Salesforce Case that has an [association](/cms_trial/space/CSFJIRA/3091760268/Work+with+associations/). Depending on how your administrator configured the view, the Jira Issue comments are displayed in their own section within the Case, similar to this:

   ![csfjira-global-list.png](/cms_trial/assets/7aafbabd-03f5-4b2e-bec8-d2d2a2e7838d.png)![salesforce and jira comments](/cms_trial/assets/d1235dd6-522c-4ac5-a829-ed6e1479c967.png)

   The comments in blue are from Salesforce, and the comments in grey are from Jira.

## View Jira comments in Chatter (Case Feed)

Jira comments can also be posted to the Case feed in Chatter. When someone creates or edits a comment in Jira, a post is made to the Case feed of the corresponding associated Case record.

You will see Jira comments in Chatter if:

- Your administrator [enabled Chatter Feed setting](/cms_trial/space/CSFJIRA/1873445656/Configure+Chatter/) in Salesforce.
- The Jira comment satisfies comment privacy and hashtag filters set by your administrator.
- The associated Jira issue is not marked as **View-only**.

  ![Jira comments in Chatter](/cms_trial/assets/e59d0fb5-5b36-402a-8361-4cc7de0bfd9a.png)

The Chatter post is posted by an administrator account due to a limitation of the Salesforce Chatter API. However, a remark is provided to indicate the user who left the comment in Jira.

## Related information

- [Filtering Jira Comments in Salesforce Cases](/cms_trial/space/CSFJIRA/1873413366/Filter+Jira+comments+in+Salesforce+Cases/)