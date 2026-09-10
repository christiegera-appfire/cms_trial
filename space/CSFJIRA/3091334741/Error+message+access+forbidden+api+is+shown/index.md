# Error message access forbidden api is shown

## Summary

When accessing some of the Connector configuration pages or trying to do a search, an error message "Access Forbidden: API is disabled for this user" is shown.

![contentId-3091334741](/cms_trial/assets/7a4f8a7c-f39f-4baa-b150-8bd31ca75296.png?version=1&modificationDate=1678792074996&cacheVersion=1&api=v2)![contentId-3091334741](/cms_trial/assets/8f753dcf-1978-405c-adc7-f1fe5d844857.png?version=1&modificationDate=1678792075283&cacheVersion=1&api=v2)![contentId-3091334741](/cms_trial/assets/49855a9a-e796-464a-9bd1-7ae2c59a6481.png?version=1&modificationDate=1678792075358&cacheVersion=1&api=v2)

## Environment

- JIRA Cloud

  ​​

## Diagnostics Steps

Check whether the Salesforce user being used for the Authorization has the "API Enabled" option enabled (ticked), either in their Profile or Permission Sets.

![contentId-3091334741](/cms_trial/assets/eb4d8cb4-3129-44f8-a857-96b61548b7a5.png?version=1&modificationDate=1678792075442&cacheVersion=1&api=v2)

## Cause

The Salesforce user being used for connection authorization does not have the "API Enabled" option ticked in their Profile or Permission sets.

## Workaround

Not applicable.

## Resolution

Edit the Salesforce user's Profile or Permission sets to enable the option.