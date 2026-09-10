# Error on Apex Trigger with CPQ Enabled

## Summary

When deploying an Apex trigger from sandbox to production, an error similar to the following appears:

![contentId-3092055716](/cms_trial/assets/b9235317-198e-496a-820d-645711b68d57.png?version=1&modificationDate=1678792050254&cacheVersion=1&api=v2)

## Environment

- JIRA Server

## Diagnostics Steps

Not applicable.

## Cause

This may be due to CPQ's package trigger being enabled.

## Workaround

Not applicable.

## Resolution

There is an option in the CPQ managed package to disable the triggers. Try to disable the triggers in Salesforce's sandbox and run the test class again.

You can do so with these steps:

1. Click **Setup** > **Installed Packages** > **Salesforce CPQ**.
2. Then click **Configure** > **Additional Settings** > **Triggers Disabled**.

Note: You may have to log out and log back in.

![contentId-3092055716](/cms_trial/assets/8d9636f5-de4d-4972-87cd-9ac218a81cb8.png?version=1&modificationDate=1678792050329&cacheVersion=1&api=v2)