# How to handle "Field is set to raise an error for unmapped values" warning

## Summary

You see the **Field is set to raise an error for unmapped values** warning message when creating a new Jira issue in Salesforce. Despite the warning, you can still create the Jira issue, but you won’t be able to synchronize it between Jira and Salesforce because the provided values are not mapped.

![Field is set to raise an error for unmapped values.png](/cms_trial/assets/56cc2141-c141-4787-9e1a-941eae5d53a4.png)

## Cause

This warning appears when the populated field value doesn't have a corresponding mapping in the Connector for Salesforce and Jira configuration, and the default value for unmapped values is set to **Raise error**.

## Resolution

To address this warning, follow these steps:

### **Configure value mapping**

1. Go to **Settings** > **Apps**. In the sidebar, under *Connector for Salesforce*, select **Bindings**.
2. On the **Bindings** screen, select the binding to configure and click **Mapping**.
3. Select the field mapping and click **Configure**.
4. Under *Configure values*, enter the values for Jira and Salesforce accordingly.
5. Click **Add** and **Save**.

For detailed instructions, see [Configure value mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).

### Set default value (Optional)

To prevent the configuration from affecting synchronization, you can change the default action:

1. Go to **Settings** > **Apps**. In the sidebar, under *Connector for Salesforce*, select **Bindings**.
2. On the **Bindings** screen, select the binding to configure and click **Mapping**.
3. Select the field mapping and click **Configure**.
4. Under *Default Value*, select a **Jira** **default** and **Salesforce default** value.
5. Click **Save.**

For detailed instructions, see [Set default value](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).

## Outcome

After updating, the error is cleared. You can continue to create the Jira issue and follow with synchronization process without errors.

## Related content

- [Create a Jira Issue from Salesforce with Jira Issues (NextGen)](https://appfire.atlassian.net/wiki/spaces/470745117/pages/1464041856/Create+a+Jira+Issue+from+Salesforce+with+Jira+Issues+NextGen?atlOrigin=eyJpIjoiMGQ5NzU0MDBkMGQ3NDUyYWFlNDVhM2Y1YmI2YjM5ZGQiLCJwIjoiYyJ9)
- [Configure value mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/)
- [Set default value](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/)