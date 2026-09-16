# Configure entity and field mappings from templates

Before any data can sync between Jira and Salesforce, the two systems need to know which entities belong together. Entity mappings define these relationships, for example, telling the Connector that a Jira task corresponds to a Salesforce case, or that a Jira epic corresponds to a Salesforce opportunity. Once you establish that relationship, Jira work items and Salesforce records can be associated and kept in sync.

From there, field mappings determine how individual fields stay current between the two systems. For example, you can map the description field in Jira to its equivalent in Salesforce.

You can also define value mappings to handle terminology differences between the two systems, such as mapping Jira's In Progress status to Salesforce's Escalated to Dev, so each team continues working with the values that make sense in their own tool.

This page helps you configure entity mappings and fields with templates.  
If you want to configure your own mappings, go to the [Configure entity and field mappings from scratch](/cms_trial/space/CSFJIRA/3664152584/Configure+entity+and+field+mappings+from+scratch/) page.

## Before you start

Make sure you have:

- Administrator rights in Jira - only administrators can set up the mappings
- Added all required Salesforce objects to be available in Jira, see more [Available Salesforce objects](/cms_trial/space/CSFJIRA/1853653945/Configure+connection+settings/).
- Created a [Binding between a project and a connection](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/).
- Understand Jira field types compatibility with Salesforce field types to properly map the fields. Visit the [Jira Field Type to Salesforce Field Type compatibility](/cms_trial/space/CSFJIRA/1522369149/Jira+field+type+to+Salesforce+field+type+compatibility/) page to learn more.

## Configure mapping with templates

You can select a template with ready entity and field mappings. There are four templates you can choose from:

- **Bug escalation**:To track unresolved bugs and bring cases from Salesforce to your engineering team in Jira. Maps Jira Bug work item type with Salesforce Case object type.
- **Feature requests**: To send customer feature requests from Salesforce into Jira and track them as they move through development in both platforms. Maps Jira Story work item type to Salesforce Case object type.
- **Deal enablement**: Connect Salesforce opportunities to Jira work items. Maps Jira Epic work item type to Salesforce Opportunity object type.
- **Deal & feature sync:** Bring sales, product, and engineering into one workflow. Send Salesforce opportunities and customer requests to Jira, so every team stays aligned and always up to date. Maps Jira Epic work item type to Salesforce Opportunity object type, and Jira Story work item type to Salesforce Case object type.

  ![Templates](/cms_trial/assets/2c76ff7f-b0bd-46ff-8e1a-55ddb3bae6db.png)

1. Select **Apps** from the left sidebar in Jira.
2. Next to *Connector for Salesforce,* click **Menu** (▢) > **App settings**.

   ![App settings](/cms_trial/assets/4e9d160b-7cae-4c49-ad97-3db4f65a1b99.png)

1. Under *Connector for Salesforce*, click **Bindings**.
2. Click **Use template** to select the template you want. For example, **Bug escalation**.

   ![Use templaete selectio](/cms_trial/assets/eedcfcc3-5373-48ac-8fba-b5db12aa59d2.png)

   The *Entity mapping* stepopens, and the Jira work item bug type is already mapped to the Salesforce Case object type.

   ![image-20260904-133910.png](/cms_trial/assets/2e904484-977f-473c-b538-6102ac74fef7.png)
3. (Optional) If you want to add more entity mappings, select the Jira work item type and the corresponding Salesforce object type, and click **Add entity mapping.**

   ![image-20260904-133452.png](/cms_trial/assets/427f7b53-6a70-4559-b416-acb4c2fe2a87.png)
4. Select the **Bug -> Case** entity mapping to open its field mapping.   
   The *Field mappings* define how individual fields of items and objects interact. For the Bug -> Case entity mapping, the following fields are mapped:

| **Jira field** | **Sync direction** | **Salesforce field** |
| --- | --- | --- |
| Summary | ← → Bidirectional | Subject |
| Status | ← → Bidirectional | Status |
| Priority | ← → Bidirectional | Priority |
| Decription | ← → Bidirectional | Description |

![image-20260916-084130.png](/cms_trial/assets/4df34e9a-4010-4808-b2f6-906d6d4ab077.png)

1. (Optional) If you want to add more field mappings, select the **Jira field** that matches the corresponding **Salesforce field**,andclick **Add field mapping**.  
   Make sure the fields you map are compatible. To learn more, see [Jira Field Type to Salesforce Field Type compatibility](/cms_trial/space/CSFJIRA/1522369149/Jira+field+type+to+Salesforce+field+type+compatibility/).
2. You can customize the **Sync direction** (inbound or outbound) by clicking the arrow buttons.

   ![image-20260904-143627.png](/cms_trial/assets/dacb458d-5f67-4dec-bfe6-d3cdcfa3294d.png)
3. Click the **Menu** (▢) icon next to **Priority -> Priority** field mapping and select **Configure** to open its value mapping.   
   The *Value mappings* define how to handle field values.

   1. Set default value - decide how to handle field values not covered by the mapping. To learn more, see the [Set default value](/cms_trial/space/CSFJIRA/3664152584/Configure+entity+and+field+mappings+from+scratch/) section.
   2. (Optional) Configure value mappings - you can also define specific value mappings to match Jira and Salesforce field values. To learn more, see the [Configure value mappings](/cms_trial/space/CSFJIRA/3664152584/Configure+entity+and+field+mappings+from+scratch/) section.
4. Click **Next**.

Using the Bug escalation template, the Jira work item type *Bug* maps to the Salesforce *case* object type. Within this mapping, four fields sync bidirectionally between the two systems: summary to subject, status to status, priority to priority, and description to description. The priority field mapping is further configured with value mappings, so priority values stay aligned between Jira and Salesforce. With this in place, teams can track and update bugs reported as Salesforce cases in Jira, keeping both teams in sync.

## Next

- [Associate Salesforce records from Jira](/cms_trial/space/CSFJIRA/3663725288/Associate+Jira+work+items+with+Salesforce+records+from+Jira/)
- If you want to configure your custom mappings, go to the [Configure entity and field mappings from scratch](/cms_trial/space/CSFJIRA/3664152584/Configure+entity+and+field+mappings+from+scratch/) page.

## 