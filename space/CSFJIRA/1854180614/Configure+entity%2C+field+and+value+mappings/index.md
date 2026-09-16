# Configure entity, field and value mappings

Select a template or create your own mappings, then control how Jira work items and Salesforce records synchronize.

Entity mappings define which Jira work item types correspond to which Salesforce object types. Field mappings then define how data moves between their fields. You can also translate values between the two systems so each team can continue using its own terminology.

Choose a starting point: use a template for a preconfigured common workflow, or create mappings from scratch for a custom use case. Templates remain customizable after you select them.

## Before you start

Make sure you have:

- Jira administrator rights. Only administrators can configure mappings.
- The required Salesforce objects available in Jira. [Configure available Salesforce objects](/cms_trial/space/CSFJIRA/1873379599/Set+up+a+connection+to+Salesforce+(Jira+Cloud)/) before you map them.
- A binding between the Jira project and a Salesforce connection. Learn about [bindings](/cms_trial/space/CSFJIRA/1873379785/Bind+a+space+to+a+connection+(Jira+Cloud)/).
- Compatible Jira and Salesforce field types. Check [field type compatibility](/cms_trial/space/CSFJIRA/1522369149/Jira+field+type+to+Salesforce+field+type+compatibility/) before adding field mappings.

### **Open the mapping configuration**

To reach the mapping options:

1. In Jira, select **Apps** from the left sidebar.
2. Next to **Connector for Salesforce**, select **Menu** (▢)> **App settings**.
3. Under **Connector for Salesforce**, select **Bindings**.
4. For the binding you want to configure, click **Menu** (▢)> **Edit**.

## Select how to create mappings

Both methods lead to the same mapping configuration. The difference is how much of the initial setup the Connector provides.

| Option | Best for | What you configure |
| --- | --- | --- |
| **Use template** | A supported, common workflow where you want a faster starting point. | Review the preconfigured entity, field, sync-direction, and value mappings. Add or adjust mappings as needed. |
| **Create from scratch** | A custom Jira work item type, Salesforce object, or workflow that does not match a template. | Select every entity pair and field pair, then set sync direction, default handling, and value mappings. |

Available templates: **Bug escalation**, **Feature requests**, **Deal enablement**, and **Deal & feature sync**. A template provides an initial configuration with entity, field, and value mappings. See [Configure entity and field mappings with templates](/cms_trial/space/CSFJIRA/3664152459/Configure+entity+and+field+mappings+from+templates/) for guidance.

## Configuration options

The following options are available whether you begin with a template or create mappings from scratch.

### Entity mappings

An entity mapping links one Jira work item type with one Salesforce object type. For example, you can map a Jira Bug to a Salesforce Case, or a custom Technical debt work item type to a Case.

| Option | Description |
| --- | --- |
| Jira work item type | The Jira type that participates in the workflow. |
| Salesforce object type | The corresponding Salesforce object made available through the connection settings. |
| Additional entity mappings | Add more entity pairs when the binding needs to support multiple workflows. |

### Field mappings

A field mapping links a Jira field to a compatible Salesforce field within an entity mapping. It determines which data can stay current between the two systems.

| Option | Description |
| --- | --- |
| Field pair | The Jira field and its Salesforce counterpart, such as Summary and Subject. |
| Compatibility | Map only compatible field types. Incompatible field types may not synchronize correctly. |
| Configuration | Open a field mapping's menu and select Configure to define default handling and specific value mappings. |

### Sync direction

Sync direction controls which system can send updates through a field mapping. Use the arrow controls on the field mapping to set one of these behaviors:

| Direction | Data flow | Use when |
| --- | --- | --- |
| Bidirectional | Jira ↔ Salesforce | Updates made in either system should update the other system. This is the default behavior. |
| Inbound only | Salesforce → Jira | Salesforce is the source of truth for the mapped field. |
| Outbound only | Jira → Salesforce | Jira is the source of truth for the mapped field. |

### Default handling for unmapped values

For each side of a field mapping, choose what happens when an incoming value is not covered by a specific value mapping:

| Option | Description |
| --- | --- |
| Copy value | Copy the source value to the destination field. This is the default option. |
| Set value | Use a predefined value that you enter, regardless of the incoming value. |
| Set empty | Leave the destination field empty. Not available for required fields. |
| Raise error | Stop synchronization and report an error instead of applying an unmatched value. |

Jira does not allow Priority to be empty. When a Jira work item is created from Salesforce and Salesforce Priority is empty, Jira uses its own default priority rather than the Connector's configured default. The Connector's configured Priority value is applied only after a later push from Salesforce.

### Value mappings

Value mappings translate specific values when Jira and Salesforce use different terminology. For example, you can map Jira priority Highest to Salesforce priority Critical, or Jira component UI to Salesforce Case Reason User Interface.

| Option | Description |
| --- | --- |
| Mapped values | The Jira and Salesforce values that should correspond. |
| Unmapped values | Handled by the default handling option selected for that field mapping. |
| User fields | When the Jira field is a user type, select from the available Jira users; the value maps to the corresponding Salesforce user record. |
| Different mappings by direction | Inbound-only and outbound-only records for the same field pair can use different value mappings in each direction, supporting one-to-many value relationships. |

## Related pages

- [Configure entity and field mappings with templates](/cms_trial/space/CSFJIRA/3664152459/Configure+entity+and+field+mappings+from+templates/)
- [Configure entity and field mappings from scratch](/cms_trial/space/CSFJIRA/3664152584/Configure+entity+and+field+mappings+from+scratch/)

- [Configure field displays and access the Details screen](/cms_trial/space/CSFJIRA/1873511110/Configure+field+displays+and+access+the+Details+screen/)
- [Import value mappings](/cms_trial/space/CSFJIRA/1873347626/Import+value+mappings/)
- [Configuring Jira cascading fields to work with Salesforce dependent fields](/cms_trial/space/CSFJIRA/1873413246/Configuring+Jira+cascading+fields+to+work+with+Salesforce+dependent+fields/)
- [Jira field type to Salesforce field type compatibility](/cms_trial/space/CSFJIRA/1522369149/Jira+field+type+to+Salesforce+field+type+compatibility/)
- [Change the Reporter and Assignee of an issue](/cms_trial/space/CSFJIRA/1858371793/Change+the+Reporter+and+Assignee+of+an+issue/)