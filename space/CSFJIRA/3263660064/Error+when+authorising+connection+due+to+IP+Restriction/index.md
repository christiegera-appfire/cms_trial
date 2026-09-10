# Error when authorising connection due to IP Restriction

## **Summary**

This article addresses the issue when establishing a connection between Salesforce and Jira Cloud using the Connector for Salesforce & Jira due to "Restricted IP" status. It covers scenarios where Salesforce security settings (Login IP Ranges or Network Access) block the connection attempt.

## **Environment:**

- **Platform:** Jira Cloud / Salesforce
- **Version:** All Cloud versions

## Problem

When authorizing the connection, the following error appears: “This is probably not the page you were looking for”

![image-20260622-032214.png](/cms_trial/assets/ccad2356-3366-494c-9b4a-b7c1a9ce4a56.png)

Checking through the **Login History** of the user account used for the authorization, the **Status** shows as **Restricted IP**.

![image (6)-20260622-033136.png](/cms_trial/assets/46906721-9052-48e5-9b44-b9766d537409.png)

## Cause

The issue is typically caused by Salesforce-side security configurations that restrict access based on IP addresses. Even if the Connector app is correctly installed, Salesforce may block the incoming request if:

1. The **Salesforce User Profile** used for the connection has specific **Login IP Ranges** defined that do not include the user's current IP address.
2. The Salesforce **Network Access** settings (Trusted IP Ranges) are restricted.

For Jira Cloud instances, there is no requirement to manually whitelist IP addresses for the app itself beyond standard installation.

## Solution

After ensuring the remote site is added as per <https://support.appfire.com/space/CSFJIRA/1873412619/Add+new+remote+site> article, follow the steps below:

### 1. Check User Profile Login IP Ranges

If the Salesforce user used for the integration has restricted IP ranges, the connection will be blocked.

1. Log in to Salesforce as an Administrator.
2. Go to **Setup** > **Users** > **Users**.
3. Click on the name of the **affected user** (the one used for the Jira-Salesforce connection).
4. Click on the user's **Profile**.
5. Scroll down to the **Login IP Ranges** section.
6. **Action:**

   - If ranges are configured, you must add the IP address mentioned in the previous **Login History** to the list.
   - Alternatively, if these restrictions are not required for your organization's security policy, remove the ranges to allow access from all IPs.

### 2. Check Network Access / Trusted IP Ranges

Check if there are global network restrictions in Salesforce.

1. Go to **Salesforce Setup** > **Security** > **Network Access**.
2. Review the **Trusted IP Ranges**.
3. **Action:** Ensure the IP address shown in the previous **Login History** is within a trusted range

## **Related articles**

- <https://support.appfire.com/space/CSFJIRA/3091334997/Page+cannot+be+found+when+I+try+to+re-authorize+connection+with+Salesforce>