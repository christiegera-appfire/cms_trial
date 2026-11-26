# Workflow trigger action failures – error codes and solutions

When a workflow trigger action fails or completes only some of its tasks, Comala Document Management displays diagnostic information to help you identify the issue.

You can view the **Error code** and **Operation ID** in **Document Activity > Diagnostics & help**. Use the error code to identify the possible cause and follow the recommended troubleshooting steps. The Operation ID helps Support investigate the failure.

Use the error code to find the possible cause and recommended troubleshooting steps in the [Error code reference](https://appfire.atlassian.net/wiki/spaces/CDMCCD/pages/edit-v2/3862593748#Error-code-reference) section. If the issue persists after following the recommended steps, contact Support and provide the error code and Operation ID.

## **When to retry, check your configuration, or contact support**

Some errors are temporary and can be resolved by retrying the action. Others require changes to workflow settings, permissions, or integrations.

| **Issue** | **When to retry** | **Configuration checks** | **When to contact Support** |
| --- | --- | --- | --- |
| The action fails for the first time, with no recent changes. | Wait 15–30 minutes before retrying, particularly for `UPSTREAM_ERROR` or `UNKNOWN`. | Review the workflow configuration if the error persists. | If the same error occurs two or more times. |
| The action fails because of insufficient permissions. | Only after resolving the permission issue. | Ask your administrator to verify the required permissions. | If the error persists after the permissions are corrected. Include the Operation ID. |
| The workflow references an incorrect or missing page or space. | No. | Verify and update the target references in the workflow builder. | If the targets are correct and the error persists. |
| Publishing or email actions consistently fail. | No. | Verify that the required integration is installed and configured. | If the error persists after verifying the integration. |
| The workflow contains an unsupported action. | No. | Remove or replace the unsupported action. | Only if the action should be supported by your app. |
| A page remains restricted after approval, or a published page is missing. | Refresh the page and retry once. | Review the workflow configuration and required integrations. | If the issue persists after retrying and reviewing the workflow configuration. |

## Error code reference

The following table explains each error code and the steps you can take to resolve the issue.

| **Error code** | **Error message** | **Possible cause** | **Recommended action** | **When to retry** | **When to contact Support** |
| --- | --- | --- | --- | --- | --- |
| `APP_PERMISSION_DENIED` | The workflow action failed because the app does not have the required permissions. | The user or app doesn't have the required Confluence permissions, or the publishing integration doesn't have access. | Confirm that you can perform the same action manually in Confluence. Ask your space or site administrator to check the app's permissions. If the `publish-page` action failed, verify the publishing permissions. | After resolving the permission issue. | If the error persists after an administrator reviews the permissions. |
| `TARGET_NOT_FOUND` | The workflow action failed because a required page or space was not found. | The workflow references a page, space, or other target that has been moved, deleted, or is no longer available. | Verify the target references in the workflow builder, including copy destinations and publishing spaces. Confirm that the targets exist, correct any invalid references, and save the workflow. | After correcting the target references. | If the targets are correct and the error persists. |
| `INVALID_CONFIGURATION` | The workflow action failed because of invalid workflow configuration. | The workflow contains invalid settings related to metadata, approvals, copy options, messages, or expiration. | Identify the failed action in **Document Activity**. Review its settings and parameters in the workflow builder. Correct the configuration and test the workflow on the affected page or a test page. | After correcting the configuration. | If the error persists after correcting the configuration. |
| `INTEGRATION_UNAVAILABLE` | The requested integration is not available. | A required integration, such as Comala Publishing or an email service, isn't installed or configured. | Ask your administrator to verify that the required integration is installed and configured. For email actions, check the organization's email service settings. | After resolving the integration issue. | If the error persists after confirming the integration is available. |
| `NOT_SUPPORTED` | The workflow action is not supported. | The action isn't supported by the app or edition you're using. | Remove or replace the unsupported action in the workflow. Use a supported alternative. | Retrying won't resolve this error. | If the action should be supported by your app or edition. |
| `UPSTREAM_ERROR` | The workflow action failed because an upstream service returned an error. | A temporary issue with Confluence or another service, such as an email provider or publishing service. | Refresh the page and check whether the action completed. If the issue affects multiple users, check for reported service incidents. | Wait 15–30 minutes before retrying. | If the error persists after retrying or affects multiple users. |
| `UNKNOWN` | A workflow action failed. | The cause of the failure couldn't be determined. | Refresh the page and check the workflow configuration if the error occurs repeatedly. Record the Operation ID for further investigation. | Retry once after refreshing the page. | If the error persists. Include the Operation ID in your support request. |

## **Quick first steps by code**

The following table provides initial troubleshooting steps for each error code.

| **Error code** | **Step 1** | **Step 2** | **When to contact Support** |
| --- | --- | --- | --- |
| `APP_PERMISSION_DENIED` | Confirm that you can perform the same action manually in Confluence. | Ask your administrator to check the app and space permissions. | If the error persists after resolving the permission issue. Include the Operation ID. |
| `TARGET_NOT_FOUND` | Verify that the target page or space exists. | Correct any invalid target references in the workflow builder. | If the targets are correct and the error persists. Include the Operation ID. |
| `INVALID_CONFIGURATION` | Identify the failed action in **Document Activity**. | Review and correct the workflow configuration. | If the error persists after correcting the configuration. Include the Operation ID. |
| `INTEGRATION_UNAVAILABLE` | Ask your administrator to verify the required integration. | Retry the workflow after resolving the integration issue. | If the error persists after confirming the integration is available. Include the Operation ID. |
| `NOT_SUPPORTED` | Identify and remove the unsupported action. | Replace it with a supported alternative. | If the action should be supported by your app or edition. |
| `UPSTREAM_ERROR` | Refresh the page and check whether the action completed. | Wait 15–30 minutes before retrying. | If the error persists after retrying. Include the Operation ID. |
| `UNKNOWN` | Refresh the page and retry once. | Review the workflow configuration if the error occurs again. | If the error persists. Include the Operation ID. |

## Common workflow issues

The following table lists common workflow issues and the error codes that may be associated with them.

| **Issue** | **Possible error codes** |
| --- | --- |
| A page remains restricted after approval. | `APP_PERMISSION_DENIED`, `UPSTREAM_ERROR` |
| A copied or published page doesn't appear. | `TARGET_NOT_FOUND`, `INTEGRATION_UNAVAILABLE`, `INVALID_CONFIGURATION` |
| Labels are applied to only some child pages. | `APP_PERMISSION_DENIED`, `UPSTREAM_ERROR` |
| A workflow email isn't delivered. | `INTEGRATION_UNAVAILABLE`, `UPSTREAM_ERROR` |
| Page metadata or version information isn't updated. | `INVALID_CONFIGURATION`, `APP_PERMISSION_DENIED` |

#### Contact Support

If the issue persists after following the recommended troubleshooting steps, contact [Appfire Support](http://appf.re/support).

Include the following information in your support request:

- **Error code:** The error code displayed in **Diagnostics & help**.
- **Operation ID:** The identifier associated with the failed workflow action.
- **Page and space:** The affected page title and space name, if you're permitted to share them.
- **Failed workflow action:** The name of the action that failed.
- **Troubleshooting steps:** The steps you've already taken to resolve the issue.

The Operation ID helps Support identify the failed operation and investigate the cause.