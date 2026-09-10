# Changing Reporter/Assignee using Case Owner email

## Purpose

To change a Jira issue's Assignee or Reporter, you are required to set the value mapping between the Jira User field and the Salesforce Case Owner. This documentation will help to provide an alternative workaround by using the Owner's email address.

## Answer

## Configuration in Salesforce

1. Go to **Setup > Object Manager >** search for the desired **Object** (for example, Opportunity).
2. Click to configure the Object, under **Fields & Relationships**, click **New**.
3. Select **Formula** to capture the Case Owner's email address and click **Next**.
4. Insert the **Field Label** and **Field Name** value. Then, choose the **Text** option. Click **Next** to proceed.
5. Click the **Insert Field** button and design your field. Click **Insert** and press **Next** until you reach last page.

   ![Inseft field.png](/cms_trial/assets/f53ee637-f2ce-4090-af25-e5b3d2dd9607.png)
6. Click **Save** to complete your custom field configuration. Confirm that the email address is now populated in the Salesforce Record.

## Configuration in Jira

1. Create a **Short Text** [custom field](https://support.atlassian.com/jira-cloud-administration/docs/create-a-custom-field/) (link for custom field in Jira. In this example it is named "Jira User".
2. Go to **Apps > Salesforce > Bindings >** select **Mappings** on an issue type and map the Jira field with the Salesforce field created.

   ![owner email.png](/cms_trial/assets/9dc6518a-e70e-4de4-86f6-7eea2cc88cbb.png)
3. Save the configuration and confirm that the email address is populated in Jira when the data is pulled from Salesforce.

## Configuration in Jira Automation

1. Select a project and navigate from **Project Settings > Automation**.
2. Create a new rule with **Trigger** is **Issue updated**.
3. Add a new component and select **New Condition > Issue Fields Condition**. Choose the Jira Field and set the condition as **is not empty**.
4. Add another component and select **New Action > Send Web Request**
5. Set the **Web Request URL** with the URL according to your Jira environment:

   1. Jira Cloud:  
      <JiraBaseURL>/rest/api/3/user/search?query={{issue.<customField\_Id>}}
   2. Jira Server:  
      <JiraBaseURL>/rest/api/2/user/search?username={{issue.<customField\_Id>}}
   3. To find the Custom Field ID, you can refer to How to find the id for custom field(s)? documentation. Link for "[How to find the id for custom field(s)? documentation.](https://confluence.atlassian.com/jirakb/how-to-find-id-for-custom-field-s-744522503.html?__hstc=72543820.dca6847bc67d72cb12dda09618bcbbf0.1610352968903.1663293812024.1663296455536.959&__hssc=72543820.27.1663296455536&__hsfp=3395054717)”
6. Before proceeding further, create an API token using a user that has the right permissions for the project based on the article below **(This step is not required for Jira Server & Data Center):**

   1. [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/?__hstc=72543820.dca6847bc67d72cb12dda09618bcbbf0.1610352968903.1663293812024.1663296455536.959&__hssc=72543820.27.1663296455536&__hsfp=3395054717).
7. Copy the API token and encode it with the username. You can use this [third-party site](https://www.base64encode.net/) to encode it.
8. In the website's text box, arrange the username and the token in the following format:

   1. Jira Cloud:  
      <username>:<APIToken>
   2. Jira Server:  
      <username>:<password>
9. Click **Encode** and copy the result back to the Jira Automation page.
10. In the **Headers** section, set the name as **Authorization**.
11. Set the **Value** with the following format, paste the encoded data from step 9 in the "<encodedToken>" portion of the text:  
    Basic <encodedToken>
12. Set the **HTTP Method** to **GET** and tick the **Delay execution** option.
13. The configuration up to this point will look like the following:

    ![contentId-3091400759](/cms_trial/assets/0b055cb2-0463-4caf-a9bc-6f3d3b64c42b.png)

    Click **Validate your web request configuration** and validate an issue from your project. The expected result is "HTTP 200 OK."
14. Add the last component > **New Action > Edit Issue**.
15. **Do not select** any field, instead expand the **More Options** section.
16. In the text box, add the following:

    1. Jira Cloud:  
       {  
        "fields": {  
        "reporter":{"id":"{{webhookResponse.body.accountid}}"}  
        }  
       }
    2. Jira Server:  
       {  
        "fields": {  
        "reporter":{"name":"{{[webhookResponse.body.name](http://webhookResponse.body.name)}}"}  
        }  
       }  
       You can change the value between Assignee” or “Reporter” depending on your configuration.
17. Save the automation and publish it.

## Related Information

- [Changing the Reporter and Assignee of an Issue](/cms_trial/space/CSFJIRA/3091400759/Changing+Reporter%2FAssignee+using+Case+Owner+email/)