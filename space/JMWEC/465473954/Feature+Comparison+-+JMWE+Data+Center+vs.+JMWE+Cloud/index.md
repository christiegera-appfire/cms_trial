# Feature Comparison - JMWE Data Center vs. JMWE Cloud

The main difference between **JMWE for Jira Cloud** and **JMWE for Jira Data Center** extensions is that Data Center uses Groovy scripting whereas Cloud uses a combination of Nunjucks and Jira expressions.

Below is a list of extensions supported by each product and their equivalents, if applicable.

## JMWE Conditions

| **Condition** | **JMWE for DC** | **JWME for Cloud** | **Notes** |
| --- | --- | --- | --- |
| Scripted (Groovy) Condition | ✅ | ✅ Build-your-own (scripted) Condition | JMWE Data Center uses Groovy scripting, while JMWE Cloud uses Nunjucks expressions and Jira expressions. |
| Current Status Condition | ✅ | ✅ |  |
| Related Issues Condition | ✅ | ✅ Linked Issues Condition |  |
| Related Issues Status Condition | ✅ | ✅ Linked Issues Status Condition |  |
| Hide transition | ✅ | ✅ (see note) | Originally supported by JMWE for Jira Data Center but currently maintained by Atlassian on Jira Cloud as part of **Hide from User**. |
| Previous Status Condition | ✅ | ✅ (see note) | Originally supported by JMWE for Jira Data Center but currently maintained by Atlassian on Jira Cloud. |
| Separation of Duties Condition | ✅ | ✅ (see note) | Originally supported by JMWE for Jira Data Center but currently maintained by Atlassian on Jira Cloud. |
| Shared Condition | ✅ | ❌ | Shared Conditions are not migrated as this functionality is not available on Jira Cloud. |
| User Condition | ✅ | ✅ |  |

## JMWE Validators

| **Validator** | **JMWE for DC** | **JMWE for Cloud** | **Notes** |
| --- | --- | --- | --- |
| Scripted (Groovy) Validator | ✅ | ✅ Build-your-own (scripted) Validator | JMWE Data Center uses Groovy scripting, while JMWE Cloud uses Nunjucks expressions and Jira expressions. |
| Comment Required Validator | ✅ | ✅ |  |
| Fields Required Validator | ✅ | ✅ (see note) | Field Required validator exists in both Native Jira and JMWE Cloud; migrated Validators will be mapped to the **Native** version. |
| Related Issues Validator | ✅ | ✅ Linked Issues Validator |  |
| Related Issues Status Validator | ✅ | ✅ Linked Issues Status Validator |  |
| User Validator | ✅ | ✅ |  |
| Field has been modified Validator | ✅ | ✅ (see note) | Originally supported by JMWE for Jira Data Center but currently maintained by Atlassian on Jira Cloud. |
| Field has single value Validator | ✅ | ✅ (see note) | Originally supported by JMWE for Jira Data Center but currently maintained by Atlassian on Jira Cloud. |
| Previous Status Validator | ✅ | ✅ (see note) | Originally supported by JMWE for Jira Data Center but currently maintained by Atlassian on Jira Cloud. |
| Parent Status Validator | ✅ | ✅ (see note) | Originally supported by JMWE for Jira Data Center but currently maintained by Atlassian on Jira Cloud. |
| Shared Validator | ✅ | ❌ | Shared Validators are not migrated as this functionality is not available on Jira Cloud. |

## JMWE Post-Functions

### Deprecated post functions will be removed

Due to updates in the Atlassian platform, the deprecated post functions in this section will be completely removed from JMWE Cloud by the **end of December 2025**. These post functions have been obsolete for some time, and now must be replaced. When this change occurs, you will not be able to:

- **Add** an obsolete post function
- **Edit** any existing obsolete post functions
- **Execute any obsolete post function - automatically or manually**

In order for your automations to continue to function, **you** ***must migrate*** obsolete post functions before they are removed. All functions that are possible with deprecated post functions are available in their current equivalents.

| **JMWE for Data Center** | **JMWE for DC** | **JMWE for Cloud** | **Notes** |
| --- | --- | --- | --- |
| Add field value to parent issue | ✅ | ✅ (see note) | Handled by **Set issue fields** in Cloud. |
| Assign issue | ✅ | ✅ |  |
| Assign to last role member (Deprecated) | ✅ | ✅ | Will migrate to deprecated post function in Jira Cloud; has been replaced with **Assign issue(s)**. |
| Assign to role member (Deprecated) | ✅ | ✅ | Will migrate to deprecated post function in Jira Cloud; has been replaced with **Assign issue(s)**. |
| Clear field(s) | ✅ | ✅ |  |
| Clear field(s) of related issues (Deprecated) | ✅ | ✅ (see note) | Handled by **Clear fields** in Cloud. |
| Comment issue | ✅ | ✅ |  |
| Comment related issues (Deprecated) | ✅ | ✅ (see note) | Handled by **Comment issue(s)** in Cloud. |
| Copy field value from parent issue (Deprecated) | ✅ | ✅ (see note) | - This post-function is deprecated as of JMWE for Data Center version 7.2.0 and later - Handled by **Copy issues fields** when migrated to Cloud |
| Copy field value from related issues (Deprecated) | ✅ | ✅ (see note) | - This post-function is deprecated as of JMWE for Data Center version 7.2.0 and later - Handled by **Copy issues fields** when migrated to Cloud |
| Copy field value to parent issue (Deprecated) | ✅ | ✅ (see note) | - This post-function is deprecated as of JMWE for Data Center version 7.2.0 and later - Handled by **Copy issues fields** when migrated to Cloud |
| Copy field value to related issues (Deprecated) | ✅ | ✅ (see note) | - This post-function is deprecated as of JMWE for Data Center version 7.2.0 and later - Handled by **Copy issues fields** when migrated to Cloud |
| Copy issue fields | ✅ | ✅ |  |
| ​Copy value from field to field (Deprecated) | ✅ | ✅ (see note) | This post-function is obsolete in the JMWE for Data Center version 7.2.0 and later and handled by Copy issues fields when migrated to Cloud |
| Create / Clone issue(s) | ✅ | Create issue(s) |  |
| Delete issue(s) | ❌ | ✅ |  |
| Display message to user | ✅ | ✅ |  |
| Email issue | ✅ | ✅ |  |
| Increase value of field | ✅ | ✅ |  |
| Link issues to the current issue | ✅ | ✅ |  |
| Log Work | ❌ | ✅ |  |
| Return to Previous Status | ✅ | ✅ |  |
| Send Slack message | ❌ | ✅ |  |
| Scripted operation on issue | ✅ (Groovy) | ✅ (see note) | JMWE Data Center uses Groovy scripting, while JMWE Cloud uses Nunjucks expressions and Jira expressions. |
| Sequence of Post-functions | ❌ | ✅ |  |
| Set field value (Deprecated) | ✅ | ✅ | Handled by **Set issue fields** in Cloud. |
| Set field value of related issues (Deprecated) | ✅ | ✅ (see note) | Handled by **Set issue fields** in Cloud. |
| Set field value from User Property Value | ✅ | ✅ |  |
| Set issue fields | ✅ | ✅ |  |
| Set issue security level based on current user's project role | ✅ | ✅ (see note) | Originally supported by JMWE for Jira Data Center but currently maintained by Atlassian on Jira Cloud. |
| Set issue, user or project Entity Property value | ✅ | ✅ Set Entity Property value | Handled by **Set Entity Property value** in Cloud. |
| Set Issue Security Level | ❌ | ✅ |  |
| Shared Action | ✅ | ✅ |  |
| Transition current issue | ✅ | ✅ | Handled by **Transition issue(s)** in Cloud. |
| Transition parent issue (Deprecated) | ✅ | ✅ (see note) | Handled by **Transition issue(s)** in Cloud. |
| Transition related issues (Deprecated) | ✅ | ✅ (see note) | Handled by **Transition issue(s)** in Cloud. |
| Unlink issues from the current issue | ✅ | ✅ |  |