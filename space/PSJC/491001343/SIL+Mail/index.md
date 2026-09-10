# SIL Mail

## Problem

Steps to follow when the `sendEmail()` function is not working.

## Configuring an SMTP email server

For instructions on configuring an SMTP server on Jira, please see this Atlassian documentation on:

[Configuring an SMTP mail server](https://confluence.atlassian.com/adminjiraserver079/configuring-an-smtp-mail-server-to-send-notifications-950288926.html).

## Sending a test email from Jira

Test that you can send an email from Jira by sending a test message. See this Atlassian documentation for further details:  
[How to send a Test Email in JIRA](https://confluence.atlassian.com/jirakb/how-to-send-a-test-email-in-jira-317197303.html)

## Troubleshooting a Gmail account

If you have Gmail configured as your SMTP mail server, you may need to change some settings on your Gmail account.

1. Enable **less secure** apps. For more information, see this Google documentation on [Less secure apps & your Google Account](https://support.google.com/accounts/answer/6010255?hl=en)
2. Unlock your Gmail account.

While you may be able to access your Gmail account, chances are it has been locked for use by third-party apps (in this case, Jira) due to excessive logins. See this Google documentation on unlocking a Gmail account: [DisplayUnlockCaptcha](https://accounts.google.com/DisplayUnlockCaptcha)

## sendEmail() troubleshooting

Try using a simple script to test that the configuration is set up correctly and that sendEmail() works as expected.

**Example sendEmail() code**

|  |
| --- |
| sendEmail("first.last@example.com", "subject", "body"); |

## null sender

If this does not work, the first thing to check is that the mail configuration is set up correctly. Check that the "Send mail via" option has a "sender" option selected. See this screenshot from the documentation:

![Power Scripts for Jira Cloud new script creation interface](/cms_trial/assets/99f5a2f8-3e27-45ff-8588-930705880341.png)

The most common error in configuration is that **Null sender** (the default option) is selected. It is suggested to select **Container sender** as this uses the least amount of system resources. For more information, see this Power Scripts documentation on [mail configuration](/cms_trial/space/PSJC/490996015/Outgoing+Mail+configuration/).

## Getting support

If these troubleshooting steps do not work, create a support request on our [Power Scripts Service Desk Portal](https://apps.appf.re/PSJ/support). Include the following information:

- Any error messages in the Jira system logs.
- Any screenshots of the Mail configuration.

To see the system logs, click **Load log** at the bottom of the SIL Manager. The logs are also available by navigating to `<JIRA_HOME>/logs/atlassian-jira.log`