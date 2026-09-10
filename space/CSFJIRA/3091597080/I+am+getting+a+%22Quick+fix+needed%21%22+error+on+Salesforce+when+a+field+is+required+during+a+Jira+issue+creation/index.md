# I am getting a "Quick fix needed!" error on Salesforce when a field is required during a Jira issue creation

## Summary

The "Quick fix needed" error message is commonly seen on Salesforce when creating a Jira issue, and when there is an issue associated to the field mappings.

However, sometimes the mappings are correct,d and the issue is instead related to the "Required fields" of the Jira issue we are working with.

![da29c478-2864-4f8e-91e9-8924d5e06457.png](/cms_trial/assets/c9cf9fa9-1a6f-4c83-80d5-5b1dbc9620de.png)

## Environment

- Jira Data Center and Cloud

## Diagnostics Steps

Sometimes this required field is displayed on the screen when creating a new Jira issue, but sometimes this field has not been added to the "Creation screen" yet and therefore not visible. In this case, we will need to add it to this screen first.  
Refer: [Atlassian documentation for Screens](https://confluence.atlassian.com/adminjiracloud/defining-a-screen-776636475.html?__hstc=72543820.fd42b407583c75b9608ead5c74b197cb.1544586047462.1577341352302.1577349894301.790&__hssc=72543820.22.1577349894301&__hsfp=257034439).

## Cause

The required field is not being populated, so the Jira issue is not created, and the "Quick fix needed!" error is seen on Salesforce.

## Workaround

Not applicable.

## Resolution

Please fill in the required field so the Jira issue can be created. If the required field cannot be seen on the "Creation screen," then it will need to be added first.