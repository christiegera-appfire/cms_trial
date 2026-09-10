# Jira Issues and Comments components are blank and Create/Associate buttons are not available

## Summary

When accessing a Salesforce Record, the **Jira Issues** and **Comments** components are shown blank. The usual **Create**/**Associate** buttons are also not available.

![contentId-3092024364](/cms_trial/assets/05b7bec7-5e83-458c-a063-f86eff3c3990.png?version=1&modificationDate=1678795886250&cacheVersion=1&api=v2)

## Environment

- Any Connector for Salesforce & Jira version
- Any Jira version

## Diagnostics Steps

Using the browser developer tools (press F12), check the Console for any CORS-related error. For example:

```text
Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at <salesforce_url>. (Reason: CORS header 'Access-Control-Allow-Origin' does not match '<salesforce_url>'.
```

## Cause

The problem is caused by a Salesforce update called "Enable Secure Static Resources for Lightning Components". More information about this update can be found on the Salesforce site below:

- <https://help.salesforce.com/s/articleView?id=release-notes.rn_lc_secure_static_resources_update.htm&type=5&release=232>

As of this KB's creation (6th Sept 2021), Salesforce has postponed the update and has suggested not enabling it.

## Workaround

Not applicable.

## Resolution

Disable the update with the steps below:

1. Navigate to **Salesforce Setup** > **Release updates** > **Archived** tab.
2. Look for Enable Secure Static Resources for Lightning
3. Click **View Update**.
4. Then click **Disable Test Run** to disable it.

An example screenshot after disabling:

![contentId-3092024364](/cms_trial/assets/0e1c37b0-5f78-4522-be71-1305f4067dcb.png?version=1&modificationDate=1678795886394&cacheVersion=1&api=v2)