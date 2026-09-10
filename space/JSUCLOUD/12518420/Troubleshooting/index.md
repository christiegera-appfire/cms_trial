# Troubleshooting

This is general troubleshooting information. Refer to the relevant documentation if you have a problem with a particular component (post function, validator, or condition). For help with error messages in the Execution Log, see the [Guide to JSU error messages](/cms_trial/space/JSUCLOUD/290194210/Guide+to+JSU+error+messages/). If you have read the documentation, analyzed your log files, and tried different configurations but are still having issues, submit a [support request.](https://appf.re/support)

## Functionality not working

In rare cases, Jira has difficulties enabling JSU. Usually, this can be solved by uninstalling/re-installing, resetting, or reloading.

We recommend checking the following:

- Manage add-ons: Is the JSU app enabled?
- Reinstall the app.

## 'Anonymous' user

JSU's functionality is only supported for logged-in users.

## Re-install JSU

Have you tried to remove JSU and reinstall it?

You can remove and reinstall JSU without losing any of your JSU configurations. All implemented features stay in your workflows and will be available again after re-installation.

**To remove JSU from your Jira instance:**

1. Log in as a Jira Administrator.
2. Select the **Settings** cog,then select **Apps**.
3. In the left sidebar, select **Manage apps** to view all apps installed on your Jira instance.
4. Select the JSU app to display the app details.
5. Select **Uninstall**. The information summary displays an *Uninstalling* message, and the app will be removed from Jira.