# Configure entity and field mappings from scratch

If your use case is not following any of the provided templates, you can start building your own mapping the way you need it. In this article, we'll guide you in creating a mapping for a custom work item type.

## Before you start

Make sure you have:

- Administrator rights in Jira - only administrators can set up the mappings
- Added all required Salesforce objects to be available in Jira, see more [Available Salesforce objects](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/).
- Created a [Binding between a project and a connection](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/).
- Understand Jira field-type compatibility with Salesforce field types to map fields correctly. Visit the [Jira Field Type to Salesforce Field Type compatibility](/cms_trial/space/CSFJIRA/1522369149/Jira+field+type+to+Salesforce+field+type+compatibility/) page to learn more.

### 1. Configure entity mappings

1. In the *Entity mapping* step, click **Create** underthe **Create from scratch** option.

   ![Create from scratch option](/cms_trial/assets/c612c1b4-26f5-43ca-8634-0bde18fe16d3.png)
2. Select the **Jira work item type** and the corresponding **Salesforce object type**.  
   For example, select a custom *Technical debt* Jira work item type and a case as the Salesforce object type to associate Jira tasks with Salesforce *case* records.

   ![entity mapping](/cms_trial/assets/e5610a38-2999-47a3-bfac-dc34987e0388.png)
3. Click **Add entity mapping**.

   ![Add entity mapping](/cms_trial/assets/98d60123-b26f-4ade-a56c-fff6ece22105.png)
4. Repeat the steps until you have mapped all required entities.

### 2. Configure field mappings

1. Click the entity mapping you have created, for example, ***Technical debt*** **-> Case** mapping.

   ![field mappings](/cms_trial/assets/951bfddf-5c80-478a-8539-682592a8b53e.png)
2. Select the **Jira fields** that match the corresponding **Salesforce fields**.   
   The example below matches:

   - the *Summary* **Jira field** to the *Subject* **Salesforce field**
   - *Description* to *Description*
   - *Priority* to *Priority*

     ![image-20260907-060401.png](/cms_trial/assets/b6657d7f-297f-424a-b030-3afa91cd410f.png)
3. Click **Add field mapping**.
4. Customize the **Sync direction** by clicking the arrow buttons if needed.  
   For example, configure the sync direction for *Priority* to synchronize fields only from Salesforce to Jira because the Salesforce support team decides the task priority. For the *Description* and *Summary* fields, keep the default bidirectional synchronization.   
   For details, check [Create inbound-only or outbound-only mappings](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/edit-v2/3664152584#5.-Create-inbound-only-or-outbound-only-mappings).

   ![Sync direction](/cms_trial/assets/638b9022-db0b-44c8-a8dd-98dea667e5dd.png)

### 3. Set default value

Before synchronizing data between Jira and Salesforce, decide how to handle field values not covered by the mapping. Setting default values and actions lets you choose whether you want to copy the original value, force a custom value, leave it empty (if allowed), or raise an error to ensure all field values are synchronized according to your needs. Choose one of the following options:

- **Copy value**:Connector copies and uses the original field value from the source to the destination system. (This is the default option.)   
  For example, if you want Jira work item status to match their equivalents in Salesforce, this option ensures that a Jira work item with the *In Progress* status is set to *In Progress* in Salesforce.
- **Set value**: Connector assigns a predefined value of your choice for the field.   
  For example, if you want all Jira work items to have *UI* as their component in Salesforce, regardless of their original component, you can set *UI* as a default component in Salesforce. This ensures consistent categorization of Jira work items in Salesforce.
- **Set empty**: Connector sets the field value to empty. This option is not available for required fields that need to have their value set.
- **Raise error**: Connector raises an error, and synchronization fails.

When creating a Jira work item from Salesforce, field values are filled based on the mapping or default values you’ve set. However, there’s one exception, which is the Priority.

Jira doesn’t allow the Priority field to be empty, so it always has a default value set. If the Priority field is empty in Salesforce, the value is populated with the Jira default priority instead of the one set in the Connector for Salesforce & Jira. The correct Priority value, as configured in the Connector, will only synchronize after pushing from Salesforce.

To define default values:

1. Click the **Menu** (▢) icon next to the selected Jira and Salesforce field mapping and select **Configure**.

   ![image-20260907-062107.png](/cms_trial/assets/c23489b5-1610-48ab-831f-7f3353e09295.png)
2. Select a **Jira** **default** and **Salesforce default** value:

   - **Copy value**
   - **Set value** (requires entering your preferred value)
   - **Set empty**
   - **Raise error**

     ![image-20260907-073654.png](/cms_trial/assets/e6e29166-5449-41f9-93e8-b332917f80e1.png)
3. Click **Configure**.

### 4. Configure value mappings

Additionally, you can define specific value mappings to match Jira and Salesforce field values to make sure the values are translated to the existing terminology. For example:

- Mapping the Jira priority *Highest* with Salesforce priority *Critical*.
- Mapping the Jira component *UI* with Salesforce Case Reason *User Interface*.

If the value is not mapped, Connector for Salesforce & Jira continues according to the defined [default values](/cms_trial/space/CSFJIRA/3664152584/Configure+entity+and+field+mappings+from+scratch/).

To map field values:

1. Click the **Menu** (▢) icon next to the selected Jira and Salesforce Field mapping and select **Configure**.

   ![image-20260804-103636.png](/cms_trial/assets/a63f854b-5ae1-4686-bd1d-1f143b2d0c02.png)
2. Enter Jira and Salesforce values accordingly.  
   For example:

   - *Highest* to *Critical*
   - *High* to *High*
   - *Medium* to *Medium*
   - *Low* to *Low*

     ![image-20260907-065018.png](/cms_trial/assets/686f844a-acfe-478d-b3a4-f9a8ca7e0191.png)
3. If the Jira field value is of user type, select available Jira users from the dropdown list.

   ![image-20260907-072123.png](/cms_trial/assets/c573dd58-35b6-4042-86d1-9e5d1c891686.png)
4. Click **Add**.
5. Click **Configure**.

### 5. Create inbound-only or outbound-only mappings

By default, a field mapping applies in both directions: a change in Jira updates Salesforce, and a change in Salesforce updates Jira. However, some fields may need to flow in one direction only. For example, you may want agents to update case descriptions in Salesforce without those changes overwriting content in Jira, or the other way around. You can also configure separate value mappings for each direction (inbound or outbound). This also lets you map values in a one-to-many relationship. Create two records for the same field, one for each direction, and then proceed with configuring the value mappings.

For example:

1. Map the **Components** Jira field to the **Case Reason** Salesforce field separately for each direction (inbound or outbound).

   ![image-20260804-104002.png](/cms_trial/assets/27f65909-fc91-413a-b81e-87e2f2dec89b.png)
2. For inbound-only mapping, map, for example, **UI** Jira task value with the **User Interface** Case Reason Salesforce value.

   ![contentId-3664152584](/cms_trial/assets/57485172-9edb-480c-8f5d-63f3a6d9741e.png)
3. For outbound-only mapping, map, for example, **Installation** Jira task value with the **Packaging** Case Reason Salesforce value.

   ![contentId-3664152584](/cms_trial/assets/365e8261-152e-4e00-b083-5a6e33f5b89b.png)

## Next steps

- [Associate Salesforce records from Jira](/cms_trial/space/CSFJIRA/3663725288/Associate+Jira+work+items+with+Salesforce+records+from+Jira/)