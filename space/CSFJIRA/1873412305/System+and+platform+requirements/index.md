# System and platform requirements

## Jira

All Jira Cloud editions are supported: Jira Core, Jira Service Management, and Jira Software.

## Web browsers

- Connector for Salesforce & Jira Cloud supports [all web browsers supported by Jira Cloud](https://confluence.atlassian.com/cloud/supported-browsers-744721663.html).

## Salesforce editions

The following Salesforce editions are supported on Jira Cloud. This covers both production and sandbox instances:

| Platform | Supported | Description |
| --- | --- | --- |
| Salesforce Professional | ✅ | Salesforce Professional Edition has certain limitations, especially with regards to Apex trigger support. Automated synchronization from Salesforce to Jira is not possible though synchronization from Jira to Salesforce is possible. For more information, see [Automate your integration](/cms_trial/space/CSFJIRA/1874001954/Automate+your+integration/). |
| Salesforce Enterprise | ✅ |  |
| Salesforce Unlimited | ✅ |  |
| Salesforce Performance | ✅ |  |
| Salesforce Developer | ✅ |  |
| Salesforce Essentials | ❌ | Currently unsupported |

## Notes

- Both Salesforce Classic and Lightning Experience are supported.
- Connector for Salesforce & Jira requires [installation](/cms_trial/space/CSFJIRA/1758232704/Install+the+Salesforce+package+in+Salesforce/) of an AppExchange-certified managed package. This is a managed package so it will not be pushed automatically to Professional Edition instances but Salesforce API access for this Connector will be automatically enabled in the organization.
- Jira next-gen projects are currently not fully supported.
- APEX Triggers cannot be developed on Professional Edition, instead develop the code in Developer Edition and deploy it to Professional Edition, see [Develop code in Developer Edition and deploy it to Professional Edition](https://help.salesforce.com/s/articleView?id=000323569&type=1) for further details.

## Related information

- [Salesforce and JIRA Server Connector Versus Cloud Connector Comparison](/cms_trial/space/CSFJIRA/1873510679/Classic+Connector+for+Salesforce+and+NextGen+Connector+for+Salesforce+%26+Jira+comparison/)
- [Installing the Connector](/cms_trial/space/CSFJIRA/1873477874/Installation/)