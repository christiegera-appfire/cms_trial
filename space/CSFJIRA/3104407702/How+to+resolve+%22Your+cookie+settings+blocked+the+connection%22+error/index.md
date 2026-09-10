# How to resolve "Your cookie settings blocked the connection" error

## Summary

After you [Set up a connection to Salesforce](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754669) and click **Authorize**, you are redirected to `sfjc.integration.appfire.app`, and the `Your cookie settings blocked the connection error` is displayed. From here, click **See how to adjust your browser settings** to open this document page, or click **Contact support** to open our support portal.

![Connector for Salesforce & Jira cookie settings blocked connection error dialog](/cms_trial/assets/0bd2262b-fd59-43a8-8b60-e9b1c40c2de4.png)

## Environment

- Jira version: All
- Add-on version: All

## Cause

This error is caused by a setting in the browser that blocks third-party cookies.

## Resolution

To fix the issue, please ensure the following setting is disabled in the browser settings:

- In *Google Chrome*:

  1. Click **Customization**▢> **Settings**.
  2. Under the *Privacy and security* section, click **Cookies and other site data**.
  3. Ensure the **Block Third Party Cookies** option is not selected (unchecked).

     ![Chrome Privacy and Security settings with Block Third Party Cookies option](/cms_trial/assets/bed9b0e1-1c5b-4559-830c-8957219e38c1.png)
- In *Safari*:

  1. Go to **Preferences** (Command + ,) > **Privacy.** Uncheck the **Prevent cross-site tracking** option.

     ![Safari Privacy preferences with Prevent cross-site tracking option](/cms_trial/assets/1b534178-9e73-40f4-90f0-75c858a0a421.png)