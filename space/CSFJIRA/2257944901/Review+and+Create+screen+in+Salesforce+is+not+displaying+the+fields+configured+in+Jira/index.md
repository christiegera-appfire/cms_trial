# Review and Create screen in Salesforce is not displaying the fields configured in Jira

## Summary

When creating a Jira Issue from the Salesforce Lightning Component or the Visualforce Page, there is a button to allow you reviewing the information before creating the ticket.

However, even after setting up the fields in the appropriate screen in Jira, those fields are not rendered into the Salesforce component.

## Environment

- Jira Cloud
- Jira Data Center

## Diagnostics Steps

The field can be found on the screen by performing the following:

1. Click **Create** to open the *Create Issue* screen on your Jira site.
2. Click the Menu icon▢on the top right corner of the *Create Issue* screen.
3. Select **Find your field**and type the field name. After finding the field, you will see the following error:

![contentId-2257944901](/cms_trial/assets/50eacaac-4a3b-451a-a41d-3a327bf501a9.png)

## Cause

The administrator has set up a custom field, but the affected project and issue type are not linked to it.

## Workaround

Not applicable.

## Resolution

In order to allow the users to interact with this field on the screen in Jira (the equivalent of the Salesforce's *Review and Create* screen), the administrator must add the missing project and issue type to the field context:

1. Go to your **Jira**site.
2. Click **Settings** (▢) > **Work items**.
3. In the left tab, search for the **Fields** section > select **Fields**.
4. Search for your field **>**click the **Menu** icon▢**> Contexts and default value**.
5. Click **Edit Context**.
6. Select the affected project and issue type.
7. Select **Modify** to save changes.