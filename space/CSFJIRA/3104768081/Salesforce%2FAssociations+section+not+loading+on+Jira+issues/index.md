# Salesforce/Associations section not loading on Jira issues

## Summary

Salesforce/Associations section not loading on Jira issues:

![Connector for Salesforce panel on Jira issue failing to load associations](/cms_trial/assets/95e78752-b808-40c7-b497-fd48ac011d06.png)

## Environment

- Jira DC

## Diagnostics Steps

Not applicable.

## Cause

Sometimes, the Jira plugins cache can affect the way the Connector works locally in Jira. In this case, the Salesforce/Association fails to load.

## Workaround

Not applicable.

## Resolution

Please clear the plugins cache in Jira by following the steps described below:

- Shut down JIRA
- Delete the following hidden plugin cache directories:

  JIRA\_HOME/plugins/.bundled-plugins JIRA\_HOME/plugins/.osgi-plugins
- Restart JIRA (These directories will be recreated on JIRA reboot with new plugin cache)

Downtime is required.