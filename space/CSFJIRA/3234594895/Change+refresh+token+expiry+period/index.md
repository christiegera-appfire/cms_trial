# Change refresh token expiry period

## Overview

Salesforce enforces a mandatory 30-day maximum on the idle refresh token TTL (time-to-live) for connected apps. This is a platform-wide security enforcement that affects all connected app integrations, including Connector for Salesforce & Jira Cloud.

If a Salesforce connection goes unused for 30 consecutive days, the refresh token expires, and you must reauthorize the connection. Each time the token is used within that 30-day window, the inactivity timer resets automatically (sliding window behavior).

30 days is the maximum — not the default. You can set the idle expiration period to less than 30 days, but you cannot exceed the 30-day maximum. Salesforce enforces this limit regardless of what your connected app policy previously specified.

For full details on Salesforce's enforcement, see the [Salesforce documentation](https://help.salesforce.com/s/articleView?id=xcloud.connected_app_limit_idle_ttl.htm&language=en_US&type=5).

## Before you start

Make sure you have:

- Administrator rights in Jira - only administrators can revoke the connection

## Configure the refresh token expiry period

1. In Salesforce, click the gear icon (▢) in the upper right corner and select **Setup**.
2. In the **Quick Find** box, type `Connected Apps`.

   ![Salesforce Setup page showing the Quick Find field and the Edit field highlighted.](/cms_trial/assets/5f244f99-87c9-4884-8bc6-73038df066e5.png)
3. From the results, click **Manage Connected Apps.**
4. Click **Edit** next to *Salesforce & JIRA Cloud Connector*.

   ![Salesforce Connected Apps page with the Expire refresh token option highlighted.](/cms_trial/assets/6c00f745-ea3d-4e3a-bf5d-220bb6f2e3a8.png)
5. Under the *OAuth Policies* section, find the **Refresh Token Policy** field.
6. Set the idle expiration to **30 days** or fewer based on your security requirements.
7. Click **Save.**

## Handling an expired connection

If a connection expires due to inactivity, you must reauthorize it. For step-by-step instructions, see [Revoke access for an expired connection](/cms_trial/space/CSFJIRA/3224731651/Revoke+access+for+expired+connection/).