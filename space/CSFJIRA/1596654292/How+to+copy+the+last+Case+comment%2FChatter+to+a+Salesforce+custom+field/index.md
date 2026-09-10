# How to copy the last Case comment/Chatter to a Salesforce custom field

## Purpose

This KB explains how to:

- Send the last Chatter comment to a custom text field in Salesforce (Feed Item object)
- Send the last Case comment to a custom text field in Salesforce (Case Comment object)

- This solution is for Case Chatter/Comments. The Salesforce connector fully supports chatter/comments on the Case object and Chatter on the Opportunity object.
- This solution has been tested in a sandbox and production environment. We recommend you to test this on a sandbox environment before deploying it to production.

The [Feed Item](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_feeditem.htm) object is for Chatter, the [Case Comments](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_casecomment.htm?q=case+comments) object is for Case comments.

## Answer

1. In Jira, create two paragraph fields. In this example, the first is named "Last Comment Jira" and the second is named "Last Chatter Jira".
2. In Salesforce, create two Salesforce Rich text fields. In this example, the first is named "Last Case Comment" and the second is named "Last Chatter Comment".

   1. Both custom fields should have a length of 32k.

## Configuring Last Case Comment to a custom field

1. Create a [Salesforce flow](https://help.salesforce.com/s/articleView?id=sf.flow.htm&language=en_US&r=https%3A%2F%2Fwww.google.com%2F&type=5#:~:text=A%20flow%20is%20an%20application,and%20scheduled%20actions%20from%20processes.) using the Case Comment object. Set the following information:

   - i.) **Object** - Set the name as "Cast Comment".
   - ii.) **Configure Trigger - Trigger the Flow when** - Set to "A record is created".
   - iii.) Set the **Condition Requirements** based on the image below:

     ![contentId-1596654292](/cms_trial/assets/66ca259d-f1d9-4937-9298-fe231eb91b71.png?version=1&modificationDate=1678857307170&cacheVersion=1&api=v2)
   - iv.) The value “5005” are the first numbers of the CASE object ID(The number varies for different users. Check your instance CASE ID starting numbers).
   - v.) The second entry condition is to check that ”commentBody” is not empty.
   - **Optimize the Flow for** - Set to "Actions and Related Records".
2. Create a [Update Records](https://help.salesforce.com/s/articleView?id=sf.flow_ref_elements_data_update.htm&language=en_US&r=https%3A%2F%2Fwww.google.com%2F&type=5#:~:text=Identify%20Salesforce%20records%20to%20update,set%20the%20field%20values%20individually.) and set the following information:

   1. i.) **How to Find Records to Update and Set Their Values** - Set to "Specify conditions to identify records, and set fields individually".
   2. ii.) **Object**- Set the name to "Case".
   3. iii.) Set the **Filter Case Records** based on the image below:

      ![contentId-1596654292](/cms_trial/assets/2776f56e-e249-4152-bb2f-b80b1767357b.png?version=1&modificationDate=1678857307241&cacheVersion=1&api=v2)
   4. **Last Case Comment** - Set it to your own wordings. The Flow will be triggered and the custom field will be updated with the last comment.
3. In Jira, map the **Last Comment Jira** field with the **Last Case Comment** field.

   inlineExtension

## Configuring Last Chatter Comment to a custom field

1. Create a [Salesforce flow](https://help.salesforce.com/s/articleView?id=sf.flow.htm&language=en_US&r=https%3A%2F%2Fwww.google.com%2F&type=5#:~:text=A%20flow%20is%20an%20application,and%20scheduled%20actions%20from%20processes.) for the Feed Item object. Set the following information:

   - i.) **Object** - Set the name as "Feed Item".
   - ii.) **Configure Trigger - Trigger the Flow when** - Set to "A record is created".
   - iii.) Set the **Condition Requirements** based on the image below:

     ![contentId-1596654292](/cms_trial/assets/0aaf8af1-54d0-4b96-90f2-35251b3cf24c.png?version=1&modificationDate=1678857307315&cacheVersion=1&api=v2)
2. Create a [Update Records](https://help.salesforce.com/s/articleView?id=sf.flow_ref_elements_data_update.htm&language=en_US&r=https%3A%2F%2Fwww.google.com%2F&type=5#:~:text=Identify%20Salesforce%20records%20to%20update,set%20the%20field%20values%20individually.) and set the following information:

   1. i.) **How to Find Records to Update and Set Their Values** - Set to "Specify conditions to identify records, and set fields individually".
   2. ii.) **Object**- Set the name to "Case".
   3. iii.) **Filter Case Records**  - Set to "All Conditions are Met (AND)

      1. Field is "ID", Operator is "Equals, Value is "$Record > Parent ID (Case) > Case ID"
   4. iv.) **Set Field Values for the Case Records** - Set Field to "Last\_Chatter\_Comment\_C" and Value to "$Record > Body".
3. In Jira, map the **Last Chatter Jira** field with the **Last Chatter Comment** field.
4. The configuration is complete.