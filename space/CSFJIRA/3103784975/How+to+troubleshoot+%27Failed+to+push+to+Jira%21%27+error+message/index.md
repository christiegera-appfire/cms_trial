# How to troubleshoot 'Failed to push to Jira!' error message

## Summary

*Failed to push to Jira* error message prompts when pushing updates manually from Salesforce to Jira.

![contentId-3103784975](/cms_trial/assets/e8d43823-2357-4fa8-a5f7-1b22d6c46bf0.png)

## Environment

- Jira Cloud/Server
- Any

## Diagnostics Steps

Web requests can provide the full error message for further troubleshooting.

## Causes

*Failed to push to Jira* error message can be caused by various issues. Below are the possible error messages you might find in the browser web requests:

"Field 'status' cannot be set. It is not on the appropriate screen, or unknown."

Jira Status field is a *Read-Only* field. Therefore, only outbound sync (Jira > Salesforce) is supported.

"Field 'customfield\_10112' cannot be set. It is not on the appropriate screen, or unknown."

As the error suggests, the custom field with ID '10112' is not on the appropriate screen. Specifically, the custom field is not on the *Edit Issue screen*.

The connector uses the mapped fields on the Jira *Edit Issue screen* to push updates from Salesforce to Jira.

"Option id 'null' is not valid"

This might be due to mapping incompatible field types. For example, having Jira 'Select List (single choice)' field type mapped with Salesforce 'Picklist(Multi)' field type.

"Option value 'Child 1' is not valid"

The mapped fields are compatible with one another. However, the value 'Child 1' is unavailable in Jira.

## Resolution

"Field 'status' cannot be set. It is not on the appropriate screen, or unknown."

1. Go to Jira, **Apps** > **Salesforce** > **Bindings** > **Mapping** > **Mappings**
2. Locate **Status** field mapping
3. Make the sync direction pointing to Salesforce only (*Outbound sync*) as shown as the picture below:

   ![contentId-3103784975](/cms_trial/assets/7a62c5de-e01f-4420-afdc-d9045b2d9e94.png)
"Field 'customfield\_10112' cannot be set. It is not on the appropriate screen, or unknown."

1. Find the custom field mentioned in the error message:

   1. In Jira, navigate to **Issues** > **Custom fields.**
   2. Click on the **Configure** for any the custom fields you have.
   3. You should see the following in the Browser URL:

      ```text
      https:JIRAurl/secure/admin/EditCustomField!default.jspa?id=15800
      ```
   4. Change `15800` to the ID you see in the error message (for example, `10112`)
   5. Press `Enter`.
2. After locating the custom field name from the step above. We need to add the field to the *Edit Issue screen*

   1. In Jira, go to **Projects** > <your project>.
   2. **Project Settings** > **Screens.**
   3. Locate the Issue type and expand it.
   4. Click on the screen on the **Edit issue** operation.

      ![contentId-3103784975](/cms_trial/assets/f1a9cb56-dc27-4b4c-903a-b881f1ebf64a.png)
   5. Add the field that you have located in the previous step.
"Option id 'null' is not valid"

This might be due to the mapped field being incompatible. Check [Jira Field Type to Salesforce Field Type compatibility](/cms_trial/space/CSFJIRA/1522369149/Jira+field+type+to+Salesforce+field+type+compatibility/) to learn more about Jira Field Type to Salesforce Field Type compatibility.

"Option value 'Child 1' is not valid"

There are two solutions to this issue:

1. Make sure that the values of the Jira and Salesforce fields are identical.
2. Configuring value mappings to non-identical value. Please refer to [Configuring Entity Mappings and Field Mappings](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field+and+value+mappings/), *Part 3: Configuring Value Mappings.*

The error message is not listed here? Please [contact Technical Support](https://appfire.atlassian.net/servicedesk/customer/portals) for further assistance.