# Use JQL to report on Jira issues with associations

Associations made with Salesforce from Jira are recorded in the issue's fields. This guide explains how those fields can be viewed and used as [Jira Query Language (JQL)](https://support.atlassian.com/jira-software-cloud/docs/what-is-advanced-searching-in-jira-cloud/) filters for reporting purposes.

This feature uses the following Jira fields when the application is installed:

- Associations - displays a list of associated Salesforce records.
- Association Count - displays the amount of associated Salesforce records.

For the application to be able to populate and update the **Associations**and **Associations Count** fields, they should be added to the *Edit Issue* Screen. An administrator is required to configure the fields in the project settings.

- If the fields are not added to the **Edit Issue Screen**, they cannot be updated.
- If the fields are added to the **View Issue Screen**, they are editable and can be edited manually. We recommend removing these fields from the *View Issue* screen and avoiding updating them manually.
- If the fields are updated manually, the application will sync them again when the next association-related action occurs.

For more information regarding screen configuration, refer to [Configure the issue detail view](https://support.atlassian.com/jira-software-cloud/docs/configure-the-issue-detail-view/).

You can use these fields to search Jira issues through the issue navigator. For example, to search for issues associated with a specific Salesforce record or issues with a specific number of associations.

## Version differences

### Jira Cloud

By default, the fields are empty; they will be populated on the following association-related actions (eg, issue being associated).

| **Jira** | **Salesforce** |
| --- | --- |
| A Salesforce record is created for the issue. | A Jira issue is created for the record. |
| A Salesforce record is associated with the issue. | A Jira issue is associated with the record. |
| The issue is unassociated (unlinked) from a Salesforce record. | The record is unassociated (unlinked) from a Jira issue. |
| A Salesforce record is created (and associated with the issue) through workflow post-function. |  |

### Jira Data Center

- If the **Associations** and **Associations Count** custom fields are not created, disable and enable the app.
- Configure the field configuration and update renderers for **Associations** field to Wiki Style Renderer to avoid the field context looking broken.

By default the fields are empty, but they will be populated when the Jira Issue is updated and if there is an association for the issue.

| **Jira** | **Salesforce** |
| --- | --- |
| A Jira issue is updated. |  |

## Creating an association

1. Open a Jira issue from a project that is bound with Salesforce. You can see the **Associations**and **Associations Count**fields are empty.

   ![contentId-3092219354](/cms_trial/assets/9464d33e-1dde-4470-bc96-7d5843de54a5.png)
2. If they are already populated, go to the next step. Otherwise, to populate those fields, check out [Configuring an association](/cms_trial/space/CSFJIRA/3091956652/Configure+an+association/) on how to create an association between Jira issues and Salesforce.

   ![screenshot of populated fields,](/cms_trial/assets/c85fb7d6-87e8-4307-8913-4b184c3f3cad.png)

If the association has been created before this feature was implemented, the Associations and Association Count fields will still be empty despite having an association. You will have to [Create a Salesforce record from Jira](/cms_trial/space/CSFJIRA/3091465546/Create+a+Salesforce+record+from+Jira/) or [Configure a new association with a Salesforce](/cms_trial/space/CSFJIRA/3091956652/Configure+an+association/) record.

We recommend unlinking the existing association and linking it back again to trigger the update for the *Associations* and *Association Count* fields.

## Use JQL to filter association fields

1. In Jira, select **Filters** > select **Advanced issue search**.
2. Next, select **More**> check **Associations** and **Association Count** options. Filter the other fields relevant to your report.

   ![screenshot of Associations and Association Count options](/cms_trial/assets/dd78b7bd-ce35-4e01-aa7d-45dd637eceb2.png)
3. Search for work item associated with a Salesforce record with a specific Object ID.

   ![Screenshot of Search for work items with association](/cms_trial/assets/35cd4d85-2e52-4265-9e41-946eaed62ba4.png)
4. Search for work items with specific counts of association.

   ![Screenshot of Search for work items association count](/cms_trial/assets/d4ddc1f5-7f63-49f3-81a3-4aebede86ff8.png)

## Related information

- [Create a Salesforce record from Jira](/cms_trial/space/CSFJIRA/3091465546/Create+a+Salesforce+record+from+Jira/)
- [Configure an association](/cms_trial/space/CSFJIRA/3091956652/Configure+an+association/)