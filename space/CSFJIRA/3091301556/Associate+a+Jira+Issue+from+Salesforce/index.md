# Associate a Jira Issue from Salesforce

This page will guide you on how to associate a Salesforce record (for example, an Account, a Case, or a Contact) with a Jira Issue from within Salesforce.

By doing so, you can easily link a Jira issue with the current record and configure its sync behavior.

For example, when Salesforce agents receive a Case caused by a known bug, they can associate the Case with an existing Jira issue containing the bug report. This way, both the team working in Jira and the team working in Salesforce can see all related Cases and Jira issues and push or pull data between the systems.

## Before you start

- Your administrator has completed a [project binding](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/) as well as [entity and field mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/) in Jira.
- Your administrator has [configured the Visualforce pages](/cms_trial/space/CSFJIRA/1873445794/Configure+Visualforce+components/) required for the Object.

## Associate a Salesforce record with a Jira Issue

1. In a Salesforce record, click **Associate**.

   ![2025-10-16_12-57-38.png](/cms_trial/assets/73806f68-8c12-4a12-8dea-1231e0d74f1b.png)

   The **Associate Jira Issue** pop-up window appears.
2. Search for your Jira issue by entering the **Issue Key** or **Issue Summary** in the search box.
3. If there are multiple matches, the most recently created issues will appear first.  
   Only issues belonging to Projects bound to the authorized Connection will be searchable.

   ![2025-10-16_12-59-44.png](/cms_trial/assets/32824cc5-3214-4b24-85df-38a4d4830502.png)
4. You may choose to toggle the following options:  
   **View Only** - Manual and automatic synchronization will be disabled.  
   **Auto Pull** - Changes to the associated Jira issue will be pulled automatically to this record.  
   **Auto Push** - Changes to this record will be pushed automatically to associated Jira issues given respective triggers are installed.

Some combinations are not possible and cannot be selected. Refer to the help provided under the **What Will Happen?** panel.

1. You can also choose what to do after the Jira issue is associated by choosing from the following options:

![2025-10-16_13-00-28.png](/cms_trial/assets/249e5d4e-c836-4ea0-a085-808fa054566e.png)

1. When you are satisfied with your configuration, click **Associate**.
2. Upon successful association, the *Issue associated successfully* message is shown.

![2025-10-16_13-02-12.png](/cms_trial/assets/1786ecc1-7f29-47aa-b461-ca5e0d2d03ee.png)

### Jira Issues Display in Lightning

JIRA issues in Salesforce Lightning are listed as cards if the association is less than 5. Otherwise, they are shown as a table that aligns with the [Lightning Design System](https://www.lightningdesignsystem.com/).

![image-20250415-091519.png](/cms_trial/assets/7b7a3a23-f0d4-4cb1-889d-de32fe5fb4ce.png)

- Each Jira issue can be associated with a maximum of 1000 Salesforce records~~.~~
- You can display up to 50 Jira associations using the Salesforce NextGen Lighting Component.

## Related information

- [Configuring an association](/cms_trial/space/CSFJIRA/3091956652/Configure+an+association/)