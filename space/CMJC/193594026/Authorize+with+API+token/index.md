# Authorize with API token

## API token for deployments between Jira Cloud sites

API tokens in Atlassian's ecosystem enable you to authenticate to Atlassian cloud apps, including *Jira Cloud, Confluence, Bitbucket, Fisheye*, and *Crucible*. With the token, you:

- Bypass two-step verification and SSO.
- Retrieve data from the cloud sites through REST APIs.

Learn about API token controls from [Atlassian's documentation](https://www.atlassian.com/software/access/guide/elements/api-token-controls#what-are-api-token-controls).

The API token used for authentication must be associated with a user registered with the same email address on both instances.

**Why you need an API token with CMJ Cloud**

CMJ Cloud uses the API token to **authorize** you to source and target Jira Cloud siteswhen deploying configurations. To create a configuration deployment in CMJ Cloud, you must provide your Atlassian account's API token.

**Benefits of using API tokens**

With API tokens, CMJ Cloud doesn't need your username and password to authorize you when communicating with Jira Cloud sites.

This approach allows CMJ Cloud to securely use the Jira Cloud services without requiring or storing user credentials.

**How to create and manage API tokens from your Atlassian account**

You can create, view, and revoke an API token from your Atlassian account. Find more details about creating an API token in the [How to get an API token](https://appfire.atlassian.net/wiki/spaces/DCMFJC/pages/143425674/Authorize+with+API+token#How-to-get-an-API-token) section below.

You can also learn how to manage API tokens from [Atlassian's documentation](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).

## Provide an API token in CMJ Cloud

1. Log in as a user with the **Site** or **Organization admin permissions** to your Jira Cloud site.
2. Choose the **cog icon**at the top right corner of the screen, then choose **Apps** from the menu.
3. Go to **Apps > Configuration Manager > Authorization**.

   ![image-20260520-074626.png](/cms_trial/assets/6c35fee6-e628-4ee1-878a-0127a2876858.png)
4. Provide an API token for your Atlassian account.
5. Click **Save token** to store the token.

   ![image-20260520-074814.png](/cms_trial/assets/b64d0117-c12b-4219-9c61-3c7c37b0aaa2.png)

   You'll see a message indicating the API token has been stored.

   ![image-20260520-074859.png](/cms_trial/assets/50950673-6c22-46bf-86c5-a2a455c7ca52.png)

You're all set to start deployments to Jira Cloud sites on the **Configuration Deployment** page.

**Can I provide an API token without having Site or Organization admin permissions?**

You can provide an API token without Site or Org admin permissions, but you won't be able to use CMJ Cloud's features.

CMJ Cloud requires Site or Org admin permissions to deploy configurations between Jira Cloud sites.

## How to get an API token

You can get an API token from your Atlassian account settings at [https://id.atlassian.com/manage](https://id.atlassian.com/manage/api-tokens).

### Create an API token

1. Log in to your Atlassian account <https://id.atlassian.com/manage/api-tokens>.
2. Click **Create API token**.
3. Choose a short and memorable label for your token from the dialog and click **Create**.
4. Click **Copy** to clipboard, then paste the token and save it:

   ![GIF showing how to create an Atlassian API token. ](/cms_trial/assets/c3da4257-7330-4397-9cd9-af5a1022a1ee.gif)

## Additional Atlassian resources

- [Making changes to the API tokens of your managed user accounts](https://support.atlassian.com/user-management/docs/make-changes-to-a-managed-user-account/)
- [Protecting your Atlassian account at all times](https://support.atlassian.com/atlassian-account/docs/protect-your-atlassian-account/)