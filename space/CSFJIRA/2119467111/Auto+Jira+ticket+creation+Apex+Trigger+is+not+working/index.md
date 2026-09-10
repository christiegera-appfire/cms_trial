# Auto Jira ticket creation Apex Trigger is not working

## Problem

You've followed the automatic Jira issue creation setup guide: [Configure automatic Jira issue creation from Salesforce](/cms_trial/space/CSFJIRA/1873413628/Configure+automatic+Jira+issue+creation+from+Salesforce/), but your Apex Trigger isn't creating Jira tickets after setting the condition in the Apex Trigger.

## Solution

The common cause of the issue is that the field condition for creating a Jira ticket has not been met. The system needs all field mappings and requirements to be correctly set up before it can create tickets in Jira

## Troubleshooting

Test configuration using the legacy Jira Issues lightning component:

1. Temporarily add the legacy Jira Issues lightning component.  
   Follow the guide: [Configure Lightning Experience components](/cms_trial/space/CSFJIRA/1873969162/Configure+Lightning+Experience+components/).
2. Click the **Create** button (**not** the **Review & Create** button).

   ![Create Jira Issue.png](/cms_trial/assets/14482dd5-7e01-411c-9b7e-e44a40a2d45e.png)
3. Look for any error messages that appear.

   ![image-20240731-051137.png](/cms_trial/assets/0bfbe59b-3671-4e9e-baa1-f54789a1ea37.png)
4. Fix any errors you fins:

   1. Check that the mentioned field is mapped  
      Follow the guide: [Configure entity, field and value mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).
   2. Verify the field it is added under the work item type *Create Issue Screen* in Jira.  
      Follow the guide: [Manage work item screens | Atlassian Support](https://support.atlassian.com/jira-cloud-administration/docs/manage-issue-screens/).
5. Trigger the Apex Trigger again to check if a Jira ticket has been created.

If the issue persists, capture a HAR file with the steps provided in the article below and contact the support team through the [support portal](https://appfire.atlassian.net/servicedesk/customer/portal/11).

- [Generate HAR files and analyze web requests for Atlassian support | Atlassian Support](https://confluence.atlassian.com/kb/generating-har-files-and-analyzing-web-requests-720420612.html)

## Related articles

- [Configure automatic Jira issue creation from Salesforce](/cms_trial/space/CSFJIRA/1873413628/Configure+automatic+Jira+issue+creation+from+Salesforce/)
- [Configure Lightning Experience components](/cms_trial/space/CSFJIRA/1873969162/Configure+Lightning+Experience+components/)
- [Configure entity, field and value mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/)
- [Manage work item screens | Atlassian Support](https://support.atlassian.com/jira-cloud-administration/docs/manage-issue-screens/).
- [Generate HAR files and analyze web requests for Atlassian support | Atlassian Support](https://confluence.atlassian.com/kb/generating-har-files-and-analyzing-web-requests-720420612.html)