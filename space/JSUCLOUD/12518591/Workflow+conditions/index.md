# Workflow conditions

---

**Conditions** determine if a workflow transition is available for the current user to select for a work item. See [JSU Rule Builder - Conditions](/cms_trial/space/JSUCLOUD/1958084925/JSU+Rule+Builder+-+Conditions/) to learn more about how to use conditions in your workflows. JSU provides the following conditions in one rule builder:

| **Condition** | **Check** | **Configuration settings** |
| --- | --- | --- |
| **Date compare** | Compares the value of two date fields | All available date fields  Operators: `= equals, ≠ not equal to, > greater than, ≥ greater than or equal to, < less than, ≤ less than or equal to` |
| **Date expression** | Compares a date field against the current date using a date expression | - All available date fields - Operators: `= equals, ≠ not equal to, > greater than, ≥ greater than or equal to, < less than, ≤ less than or equal to` - Date expression: For example, `2w 4d` |
| **Field value** | Compares the value of a selected field with a constant value | - All available fields - Operators: `= equals, ≠ not equal to, > greater than, ≥ greater than or equal to, < less than, ≤ less than or equal to` - Expected field value dependent on selected field type |
| **Fields required** | Checks if a selected field has a value | - All available fields (multi-select) |
| **Issue status changed** | Checks if the issue status changes on transition | - None |
| **Only selected users** | Checks if the current user is one of the selected users | - All available users |
| The **Only selected users** condition replaces User is in any user. |
| **Regular expression** | Compares the value of a text, number, or URL field against a regular expression. Use this to ensure that values are entered in the correct format. | - Regular expression: For example, `[0-9]+ EUR$` or `[0-9]{4}-[0-9]{4}` - All available fields |
| **Related issue status** | Checks if related issues are in a selected status | - Relation to the issue in transition - Operators: `In`, `Not in` - All available statuses (multi-select) |
| **User in field** | Checks if the user is in a selected field | - All available fields (single-select) |
| **User in group** | Checks if the user is in any of the selected groups | - All available groups (multi-select) |
| **User in project role** | Checks if the user is in any of the selected project roles | All available project roles (multi-select) |

### Supported fields

JSU supports many different field types; system fields, as well as custom fields.

Note that not all field types or combinations are supported. We are continuously adding more and improving the way we support different field types. If you don’t see a field that you need when configuring your conditions, you can raise a request with our [support team](https://appf.re/support).