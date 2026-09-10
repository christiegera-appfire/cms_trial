# Salesforce Objects are not loading after configuring Connection

## Summary

After configuring the Salesforce Connection in JIRA, the Salesforce Objects are not loading:

![contentId-3091368118](/cms_trial/assets/a76f41e5-8d7b-43f0-806e-cffdb2cb35ed.png?version=1&modificationDate=1678857296741&cacheVersion=1&api=v2)

## Environment

JIRA Cloud

Chrome browser.

## Diagnostics Steps

Not applicable.

## Cause

Chrome browser prevents websites from saving and reading cookie data.

## Workaround

Not applicable.

## Resolution

Disable "Block Third Party Cookies" in Chrome setting:

1. On your computer, open Chrome ▢.
2. At the top right, select **More**▢ **Settings**▢.
3. Select **Privacy and security > Third-party cookies.**
4. Select **Allow third-party cookies**.

Learn more about cookies: [turn cookies on or off.](https://support.google.com/accounts/answer/61416?hl=en&co=GENIE.Platform%3DDesktop)