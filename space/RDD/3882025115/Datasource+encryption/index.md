# Datasource encryption

Revoke the active site encryption key and re-encrypt the API tokens stored for your datasources.

## Overview

When you connect a datasource with an API token, Dashboard Hub stores the token securely on Appfire infrastructure, encrypted with a site encryption key. The **Datasource encryption** tab in Global Settings shows which key protects your stored tokens. You can also revoke that key and re-encrypt every stored token with a new key, without deleting and re-creating your datasources.

Revoke the key and re-encrypt your tokens:

- After a security incident, if you think an encryption key was exposed.
- When your security policy requires you to rotate encryption keys.

## Open Datasource encryption

1. Go to **Dashboard Hub** > **App settings** to open the Global Settings.
2. Select **Datasource encryption**.

   ![Datasource encryption tab in Dashboard Hub's Global Settings](/cms_trial/assets/8dbc829a-6043-4632-b235-aa4233b053ad.png)

## Check the current status

The **Current status** section shows two messages: one about your site encryption key, and one about the datasource tokens stored for your site.

### Site encryption key

| **Message** | **What it means** |
| --- | --- |
| Site encryption key active since {date} | Your site has an active encryption key, created on that date. |
| No site encryption key is active. Datasource tokens use a key from {date}. | Your site has no active key. Your stored tokens are encrypted with an older key from that date. |
| No site encryption key is active. | No encryption key has been created for your site. |

### Stored datasource tokens

| **Message** | **What it means** |
| --- | --- |
| No datasource API tokens are stored for this site. | None of your datasources store an API token, so there's nothing to re-encrypt. |
| All datasources with stored tokens use the active encryption key. | All your stored tokens are encrypted with the active key. |
| {x} of {total} datasources with stored tokens use the active encryption key; {y} are on an older key or legacy format. | Some tokens are still encrypted with an older key, or in the format used before site encryption keys were introduced. To move them all to a new key, revoke the key and re-encrypt. |
| No active encryption key. {x} of {total} datasources with stored tokens are not encrypted under an active key. | Your site has stored tokens but no active key. To encrypt them with a new key, revoke the key and re-encrypt. |

## Revoke the key and re-encrypt tokens

1. Select **Revoke encryption key**.
2. In **Revoke active encryption key?**, type `REVOKE` to confirm.
3. Select **Revoke and re-encrypt**.

   ![Revoke encryption key confirmation message in Dashboard Hub](/cms_trial/assets/f45f4da3-8229-469a-9f13-9804dd816ba7.png)

1. Keep the page open. A **Re-encryption in progress** message appears while your tokens are re-encrypted, and the page updates when it's complete.

Dashboard Hub keeps the revoked key as an inactive key, so any datasource that still uses it keeps working. For example, if re-encryption is interrupted or some tokens fail to re-encrypt.

## Review the result

When re-encryption is complete, **Migration result** shows how many datasources were re-encrypted, and the date the new key was created. For example: *67 datasources re-encrypted under the active encryption key created on Nov 5, 2026, 10:35 AM.*

If any datasources couldn't be re-encrypted, they're listed under **Failures** by datasource ID, with the reason. Try again. If the datasources still fail, contact Appfire support and include the datasource IDs and reasons.