# What is the difference between "Create" and "Review & Create" buttons?

## Summary

What are the main differences in using the *Create* button vs using the *Review & Create* button?

## Environment

- Jira DC
- Jira Cloud

## Diagnostics Steps

Not applicable.

## Cause

Not applicable.

## Workaround

Not applicable.

## Resolution

When creating a Jira ticket from Salesforce, it's important to take note about the differences between these two buttons which are as follows:

**Create button:**  
When using this button, you have to make sure that all mapped fields have been included in the *Create Issue Screen*in the Jira project settings for the project that you are creating the issue for. If any of the mapped fields is missing from this screen, you will receive an error message like the one shown below:

![contentId-3102867486](/cms_trial/assets/297f4b12-0840-4cf3-97a1-fd45925c634c.png)

**Review & Create button:**  
This button does not require the mapped fields to be added to the *Create Issue Screen* in Jira as the issue will be created successfully.  However, any mapped field that is not included in this screen will not be synced at the time of creation.