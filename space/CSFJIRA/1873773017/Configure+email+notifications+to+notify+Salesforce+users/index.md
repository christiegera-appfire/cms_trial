# Configure email notifications to notify Salesforce users

It is possible to configure a connection to send email notifications to all Case owners from Salesforce whenever a Jira comment is created or updated.

## Configure email notifications

1. Select **Apps** from the left sidebar in Jira.
2. Next to *Connector for Salesforce,* click **Menu** (▢) > **App settings**.

   ![Appsettings.png](/cms_trial/assets/9892acbf-a412-44f8-8814-b63decd03be9.png)
3. Under *Connector for Salesforce*, click **Connections**.
4. Choose the connection to configure, then under *Operations*, click **Configure**.
5. Scroll down to *Salesforce Notification Settings* and toggle **Simple Email Notification** to enable the feature.

   ![ae4ce806-633c-4842-9e5b-242f363255c4.png](/cms_trial/assets/54bf14f5-cdbf-4048-8eae-89915be53fe2.png)
6. Select a **Sender Type.**  
   The email address used as the email's *From* and *Reply-To* addresses can be one of the following:

   - **Current User:** The email address of the user running the flow. For example, the Salesforce user who has authorized the Salesforce Connection in Jira.
   - **Default Workflow User:** The email address of the default workflow user of the Salesforce organization.
   - **Organization-Wide Email Address:** A specific organization-wide email address that needs to be specified in **Connection Configuration**.
7. If the **Sender Type** is set to *Org-Wide Email Address*, enter the address of the organization-wide email. Otherwise, this field is not required.
8. Scroll to the bottom of the page and click **Apply Changes** to save your settings.

For more information on configuring **Organization-Wide Email Addresses**, consult the [Salesforce documentation](https://help.salesforce.com/articleView?id=emailadmin_manage_orgwide_email_addresses.htm&type=0).

## Email format

An email is sent out to Case owners.

![example of email format after configuration in Salesforce](/cms_trial/assets/3c15d84c-5edf-4d14-a0dd-b27d4e49c0fe.png)

- The email has a fixed format.
- The email subject is similar to Jira emails that are sent out for comments and issue update notifications.

## Conditions and limitations

For the notification emails to be sent out, the following must be true:

- The connection to Salesforce is properly authorized.
- Case objects are supported.
- The `Notify by Simple Email` flag is enabled for the connection.
- A valid sender is configured.

For a comment creation or update to trigger the notification email:

- The issue the comment belongs to must be associated with at least one Case record in Salesforce.
- The association is not *view only* (for example, it is a synchronized association).
- The body of the comment (created or updated body) satisfies existing Jira Comment Privacy filters (Show All, Viewable by All Users). Currently, this configuration is only visible on the Salesforce package configuration page.

Comments with visibility restricted to a Jira project role do not trigger a notification email to prevent disclosure of role-restricted content.

- The body of the comment satisfies existing Jira Comment Tag filters. Currently, this configuration is only visible on the Salesforce package configuration page.

### Known limitations

- The email body is in plain text. HTML is currently unsupported. This is a known limitation of the Salesforce `simpleEmail` API.