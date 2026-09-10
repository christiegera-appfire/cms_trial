# Chatter posts on the Jira Comment component are visible to admins only

Users without the **View All Data** permission enabled in their Salesforce profile cannot view Chatter comments and posts in the Jira Comment component.

View for admins:

![test com1.png](/cms_trial/assets/6f4e48d5-0aa4-4875-889f-6c66cf6ce410.png)

When a user with limited permissions attempts to view Chatter content in Jira, they see a restricted view compared to administrators:

![userjiraissue-20240620-125457.PNG](/cms_trial/assets/444f4a4a-8103-43dc-8f55-32204b3ee7e1.PNG)

This limitation occurs because the Jira Comment component uses the Salesforce `FeedItem`query to load Chatter posts, which requires the **View All Data** permission. To learn more, see [Salesforce API Objects: FeedItem](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_feeditem.htm).

## Solution

To allow users to load the Chatter comments and posts in the Jira Comment component, the administrator needs to follow the steps:

1. In Salesforce, go to **Setup** > **Users** > **Profiles**.
2. Select the profile of the users who need access to Chatter comments in Jira and click **Edit**.
3. Locate and enable the **View All Data** permission.

![image-20240814-095733.png](/cms_trial/assets/9487f2c1-0d59-4774-80a8-e5257ed07e79.png)

1. Click **Save**.