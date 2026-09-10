# Jira custom field limitations (Priorities module)

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

With recent Atlassian API changes, you may encounter the following limitations in the Priorities module when working with Jira custom fields.

### **Field values appear empty**

Limitation description If you add Jira custom fields to the view in the Priorities module, their values will appear empty. This happens because the custom fields aren’t included in the relevant Jira screen.

![Screenshot of the Business Value column added to the view in the Priorities module. ](/cms_trial/assets/5e4383f5-29bb-4dd0-b608-f05012323699.png)

### Priority score can’t be calculated

Limitation description If you’re using a [prioritization template with metrics linked to Jira fields](/cms_trial/space/SPM/1918506690/Create+new+prioritization+templates/), the priority score won’t be calculated unless those fields are added to appropriate Jira screens.

![Screenshot of a situation when the priority score can't be calculated in the Priorities module.](/cms_trial/assets/6a4e0c25-b504-4186-80af-6daaab5c344d.png)

In **Configuration**, you can check what prioritization template is in use and see if metrics are based on Jira fields.

![Screenshot presenting metrics based on Jira fields in the Priorities module. ](/cms_trial/assets/73e78c69-1a99-4ff0-8f10-c4bdbdaae464.png)

### Solution

To resolve the above limitations, add the required fields to the appropriate Jira screens. See full instructions in the [Add a field to a screen](https://support.atlassian.com/jira-cloud-administration/docs/add-a-custom-field-to-a-screen/) Jira article.

If you can’t access Jira settings, contact your Jira admin.

Once the necessary fields are added to Jira screens:

- The values of Jira fields added to the column view will be visible.
- The priority score will be calculated when a prioritization template based on Jira fields is in use.