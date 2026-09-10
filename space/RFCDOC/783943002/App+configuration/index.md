# App configuration

The *App configuration* page is accessible from the left pane under the Rich Filters section by clicking **Config** . Only [Jira admins](https://support.atlassian.com/jira-cloud-administration/docs/manage-global-permissions/) have access to this configuration page.

![app configuration options](/cms_trial/assets/f877d51e-0099-4540-bfc3-e257fa96944d.png)

## Permissions

This tab gives access to the following settings:

- **Creating rich filters**: select who can create new rich filters (this includes the right to copy existing rich filters). This permission can be granted to *All logged-in users* (the default option) or to specific Jira groups.
- **Managing rich filters**: Grant additional user groups the *admin permission* over all rich filter objects, including the ability to edit or delete any rich filter, even without explicit assignment. Jira admins always retain this permission by default.
- **Bulk operations on rich filters**: Select who is allowed to perform bulk operations on rich filters. Authorized users can only perform bulk operations on the rich filters for which they have the *admin permission*.
- **Exporting rich filter gadget results**: Select who is allowed to export results displayed by rich filter gadgets (this applies to all export types—PDF, Excel, CSV). This permission can be granted to *Anyone* (the default option) or specific Jira groups. Authorized users can only export results they have access to, i.e., results they can see in dashboards.

See [Rights and Permissions](/cms_trial/space/RFCDOC/783941839/Rights+and+Permissions/) for more details about these settings.

## Delete all app data

This tab lets you easily delete all your data in the *Rich Filters for Jira Dashboards* app. You may wish to do this before uninstalling the app on an instance where you will not use it anymore or to reset the app and start over.

The app data deletion covers the rich filter objects and the permissions configured in the app. Dashboards and gadgets that use rich filters are not stored in the app but directly in Jira, so this operation does not delete them. However, these gadgets will stop working after the deletion since the rich filters they rely on will no longer exist.

There is a one-week delay between initiating the deletion and performing it. A Jira admin can abort the deletion at any time during this period. The app cannot be used while the deletion is pending. It becomes usable again after the deletion is completed or aborted.

The process is straightforward and thoroughly explained in the app itself. At any given time, the app can be in one of three states:

- normal operation
- app data deletion is pending (one week) – a Jira admin has initiated the deletion process, but the actual deletion hasn't yet started
- app data deletion is ongoing (seconds to a few minutes) – the app is automatically deleting the data, and the operation cannot be aborted anymore

To initiate the data deletion process, read carefully the information provided, then click **Delete all app data**.

![image-20240516-151735.png](/cms_trial/assets/d03424f8-17f4-4518-9018-6585a679053c.png)

A confirmation dialog will appear. Follow the instructions to initiate the deletion process. Once the process is initiated, while the deletion is pending, the app cannot be used except to monitor and, if necessary, to abort the deletion process. This can be done by any Jira admin on the same page, which then looks like this:

![image-20240516-151828.png](/cms_trial/assets/951d0321-d1ca-4e68-a75a-572d0a380091.png)

While the deletion is pending, if you need to abort the process, click the **Abort deletion** button and confirm your choice in the confirmation dialog that appears. In that case, the data will not be deleted, and the app will return to normal operation.

If the deletion is not aborted, at the end of the one-week delay, the app will automatically delete the data and return to normal operation without any configuration (except for the dashboards and their rich filter gadgets, which are stored in Jira—these gadgets will not work anymore and will need to be deleted or reconfigured).

**Your data after the app is uninstalled**

Suppose you haven't manually requested the app data deletion after you uninstalled the app. In that case, your data will be stored for a limited period of time (between 4 and 6 months), after which it will be automatically deleted. If you reinstall the app during this period, you will still find your data (the rich filter objects and the permissions configured) and can continue to use the app normally.