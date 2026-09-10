# Use Jira Issues (NextGen) with Lightning Experience

Add a Jira Issues component directly to your Salesforce record pages, so your team can view and work with related Jira issues without leaving Salesforce.

This page walks you through configuring the Jira Issues (NextGen) Lightning Web Component (LWC) for standard and custom objects in Salesforce Lightning Experience. LWCs inherit global HTML attributes and events, making them more functional and performant than their Aura counterparts, so this is the recommended way to surface Jira data in your Salesforce pages.

Using the Classic view? Check out [Configuring Jira Issues with Visualforce](/cms_trial/space/CSFJIRA/1873511459/Use+Jira+Issues+(NextGen)+with+Visualforce/).

## Before you start

Before continuing, ensure you have already:

- [Installed the Salesforce package](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/)
- [Configured a connection](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/)
- [Configured Salesforce subdomain](https://help.salesforce.com/articleView?id=domain_name_overview.htm&type=5)
- Published the Salesforce domain

if the Salesforce domain has not been published, custom components will not be displayed in the *Edit Page* section.

## Use the Lightning App Builder to configure a custom page layout

1. In your Salesforce, load a record page.
2. Click **Settings** > **Edit Page**.
3. The Lightning App Builder loads.  
   In the sidebar, scroll to the bottom to find the following component:

   - **Jira Issues (NextGen)**

     ![Next Gen.gif](/cms_trial/assets/807cb013-2271-40d8-9f64-301477252ee1.gif)
4. Drag the component onto the desired location for your page layout.
5. After you've placed the components in the desired locations for your page layout, click **Activation...** to [set your Lightning page assignment](https://help.salesforce.com/articleView?id=lightning_app_builder_customize_lex_pages_activate.htm&type=0).

   ![Activation.png](/cms_trial/assets/86c15503-ab17-4492-bbb8-29351d9293df.png)
6. When you're done setting the page assignment, click **Save**.
7. Now, when you load a record page, you can see Jira issues associated with the record.

   ![csfjira-lightning-jira-issues.png](/cms_trial/assets/c6d6dd38-6d11-4879-9af2-05a09c6c155e.png)

## Next steps

- [Generating a Jira Issue from Salesforce with Jira Issues (Nextgen](/cms_trial/space/CSFJIRA/3092088339/Create+a+Jira+work+item+from+Salesforce+with+Jira+Issues+(NextGen)/))