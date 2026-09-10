# How to synchronize customer tier/type from Salesforce with SLAs in Jira

You can configure Jira to apply different SLA goals based on Salesforce customer data like Customer Tier or Account Type using the Connector for Salesforce & Jira.

## Overview

This integration allows you to automatically apply appropriate SLA policies to customer issues based on their status in Salesforce, ensuring consistent service delivery across platforms.

## Steps

1. Create a custom field in Jira to receive the value of the Salesforce field, which determines the SLA goals.

   - Make sure the two Jira fields are [compatible](https://appfire.atlassian.net/wiki/x/fYK9Wg) with the Salesforce field you're mapping
2. Map your Jira custom field to the corresponding Salesforce field.  
   Follow the detailed instructions in [Configure entity, field and value mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/)
3. Configure SLA Goals Based on Customer Data.

   1. In Jira, select **Project** > **View all projects**.
   2. Under **More actions,** click **Project settings** for your project.
   3. Click **Request management** > **SLAs**.   
      There is a list of SLAs already created, such as **Time to first response**.
   4. Click **Edit** to set up goals.  
      In the **Goals** view, under **Apply to work items,** you can see all work items that match the query.
   5. Set up your goals:

      - Create filters based on your custom field values
      - Assign appropriate timeframes for each customer category

        ![tier.jpeg](/cms_trial/assets/08e8549c-6445-4b0d-8a0c-58f74b269471.jpeg)

As shown in the image, the Customer Tier (custom field) is the filter to apply the different goals.

- For **Tier 1**,the goal for **Time to first response**is 2 hours.
- For **Tier 2**,the goal for **Time to first response**is 4 hours.
- For **Tier 3**,the goal for **Time to first response**is 6 hours.