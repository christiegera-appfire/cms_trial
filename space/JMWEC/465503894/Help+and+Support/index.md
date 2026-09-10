# Help and Support

This section details the troubleshooting and support options provided for the *Jira Misc Workflow Extensions* add-on and is applicable to Jira admins.

If one of the post-functions provided by the *Jira Misc Workflow Extensions (JMWE)* add-on does not seem to be working as you would expect, follow these steps:

1. First, check for error messages on the issue view right after triggering the transition. If any of the post-functions configured on the triggered transition fails with any error, JMWE displays a message with a link to the error log. **Note**: this message is visible only to the admins and is not visible on Jira Software boards and Jira Service Desk customer portals.
2. Second, check if there are currently any known outages or major incidents affecting the add-on. Active incidents are visible automatically on the [status page for the JMWE add-on](https://innovalog.statuspage.io). See below for more information.
3. Third, you should head to the post-function view screen to see the count of errors and warnings that occurred over the past 24 hours for that post-function. Clicking on the errors or warnings will direct you to the [JMWE Logs](/cms_trial/space/JMWEC/466321741/JMWE+Logs/) page under the **Add-ons** section, which will give you detailed information on the errors and warnings for the specific post-function. In general, you can access the add-on logs on this page for errors or warnings you might have overlooked. If there are any errors or warnings, you can download the logs and investigate the errors.
4. Fourth, you can search our [Knowledge Base](/cms_trial/space/JMWEC/465241585/Knowledge+Base/) and refer to the [Atlassian Community](https://community.atlassian.com/t5/tag/addon-com.innovalog.jmwe.jira-misc-workflow-ex/tg-p) website for existing answers to any issues. You can also [ask the community](https://community.atlassian.com/t5/forums/postpage/choose-node/true/interaction-style/qanda?add-tags=addon-com.innovalog.jmwe.jira-misc-workflow-ex,jmwe) for help with your specific problem, especially if you are looking for a solution to a specific use case.

Lastly, if you believe you are running into a bug in the JMWE add-on, or if you would like to suggest a new feature, don't hesitate to [raise a support request](https://appfire.atlassian.net/servicedesk/customer/portal/11) with us.

### Automated error checking

Another special notification appears on this page when there are any errors detected in your logs that are related to Permission Schemes and/or some Issue Security Schemes.

### Errors or/and warnings detected in your logs

If errors and/or warnings are detected in your logs, a message box will appear on the Troubleshooting and Support page, after a slight delay. If you click on one of the numbers, the corresponding errors or warnings will start downloading.

**reset counters** : Clicking on this link will reset the error and warnings counters, after which only new errors or warnings (appearing after the reset) will be taken into account. Thus, next time you visit this page, the message box will only appear if new warnings or errors are detected.

## Accessing the Innovalog status page

You can access the status page for the JMWE for Jira Cloud add-on here: <https://innovalog.statuspage.io> .  This page helps in keeping you informed about outages and major incidents, if any, in the add-on.

You can subscribe to updates to this page to be notified via Email or SMS whenever a new incident is reported.