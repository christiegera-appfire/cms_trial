# Jira field type to Salesforce field type compatibility

This page outlines which Jira field types are compatible with Salesforce field types in Connector for Salesforce & Jira. When mapping fields between Jira and Salesforce, not every field type pairing works the same way, and some are incompatible. Compatibility depends on the data types involved, the sync direction, and whether the source value matches the format the target field expects.

## **Synchronization direction**

Field mapping compatibility depends not only on the Jira and Salesforce field types but also on the synchronization direction. Some fields are compatible for synchronization from Jira to Salesforce, but are incompatible in the opposite direction from Salesforce to Jira.

- Mappings below apply to both standard and custom Jira and Salesforce field types
- You can get [Jira string type compatibility with Salesforce string textarea](https://support.appfire.com/space/CSFJIRA/3092252116)
- A combination of multiple styles (for example, bold, italics, etc.) on Salesforce does not translate well to Jira Wiki Markup

The *Compatibility matrix* below shows how each Jira field type maps to each Salesforce field type in both directions (Salesforce → Jira and Jira → Salesforce). Use the legend to quickly assess whether a mapping is fully supported, requires a specific format or value mapping to succeed, or should be avoided altogether. For the most common pairings, such as text, numbers, and dates, see the detailed breakdowns in [Common compatible mappings](/cms_trial/space/CSFJIRA/1522369149/Jira+field+type+to+Salesforce+field+type+compatibility/) further down the page.

## Compatibility symbols

|  |  |  |
| --- | --- | --- |
| [green check mark icon] | **Unconditionally compatible** | Mapping is fully supported. |
| [circle icon] | **Format-sensitive** | Mapping is supported only if the field source value is in the expected target format, or you have defined the explicit value mapping.  **If the format doesn’t match,** **sync can fail, the target field may be emptied, or left unchanged,** depending on the field type. For example, when a Jira string field mapped to a Salesforce picklist field, when the field value (high priority) matches exactly a picklist option (high priority defined in Salesforce), or an explicit value mapping is defined for it. |
| ⚠️ | **Not recommended** | Mapping may work with explicit value mapping configured, but fails in most cases.  In most cases, a more suitable field type pairing exists in Jira or Salesforce.  For example: mapping a Jira number field to a Salesforce date field requires a value mapping and is fragile; a Jira date field is the better choice. |
| ❌ | **Incompatible** | These field types cannot be mapped.  This includes fields that are structurally incompatible, and Jira fields that are read-only (system-managed), which block any mapping from Salesforce to Jira. |

## Compatibility matrix

Rows are Jira field types and Columns are Salesforce field types. For each Jira field type, there are two rows representing the synchronization direction.

|  | Direction | boolean | date | datetime | double  currency  percent | encryptedstring | id  reference | int | multipicklist | picklist | string,  textarea | Text Area (Rich) | url  phone  email |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| array←component→ | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ❌ | [circle icon] | [circle icon] | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ❌ | [green check mark icon] | [green check mark icon] | ❌ |
| array←group→ | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | [circle icon] | [circle icon] | [circle icon] | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ⚠️ | [green check mark icon] | [green check mark icon] | ❌ |
| array←option→ | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | [circle icon] | [circle icon] | [circle icon] | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ❌ | [green check mark icon] | [green check mark icon] | ❌ |
| array←string→ | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ❌ | [circle icon] | [circle icon] | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ❌ | [green check mark icon] | [green check mark icon] | ❌ |
| array←version→ | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ❌ | [circle icon] | [circle icon] | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ❌ | [green check mark icon] | [green check mark icon] | ❌ |
| date | **SF → Jira** | ❌ | [green check mark icon] | ❌ | ⚠️ | ❌ | ❌ | ⚠️ | ⚠️ | [circle icon] | ⚠️ | ⚠️ | ❌ |
| **Jira → SF** | ⚠️ | [green check mark icon] | ❌ | ⚠️ | ❌ | ⚠️ | ⚠️ | [circle icon] | [circle icon] | [green check mark icon] | [green check mark icon] | ⚠️ |
| datetime | **SF → Jira** | ❌ | ❌ | [green check mark icon] | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | ⚠️ | ❌ |
| **Jira → SF** | ❌ | ❌ | [green check mark icon] | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | [green check mark icon] | [green check mark icon] | ❌ |
| issuetype | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | [minus icon] | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | [circle icon] | [circle icon] | [green check mark icon] | [green check mark icon] | ❌ |
| number | **SF → Jira** | ⚠️ | ⚠️ | ⚠️ | [green check mark icon] | ❌ | ⚠️ | [green check mark icon] | ⚠️ | ❌ | [circle icon] | [green check mark icon] | ⚠️ |
| **Jira → SF** | ⚠️ | ⚠️ | ⚠️ | [green check mark icon] | ❌ | ⚠️ | [green check mark icon] | [circle icon] | ❌ | [green check mark icon] | [green check mark icon] | ⚠️ |
| option | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | [circle icon] | [circle icon] | [circle icon] | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | [circle icon] | [circle icon] | [green check mark icon] | [green check mark icon] | ❌ |
| option-with-child | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | [circle icon] | [circle icon] | [circle icon] | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | [circle icon] | [circle icon] | [green check mark icon] | [green check mark icon] | ❌ |
| priority | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ | [circle icon] | [circle icon] | [circle icon] | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | [circle icon] | [circle icon] | [green check mark icon] | [green check mark icon] | ❌ |
| project | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | [circle icon] | [circle icon] | [green check mark icon] | [green check mark icon] | ❌ |
| resolution | **SF → Jira** | [green check mark icon] | [green check mark icon] | [green check mark icon] | [green check mark icon] | ⚠️ | [green check mark icon] | [green check mark icon] | ⚠️ | [green check mark icon] | [green check mark icon] | [green check mark icon] | [green check mark icon] |
| **Jira → SF** | ❌ | ⚠️ | ⚠️ | ❌ | ❌ | [circle icon] | ❌ | [circle icon] | [circle icon] | [green check mark icon] | [green check mark icon] | [circle icon] |
| sd-customerrequesttype | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | [circle icon] | [green check mark icon] | [green check mark icon] | ❌ |
| status | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | [circle icon] | [circle icon] | [green check mark icon] | [green check mark icon] | ❌ |
| string | **SF ←Jira** | [green check mark icon] | [green check mark icon] | [green check mark icon] | [green check mark icon] | ⚠️ | [green check mark icon] | [green check mark icon] | ⚠️ | [green check mark icon] | [circle icon] | [circle icon] | [green check mark icon] |
| **Jira → SF** | [circle icon] | ⚠️ | ⚠️ | [circle icon] | ❌ | [circle icon] | [circle icon] | [circle icon] | [circle icon] | [circle icon] | [circle icon] | [circle icon] |
| string textarea | **SF → Jira** | [green check mark icon] | [green check mark icon] | [green check mark icon] | [green check mark icon] | ⚠️ | [green check mark icon] | [green check mark icon] | ⚠️ | [green check mark icon] | [circle icon] | [circle icon] | [green check mark icon] |
| **Jira → SF** | [circle icon] | ⚠️ | ⚠️ | [circle icon] | ❌ | [circle icon] | [circle icon] | [circle icon] | [circle icon] | [circle icon] | [circle icon] | [circle icon] |
| timetracking - original estimate | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | [green check mark icon] | ❌ | ❌ | [green check mark icon] | ❌ | ❌ | [green check mark icon] | [green check mark icon] | ❌ |
| timetracking - Σ original estimate | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | [green check mark icon] | ❌ | ❌ | [green check mark icon] | ❌ | ❌ | [green check mark icon] | [green check mark icon] | ❌ |
| timetracking - remaining estimate | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | [green check mark icon] | ❌ | ❌ | [green check mark icon] | ❌ | ❌ | [green check mark icon] | [green check mark icon] | ❌ |
| timetracking - Σ remaining estimate | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | [green check mark icon] | ❌ | ❌ | [green check mark icon] | ❌ | ❌ | [green check mark icon] | [green check mark icon] | ❌ |
| timetracking - time spent | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | [green check mark icon] | ❌ | ❌ | [green check mark icon] | ❌ | ❌ | [green check mark icon] | [green check mark icon] | ❌ |
| timetracking - Σ time spent | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | [green check mark icon] | ❌ | ❌ | [green check mark icon] | ❌ | ❌ | [green check mark icon] | [green check mark icon] | ❌ |
| user | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | [circle icon] | ❌ | ⚠️ | [circle icon] | [circle icon] | [circle icon] | ⚠️ |
| **Jira → SF** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | [circle icon] | [circle icon] | [green check mark icon] | [green check mark icon] | ❌ |
| version | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Jira → SF** | ⚠️ | ❌ | ❌ | ⚠️ | ❌ | ❌ | ⚠️ | [circle icon] | [circle icon] | [green check mark icon] | [green check mark icon] | ❌ |
| watchers | **SF → Jira** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Jira → SF** | ❌ | ❌ | ❌ | [green check mark icon] | ❌ | ❌ | [green check mark icon] | ❌ | ❌ | ❌ | ❌ | ❌ |

## Common compatible mappings

**Text fields** - Jira *string* and *string textarea* mapped to Salesforce *string* and *Text Area* support mapping in both directions. However, compatibility is **format-sensitive**: sync succeeds only when the source value matches the expected target format, or a value mapping is configured to handle the conversion. If neither condition is met, the sync leave the target field empty or unchanged.

To learn more, see [Jira string type compatibility with Salesforce string textarea](/cms_trial/space/CSFJIRA/3092252116/Jira+string+type+compatibility+with+Salesforce+string+textarea/)

|  | Direction | string  textarea | Text Area (Rich) |
| --- | --- | --- | --- |
| string | **SF → Jira** | [circle icon] | [circle icon] |
| **Jira → SF** | [circle icon] | [circle icon] |
| string textarea (richtext) | **SF → Jira** | [circle icon] | [circle icon] |
| **Jira → SF** | [circle icon] | [circle icon] |

**Number** - Jira number with Salesforce int, double, currency, and percent are unconditionally compatible in both directions.

|  | Direction | int | double  currency  percent |
| --- | --- | --- | --- |
| number | **SF → Jira** | [green check mark icon] | [green check mark icon] |
| **Jira → SF** | [green check mark icon] | [green check mark icon] |

**Date** -Jira date with Salesforce date field type is unconditionally compatible in both directions.

|  | Direction | date |
| --- | --- | --- |
| date | **SF → Jira** | [green check mark icon] |
| **Jira → SF** | [green check mark icon] |

**Datetime** -Jira datetime with Salesforce datetime field type is unconditionally compatible in both directions.

|  | Direction | datetime |
| --- | --- | --- |
| datetime | **SF → Jira** | [green check mark icon] |
| **Jira → SF** | [green check mark icon] |

## Incompatible fields

| Jira field types incompatible with Salesforce fields | Salesforce field types incompatible with Jira field types |
| --- | --- |
| - array←issuelinks→ - array←worklog→ - array←attachment→ - comments-page - progress - securitylevelarray←sd-customerorganization→ - votes | - address - location |