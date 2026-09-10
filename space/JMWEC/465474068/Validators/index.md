# Validators

### **Action Needed: Update your JMWE Validator Configurations**

Atlassian has modified the handling of Rich Text fields (for example, Description and Comments) in Jira expressions, impacting JMWE Validators. Any JMWE Validators that use Rich Text fields will fail.

If you’re impacted, please update your expressions as follows:

`issue.customfield_12345 == “Foobar”` → `issue.customfield_12345.plainText == “Foobar”`

Please reach out to Appfire support if you have any questions or experience any additional errors.

Validators are used to ensure that specific values for an issue are present and/or correct when a transition is triggered. Using Validators, you can guarantee that certain fields have values, that comments have been added, that linked issues exist or have specific status values, or that that field values match requirements (using a scripted Validator).

**Note**: Validators are used to check that an issue has specific data points (fields populated, linked issues, etc.)