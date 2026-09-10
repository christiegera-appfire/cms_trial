# Page cannot be found when I try to re-authorize connection with Salesforce

## Summary

When trying to reauthorize the connection I'm getting this error:

"This is probably not the page you were looking for."

## Environment

- Jira Cloud

## Diagnostics Steps

- Check the error URL, make sure that it doesn't contain this string - "OAUTH\_APP\_ACCESS\_DENIED". If it does, [proceed to this related KB page instead](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470756126/This+is+probably+not+the+page+you+are+looking+for+error).
- Once we've confirmed that it is not the issue related to the "OAUTH" string above, we need to check the HAR file. To do so, follow Atlassian's guide for "[Generating HAR files and analysing requests](https://confluence.atlassian.com/kb/generating-har-files-and-analyzing-web-requests-720420612.html?__hstc=72543820.ab19c70c621fe76686456a1bcc7fc053.1629983345841.1643007110666.1643081238260.349&__hssc=72543820.5.1643081238260&__hsfp=3471989517)"
- Once the HAR file has been generated, check for the following error

#### **Error**

```text
Error occurred while trying to authorize the user with Salesforce: {"error":"invalid_grant","error_description":"ip restricted"}
```

## Cause

This usually happens when the Salesforce instance has been configured with IP address restrictions.

## Workaround

Not applicable.

## Resolution

On the Salesforce instance check the following:

- **Org-wide: Security Controls > Session Settings >**The option "**Lock sessions to the IP address from which they originated**" should be unchecked.

  ![contentId-3091334997](/cms_trial/assets/3dea9bec-d15e-4bbf-9fbe-681f27967171.png)
- **Profile of the user: System > Login IP Ranges**.  If one or more ranges are listed here, verify that your IP address is on this list.

You can view the IP addresses as logged by Salesforce by looking **Setup** -> **Login History**. The entries where Login Type = “Remote Access 2.0” and Status = “Restricted IP” would correspond to failed oAuth authentication attempts by Salesforce & JIRA Cloud Connector on your behalf.