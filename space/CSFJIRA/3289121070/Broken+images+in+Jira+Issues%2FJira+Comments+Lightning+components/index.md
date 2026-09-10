# Broken images in Jira Issues/Jira Comments Lightning components

## Broken image thumbnails and missing icons

The Jira Issues and Jira Comments Lightning components may display broken image thumbnails or user avatars. This happens when Salesforce security settings block the external image sources used for user profiles and issue icons.

You may encounter the following issues in the app's components in Salesforce:

- Broken images for user avatars in the Jira Comments component.
- The epic icon (lightning bolt) and other issue-type icons don't load correctly.
- Browser console logs show "violated the following Content Security Policy directive: img-src..." errors for specific domains.

## Restore images by updating CSP settings

Salesforce's Content Security Policy (CSP) can block images loaded from external domains. Avatars and icons load from various Atlassian and Gravatar services, and if you don't add these domains to the Trusted URLs in Salesforce, the browser blocks them.

### Identify blocked URLs

Before adding URLs, confirm which specific domains are blocked.

1. In your **browser**, right-click anywhere on the Salesforce page and select **Inspect**.
2. Click the *Console* tab.
3. Look for error messages containing `violates the following Content Security Policy directive: "img-src...`.
4. Note the domain names mentioned in those errors (for example, `https://i0.wp.com`).
5. In **Salesforce**, navigate to **Setup** > **Security** > **Trusted URL and Browser Policy Violations**.
6. Note the domain names listed.

### Add trusted URLs in Salesforce

1. Navigate to **Setup** > **Security** > **Trusted URLs**.
2. Click **New Trusted URL**.
3. In the **API Name** field, enter a unique name (for example, `Atlassian_Avatars`).
4. In the **URL** field, enter the domain to trust. Common domains that require authorization include:

   - `https://secure.gravatar.com`
   - `https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net`
   - `https://i0.wp.com`
5. In the *CSP Directive* section, select the **img-src (image)** checkbox.
6. Click **Save**.
7. Refresh the Salesforce page containing the Jira components. The images now load correctly.

## Related articles