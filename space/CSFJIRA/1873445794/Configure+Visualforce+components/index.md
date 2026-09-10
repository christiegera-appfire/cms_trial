# Configure Visualforce components

The Salesforce Package provides a set of Visualforce pages to show associated Jira issues and some operation buttons to create or associate. It also provides a page to view Jira comments related to the associated Jira issues.

This page guides you on how to configure Visualforce pages for both standard objects and custom objects in Salesforce.

Using the Lightning view? Check out [Configuring Lightning Experience components](/cms_trial/space/CSFJIRA/1873969162/Configure+Lightning+Experience+components/).

Ensure that you have already [installed the Salesforce Package](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/) and [configured a connection](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/) before continuing with this guide.

## Create a Visualforce page

The package is shipped with ready-made Visualforce pages for **Case**. If you plan to use it for **Case** only, you can skip to [Add a Visualforce page to an Object Layout](/cms_trial/space/CSFJIRA/1873445794/Configure+Visualforce+components/). For other standard objects and custom objects, follow the steps in this section.

### Create a Jira Issues Visualforce page

1. Go to **Setup** and type `Visualforce Page`in the **Quick Find** box.
2. Click **New**.

   ![Visualforce Pages.png](/cms_trial/assets/60411820-293f-45d6-bcb7-1397436dba42.png)
3. Provide a name and a label for the Visualforce page.   
   We recommend using **Jira Issues** as the label and ***ObjectName*****JiraIssuesPage**as the name. Replace ***ObjectName***accordingly. For example:

   - ***Account*****JiraIssuesPage** for **Account**
   - ***Opportunity*****JiraIssuesPage** for **Opportunity**
   - ***MyCustomObject\_\_c*****JiraIssuesPage** for **MyCustomObject\_\_c**

     ![visual page.png](/cms_trial/assets/a6a6830d-d604-4d9a-8aaa-8f017ec2e16d.png)
4. Paste the following into the **Visualforce Markup**editor:  
   **Cloud**

   **JIRA Issues Visualforce Page**

   ```xml
   <apex:page standardController="ObjectName" extensions="JCFS.GenericObjectController">
       <JCFS:JiraIssuesComponent son="{!son}" soid="{!soid}"></JCFS:JiraIssuesComponent>
   </apex:page>
   ```

   **Server**

   **JIRA Issues Visualforce Page**

   ```xml
   <apex:page standardController="ObjectName" extensions="JSFS.GenericObjectController">
       <JSFS:JiraIssuesComponent son="{!son}" soid="{!soid}"></JSFS:JiraIssuesComponent>
   </apex:page>
   ```
5. Remember to replace `ObjectName`accordingly.

   ![image-20251015-122031.png](/cms_trial/assets/0358a6bd-4f5a-458d-ba51-6af46b931ffe.png)
6. Click **Save**.

### Create a Jira Comments Visualforce Page

To display Jira comments for your object, repeat the steps in the [*Create a Jira Issues Visualforce page*](/cms_trial/space/CSFJIRA/3091792703/Create+a+Jira+work+item+from+Salesforce/) section above with the following details:  
**Label:** `Jira Comments`  
**Name:** `ObjectNameJiraCommentsPage`  
**Visualforce Markup:**

**Cloud**

**JIRA Comments Visualforce Page for Custom Objects**

```xml
<apex:page standardController="ObjectName" extensions="JCFS.GenericObjectController">
    <JCFS:JiraCommentsComponent son="{!son}" soid="{!soid}"></JCFS:JiraCommentsComponent>
</apex:page>
```

**Server**

**JIRA Comments Visualforce Page for Custom Objects**

```xml
<apex:page standardController="ObjectName" extensions="JSFS.GenericObjectController">
    <JSFS:JiraCommentsComponent son="{!son}" soid="{!soid}"></JSFS:JiraCommentsComponent>
</apex:page>
```

## Add a Visualforce page to an Object Layout

1. Log in to your Salesforce instance and click **Setup**.
2. To customize your object**Page Layout**, under the sidebar, navigate to **Build** > **Customize >** (object name) > **Page Layout**.
3. Choose the layoutyou want to edit in the list, then click **Edit**.   
   Example of *Case Page Layout*

   ![contentId-1873445794](/cms_trial/assets/68c35e4d-e0ee-466a-af6e-b64605e1b80b.png)
4. Under the**Layout** panel, scroll until you find **Visualforce Pages**.

   ![contentId-1873445794](/cms_trial/assets/e155168f-a190-45e2-9772-5da054da6f85.png)

   If you don't see the Visualforce page you're looking for, review the steps in [Create a Visualforce Page](/cms_trial/space/CSFJIRA/1873445794/Configure+Visualforce+components/).
5. Click and drag **Section**to a preferred section in the layout. Give this section a name. In this case, we've named it `Jira Section` and configured it as a two-column layout.
6. Click and drag **Jira Issues** and **Jira Comments** onto the newly-created *Jira Section* and place them side by side. You can also adjust the properties so that the panel size is more usable (a minimum height of 500px is recommended).

   ![contentId-1873445794](/cms_trial/assets/15b88ad2-f845-4518-bd93-a6bd88909eff.png)![contentId-1873445794](/cms_trial/assets/640bf1cc-a3fd-4c07-8546-52468b5b9c75.png)
7. Click **Save**.

Now, when you load an object's page, you can see the Jira issues associated with it, along with their comments.

![2025-10-23_11-46-57.png](/cms_trial/assets/f19b59b8-a5c5-43dd-86a9-60efbc922588.png)

Upon creating a new Jira issue or associating it with an existing one, the **Jira Comments** page will refresh automatically.

## Next steps

- [Creating a Jira Issue from Salesforce](/cms_trial/space/CSFJIRA/3091792703/Create+a+Jira+work+item+from+Salesforce/)