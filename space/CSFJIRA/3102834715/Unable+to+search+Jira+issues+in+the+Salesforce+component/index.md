# Unable to search Jira issues in the Salesforce component

## Summary

Searching for Jira issues doesn't populate any results neither in the Salesforce Visualforce page nor in the Jira Issues component.

![contentId-3102834715](/cms_trial/assets/fd9740ce-44ea-4795-847d-4110dca9faae.png)![contentId-3102834715](/cms_trial/assets/b62828a0-22fa-4548-a69a-135ce9ca2d12.png)

## Environment

- Jira Cloud

## Cause

The integration user has to have the **Browse Project** permission granted to **all** of the bound projects.

## Resolution

Ensure that all of the bound projects (**Jira icon > Salesforce > Bindings**) have been granted the **Browse Project** permission.