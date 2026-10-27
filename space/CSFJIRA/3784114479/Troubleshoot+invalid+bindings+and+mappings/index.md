# Troubleshoot invalid bindings and mappings

Bindings and mappings in Connector for Salesforce & Jira can become invalid when your Jira or Salesforce configuration changes. For example, this can happen when you delete a Jira work item type or field, or when you migrate from Jira Data Center to Jira Cloud.

Invalid mappings can cause errors when configuring bindings or synchronizing data between Jira and Salesforce.

This article explains how to identify invalid bindings and mappings and resolve common configuration issues.

## Why do bindings and mappings become invalid?

Bindings connect Jira spaces to Salesforce connections. Mappings define which Jira work item types, fields, and values correspond to Salesforce objects, fields, and values.

A binding or mapping can become invalid when:

- A Jira space, work item type, or field referenced by a mapping has been deleted or is no longer available through the connection.
- A Salesforce object or field used in a mapping has been removed or is no longer available through the connection.
- You migrate from Jira Data Center to Jira Cloud: Migrated bindings can contain references to work item types or fields that do not exist in the Cloud environment or are not available in the corresponding Jira space.

## Find invalid bindings and mappings

You can use the filter on the Bindings page to identify bindings that contain invalid configuration.

1. In Jira, go to **Settings > Apps**.
2. Under **Connector for Salesforce**, select **Bindings**.
3. Click the **Show only invalid bindings** filter to display bindings that contain invalid items.

   ![image-20261027-090714.png](/cms_trial/assets/c4b0688c-9188-4808-9273-19a5242aa5c6.png)
4. Review the bindings displayed in the list:

   1. If the Jira space no longer exists, the binding is grayed out and cannot be edited.   
      To remove it, click **Menu** (▢) > **Delete**.

      ![image-20261027-090922.png](/cms_trial/assets/394f6d33-a258-4b02-8532-5c22f0860d49.png)
   2. If the binding is editable, it contains some invalid mappings that need to be reviewed.   
      Click **Menu** (▢) > **Edit** to identify and resolve the invalid mappings.

      ![image-20261027-091528.png](/cms_trial/assets/1e5905cb-8f1f-45d8-9cf5-347260754a80.png)

## Resolve invalid mappings

If a Jira work item type, Salesforce object type, or a field used in a mapping has been deleted or is no longer available, edit or remove the affected mapping.

1. Click the **Show only invalid mappings** filter to display entity mappings that contain invalid items.

   ![image-20261027-091731.png](/cms_trial/assets/a0a1c6e0-614d-4f6b-8113-3d3fc256f838.png)
2. Review the entity mappings displayed in the list. Depending on the error, you may need to remove an invalid entity mapping or open an editable mapping to fix its field mappings.

   1. If an entity mapping references a Jira work item type or Salesforce object that is no longer available, the entity mapping is flagged. If you still need the mapping, check whether you can make the missing entity available again in Jira or Salesforce, or map it to a different entity type.   
      Otherwise, click the **Delete** (▢)icon to remove the mapping.

      ![remove the mapping](/cms_trial/assets/ffb4d273-043d-4a7e-bd42-c56bbc0dce45.png)
   2. If an entity mapping is editable, click it to open the *Field mapping* window.  
      Review the flagged field mappings and choose one of the following actions:

      1. To remove an invalid field mapping, click **Menu** (▢) > **Delete**.

         ![remove an invalid field mapping](/cms_trial/assets/b3b459c8-f4a0-4c3e-9197-66aba714cfc7.png)
      2. To fix an invalid field mapping, select an existing field from the dropdown.

         ![Fix invalid mappings](/cms_trial/assets/3728d9e5-060b-4cbc-a2e3-c0cd0753c04c.png)
3. After resolving all invalid mappings, click **Save** to apply your changes.

Before deleting a binding or mapping, make sure you no longer need it. Removing bindings or mappings can affect synchronization between Jira and Salesforce.

## Related documentation

- [Bind a space to a connection (Jira Cloud)](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/)
- [Configure entity and field mappings from scratch](/cms_trial/space/CSFJIRA/3664152584/Configure+entity+and+field+mappings+from+scratch/)
- [Configure entity, field and value mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field%2C+and+value+mappings/)