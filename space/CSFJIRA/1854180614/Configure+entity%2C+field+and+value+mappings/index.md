# Configure entity, field and value mappings

Before any data can sync between Jira and Salesforce, the two systems need to know which entities belong together. Entity mappings define these relationships, for example, telling the Connector that a Jira task corresponds to a Salesforce case, or that a Jira epic corresponds to a Salesforce opportunity. Once that relationship is established, Jira issues and Salesforce records can be associated and kept in sync.

From there, field mappings determine how individual fields stay current between the two systems. For example, you can map the description field in Jira to its equivalent in Salesforce.

You can also define value mappings to handle differences in terminology between the two systems, such as mapping Jira's In Progress status to Salesforce's Escalated to Dev, so each team continues working with the values that make sense in their own tool.

This page helps you configure entity mappings, fields, and value mappings for your bindings.

- Configure entity mappings to set up Jira issue types to match the corresponding Salesforce object type.
- Configure field mappings to set up Jira fields to match the corresponding Salesforce fields.
- Set up value-to-value mapping for each field mapping and define what should be done in cases not covered by the mappings.

Watch how entity, field, and value mappings work together in practice, including how a description updated in Salesforce automatically appears in the linked Jira task.

Video script

The first video we demonstrated how to view Salesforce data in Jira and view Jira data in Salesforce. In this video, we're gonna manipulate the data between the two.

What that means is if I were to change the description in Jira in Salesforce, so let's go ahead and do that.

This is a whole new description. That is now going to be replicated in Jira. This is an oversimplification of really what it can do amongst all the other fields that may exist within Jira, but this just kind of gives you a quick demonstration of how we can change data and how we can then map these fields to coexist amongst the two different systems.

The way we're going to achieve that is through the binding section. In the app configurations. So again, we're going to go to the app section, go to Connector to Salesforce. Once you get there, you're going to see this bindings connection right here. This is then going to allow you to choose a binding, which ultimately allows you to map a project to a Salesforce instance.

So in this particular instance, I have four projects connected to one single Salesforce instance, so that users within Salesforce can create tickets into four separate projects within Jira. For this demonstration, I'm going to go into the Jira integration plus demo and go to this Mappings button. Once in here, this is going to bring up the different values that you can configure, the field values that you can configure, from an issue type to a Salesforce object. So in this demonstration, you can choose in this entity mapping. What Salesforce object and what type of ticket you ultimately want to be creating in Jira. So you can see I have a case that for this Jira integration plus demo project can create a task, a case can create an epic and a case can create a bug. But if you want only accounts to create tasks and maybe an account that can only create a feature enhancements as well, you're going to be able to set that criteria up.

Then if we go deeper into the configurations we dig in one more level, Case to task. Let's go ahead and go to this Mappings.

This is where you're going to be able to choose how you want the data to synchronize between the two systems.

If you want the summary to change, when I have the value and your change, It will change the value in Salesforce. It will. If I then change the value in Salesforce, but this arrow is not turned on, it's not going to change the value in Jira.

So there are some values that you're going to want to have bidirectional, and some values that you're only going to want to have one way.

You'll be able to configure these mappings any way you want, but there is some compatibility matrix, matrix documentation that you will need to review to ensure that the field is compatible in Salesforce with the, field in Jira.

Additionally, there are, some additional settings that exist in these fields for, value mapping. So, In progress, in Jira means something else, In review within Salesforce. So you can go very granular in each of these configurations, but ultimately, at the highest level, you're gonna be able to have whichever data and field that exists in Salesforce, change it in Jira, or vice versa, through this configuration Bindings that you can set up within the app settings.

If you have any more questions about this, please go ahead and raise a support ticket with our team.

We'd be happy to help. Thanks.

## Before you start

Make sure you have:

- Administrator rights in Jira - only administrators can set up the mappings
- Added all required Salesforce objects to be available in Jira, see more [Available Salesforce objects](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/).

- Created a [Binding between a project and a connection](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/).

To find out what Jira field types are compatible with Salesforce field types, visit the [Jira Field Type to Salesforce Field Type compatibility](/cms_trial/space/CSFJIRA/1522369149/Jira+field+type+to+Salesforce+field+type+compatibility/) page.

## Step 1: Configure entity mappings

1. Select **Apps** from the left sidebar in Jira.
2. Next to *Connector for Salesforce,* click **Menu** (▢) > **App settings**.

   ![App settings](/cms_trial/assets/04b192eb-dfca-472c-9373-fce967fb45be.png)

1. Under *Connector for Salesforce*, click **Bindings**.
2. On the *Bindings* window, choose the binding to configure and click **Mapping**.

   ![bindings window](/cms_trial/assets/9ce7fd87-6e0c-4b81-a3fa-742724a94584.png)
3. On the *Mapping Configuration* window, click **+Add Entity Mapping**.  
   (Alternatively, if you have a previously exported entity mapping, you can also **Import** it here.)

   ![add entity mapping ](/cms_trial/assets/0248b0b4-8475-4e90-8211-9bd6b3601b67.png)

   The *Add Entity Mapping* window appears.

   ![Add Entity Mapping window](/cms_trial/assets/344b781b-9e69-4f1d-aac1-30b789784544.png)
4. Select the **Issue Type** you want mapped to specific **Salesforce Objects**.  
   For example, select a task for the Jira issue type and a case for the Salesforce object types to allow associating Jira tasks with Salesforce case records.
5. Click **Add**.

## Step 2: Configure field mappings

1. On the *Mapping Configuration* window, click **Mappings** for the entity you created.

   ![Mappings option](/cms_trial/assets/4202f299-bac4-4a8e-8e28-98b15bf132ce.png)

   The *Story to Case field mappings* window appears.

   ![field mapping window](/cms_trial/assets/f0c438d0-d1b1-4230-97ea-61d7ed53f5e4.png)
2. Choose the **Jira Fields** that match the corresponding **Salesforce Field**.  
   You can customize the **Sync Direction** (inbound or outbound) by clicking the green arrow buttons.  
   The example below matches the *Summary* **Jira Issue Field** to the *Subject* **Salesforce Field** and the *Description* **Jira Issue Field** to the *Description* **Salesforce Field**:

   ![field mapping for story to case](/cms_trial/assets/70f3b15a-08db-426d-b2e2-c175059ba765.png)
3. Click **Add**.
4. Click **Save**.

## Step 3: Set default value

Before synchronizing data between Jira and Salesforce, decide how to handle field values not covered by the mapping. Setting default values and actions lets you choose whether you want to copy the original value, force a custom value, leave it empty (if allowed), or raise an error to ensure all field values are synchronized according to your needs. Choose one of the following options:

- **Copy value**:Connector copies and uses the original field value from the source to the destination system. (This is the default option.)   
  For example, if you want Jira issue status to match their equivalents in Salesforce, this option ensures that a Jira issue with the *In Progress* status is set to *In Progress* in Salesforce.
- **Set value**: Connector assigns a predefined value of your choice for the field.   
  For example, if you want all Jira issues to have *UI* as their component in Salesforce, regardless of their original component, you can set *UI* as a default component in Salesforce. This ensures consistent categorization of Jira issues in Salesforce.
- **Set empty**: Connector sets the field value to empty. This option is not available for required fields that need to have their value set.
- **Raise error**: Connector raises an error, and synchronization fails.

When creating a Jira issue from Salesforce, field values are filled based on the mapping or default values you’ve set. However, there’s one exception—Priority.

Jira doesn’t allow the Priority field to be empty, so it always has a default value set. If the Priority field is empty in Salesforce, the value is populated with the Jira default priority instead of the one set in the Connector for Salesforce & Jira. The correct Priority value, as configured in the Connector, will only synchronize after pushing from Salesforce.

To define default values:

1. Click **Configure** next to the selected Jira and Salesforce Field mapping.

   ![configure window](/cms_trial/assets/e5158b7c-f36f-47df-90b7-1d11c079dabf.png)
2. Select a **Jira** **default** and **Salesforce default** value:

   - **Copy value**
   - **Set value** (requires entering your preferred value)
   - **Set empty**
   - **Raise error**

     ![default  value](/cms_trial/assets/d2482a6f-5c79-4304-a882-dd095af19640.png)
3. Click **Save**.

## Step 4: Configure value mappings

Additionally, you can define specific value mapping to match Jira and Salesforce field values. For example:

- Mapping the Jira status *In Progress* with Salesforce Status *Escalated to Dev*.
- Mapping the Jira priority *Major* with Salesforce priority *High*.
- Mapping the Jira component *UI* with Salesforce Case Reason *User Interface*.

If the value is not mapped, Connector for Salesforce & Jira continues according to the defined [default values](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).

To map field values:

1. From Step 2, select the **Sync direction** (inbound or outbound) desired for the field mapping.

   ![Sync direction](/cms_trial/assets/2c0c111a-c0f0-49b9-8e5f-d3250ea896c5.png)
2. Click **Configure.**
3. Under *Configure values*, enter the Jira and Salesforce values accordingly.

   ![configure value.png](/cms_trial/assets/b1db27bc-09b4-4769-a130-05c6eda613f6.png)
4. If the value of the Jira field is the User type, then select available Jira users from the dropdown list.

   ![reporter.png](/cms_trial/assets/765d6235-472a-450d-8bd9-f628244182f4.png)
5. Click **Add**.
6. Click **Save**.

## Step 5: Create inbound-only or outbound-only mappings

By default, a field mapping applies in both directions: a change in Jira updates Salesforce, and a change in Salesforce updates Jira. However, some fields may need to flow in one direction only. For example, you may want agents to update case descriptions in Salesforce without those changes overwriting content in Jira, or the other way around. You can also configure separate value mappings for each direction (inbound or outbound). This also lets you map values in a one-to-many relationship. Create two records for the same field, one for each direction, and then proceed with configuring the value mappings.

For example:

1. Map **Components** Jira field to **Case Reason** Salesforce field separately for each direction (inbound or outbound).

   ![Sync direction.png](/cms_trial/assets/2c0c111a-c0f0-49b9-8e5f-d3250ea896c5.png)
2. For inbound-only mapping, map, for example, **UI** Jira task value with the **User Interface** Case Reason Salesforce value.

   ![contentId-1854180614](/cms_trial/assets/50b2a312-fb38-4b1e-9e70-8c818aa6a759.png)
3. For outbound-only mapping, map, for example, **Installation** Jira task value with the **Packaging** Case Reason Salesforce value.

   ![contentId-1854180614](/cms_trial/assets/6731d294-61d9-4e58-8649-b917978f21ae.png)

## Related information

- [Associate a Salesforce record from Jira](/cms_trial/space/CSFJIRA/3092284964/Associate+a+Salesforce+record+from+Jira/)
- [Change the reporter and assignee of an issue](/cms_trial/space/CSFJIRA/1858371793/Change+the+Reporter+and+Assignee+of+an+issue/)
- [Jira field type to Salesforce field type compatibility](https://apps.appf.re/sfjc/doc/mapping-matrix)