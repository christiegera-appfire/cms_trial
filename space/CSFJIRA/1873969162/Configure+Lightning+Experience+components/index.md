# Configure Lightning Experience components

The Salesforce Package features the Lightning Experience component, which lets you use the Lightning App Builder to create customized page layouts. The components show Jira information and operation buttons to create or associate, as well as Jira comments related to the associated Jira issues.

This page explains how to configure Lightning Experience components for both standard and custom objects in Salesforce.

Using the Classic view? Check out [Configuring Visualforce components](/cms_trial/space/CSFJIRA/1873445794/Configure+Visualforce+components/).

## Before you start

Before continuing, ensure you have already:

- [Installed the Salesforce package](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/)
- [Configured a connection](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/)
- [Configured Salesforce subdomain](https://help.salesforce.com/articleView?id=domain_name_overview.htm&type=5)
- Published the Salesforce domain

If the Salesforce domain has not been published yet,  custom components are not displayed in the **Edit Page** section.

## Use the Lightning App Builder to configure a custom page layout

1. In your Salesforce, load a record page.
2. Click **Settings** > **Edit Page**.

   ![contentId-1873969162](/cms_trial/assets/df5193ac-7c64-46b6-9723-9f323001a494.png)

   The Lightning App Builder loads.
3. In the sidebar, scroll to the bottom to find the following two components:

   - **Jira Comments**
   - **Jira Issues**

     ![2025-10-15_13-25-21.png](/cms_trial/assets/b40129b0-3f61-4a72-9ef8-24ff12261ec3.png)
4. Drag the components onto the desired location for your page layout.

   ![drag components to the desired location for your page layout](/cms_trial/assets/bb8458a2-b424-434f-a171-8cd1a089ec48.gif)
5. After you've placed the components in the desired locations for your page layout, click **Activation...** to [set your Lightning page assignment](https://help.salesforce.com/articleView?id=lightning_app_builder_customize_lex_pages_activate.htm&type=0).
6. When you're done setting the page assignment, click **Save**.
7. Now, when you load a record page, you are able to see Jira issues associated with the record, along with their comments.

   ![Jira issue and comments associated with Salesforce object](/cms_trial/assets/6f7d95e9-19a9-4a65-8e6d-2512fcd2b7d1.png)

   When you create a new Jira issue or associate it with an existing one, the Jira comments section automatically reflects the changes.

## Next steps

- [Create a Jira Issue from Salesforce](/cms_trial/space/CSFJIRA/3091792703/Create+a+Jira+work+item+from+Salesforce/)