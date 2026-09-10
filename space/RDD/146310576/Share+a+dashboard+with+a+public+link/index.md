# Share a dashboard with a public link

## Overview

In this article, you’ll learn how to securely share dashboards externally without giving internal access to your instance.

Do you want to share your dashboards with users of the Jira Service Management Customer Portal? Read [Manage access to the Jira Service Management Customer Portal](/cms_trial/space/RDD/146309699/Manage+access+to+the+Jira+Service+Management+Customer+Portal/).

## How to create public links

Independent of the permissions set in the dashboard (see [Dashboard permissions](/cms_trial/space/RDD/146309693/Dashboard+permissions/)), the dashboard can be shared externally. This option is intended to enable anonymous access, so anyone with the link (optionally secured with a password) can view the dashboard content without access to the Jira or Confluence instance.

External users can only view and access the content you share; they have no additional access.

### Considerations for public links

When you share a dashboard with a public link, consider the following if your gadgets use the **Instance** as the datasource, for example, *This Jira Instance* or, for Dashboard Hub for Confluence, *This Confluence Instance*:

- Dashboard owner permissions apply when gadgets use the instance datasource and the default *Run As Owner* permission option.
- If an admin restricts the Owner View Mode in the *Global Settings* for Dashboard Hub, then all gadgets configured with the instance datasource will render with the Viewer permission, which requires a login. Public links don’t require logged-in user credentials; therefore, the gadgets won’t render any data and will display an error instead. If you want to share a dashboard with the Owner permission turned off, use another datasource type, for example, API token-based, where this setting does not apply.
- If a gadget is configured with Viewer permission by default, it will use the logged-in user permissions instead of the dashboard owner permissions for instance datasources.

**Atlassian IP Allowlist:** If you are on a Premium Jira, JSM, or Confluence Cloud instance, your admin can use the IP Allowlist for added security. If Dashboard Hub’s IP addresses aren’t included in the list, public links won’t work.

If you are the admin for your organization, add the following IP addresses to the Allowlist to permit the sharing of public links:

- Europe: `52.29.146.56, 3.79.160.48`
- US: `34.193.47.49, 3.219.102.173`

Refer to Atlassian’s [support documentation](https://support.atlassian.com/security-and-access-policies/docs/specify-ip-addresses-for-product-access/) to learn more about the IP Allowlist.

### Enable the public link

To create a public link, click the **Share** icon in the top navigation bar, or in the [How to manage dashboards](/cms_trial/space/RDD/146309328/How+to+manage+dashboards/) section, then enable the *Public Link* option.

If your dashboard gadgets use the instance datasource, users with the link will only see content for gadgets if the datasource uses the default Owner permissions. Refer to [Datasource viewing modes](/cms_trial/space/RDD/146309943/Learn+about+datasources/) to learn more.

### Disable the public link

If you want to stop sharing the dashboard publicly, click the **share icon** in the top navigation bar or in the [How to manage dashboards](/cms_trial/space/RDD/146309328/How+to+manage+dashboards/)section. Toggle the option to disable the public link, which is indicated in grey.

![Share dashboard options in Dashboard Hub.](/cms_trial/assets/605ae3d0-f416-4fb5-a2e8-17cfbd2a2de7.png)

### Password-protect the link

By default, the link uses a 400-character token, which, together with internal security measures, makes it secure. However, if you send the link by insecure channels, anyone could access the shared content. To avoid this, you can increase the protection by adding a password.

The password must be at least six characters long. It can be viewed and edited only by the creator and can be changed or removed at any time.