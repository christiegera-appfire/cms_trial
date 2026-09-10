# Updates from Salesforce to Jira are not reflected in other Salesforce objects associated to Jira ticket

## Problem

I have two objects associated to one Jira work item (Case, Contact). I'm pulling some fields from Salesforce to fields mapped to both Case and Contact records.

The Connector automatically pulls Contact fields correctly, but it doesn’t automatically push them to the Case record.

**Case mapping**

![contentId-3091892143](/cms_trial/assets/88be4efa-37ab-4356-9299-c7c041c939ad.png)

**Contact Mapping**

![contentId-3091892143](/cms_trial/assets/c755ca17-481c-4365-9a70-f7c53e75b7e4.png)

## Solution

This is a current limitation of our Connector, mainly to prevent infinite loops if you configure the mapping inaccurately. For more details, you can refer to our documentation here: [Why does my association not auto-push back to other associated Salesforce Objects after pulling to Jira](/cms_trial/space/CSFJIRA/3104571412/Why+does+my+association+not+auto-push+back+to+other+associated+Salesforce+Objects+after+pulling+to+Jira/)

Because of this safeguard, you cannot auto-push other association fields back at this time.

## Recommended solutions

1. Use Manual Push when you associate records in Jira to sync fields to Salesforce.
2. Create a custom Workflow with the [Push to Salesforce post-function](/cms_trial/space/CSFJIRA/1873969278/Configure+workflow+post+functions+in+Jira/). This is the failsafe for pushing the fields you haven't manually pushed. You can set this on the next transition.
3. Utilize Jira Automation and a separate Jira Custom Field.

   1. The Logic is to create a separate Jira Custom Field that will be updated with the Account ID/Contact ID value from the Contact Record using Jira Automation. This automation ensures the update happens separately from the auto-push/pull process.
   2. For the Jira-Contact association, maintain the Mappings to a designated field (for example, Jira Text Read Only Custom Field 2 or 3)

      ![contentId-3091892143](/cms_trial/assets/0f2237dd-d868-4f37-9a2f-ff29e5a385d2.png)

c. Create a new Jira Custom Field that will be updated with the value from Jira Custom Field A using Jira Automation, and add this into the Mappings (for *example, Jira Text Read Only Custom Field*)

![contentId-3091892143](/cms_trial/assets/f523240a-a391-49b0-9a95-32b95c7ee691.png)

d. When you associate with the Contact Record, which pulls in the data, this data will be copied to the new custom field, which will act as a manual update to the field and push to Salesforce.

The feature is not supported out of the box. These suggestions are provided to the best of our ability. If there are any issues with the implementation, it is beyond the scope of our standard support.

### **Other limitations**

- The post function would not respect the After Create Salesforce Object settings.

  - Use the APEX trigger to auto-push from SF to update and pull information to Jira after creating the Salesforce record using the post function.
- Jira Read-only fields won't trigger the auto push.
- Salesforce read-only fields won't trigger the auto push to Jira.
- The post function won't create another record if there is already an existing one.