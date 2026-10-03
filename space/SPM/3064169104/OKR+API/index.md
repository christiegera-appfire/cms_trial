# OKR API

**About this page**

This page describes features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

The REST API offers a streamlined way to integrate your OKR data with external tools and automated workflows.

- **OKR API tokens**: Tokens created in the OKR module are used to authenticate OKR-related API requests within BigPicture. You can also use them to connect external applications. For instance, if you use Dashboard Hub, an OKR token is required to access and [display your BigPicture OKR data](https://support.appfire.com/space/RDD/3402104953/BigPicture+OKRs).
- **BigPicture API tokens**: BigPicture tokens are needed to authenticate actions made to the BigPicture app. Visit the [API tokens](/cms_trial/space/SPM/1918666949/API+tokens/) page to learn more.

## Permissions

Only [permitted users](/cms_trial/space/SPM/1918765815/OKR+module+permissions/) can create, rename, and revoke API tokens:

- Jira Admin
- In-module Admin
- Users in roles with granted **API access** (to manage own OKR tokens) and **API admin table access** permissions (to manage all OKR tokens).

## **Create an API token**

1. On the **Settings** > **API** page, click **+Generate new token**.
2. A **Generate token** modal displays. Add a name for the token.

![Generate token modal.](/cms_trial/assets/b87e0b1a-891a-4f91-afc1-30e3f76f4788.png)

1. Click **Create** to generate a token.
2. Use the **Copy** button to copy the generated API token. Store it securely, as you will not be able to retrieve it later. Click **Close** to close the modal.
3. A new API token for your organization is now listed at the top of the *API* page.

## Manage API tokens

1. In the **Actions** column, click **More actions** (**…**) next to the token you want to manage.
2. From the dropdown, select **Rename** or **Revoke**, depending on the action you want to perform on the token.

![manage-okr-api-tokens.pngMore actions dropdown next to the okr api token.](/cms_trial/assets/e2c605d9-b44c-4c79-ba56-2ee26f1760d1.png)

1. Confirm the action.

## **Authentication**

All requests made to the BigPicture OKR module require authentication using your generated API token. This is achieved by including an `API-Token` header in your requests. If the header is not present, you will receive a “400 Bad Request” response.

Make sure you usethe`API-Token`header, not the`Authentication`header.

## **Organization’s tokens**

You can oversee all API tokens created in your organization. Users with the `API_ADMIN_TABLE_ACCESS` permission have access to an expanded view on the *API* settings page.

The API administrator table lets you view, rename, or revoke tokens created by other members of your organization.

![API settings in the OKR module.](/cms_trial/assets/ea6a0952-6494-4129-997d-0d987f22e15e.png)

## REST API endpoints

Visit the [Developer Portal](https://developer.bigpicture.one/reference/whatisbigpicture) for the full list of all BigPicture endpoints.