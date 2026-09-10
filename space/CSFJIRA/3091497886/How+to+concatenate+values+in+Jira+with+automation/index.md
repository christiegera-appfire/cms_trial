# How to concatenate values in Jira with automation

## Issue

When Salesforce pushes an update to Jira, the field value gets overwritten instead of concatenated.

For example, the Jira *Account Name* field is mapped with the *Salesforce Account* field. Whenever the value changes in Salesforce, it overwrites the value in Jira. This makes you unable to determine the previous account name without checking the Jira issue history.

The proposed solution is to concatenate the values that changed in the *Account Name* field into another Jira text field.

## Before you start

Make sure that:

- You have mapped the required fields correctly. This solution allows mapping a Salesforce text field (for example *Account name*) to a Jira text field.
- You have created a new Jira text field to store the concatenated value. In this example, this custom field ID is 10155, and the field name is Concatenate *Account name* from Salesforce

## Instructions

1. In Jira, navigate to **Settings > System > Global automation.**
2. Click **Create rule with AI**.
3. Add the **Field value change** trigger.   
   Edit the rule for this case:

   - **Fields to monitor for changes**, select **Account name**
   - For **Change type**, select **Any changes to the field value**
   - **For**, select **Edit issue** and **Create issue**
   - ![image-20240621-162723.png](/cms_trial/assets/5e49e378-80f2-42fe-8992-eb53ffb12664.png)
4. Add a **User condition** to ensure the **Salesforce & Jira Cloud Connector** user triggered the event.

   - For **User**, select **User who triggered the event**
   - For **Check to perform**, select **is**
   - For **Criteria**, select **Salesforce & Jira Cloud Connector**

     ![image-20240621-162740.png](/cms_trial/assets/eac219aa-130c-4385-adff-d50fd808d7d6.png)
5. Implement **IF ELSE** blocks to cover different conditions:

   - IF   
      `{{fieldChange.fromString}}` equals Empty   
     AND   
     `{{issue.customfield_10155}}` equals Empty

     ![image-20240621-175756.png](/cms_trial/assets/e872d0d7-2687-497c-b0a1-d927eb23e88c.png)
     - THEN: Set the **Concatenate Account name from Salesforce** field with `{{fieldChange.toString}}` value.

       ![image-20240621-175819.png](/cms_trial/assets/e02b17d3-cd58-4640-9fe4-70c723a155e2.png)
   - Set **ELSE IF** block:  
     `{{fieldChange.fromString}}` does not equal EMPTY  
      AND  
      `{{issue.customfield_10155}}` equals EMPTY

     ![image-20240621-175834.png](/cms_trial/assets/8c1f07bd-5605-4380-a81c-f04f93a6abb3.png)
     - THEN: Edit **Concatenate Account name** from Salesforce field with `{{fieldChange.fromString}}`, and `{{fieldChange.toString}}` value

       ![image-20240621-175847.png](/cms_trial/assets/49527f50-a2a4-4850-9491-57d8c662d1f0.png)
   - **ELSE IF**:   
     `{{fieldChange.toString}}` does not equal EMPTY   
     AND   
     `{{issue.customfield_10155}}` does not equal EMPTY   
     AND   
     `{{issue.customfield_10155}}` does not contain `{{fieldChange.toString}`

     ![image-20240621-175858.png](/cms_trial/assets/1a46f4c8-bbff-482d-a23a-8710f5019236.png)
     - THEN: **Edit Concatenate Account name** from Salesforce field with `{{issue.customfield_10155.trim()}}`, and `{{fieldChange.toString}}` value.

       ![image-20240621-175934.png](/cms_trial/assets/b574daca-41f3-40a9-9cd4-318e8e577915.png)
   - **ELSE IF**:   
     `{{fieldChange.fromString}}` equals EMPTY   
     AND   
     `{{issue.customfield_10155}}` does not equal EMPTY   
     AND   
     `{{issue.customfield_10155}}` does not contain `{{fieldChange.toString}}`

     ![image-20240621-175945.png](/cms_trial/assets/f1bbba3b-66e3-4ddd-9bbd-7569f88fb76e.png)
     1. **THEN**: Edit Concatenate Account name from Salesforce field with {{issue.customfield\_10155.trim()}}, {{fieldChange.toString}} value.

        ![image-20240621-175956.png](/cms_trial/assets/1c22465a-6836-4e7d-af8f-3be90c186034.png)

### **Automation overview**

![image-20240621-180448.png](/cms_trial/assets/ae0ac14c-89d6-412f-806b-92681d259afd.png)

**Why four conditions?**

**First condition:**

- Only copies the new value of the *Account name* field to the *Concatenate Account name from Salesforce* field if the *Account name* previous value is NULL and the *Concatenate Account name from Salesforce* field is empty.
- This covers when the Concatenate *Account name* from the S*alesforce field and Account name* field is just implemented in Jira.

**Second condition:**

- Copies the previous and new values in the *Account name* field to the *Concatenate Account name from Salesforce* field.
- This ensures the previous and new values are recorded when the *Concatenate Account name from Salesforce* field is implemented.

**Third condition:**

- Copies the new value of the *Account Name* field, and makes sure the new value is not NULL and does not duplicate the value in the *Concatenate Account name from Salesforce* field.
- This ensures that the new value of the *Account name* field is appended behind the existing value in the *Concatenate Account name from Salesforce* field and does not have a duplicate value.

**Fourth condition:**

- Copies the new value of the *Account Name* field, and makes sure the new value does not duplicate the value in the *Concatenate Account name from Salesforce* field.
- This is to ensure the new value of the *Account Name* field is appended behind the existing value in the *Concatenate Account name from Salesforce* field and has no duplicate value. It also triggers this when the *Account Name* field was previously empty.