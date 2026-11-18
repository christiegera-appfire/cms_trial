# JMWE Logs

![admin-JMWELogs.png](/cms_trial/assets/55e1af8e-4147-4dc1-a437-d79d3fceaea5.png)

**Note**: With the [move to Forge](/cms_trial/space/JMWEC/3765207131/October+5%2C+2026/), log access for all third-party apps has moved to Atlassian Administration. This means a few things for JMWE:

1. It is no longer possible to set the logging level specifically for JMWE.
2. To access JMWE logs you will need to download and parse Jira logs external to Jira or JMWE.
3. Lastly, the existing webhook configuration options for sending logs to a webhook have been moved to [JMWE Configuration](/cms_trial/space/JMWEC/466288938/JMWE+Configuration/).

This reflects the current logging capabilities available on the Atlassian Forge platform. We recognize that this may impact your experience and encourage you to review and vote on [ECO-1918](https://jira.atlassian.com/browse/ECO-1918) to help highlight to Atlassian the need for improvements to Forge log functionality.

The **JMWE Logs** administration page (Figure 1, right) only shows select errors and warnings. For access to the complete JMWE logs, see **JMWE logs in Atlassian Admin**, below.

## Log viewer

The logs available in the **Troubleshooting** table can be filtered based on several conditions:

- **Type** - Select Errors, Warnings, or both.
- **Extension** - Filter for logs for a specific JMWE extension.
- **Message** - The system message for the log.
- **Timestamp** - The timestamp for log creation.
- **See more** - Click to view more details from the log, including:

  - **Execution ID**
  - **Timestamp**
  - **Extension**
  - **Location** - Where the specific extension is configured.
  - **Triggered By** - The user account that triggered the extension.
  - **Summary**
  - **Full Message**

## Utilities

Currently, the only log utility available is to delete all JMWE logs.

**Note**: This action cannot be undone!

## JMWE logs in Atlassian Admin

For full access to JMWE logs at any logging level - INFO through ERROR - you must enable logging through Connected apps and then download the logs. To do this, follow these steps:

1. Log in to your instance as an administrator.
2. In the upper right corner, click **Settings** → **Marketplace Apps**.
3. Click **Take me there** to go to Atlassian Administration.
4. Locate **Jira Misc Workflow Extensions** in your list of installed apps and click **View app details**.
5. Under *ANALYTICS AND LOGS*, click **Enable log access**.

After log access has been enabled, JMWE events will be included in the Atlassian log file. Click **Download Logs** to access your Jira logs. You will need to use an external tool to read and parse the log file.