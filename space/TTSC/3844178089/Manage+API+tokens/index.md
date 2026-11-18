# Manage API tokens

You can manage your API tokens from **Administration** > **API Tokens** in Time to SLA.

The API Tokens page displays each token's name, status, access level, last-used information, creator, creation date, and expiration date.

![image-20261111-004140.png](/cms_trial/assets/b6b50d2d-fb09-4b9b-bb40-3099b0f3eacf.png)

### Find and review API tokens

Use the **Search API tokens** field to find tokens by name.

You can also filter the token list using:

- **Access type:** Filter tokens by their access level.
- **Last used:** Find tokens based on when they were last used.
- **Expires:** Filter tokens by expiration date.

The **Last used** column shows when a token was last used to make an API request. Tokens that haven't been used display **Never used**.

Click the **Last used** column header to sort tokens by their last-used time.

Review tokens that haven't been used recently to determine whether they're still needed.

### Revoke API tokens

Revoke an API token when it is no longer needed or when you want to prevent an integration from using it.

To revoke a token:

1. Go to **Administration > API Tokens**.
2. Find the token you want to revoke.
3. Click **Revoke** next to the token.
4. In the *Revoke API token* confirmation dialog, review the token name and click **Revoke** to confirm.

**Important:** Revoking a token immediately prevents integrations using it from accessing Time to SLA. This action cannot be undone. Make sure the token is no longer required before revoking it.

To cancel the operation without revoking the token, click **Close** or dismiss the confirmation dialog.