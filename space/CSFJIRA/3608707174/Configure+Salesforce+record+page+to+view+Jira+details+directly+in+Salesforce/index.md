# Configure Salesforce record page to view Jira details directly in Salesforce

Add a Jira Issues component directly to your Salesforce record pages, so your team can view and work with related Jira work items without leaving Salesforce.

This page walks you through configuring the Jira Issues (NextGen) Lightning Web Component (LWC) for standard and custom objects in Salesforce Lightning Experience. LWCs inherit global HTML attributes and events, making them more functional and performant than their Aura counterparts, so this is the recommended way to surface Jira data in your Salesforce pages.

## Before you start

Make sure you have:

- [Installed the Salesforce package](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/)
- [Configured a connection](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/)
- [Configured Salesforce subdomain](https://help.salesforce.com/articleView?id=domain_name_overview.htm&type=5)
- Published the Salesforce domain

If the Salesforce domain has not been published, custom components will not be displayed in the *Edit Page* section.

## Use the Lightning App Builder to configure a custom page layout

1. In your Salesforce, load a record page.
2. Click **Settings** > **Edit Page**.
3. The Lightning App Builder loads.  
   In the sidebar, scroll to the bottom to find the following component:

   - **Jira Issues (NextGen)**
4. Drag the component onto the desired location for your page layout.

   ![Next Gen.gif](/cms_trial/assets/d109ee7a-f306-40f0-83f7-57273a9d1c21.gif)
5. After you've placed the components in the desired locations for your page layout, click **Activation...** to [set your Lightning page assignment](https://help.salesforce.com/articleView?id=lightning_app_builder_customize_lex_pages_activate.htm&type=0).

   ![Activation.png](/cms_trial/assets/432ff1c7-06ae-48fc-b1db-e526d0a6b461.png)
6. When you're done setting the page assignment, click **Save**.