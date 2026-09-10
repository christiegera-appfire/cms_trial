# Push updates for multiple Jira Issues in bulk mode

This page explains how to bulk push updates to multiple Jira Issues at once.

## Before you start

Confirm the following Jira permission settings:

- You need to have the **Bulk Change** global permission.
- You need to have **View** and **Edit** permissions for the related issues.

## Guide

1. If you are using *Jira Cloud*, click the **Apps** menu at the top of the screen and under *CONNECTOR FOR SALESFORCE* select **Bulk Operations**.  
   If you are using *Jira Data Center*, click the *CONNECTOR FOR SALESFORCE* menu at the top of the screen **>** **Bulk Operations**.  
   Only users with the **Bulk Change** permission are able to see the menu and access the **Bulk Operations** screen.
2. At the **Bulk Operations** screen, type in your JQL query and click **Search**.

- JQL Query search in Bulk Operation will only return **associated** Jira issues.
- The “ORDER BY’ operation does not work in the **Bulk Operations** JQL search.

1. Results based on your JQL query search are displayed in a table on the screen.  
   If you are satisfied with your JQL Query search, click **Bulk Push** to update the related Salesforce records.

   ![Screenshot of Bulk operations window](/cms_trial/assets/5f48ca24-08f9-42b6-9ff9-ad3239dced09.png)