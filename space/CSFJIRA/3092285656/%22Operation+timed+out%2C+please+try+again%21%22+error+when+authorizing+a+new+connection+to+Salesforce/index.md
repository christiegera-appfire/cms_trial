# "Operation timed out, please try again!" error when authorizing a new connection to Salesforce

## Summary

When performing the authorization to a new Salesforce connection, clicking "Authorize" triggers the following error:

![contentId-3092285656](/cms_trial/assets/6747155a-e252-4572-a07e-56a4d2c21718.png?version=1&modificationDate=1678796165719&cacheVersion=1&api=v2)

## Environment

- Jira Cloud
- Jira Data Center

## Diagnostics Steps

Not applicable.

## Cause

When the administrator sets up a connection to a Salesforce Government Cloud instance, the following options can be viewed during the authorization phase:

- Production: <https://login.salesforce.com/setup/connect/>
- Sandbox: <https://test.salesforce.com/setup/connect/>

Salesforce Government Cloud handles a different set of URLs to authenticate users, it's not possible to authorize new connections from the Salesforce Connector app to this version of Salesforce.

## Workaround

Not applicable.

## Resolution

These login options are not available for Salesforce Government Cloud.

This edition of Salesforce uses another URL for login, along with a different set of IP addresses.

For more information on the login information, refer to this documentation:

- [Login tips and considerations for Salesforce Government Cloud](https://help.salesforce.com/s/articleView?id=000331188&type=1)