# Get started with Connector for Salesforce & Jira

Connector for Salesforce & Jira lets you keep information in sync between Salesforce and Jira. You can connect Jira instances with a Salesforce environment to allow associating Jira work items and Salesforce objects and synchronizing data.

Follow the step-by-step guide for administrators to install the app and set up a new Salesforce connection in Jira with Connector for Salesforce & Jira. By the end of this guide, you will have a connection between Salesforce and Jira, configured settings, and created a binding for your Jira space using a template with field mappings. In other words, you can configure which Jira space should connect to Salesforce and what type of Jira work items and Salesforce objects should be mapped together.

## Before you start

Verify compatibility and make sure your Jira and Salesforce environments meet the required versions and permissions before installing Connector for Salesforce & Jira.

- [Salesforce requirements](/cms_trial/space/CSFJIRA/1873412305/System+and+platform+requirements/)
- Make sure you have:

  - Administrator rights in Jira - only administrators can set up the integration.
  - Administrator rights in Salesforce - only administrators can set up the integration.

## The final result of this tutorial

By the end of this tutorial, you'll have:

- Installed the app in Jira and in Salesforce.
- An **authorized connection** between Jira and Salesforce.
- Imported Salesforce objects (for example, Case, Account, and Opportunity) available in Jira.
- A **binding** linking a Jira space to that connection.
- **Entity, field, and value mappings** that keep Jira work items and Salesforce records in sync.

## 1. Install the Connector

Install the app on both sides of the integration. Choose the guide that matches your platform.

1. [Install Connector for Salesforce & Jira in](/cms_trial/space/CSFJIRA/1873412370/Install+the+Connector+in+Jira+Cloud/) [**Jira**](/cms_trial/space/CSFJIRA/1873412370/Install+the+Connector+in+Jira+Cloud/)[**Cloud**](/cms_trial/space/CSFJIRA/1873412370/Install+the+Connector+in+Jira+Cloud/)

   - [Work with Jira Service Management projects](/cms_trial/space/CSFJIRA/1873510574/Work+with+Jira+Service+Management+projects/)
2. [Install the Salesforce package in Salesforce](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/).

   - [Install the Connector for Salesforce package in a sandbox](/cms_trial/space/CSFJIRA/3510861933/Install+the+Connector+for+Salesforce+package+in+sandbox/)

## 2. Create a new connection in Jira

A connection is the initial authorization between Jira and Salesforce, and it determines which Salesforce object types are available in Jira. Setting this up first pre-populates the objects and fields you can use for associations and mapping later.

1. [Set up a connection to Salesforce](https://support.appfire.com/space/CSFJIRA/1873379599).
2. [Add Salesforce object types and fields](/cms_trial/space/CSFJIRA/1873379599/Set+up+a+connection+to+Salesforce+(Jira+Cloud)/).
3. [Configure connection settings](https://support.appfire.com/space/CSFJIRA/1853653945).

## 3. Set up your integration in Salesforce

This step completes the Salesforce side of the setup, allowing Salesforce to communicate securely with Jira and display Jira information alongside your Salesforce records.

1. [Set up your integration in Salesforce](/cms_trial/space/CSFJIRA/1873772649/Set+up+your+integration+in+Salesforce/).
2. [Add a remote site](/cms_trial/space/CSFJIRA/1873412619/Add+new+remote+site/).
3. [Set up a connection to Jira](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/).
4. [Configure the Salesforce record page to view Jira details directly in Salesforce](/cms_trial/space/CSFJIRA/3608707174/Configure+Salesforce+record+page+to+view+Jira+details+directly+in+Salesforce/).

## 4. Add a space binding and configure mappings

Bindings connect specific Jira spaces to your Salesforce connection. You need to bind a Jira space to a connection before you can associate Jira work items with Salesforce records and synchronize them.

Before any data can sync between Jira and Salesforce, the two systems need to know which entities belong together. Entity mappings define these relationships, for example, telling the Connector that a Jira task corresponds to a Salesforce case. Once that relationship is established, Jira work items and Salesforce records can be associated and kept in sync.

1. [Add a space binding](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/).
2. Configure mappings.

   - Use pre-defined templates to speed up the process:  
     [Configure mapping with templates](/cms_trial/space/CSFJIRA/3664152459/Configure+entity+and+field+mappings+from+templates/).
   - You can also set up the mappings from scratch:  
     [Configure entity and field mappings](/cms_trial/space/CSFJIRA/3664152584/Configure+entity+and+field+mappings+from+scratch/).

## 5. Start associating

With connection, binding, and mappings in place, you can now link an individual Jira work item to a specific Salesforce record so the two stay synchronized going forward. You can also create Salesforce records directly from a Jira work item view and create Jira work items from Salesforce records.

1. [Associate a Jira work item with a Salesforce record](/cms_trial/space/CSFJIRA/3663725288/Associate+Jira+work+items+with+Salesforce+records+from+Jira/).
2. [Work with associations](/cms_trial/space/CSFJIRA/3091760268/Work+with+associations/).