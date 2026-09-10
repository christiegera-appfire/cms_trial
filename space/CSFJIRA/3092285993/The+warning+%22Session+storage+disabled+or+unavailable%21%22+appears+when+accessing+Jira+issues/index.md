# The warning "Session storage disabled or unavailable!" appears when accessing Jira issues

## Summary

When opening a Jira issue, the following message appears on the screen:

![contentId-3092285993](/cms_trial/assets/28d694ae-314c-4bc5-a64a-32a5b4a62daf.png?version=1&modificationDate=1678796155982&cacheVersion=1&api=v2)

## Environment

- Chrome browser

## Diagnostics Steps

Not applicable.

## Cause

This happens when a user enables the "Block third-party cookies" settings in Chrome (or a similar setting in other browsers).

## Workaround

Not applicable.

## Resolution

1. On your computer, open Chrome.
2. At the top right, click the vertical ellipsis **> Settings**.
3. Scroll down to **Privacy and security**, and click **Cookies and other site data**.
4. Select the option “**Allow all cookies**" or add [sfjc.integration.appfire.app](https://sfjc.integration.appfire.app/) under "**Sites that can always use cookies**".

sfjc.integration.appfire.app is an intermediary server that transfers data between Jira and Salesforce.  For more info, please refer to [Security statement](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754905/Security+statement).