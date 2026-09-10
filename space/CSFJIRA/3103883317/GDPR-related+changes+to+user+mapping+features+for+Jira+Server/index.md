# GDPR-related changes to user mapping features for Jira Server

## What's changing?

The changes affect features related to Jira user field types, e.g. Reporter, Assignee or custom user field types.

An affected setup will typically look like this:

![contentId-3103883317](/cms_trial/assets/32f98606-45b3-4cec-a250-da72e2ef6937.png)

### Change 1: Value mapping will no longer accept text input

The value mapping screen will now show a dropdown menu to select Jira users. You can search by either username or display name.

| Before | After |
| --- | --- |
| contentId-3103883317 | contentId-3103883317 |

This change has already taken effect for any new creation of such mapping.

### Potential issue with existing mappings

For existing mappings, you may come across users which have different user keys and usernames. If you have a user who has a different user key and username, you will come across an issue similar to the following:

![contentId-3103883317](/cms_trial/assets/47ecb376-9a39-4994-9708-462161159502.png)

To resolve this, you will need to delete the value mapping and manually recreate it using the user picker.

### Change 2: Related sync will only send user keys

All sync functionality will now only send user keys (instead of Jira usernames) to Salesforce. Refer to both examples below.

If you don’t specify any value mappings, Salesforce will now display the user key:

| Before | After |
| --- | --- |
| contentId-3103883317 | contentId-3103883317 |

If you specify a value mapping, Salesforce will display the corresponding mapped value as usual:

| Before | After |
| --- | --- |
| contentId-3103883317 | contentId-3103883317 |

### Impact on bindings without existing value mappings

If you have a user field type mapping but without any value mapping, all the syncs will now use Jira user keys instead of Jira usernames. This typically affects any Jira user field types e.g. Reporter and Assignee that is mapped to a non-user type field in Salesforce, such as text fields.

Before the changes, the following illustrates the operations:

Jira ( username ) > (Outbound push to) > Salesforce (text field, with value username)

Salesforce (text field, with value username) > (Inbound push to) > Jira (username)

After the changes, it will change to:

Jira (user key) >  (Outbound push to) > Salesforce (text field, with value account ID)

Salesforce (text field, with value account ID ) > (Inbound push to) > Jira (user key)

The above will continue to work despite the usage of user key. However, if you would like to change this behavior to show a more meaningful information in Salesforce, OR making sure an existing association’s inbound push (from Salesforce to Jira) will continue to work, we recommend you to start adding explicit field value mappings.

With explicit value mappings, the operations will be such:

Jira (user key) > (Outbound push to) > Salesforce (text field, with value name )

Salesforce (text field, with value name ) > (Inbound push to) > Jira (user key)

## Need help?

If you require assistance, contact our [support team](https://apps.appf.re/support).