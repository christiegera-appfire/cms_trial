# Jira custom field limitations

With recent Atlassian API changes, you may encounter the following limitations when working with Jira custom fields.

### **Field values appear empty**

Limitation description If you add Jira custom fields to the view, their values will appear empty. This happens because the custom fields aren’t included in the relevant Jira screen.

![Screenshot of adding a field to the column view in Foxly.](/cms_trial/assets/774955c7-a0ba-4aa2-8178-0d2ee0db0b6c.png)

### Priority score can’t be calculated

Limitation description If you’re using a prioritization template with metrics linked to Jira fields, the priority score won’t be calculated unless those fields are added to appropriate Jira screens.

In **Configuration**, you can check what prioritization template is in use and see if metrics are based on Jira fields.

![Screenshot of the Configuration page in Foxly.](/cms_trial/assets/08bf6790-2dad-49b7-95d8-1ed675b7c447.png)

### Solution

To resolve the above limitations, add the required fields to the appropriate Jira screens. See full instructions in the [Add a field to a screen](https://support.atlassian.com/jira-cloud-administration/docs/add-a-custom-field-to-a-screen/) Jira article.

If you can’t access Jira settings, contact your Jira admin.

Once the necessary fields are added to Jira screens:

- The values of Jira fields added to the column view will be visible.
- The priority score will be calculated when a prioritization template based on Jira fields is in use.