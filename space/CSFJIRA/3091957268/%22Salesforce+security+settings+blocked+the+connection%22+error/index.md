# "Salesforce security settings blocked the connection" error

## Summary

When trying to authorize the connection after logging into Salesforce, rather than continuing to the configuration wizard, a message stating *Salesforce security settings blocked the connection* displays.

![contentId-3091957268](/cms_trial/assets/089b38c9-462d-4fe3-a017-9a6ca078e373.png)

The message also provides links to this document page and to the *Support* portal.

## Environment

- JIRA Cloud

  ​​

## Diagnostics Steps

- Check the URL shown in the browser and whether it contains this string - `OAUTH_APP_ACCESS_DENIED`  
  If you do not see the `OAUTH_APP` string, read [Page cannot be found when I try to re-authorize connection with Salesforce](/cms_trial/space/CSFJIRA/3091334997/Page+cannot+be+found+when+I+try+to+re-authorize+connection+with+Salesforce/).
- In Salesforce, navigate to **Apps** > **Connected Apps** > **Manage Connected Apps** to check the connector policies.

## Cause

Either the Salesforce user that is used for authorization has not been approved by the Salesforce admin, or the connector is not set to *All users may self-authorize*.

## Workaround

Not applicable.

## Resolution

Do either of the following:

- Make sure that the Salesforce user being used for authorization is approved by the Salesforce admin. More details are available [on this Salesforce page](https://help.salesforce.com/articleView?id=connected_app_manage_additional_settings.htm&type=5).
- Or, edit the policies to change the **Permitted Users** option to "All users may self-authorize"