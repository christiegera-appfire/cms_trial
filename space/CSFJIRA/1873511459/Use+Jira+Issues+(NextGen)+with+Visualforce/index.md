# Use Jira Issues (NextGen) with Visualforce

You can configure Visualforce pages for both standard objects and custom objects in Salesforce.

The Salesforce Package provides Lightning Web Component pages to show associated Jira issues and some operation buttons to create or associate.

Using the Lightning view? Check out [Using Jira Issues (NextGen) with Lightning Experience](/cms_trial/space/CSFJIRA/1873543771/Use+Jira+Issues+(NextGen)+with+Lightning+Experience/).

Ensure you have already [installed the Salesforce Package](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/) and [configured a connection](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/) before continuing with this guide.

## Step 1: Create a Visualforce page

The package is shipped with ready-made Visualforce pages for **Case**. If you plan to use it for **Case** only, you can skip to Step 2. For other standard objects and custom objects, follow the steps in this section.

1. Go to **Setup** and type `Visualforce Pages`in the quick find box.
2. Click **New**.

   ![Visualforce Pages.png](/cms_trial/assets/01ddc85c-fb2b-48b7-8be1-ca8baac1aa94.png)
3. Provide a name and a label for the Visualforce page.   
   We recommend *Jira Issues* as the label and *ObjectNameJiraIssuesPage* as the name. Replace *ObjectName*accordingly. For example:

   - *AccountJiraIssuesPage* for **Account**
   - *OpportunityJiraIssuesPage* for **Opportunity**
   - *MyCustomObject\_\_cJiraIssuesPage* for**MyCustomObject\_\_c**

     ![visual page.png](/cms_trial/assets/203226d4-06e3-495a-97e2-9ccf355852fc.png)
4. Paste the following into the **Visualforce Markup**editor:  
     
   **Cloud**

   **JIRA Issues Visualforce Page**

   ```xml
   <apex:page standardController="Case" extensions="JCFS.GenericObjectController">
       <apex:includeLightning />
       <div id="jiraIssuesLwcVfContainer" />
       <script>
           $Lightning.use("JCFS:LightningOutDependencies", () => $Lightning.createComponent("JCFS:jiraIssuesLwc", {
               objectApiName: "{!JSINHTMLENCODE(son)}",
               recordId: "{!JSINHTMLENCODE(soid)}",
               isVisualforce: true,
           }, "jiraIssuesLwcVfContainer", cmp => {}));
       </script>
   </apex:page>
   ```

   **Server**

   **JIRA Issues Visualforce Page**

   ```xml
   <apex:page standardController="Case" extensions="JSFS.GenericObjectController">
       <apex:includeLightning />
       <div id="jiraIssuesLwcVfContainer" />
       <script>
           $Lightning.use("JSFS:LightningOutDependencies", () =>
               $Lightning.createComponent(
                   "JSFS:jiraIssuesLwc",
                   {
                       objectApiName: "{!JSINHTMLENCODE(son)}",
                       recordId: "{!JSINHTMLENCODE(soid)}",
                       isVisualforce: true,
                   },
                   "jiraIssuesLwcVfContainer",
                   cmp => {}
               )
           );
       </script>
   </apex:page>
   ```

   Remember to replace **ObjectName**accordingly.

   ![Screenshot of Visualforce page editing](/cms_trial/assets/a8568187-75ac-4553-9547-3f2fce4f43b4.png)
5. Click **Save**.

## Step 2: Add a Visualforce page to Object Layout

1. Log in to your Salesforce instance and click **Setup**.
2. Now let's customize your object**Page Layout**.  
   Under the sidebar, go to **Build > Customize >** (object name)**> Page Layout**.
3. Choose the layoutyou want to edit in the list, then click **Edit**.   
   Here's an example for Case:

   ![contentId-1873511459](/cms_trial/assets/f96ddb44-ca53-4f4a-8e04-ef1390dfb1c8.png)
4. Under the**Layout** panel, scroll until you find **Visualforce Pages**.

   ![contentId-1873511459](/cms_trial/assets/96aa75ed-569b-4d32-baff-429667a54c65.png)

   If you don't see the Visualforce page you're looking for, review the steps in "Step 1: Creating a Visualforce Page".
5. Click *and*drag **Section**to a preferred section in the layout. Give this section a name, in this case, we've named it "Jira Issues (NextGen)" and configured it as a one-column layout.  
   Now click *and* drag **Jira Issues(NextGen)** onto the newly-created "Jira Issues (NextGen)" section. You may also want to adjust the properties so that you get a panel with a size you'll be more comfortable working in (a minimum height of 500px is recommended).

   ![contentId-1873511459](/cms_trial/assets/8db70f37-25f7-4164-b512-f12f9a09e060.png)
6. Click **Save**.  
   Now when you load a record page, you can see Jira issues associated with the record.

   ![2025-10-16_08-01-20.png](/cms_trial/assets/508d3352-7431-4f50-bb61-4b7ecffc65e5.png)

## Next steps

- [Create a Jira Issue from Salesforce with Jira Issues (NextGen)](/cms_trial/space/CSFJIRA/3092088339/Create+a+Jira+work+item+from+Salesforce+with+Jira+Issues+(NextGen)/)