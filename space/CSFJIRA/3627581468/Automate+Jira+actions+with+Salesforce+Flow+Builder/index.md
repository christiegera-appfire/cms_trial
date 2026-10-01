# Automate Jira actions with Salesforce Flow Builder

Use Connector for Salesforce & Jira actions in Salesforce Flow Builder to automate work between Salesforce and Jira.

You can use Flow Builder to:

- **Create Jira work item**: Create a new Jira work item from a Salesforce record and automatically associate the two items. You can use this action in record-triggered flows.
- **Push updates to Jira**: Push changes from a Salesforce record to Jira work items that are already associated with it. You can use this action in record-triggered and schedule-triggered flows.

This lets support and engineering teams keep Salesforce and Jira aligned without manually copying information between systems.

Watch the video for a step-by-step example of configuring the **Create Jira work item** action:

## Before you start

Make sure you:

- Have a working connection to your Jira instance (set up by your Salesforce administrator).
- Have an account with permission to create work items in the target Jira space.
- Map the entities for the Salesforce object type and Jira work item type you want to create. See [Configure entity, field and value mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).
- Have enabled **Automatic Pull** in the general configuration of the connection you'll select in the flow.
- The specific association between the Salesforce record and the Jira work item has **Auto-Pull** turned on. Associations set to View-only are not updated by this action.
- Understand the Flows in Salesforce. See [Build Record-Triggered Flows Guide](https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/build-a-record-triggered-flow).

## Set up the flow

1. In Salesforce, open the **Setup** menu.
2. Search for **Flows** in the **Quick Find** box, and click **New Flow** to open the Flow Builder.

   ![New Flow option](/cms_trial/assets/4a41c5c5-4080-40b3-9582-92d84e27a99d.png)
3. In the *New Automation* window, select **Record-Triggered Flow**.  
   To use **Push updates to Jira** in a schedule-triggered flow, select **Schedule-Triggered Flow** instead. See [Use Push updates to Jira in a schedule-triggered flow](/cms_trial/space/CSFJIRA/3627581468/Automate+Jira+actions+with+Salesforce+Flow+Builder/) for the differences.

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
7. Select the Connector action you want to use:

   1. **Create Jira work item**  
      Creates a new Jira work item from the Salesforce record and automatically associates it with the record.
   2. **Push updates to Jira**  
      Pushes changes from the Salesforce record to Jira work items that are already associated with it. The update is sent through the connection you select and follows the synchronization rules configured for that connection. The connection must have **Allow Automatic Pull** enabled, and the association must have **Auto-Pull** on.

      ![Select the Connector action](/cms_trial/assets/2b9b91c1-2d8e-46f5-b8ea-66e03e28e324.png)
8. Type the **Label** name for the element, for example, `Bug flow`.  
   The **API name** field fills out automatically.
9. Fill in the fields for the selected action

   - **Record ID** -The Salesforce record the work item should use. In most cases, this is the record that triggered the flow; click **Use Triggering Record** to fill it in automatically. However, it can also reference a different, specific record depending on your use case. Set Record ID instead of the triggering record.
   - **Object API name -** The type of Salesforce object the record belongs to (for example, Case or Opportunity). Select it from the dropdown list. You can start typing to filter it.
   - **Select a connection** -The Jira connection you want to use for the automation.   
       
     If you selected **Create Jira work item**, also configure:
   - **Jira space** -The Jira space the new work item should be created in.
   - **Work item type** - The type of work item you want to create automatically (for example, bug, task, or story). Make sure that you have mapped the entities for the selected work item type in Jira. In this example, you need a mapping for the Bug Jira work item type and a Case object type. To learn more, see [Configure entity, field and value mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).

     ![Configure Create Jira work item section showing the required action fields.](/cms_trial/assets/1eebf68b-a2fa-44b7-a4f2-2a3f9a26f9f2.png)

     If you selected **Push updates to Jira**, you don't need a Jira space or work item type. The connector pushes record changes to applicable Jira work items already associated with the Salesforce record on the selected connection.

     ![Push updates to Jira](/cms_trial/assets/a7989ba7-f51c-4dc9-a775-b1843bff992d.png)
10. Type the **Flow Label name**, for example, `Create a Jira bug on a Case` or `Push Case updates to Jira`.   
    The Flow API name fills out automatically.

![Flow settings showing the Flow Label field and automatically generated Flow API name.](/cms_trial/assets/e005ff2c-b04d-4ac7-b7f3-08ae59f9c210.png)

1. Click **Activate**.  
   When the flow runs:

   - **Create Jira work item** creates a new Jira work item and associates it with the Salesforce record.
   - **Push updates to Jira** synchronizes the Salesforce record with its applicable existing Jira associations on the selected connection, according to the connection's synchronization rules.

### Example: Escalate a case to Jira

**Scenario:** Your support team wants every Salesforce case marked "Escalated" to automatically become a Bug in the Engineering Jira project.

- **Trigger:** Record-Triggered Flow on `Case`, when `Status` changes to `Escalated`.
- **Record:** The Case record.
- **Object API name:** `Case`
- **Connection name:** `Engineering Jira`
- **Jira space:** `ENG`
- **Jira work item type:** `Bug`

**Result:** As soon as a Case is escalated, a Bug appears in the ENG space, associated to the Case.

Each Create Jira work item step works with one object type per group of records. If your Flow handles multiple object types, add a decision step to route records or run the action per object type.

## **Use Push updates to Jira in schedule-triggered flow**

You can also use Push updates to Jira in a schedule-triggered flow, for example, to push updates for a specific record at regular intervals.   
The same prerequisites apply: Allow Automatic Pull on the connection and Auto-Pull on the association.   
In that case, you must provide these values:

- **Record ID** – the ID of a specific Salesforce record.
- **Object API name** – the object the record belongs to, for example, Case.
- **Select a connection** -The Jira connection you want to use for the automation.

  ![image-20261001-081350.png](/cms_trial/assets/1caa876f-d5b6-4ad8-aae9-033635fa2072.png)

When the flow runs with valid values, the action enqueues the push. The sync changes can take a moment to appear in Jira.

## Need help?

Contact your Salesforce administrator if:

- The connection you need isn't in the list.
- You don't see the Jira space or work item type you expect (this usually means a permissions problem in Jira).

## Learn more

- [Build Record-Triggered Flows Guide](https://trailhead.salesforce.com/content/learn/modules/record-triggered-flows/build-a-record-triggered-flow)