# Supported custom field types

This page provides a comprehensive reference for mapping Jira custom field types to Simple Issue Language (SIL) data types, enabling developers to properly handle custom field data in their SIL scripts.

## Standard field types reference

SIL automatically converts custom field values to SIL data types following established mapping patterns. The table below lists all supported standard field types and their corresponding SIL representations:

| **Group name** | **Custom field type** | **SIL data type** | **Usage and notes** |
| --- | --- | --- | --- |
| Date and time fields | DateTime | `date` | Supports full DateTime with timezone |
| DatePicker | `date` | Date only, Time component is ignored |
| Numeric fields | Number field | `number` | Supports both integers and decimals |
| Text-based fields | URL field | `string` | Stores complete URL as text |
| Text field | `string` | Single-line text input |
| Textarea | `string` | Multi-line text input  Test formatting behavior in your specific Jira environment. |
| User and group fields | User Picker | `string` | Stores username (not full name) |
| Multi User Picker | `string []` | String array of usernames |
| Group Picker | `string` | Group name as string |
| Multi Group Picker | `string []` | String array of group names |
| Selection fields | Multi Checkboxes | `string []` | String array of selected values |
| Multi Select | `string []` | String array of selected options |
| Radio Buttons | `string` | Single selected value |
| Select List | `string` | Single selected option |
| Cascading Select | `string []` | Two-element array: [parent, child]  - Setting an invalid parent-child combination will be rejected. - When you assign a single value to a cascading select field in SIL, it will be treated as the parent/root selection only. |
| Project and version fields | Project Picker | `string` | Project key |
| Version field | `string` | Version name as string |
| Multi Version field | `string []` | String array of version names |
| Labels Field | `string []` | Array of label strings |

---

## Product-specific fields

| **Product name** | **Notes** |
| --- | --- |
| Jira Service Management (JSM) fields | JSM custom fields are supported with the same type mappings as standard fields. Special fields like SLA data and request participant fields are accessible through dedicated SIL functions. |
| Jira Software fields | Agile fields, such as Sprint and Story Points, are directly accessible like standard custom fields. No special handling required. |
| Portfolio for Jira fields | Portfolio-specific fields can be accessed using the same patterns as standard custom fields. |