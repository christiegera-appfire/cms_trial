# Troubleshooting Email issue post-function configuration

If the Email issue post-function fails to send emails to the specified recipients here are a few things to look out for:

1. The user executing the post-function (by default the current user) will not receive any notification unless they select the "Notify me of my changes" option on their User Preferences page. Make sure that you enable to option to receive notifications.
2. To use the “Email addresses” option in the post-function configuration you will need Jira Service Desk in your instance. Using this option you can send emails to explicit email addresses. A new Service Desk Customer will be created for each email address and they don't count towards your license.