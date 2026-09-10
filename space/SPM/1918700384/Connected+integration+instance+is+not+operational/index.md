# Connected integration instance is not operational

If you can see this message, there is a communication problem with the connected integration instance.

![contentId-1918700384](/cms_trial/assets/6bb24219-7b1f-4e12-9737-6dce8354893f.png)

As a result, tasks from this platform will not be displayed to prevent them from being modified locally.  
The above situation may be due to the following:

1. **Instance connection issues** (your Jira/Trello can't connect)

   - Can't add new integration → incorrect authorization data (e-mail address, organization name, access token, etc).
   - The default user has been removed from the connected integration instance or has lost permission in the connected integration.
   - There are prolonged and persistent problems with the connection to the integration instance.
   - The administrator has manually deactivated the integration instance.
2. **Synchronization issues** (synchronization cannot happen for reasons related to the scope definition of a Box - something no longer exists OR permissions lost):

   - Scope element removed or permissions changed (e.g., a Jira project was in the scope of a Box. A Jira project has been removed. The Box will try to synchronize with Jira but will fail)
   - Scope owner doesn't exist or has lost permissions

Troubleshooting the connected integration instance requires BP administrator privileges.  
If you do not have such permissions, please ask the BP administrator for assistance.

The solutions to the above problems are described in this article: [Connection warnings for integrations](https://appfire.atlassian.net/wiki/spaces/DLP/pages/296850528).