# View Salesforce comments in Jira

If Jira Issues are [mapped to Salesforce Cases](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/), Connector for Salesforce & Jira automatically aggregates comments from [a Salesforce Case associated with a Jira Issue](/cms_trial/space/CSFJIRA/3092284964/Associate+a+Salesforce+record+from+Jira/).

Though pulled from Salesforce, these Salesforce Comments are not stored in Jira.

## View Salesforce comments in a Jira Issue

1. Go to a Jira Issue with which you’ve already associated a Case.
2. Scroll down and click the **Salesforce Comments** tab in the **Activity** section.

![Salesforce comments.png](/cms_trial/assets/57c09814-cd93-42f0-940c-2eb2ae155b67.png)

If the associated **Salesforce Case** has any comments, they are shown here.

![private comment.png](/cms_trial/assets/2f0de14d-41c1-4340-ab96-006023d7842f.png)

A Salesforce Comment is displayed with a tag to show whether it is **Private** or **Public**. Click the upper section of the *Salesforce Comment* to expand or contract the comment panel.

![View Replies.png](/cms_trial/assets/e6cac35d-e951-49ce-9d3b-82199efb9c1a.png)

## View Chatter (Case Feed) comments in Jira

### Case Feed (Chatter) comments

Case Feed (Chatter) comments can be posted via the Salesforce Comments tab in a Jira issue.

When someone creates or edits a comment in Jira, a post is made to the Case Feed of the corresponding associated Case object.

You will see Chatter comments in Jira if:

- Your administrator [enabled Chatter Feed setting](/cms_trial/space/CSFJIRA/1873445656/Configure+Chatter/) in Salesforce.
- The Chatter comment satisfies Jira comment privacy and hashtag filters set by your administrator.
- The Chatter post is made in the Case object (another object is not supported).

![contentId-1962443468](/cms_trial/assets/e5bc106f-4c67-4084-a7cb-9b3383817858.png?version=1&modificationDate=1730966654292&cacheVersion=1&api=v2&width=700&height=129)

### Nested comments

Replies posted to Case Feed (Chatter) comments are automatically nested in Jira but are expanded.

![contentId-1962443468](/cms_trial/assets/d4e328c5-c13f-4f43-bc63-b2e487082930.png?version=1&modificationDate=1730966654093&cacheVersion=1&api=v2&width=635&height=108)

Click **View Replies** to expand all available replies from the Case Feed (Chatter) comments:

![view replies from the Case Feed comment](/cms_trial/assets/b4a14eb4-06f1-4fb3-8702-fb52e4f72ac3.png?version=1&modificationDate=1730966653884&cacheVersion=1&api=v2&width=634&height=291)

## Related information

- [Filtering Salesforce Comments in Jira Issues](/cms_trial/space/CSFJIRA/1873380322/Filter+Salesforce+comments+in+Jira+work+items/)