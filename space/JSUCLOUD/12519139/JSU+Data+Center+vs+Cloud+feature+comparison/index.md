# JSU Data Center vs Cloud feature comparison

We’ve achieved full value parity between JSU for Jira Data Center and JSU for Jira Cloud. This means that nearly all JSU for Jira Data Center features are available in JSU for Jira Cloud, or have a Cloud equivalent. In a few cases, some specific parameters or behaviors are not available in Jira Cloud because of Jira Cloud platform or API limitations. These limitations are not specific to JSU.

We’ve also introduced the [Universal Rule Builder](/cms_trial/space/JSUCLOUD/12517805/Universal+Rule+Builder/) in JSU for Jira Cloud, giving Cloud users a simpler and more visual way to build workflow rules. This experience improves usability beyond what is currently available in JSU for Jira Data Center.

This page provides a detailed breakdown of the features of JSU for Jira Data Center and how they are available in JSU for Jira Cloud.

While some unavoidable API limitations in Jira Cloud restrict the full capabilities of some minute features of JSU for Jira Data Center, we've pushed the parity as far as Jira Cloud allows. Rest assured, this does not affect the value JSU brings to customizing your Jira workflows, regardless of platform.

See the parity tables of JSU features below for complete details.

Last updated November 21, 2025

## Conditions

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| User Is In Any Groups | ✅ | ✅ \* | **\***Atlassian managed integration with Jira Cloud |
| User Is In Any Roles | ✅ | ✅ \* | **\***Atlassian managed integration with Jira Cloud |
| User Is In Custom Field | ✅ | ✅ \* | **\***Atlassian managed integration with Jira Cloud |
| Value Field | ✅ | ✅ \* | **\***Atlassian managed integration with Jira Cloud |
| JQL | ✅ | ❌ | Jira Cloud architecture limitation |
| User Is In Any Users | ✅ | ✅ |  |
| Status Changed | ✅ | N/A | N/A - Jira Cloud natively prevents ANY → ANY transitions to/from the same status. |

## Validators

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Date Compare | ✅ | ✅ \* | \*Atlassian managed integration with Jira Cloud |
| Date Expression Compare | ✅ | ✅ \* | \*Atlassian managed integration with Jira Cloud |
| Field Value | ❌ | ✅ |  |
| Fields Required | ✅ | ✅ \* | \*Atlassian managed integration with Jira Cloud |
| Issue Status Changed | ❌ | ✅ |  |
| Only Selected Users | ❌ | ✅ |  |
| Regular Expression Check | ✅ | ✅ \* | \*Atlassian managed integration with Jira Cloud |
| Date Window | ✅ | ✅ \* | \*Atlassian managed integration with Jira Cloud |
| Linked Status | ✅ | ✅ |  |
| User in Field | ❌ | ✅ |  |
| User in Group | ❌ | ✅ |  |
| User in Project Role | ❌ | ✅ |  |

All features marked \* were originally supported by JSU for Jira Server but are currently maintained by Atlassian on Jira Cloud.

## Preconditions

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Date Compare | ✅ | ✅ |  |
| Date Expression Compare | ✅ | ✅ |  |
| Date Window | ✅ | ✅ |  |
| Fields Required | ✅ | ✅ |  |
| Linked Status | ✅ | ✅ |  |
| Regular Expression Check | ✅ | ✅ |  |
| User Is In Any Groups | ✅ | ✅ |  |
| User Is In Any Roles | ✅ | ✅ |  |
| User Is In Custom Field | ✅ | ✅ |  |
| Value Field | ✅ | ✅ |  |
| JQL | ✅ | ✅ |  |

## Post functions

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Copy Value From Other Field\* | ✅ | ✅ | 99% (Does not include the `*** default value ***` parameter due to Jira API limitations) |
| Update any Issue Field\* | ✅ | ✅ |  |
| Clear Field Value\* | ✅ | ✅ |  |
| Create a Linked Issue\* | ✅ | ✅ | 99% (Does not include the `***default value***` parameter due to Jira API limitations) |
| Linked Transition\* | ✅ | ✅ | 99% (Does not include the `Set Resolution - None` and `***default value***` parameters due to Jira API limitations) |
| Follow Up Transition | ✅ | ✅ |  |
| Copy or Move Attachments | ✅ | ✅ |  |
| Calculated Field\* | ❌ | ✅ |  |
| \*⚠️ see note below about Jira Cloud Screen Security Configuration |  |  |  |

Jira admins should be aware of Jira Cloud’s *screen security configuration.* This requires fields to be on the relevant screens to be edited. You can learn more in the [Jira Cloud API documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-rest-api-3-issue-issueidorkey-put). This highlights an important distinction between our Server/Data Center and Cloud apps.

On Jira Data Center, a JSU post function can be configured to run as either the initiating user or as a selected user. Both impersonation options can also be migrated to the cloud version, on which a third option is available: the *JSU Add-on user*. This configuration feature is called **Perform As User** in JSU.

If the field is present on a screen, JSU can edit it using the permissions of the user set in the Perform As User configuration, provided that user has permission to edit the field. If the field is not on the edit screen, JSU cannot edit it unless the post function is set to run as the **JSU Add-on user**. This overrides the screen security configuration using the `overrideScreenSecurity` and `overrideEditableFlag` query parameters.

**Custom fields context**

If you use custom fields, you can select which work item types and spaces the custom field appears in. The JSU Add-on user can’t be used to override fields that are missing due to their screen context. For example, if you have configured a post function to edit a custom field that is used only on a bug work item type and it is executed when a user transitions a different work item type, the execution will fail. See the [Atlassian documentation](https://support.atlassian.com/jira-cloud-administration/docs/configure-custom-field-context/) to learn more.

**Deactivated or missing users**

If the selected Perform As User is deactivated or doesn’t exist in the Cloud instance after migration, JSU will use the JSU Add-on user to run the post function.

## Perform as user

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Selected user | ✅ | ✅ |  |
| Initiating user | ✅ | ✅ | Default setting |
| JSU Add-on user | ❌ | ✅ | Default setting |

If you migrate a post function that uses the initiating user from Jira Data Center, JSU maintains that behavior in Jira Cloud.

## Custom fields

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Location Text | ✅ | ❌ |  |
| Location Select | ✅ | ❌ |  |
| Directions | ✅ | ❌ |  |

## Additional features

| **Feature/Parameter** | **DC** | **Cloud** | **Notes** |
| --- | --- | --- | --- |
| Issue Transitions Tab | ✅ | ❌ |  |
| Bulk Copy | ✅ | ❌ |  |
| Transition Trigger Service | ✅ | ❌ |  |
| Calculated Field | ❌ | ✅ |  |

The Product team has prioritized the features that matter most to you. The features marked with ❌ in JSU for Jira Cloud are not being implemented in the near future due to low popularity. We are, however, always interested in hearing if any of these are critical for you. [Contact us](https://appf.re/support) and share your use cases with our team. Help us make JSU even better for you!