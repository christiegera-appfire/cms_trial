# How to map an Epic Link when creating a story

## Purpose

How do I map a value from Salesforce to certain Epics (**Epic Link** field in Jira) when a Jira Issue is created.?

## Answer

1. First, create a custom field in Salesforce with type: string.
2. Then, map the Salesforce custom field to JIRA's "Parent" field. If you are unsure on how to do this, refer to [Configuring Entity Mappings and Field Mappings](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754325/Configuring+Entity+Mappings+and+Field+Mappings).

   ![contentId-1596621419](/cms_trial/assets/963fd217-b546-4b8a-99bf-c00a9e79be7d.png)
3. To ensure the value in Salesforce synchronizes with Jira, make sure Epic Issue Key (not just a Jira key) is mapped Salesforce Text Custom Field like the example below.

   ![contentId-1596621419](/cms_trial/assets/93583e60-bd0a-40d6-b654-c97088ed658c.png)

Once the Salesforce object and the JIRA issue is synchronized, the Epic Link will automatically be converted according to the JIRA Issue:

![contentId-1596621419](/cms_trial/assets/11e3c26b-2c07-4a99-8354-215d10764def.png)

### Important

The fields **Epic Link** and **Parent Link** will be deprecated by Nov 11, 2022. It is crucial to update your mapping before that date by updating the deprecated fields to **Parent**.