# Connection warnings for integrations

Refer to this article for connection warnings related to Tempo authorization: [Authorization (Jira Cloud)](/cms_trial/space/SPM/1918700384/Connected+integration+instance+is+not+operational/).

## Integration has been manually turned off

**Reason**

The integration has been manually turned off in the App Configuration.

Also, all integrations connected to BigPicture are set as Not operational after their dump is restored on a new instance.

**Solution**

You can turn on an inactive instance by sliding the switch to the Active position.

![image2021-12-2_17-29-36.png](/cms_trial/assets/e7e86c2a-0181-4b01-a62f-e088f5bfefc8.png)

---

## Failed to authorize access to the integration

If the error occurs while connecting an integration

**Reason**

If you are trying to add a new integration, this error means that you provided incorrect authorization data (email address, organization name, access token, etc.).

**Solution**

**For Trello**

Check the information provided on this [page](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297701340).

**For Jira Cloud**

Ensure that the provided data are correct (there is no typo in the HTTPS address of the instance, and a valid e-mail address is used).  
You can also try to create a new API token at <https://id.atlassian.com/manage-profile/security/api-tokens>.

If the error occurs for an already connected integration

**Reason**

The integration has gone into Unavailable mode, although it has already been added. This error means that your access token has expired or been revoked.

**Solution**

**For Trello**

Check the information provided on this [page](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297701340).

**For Jira Cloud**

Create a new API token at <https://id.atlassian.com/manage-profile/security/api-tokens>  and click *Re-authorize*next to the message in the warning window.

---

## Application failed to connect to the integration

If the error occurs while connecting an integration

**Reason**

If you are trying to add a new integration, this error may mean that you entered an invalid URL for the integration or network problems when connecting to an external source.

**Solution**

Check whether the integration URL is entered correctly, the integration is available in your browser, and the network settings are correct (especially the firewall settings).   
If the integration is unavailable, wait until it is available again or consult the integration vendor.

If the error occurs for an already connected integration

**Reason**

For a previously added integration, this error indicates a communication problem with the integration (the integration is not responding, or there is a network problem).

**Solution**

Check the availability of utilities and network settings (especially the firewall settings).   
If the integration is unavailable, contact the integration supplier.

If the integration is available, click the *Re-check connection*button.

---

## The integration instance is throttling the application for making too many requests

If the error occurs while connecting an integration

**Reason**

Too many requests were sent to the integration instance.

**Solution**

Wait about 10 to 15 minutes and try adding the integration again.

If the error persists, get in touch with support.

If the error occurs for an already connected integration

**Reason**

Too many requests were sent to the integration instance.

**Solution**

After waiting a few minutes, click the *Re-check connection*button.

If the error persists, get in touch with support.

---

## Webhooks required by the application are not registered in the integration

**Context**

Webhooks are a mechanism for notifying external applications about changes in the integration (e.g., creating a task or editing a task).

The BigPicture/BigGantt application cannot work correctly without webhooks defined for the integration.

For specific integrations (e.g., Jira Cloud), before adding the integrations to our Application, it is necessary to add the webhooks manually.

Additionally, the mechanism contained in the Application checks whether all webhooks are registered for a given integration.

If the error occurs while connecting an integration

**Reason**

At least one of the necessary webhooks is missing. When adding a new integration, the application prevents it from being added where one of the end webhooks is missing.   
In the case of an existing integration, unregistering one of the necessary webhooks causes the integration to go into the Unavailable state.

**Solution**

Check whether all desired webhooks are registered. If they are not, add them (refer to the information below) and try again.

If the error occurs for an already connected integration

**Reason**

At least one of the necessary webhooks to be registered is missing. When adding a new integration, the application prevents it from being added when one of the end webhooks is missing.   
In the case of an existing integration, unregistering one of the necessary webhooks causes the integration to go into the Unavailable state.

**Solution**

Check whether all desired webhooks are registered and click the *Re-check connection* button.

**Webhook registration process for Jira Cloud instance**

For Jira Cloud, the webhook validation mechanism cannot register the webhooks by itself, so it is necessary to register them following the instructions below.

1. The URL address for which the webhooks must be registered is given in the appropriate window when adding the integration: Jira Cloud: *Settings> System> Advanced> Webhooks.*
2. Click the *Create a Webhook*button.
3. Name: *BigPicture webhooks*
4. Status*: Enabled*
5. URL: *provided in the creation dialog box*
6. Events: *All issues*
7. Check all checkboxes except *Exclude body*.
8. Click the *Create*button.

After creating the webhook, you should see the following information:

![image2021-7-20_14-40-41.png](/cms_trial/assets/d68e093b-6558-40f2-8d8a-eb440a0bf344.png)

---

## The application license is not valid

**Requirements**

The secondary Jira Cloud must have an active BigPicture installation (with a valid license).

**Limitations**

BigGantt is excluded - the setup works only for BigPicture.

---

## Jira license has expired

If the error occurs while connecting an integration

**Reason**

Your license for the Jira integration has expired.

**Solution**

Extend the license for the Jira integration and try adding the integration again.

If the error occurs for an already connected integration

**Reason**

Your license for the Jira integration has expired.

**Solution**

Extend the license for the integration and click the *Re-check connection*button.

---

## Jira administrative permissions are required

If the error occurs while connecting an integration

**Reason**

This error means that the Atlassian-addons-admin group has not been granted administrative rights.   
For the correct operation of the Jira Cloud integration, it is required to grant administrative privileges for the Atlassian-addons-admin group.

It is not possible to grant permissions to this group from the UI level.

**Solution**

Contact the Atlassian support.

After giving administrative privileges to this group, try adding the integration again.

If the error occurs for an already connected integration

**Reason**

This error means that the Atlassian-addons-admin group has not been granted administrative rights.   
For the correct operation of the Jira Cloud integration, it is required to grant administrative privileges for the Atlassian-addons-admin group.

It is not possible to grant permissions to this group from the UI level.

**Solution**

Contact the Atlassian support.

After giving administrative privileges to this group, click the *Re-check connection*button.

---

## Jira is temporarily unavailable

If the error occurs while connecting the integration

**Reason**

Problems with the availability of the integration occur.

**Solution**

Contact the Atlassian support.

After solving the problem, try adding the integration again.

If the error occurs for an already connected integration

**Reason**

Problems with the availability of the integration occur.

**Solution**

Contact the Atlassian support.

After solving the problem, click on the *Re-check connection*button.