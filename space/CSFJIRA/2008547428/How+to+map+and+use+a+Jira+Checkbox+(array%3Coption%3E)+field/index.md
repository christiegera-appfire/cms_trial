# How to map and use a Jira Checkbox (array<option>) field

## Overview

When connecting Jira Checkbox fields with Salesforce, you have two options:

1. Use text values that match exactly (the field is case-sensitive)
2. Set up value mapping to translate between systems. To learn more, see [Value mapping](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).

## Compatibility

Jira Checkbox field is an `array<option>` type for the Connector.

![image-20240529-164913.png](/cms_trial/assets/29902221-bb45-46e5-90fd-d41267e2e70b.png)

Here are the values of a sample Checkbox:

![image-20240529-164953.png](/cms_trial/assets/d19999ac-ea48-42d4-b4d8-3a18d7c9cff8.png)

You can synchronize Jira Checkbox fields (`array<option>` type) with these Salesforce field types:

| Salesforce field type | Compatibility notes |
| --- | --- |
| String, text area | < Inbound: format sensitive  > Outband: fully compatible |
| Rich text area | < Inbound: format sensitive  > Outband: fully compatible |
| Picklist | < Inbound: format sensitive  > Outband: not supported |
| Multi-picklist | < Inbound: format sensitive  > Outband: format sensitive |

Other Salesforce field types are not compatible, as stated in the compatibility matrix [Jira Field Type to Salesforce Field Type compatibility](https://appfire.atlassian.net/wiki/x/fYK9Wg).

Remember that the Checkbox field is case-sensitive.

One easy way to understand how the field behaves is to push the field to Salesforce. The text field will get the correct values from the checkbox:

**Jira:**

![image-20240529-165325.png](/cms_trial/assets/f989f5e3-3227-43d6-ba8b-ff759c649abe.png)

**Salesforce:**

![image-20240529-165317.png](/cms_trial/assets/46ed065d-eef3-42b3-aa8b-4e9974c57778.png)

### Using value mapping

You can translate values between Jira and Salesforce using the value mapping feature. To learn more, see [Value mapping](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/).

#### Example

Map Jira value "1" to appear as checkbox "one" in Salesforce

![image-20240617-142326.png](/cms_trial/assets/db486b4d-c69e-4d0a-af04-c1b133bda86d.png)

As observed, the values sent to Salesforce receive a semicolon (;). If those values are mapped in that manner, the checkbox will receive the values one and two.

**Mapping**

![image-20240529-165710.png](/cms_trial/assets/156dcfa5-47ea-4f1f-b8f3-541a3eb833cd.png)

Jira Field

![image-20240529-165724.png](/cms_trial/assets/97101342-4687-4dcc-bb88-040adf463260.png)