# Create a JSM issue with request types from Salesforce with Jira Issues (NextGen)

The request type field in Jira Service Management (JSM) is crucial in categorizing customer requests. It links these requests to specific workflows, forms, and service desk configurations, defining how customers interact with the service desk and ensuring their issues are processed accurately.

With Connector for Salesforce & Jira, you can create a JSM issue with the request type field using the Jira Issues (NextGen) component from Salesforce to ensure continuous data integrity between JSM and Salesforce teams. This feature enhances collaboration between Salesforce and Jira teams by ensuring all customer requests are correctly categorized and visible in both systems.

For example, when a Salesforce agent needs to escalate a customer request to the IT support team in JSM, they can create the JSM issue with the request type using the Jira Issues (NextGen) component customized for the Salesforce case record. This way, both the team working in JSM and the team working in Salesforce can see the same information.

You can learn more about the [Request Types in JSM](https://confluence.atlassian.com/servicemanagementserver/setting-up-request-types-939926357.html).

## Before you start

- Project binding links your JSM project with Salesforce, allowing data synchronization. Ensure your administrator has completed a [project binding](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/) as well as [entity and field mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/) for a JSM project.
- Your administrator has [configured the Jira Issues (NextGen) component](/cms_trial/space/CSFJIRA/1873543771/Use+Jira+Issues+(NextGen)+with+Lightning+Experience/) required for the Object.

Note that **Request type fields** are only supported in Lightning Web Components.

## Procedure

1. In a Salesforce record, click **Associate/Create.**  
   The **Associate/Create Jira Issue** pop-up window appears.

   ![image-20250605-055500.png](/cms_trial/assets/18a1a00d-46ff-4ba6-821f-703c625aede4.png)
2. Click **Create Jira Issue.**

   ![req.png](/cms_trial/assets/b9ab737b-9ab2-4409-a389-eb711fd1e9f5.png)
3. Select your **Project** and **Issue Type**. All field and value mappings set by your administrator will be used to create the issue.
4. Select the **Request type** and enable the **Use Request type fields** toggle.

   - Click **Required Fields** and provide the required information.  
     The fields change depending on the configuration of the request type.

     ![fields.png](/cms_trial/assets/a56e85d6-99c0-4dc1-b095-5f9a2a173552.png)
5. Set the **Association Configuration**.   
   For detailed instructions, see [Associate a Jira Issue with a Salesforce record.](/cms_trial/space/CSFJIRA/3092284698/Associate+a+Jira+work+item+from+Salesforce+with+Jira+Issues+(NextGen)/)
6. Click **Create**.  
   The *Issue created successfully* message is shown.

<https://app.arcade.software/share/eJyi8ytfgFRt71Km0M26>

## Next steps

- [Automate your integration](/cms_trial/space/CSFJIRA/1874001954/Automate+your+integration/)