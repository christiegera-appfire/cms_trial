# Automatically create Jira work items with Salesforce Flows

Keep your support and engineering teams in sync without manual copy-pasting. The **Create Jira work item** action for Salesforce Flows automatically creates a Jira work item whenever a Flow-defined event happens in Salesforce, for example, whenever someone creates a Case record. Add it as a step in Flow Builder, specify the record, connection, Jira space, and work item type to use, and it handles the rest.

Once the work item is created, it's also automatically associated with the Salesforce record, so you can see the association in both Jira and Salesforce. Your connection's settings control how the associated items stay in sync. You don't need to configure anything extra in the Flow step itself.

## Before you start

Make sure you:

- Have a working **connection** to your Jira instance (set up by your Salesforce admin).
- Have an account with permission to create work items in the target Jira space.
- Map the entities for the Salesforce object type and Jira work item type you want to create. To learn more, see [Configure entity, field and value mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).
- Understand the Flows in Salesforce: [Build Record-Triggered Flows Guide](https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/build-a-record-triggered-flow).

## Enable Apex Class Access for your user

Before building the flow, your Salesforce administrator needs to grant the System Administrator profile access to the Apex classes the action depends on.

1. In Salesforce, open **Setup**.
2. Search for **Profiles** in the **Quick Find** box, and select the **System Administrator** profile.

   ![Profiles page showing the profile selected for Apex Class Access.](/cms_trial/assets/3234ec7b-01f1-4f40-9175-6733568a3c28.png)
3. Under **Enabled Apex Class Access**, click **Edit**.

   ![Enabled Apex Class Access section showing the Edit button.](/cms_trial/assets/e161765c-ab6a-41f5-bcb5-06335a492b62.png)
4. In the **Available Apex Classes** list, select the following classes:

   - `JCFS.ActionEditorController`
   - `JCFS.CreateJiraIssueAction`
   - `JCFS.InvocableUtils`

     ![Available Apex Classes list showing the required Apex classes to select.](/cms_trial/assets/55449155-ea12-4a19-865b-4522245d6b79.png)
5. Click **Add** to move them to the **Enabled Apex Classes** list.

   ![Enabled Apex Classes list showing the selected Apex classes after clicking Add.](/cms_trial/assets/3663c58a-000c-4611-8389-4d07b9c5c2c4.png)
6. Click **Save**.

## Set up the flow

1. In Salesforce, open the **Setup** menu.
2. Search for **Flows** in the **Quick Find** box, and click **New Flow** to open the Flow Builder.

   ![New Flow option](/cms_trial/assets/4a41c5c5-4080-40b3-9582-92d84e27a99d.png)
3. In the *New Automation* window, select **Record-Triggered Flow**.

   ![New Automation window showing the Record-Triggered Flow option.](/cms_trial/assets/9f925125-a9ba-4f9c-ad55-083f38df0933.png)
4. Under *Configure Start,*select the Salesforce object type whose records you want to trigger the flow (for example, Case).

   ![Configure Start section showing where to select the Salesforce object that triggers the flow.](/cms_trial/assets/ffc3dc00-9d32-4d86-a5f3-1b6d708d6c8c.png)
5. Select the event that will trigger the flow. For example, **A record is created**.

   - **A record is created**
   - **A record is updated**
   - **A record is created or updated**
   - **A record is deleted**

     ![Trigger configuration showing the available record-trigger options.](/cms_trial/assets/f8819841-7bc4-4413-8a9d-8c74a5730eef.png)
6. Click the **Add element** (▢) icon, then select **Action**.

   ![Flow Builder showing how to add an Action element to the flow.](/cms_trial/assets/d9b966f0-95a1-40ff-989b-8f09eea6c4a1.png)
7. Select the **Create Jira work item** action.

   ![Action selector showing the Create Jira work item action.](/cms_trial/assets/bcb70886-aafd-4d39-84be-13592e4893db.png)
8. Type the **Label** name for the element , for example, `Bug flow`.  
   The **API name** field fills out automatically.
9. Fill in the fields under the *Configure Create Jira work* i*tem* section.

   - **Record ID** -The Salesforce record the work item should be based on. In most cases, this is the record that triggered the flow; click **Use Triggering Record** to fill it in automatically. However, it can also reference a different, specific record depending on your use case. Set Record ID instead of the triggering record.
   - **Object API name -** The type of Salesforce object the record belongs to (for example, Case or Opportunity). Select it from the dropdown list. You can start typing to filter it.
   - **Select a connection** -The Jira connection you want to use for the automation.
   - **Jira space** -The Jira space the new work item should be created in.
   - **Work item type** - The type of work item you want to create automatically (for example, bug, task, or story). Make sure that you have mapped the entities for the selected work item type in Jira. In this example, you need a mapping for the Bug Jira work item type and a Case object type. To learn more, see [Configure entity, field and value mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).

     ![Configure Create Jira work item section showing the required action fields.](/cms_trial/assets/1eebf68b-a2fa-44b7-a4f2-2a3f9a26f9f2.png)

1. Type the **Flow Label name**, for example, `Create a Jira bug on a Case`.  
   The Flow API name fills out automatically.

   ![Flow settings showing the Flow Label field and automatically generated Flow API name.](/cms_trial/assets/e005ff2c-b04d-4ac7-b7f3-08ae59f9c210.png)
2. Click **Activate**.  
   Whenever a new case record is created in Salesforce, an associated Jira work item is also created in Jira. Make sure you refresh your page to see the newly associated item.

## Example

### Escalate a case to Jira

**Scenario:** Your support team wants every Salesforce case marked "Escalated" to automatically become a Bug in the Engineering Jira project.

- **Trigger:** Record-Triggered Flow on `Case`, when `Status` changes to `Escalated`.
- **Record:** The Case record.
- **Object API name:** `Case`
- **Connection name:** `Engineering Jira`
- **Jira space:** `ENG`
- **Jira work item type:** `Bug`

**Result:** As soon as a Case is escalated, a Bug appears in the ENG space, associated to the Case.

Each Create Jira work item step works with one object type per group of records. If your Flow handles multiple object types, add a decision step to route records or run the action per object type.

## Need help?

Contact your Salesforce admin if:

- The connection you need isn't in the list.
- You don't see the Jira space or work item type you expect (this usually means a permissions problem in Jira).

## Learn more

- [Build Record-Triggered Flows Guide](https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/build-a-record-triggered-flow)