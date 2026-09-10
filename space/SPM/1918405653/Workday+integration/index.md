# Workday integration

**About this page**

This page describes integration features that are supported **only** in [**BigPicture Advanced**](/cms_trial/space/SPM/3451617346/BigPicture+Standard+vs+Advanced/). These features are not available in BigPicture Standard.

Integrating BigPicture with Workday allows for automated synchronization of employee absences, ensuring that project timelines are always up to date.

## Integrate BigPicture with Workday

After integration, Workday data becomes the primary source of absences. Resources are matched based on their work email in both Atlassian and Workday. Absences need to be approved in Workday to be reflected in BigPicture.

### Full integration

When all resources are managed in Workday, integration with Workday fully replaces BigPicture absences. Once the integration is active, manual adjustments in BigPicture are disabled to prevent inconsistencies.

### Partial integration

If some resources are not in Workday, you can still manage their data manually in BigPicture. Partial integration lets you be flexible in resource management across systems. Users who are in Workday are mapped with BigPicture by their email addresses.

### Step-by-step instructions

To integrate BigPicture with Workday:

1. You need to configure Workday integration.

   1. Go to **App Configuration** > **Integrations** > **Workday**.

      ![integrations-workday.png](/cms_trial/assets/ae448e1d-b73d-4859-9493-a31f71de7d2e.png)
   2. To get your Workday credentials, follow the steps described in the **Configure REST API in Workday** section below.
   3. Once you completed the steps in the **Configure REST API in Workday** section below and have all the credentials, provide:

      1. **Client ID**
      2. **Client Secret**
      3. **Refresh Token**
      4. **Workday REST API Endpoint**
      5. **Token Endpoint**
   4. Specify a start date for the **Start sync with Workday from** field. From that date onward, BigPicture absences will be replaced, and Workday data will become the primary source of absences.
   5. When ready, click **Save**.

      ![Screenshot of the Workday integration page.](/cms_trial/assets/3a1e8b97-a909-4eef-9921-b36c5de9ba6d.png)

## Configure REST API in Workday

### Register API client for integrations

You need to be a Workday administrator to complete the following steps:

1. Search for **Register API Client for Integrations** in Workday's search field.
2. Select the **Register API Client for Integrations** task to access the registration page.
3. Enter a name for your API client in the **Client Name** field.
4. Select the **Non-Expiring Refresh Tokens** option.
5. Select **Scope (Functional Areas)**.
6. Click **OK** to generate the Client ID and Client Secret.

   ![image-20241016-110013.png](/cms_trial/assets/91b4a31e-09ef-4d81-8446-fcc4e003dddf.png)
7. Save the **Client Secret** and **Client ID**.
8. When saved, click **Done**.

   ![workday8.png](/cms_trial/assets/13ec7f3e-3dbc-488c-ae19-8542b6c8ab3a.png)
9. Navigate to the **API Clients for Integrations** tab.
10. Select the **API client** you registered in the previous steps.
11. Click the **… More actions** menu next to the client name and go to **API Client** > **Manage Refresh Tokens for Integrations**.

    ![workday11.png](/cms_trial/assets/89e804bd-c2ff-468f-af00-0a6d0b54b4ce.png)
12. Use your existing **Integration System User (ISU) account** or create a new one for the integration. When ready, click **OK**.

    ![workday12.png](/cms_trial/assets/9622130c-297c-4470-aa37-b86995c064ac.png)
13. Select the **Generate New Refresh Token** option and click **OK**.

    ![workday13.png](/cms_trial/assets/35bb5250-d47d-4567-80a7-725b60776bea.png)
14. Copy the **Refresh token** from the **Successfully Regenerated Refresh Token** page.

    ![workday14.png](/cms_trial/assets/97792b12-a5b9-4c06-ac3f-d1639b794ce5.png)
15. Click **Done** to complete the process. After completing the steps above, you should have the Client ID, Client Secret, and Refresh Token.

### Get Workday REST API endpoint

To understand where the API endpoints come from, refer to the [Workday REST API](https://doc.workday.com/admin-guide/en-us/integrations/workday-rest-api/rest-api-fundamentals/dan1370797985682.html) page.

The Workday REST API base path format is:

`https://{tenantHostname}/api/{serviceName}/{version}/{tenant}`

**How to determine your tenant’s REST API path:**

**{tenantHostname}**

- The hostname of the Workday REST web service. You can use the **View API Clients** task to get the hostname.

*Example*: If the **Workday REST API Endpoint** on **View API Clients** displays `https://services1.myworkday.com/ccx/api/v1/gms` the hostname is `services1.myworkday.com`.

**{serviceName}**

- The name of the Workday REST web service. You can find the service names in the [Workday REST Services Directory](https://community.workday.com/sites/default/files/file-hosting/restapi/index.html#absenceManagement/v1/get-/workers).

**{version}**

- The version of the Workday REST web service. You can find the service versions in the [Workday REST Services Directory](https://community.workday.com/sites/default/files/file-hosting/restapi/index.html#absenceManagement/v1/get-/workers).

**{tenant}**

- The name of your tenant.

#### Workday REST API for time off details

1. Go to the **Workday REST Services Directory** and find the path for absence details.

   ![workday-rest-api1.png](/cms_trial/assets/aa25b604-4462-4f85-9bcd-333878f99cf0.png)
2. This example will use the path: `/workers/{ID}/timeOffDetails`
3. Add the above path to your tenant’s API endpoint. It should look similar to: `https://services1.myworkday.com/ccx/api/absenceManagement/v1/gma/workers/{ID}/timeOffDetails`
4. Use an API platform (e.g. Postman) to retrieve the access token.
5. Use the access token to GET REST API time off details.

## Synchronization rules

Synchronization takes place automatically once a day.

If you want to manually synchronize data:

1. Go to **BigPicture Administration** > **Resources** > **Individuals**.
2. Click the **Synchronize with Workday** button.

   ![Screenshot of the Synchronize with Workday button.](/cms_trial/assets/9fb19006-092e-4518-8316-8fa0816a65d5.png)
3. The synchronization is in progress. You will be informed when the process is completed.

## Remove Workday integration

To remove Workday integration:

1. Go to **App Configuration** > **Integrations** > **Workday**.
2. Click **Remove integration** at the bottom of the page.

   ![Screenshot of the Remove integration button on the Workday integration page in BigPicture.](/cms_trial/assets/3571286b-9494-4f24-a20e-54c8005754fd.png)
3. When you remove Workday integration, the absences already synchronized will remain in BigPicture, so none of your data will be lost. However, the integration will be removed, and new data will no longer be synchronized.
4. To confirm, click **Remove**.

   ![remove-workday-integration.pngaScreenshot of the Remove integration button on the Workday integration page in BigPicture.](/cms_trial/assets/79f688c4-b7c5-44ee-a1c6-b6e4b8985b25.png)

## Absences management in BigPicture

After integration with Workday, you **can’t** manually add absences for users managed by Workday in BigPicture. If a user **isn’t** managed in Workday, you can still manually manage their absences in BigPicture.

The **Add absence** button is disabled on:

- **My settings** > **Absences**

  ![my-setting-absences-disabled.png](/cms_trial/assets/9b75ece9-9bd2-4ffc-a241-be991b81a7ac.png)
- **BigPicture Administration** > **Resources** > **Individuals** > **Resource’s page**

  ![individual-page-absences-disabled.png](/cms_trial/assets/0bdf6a53-5278-4a53-b840-8d1c4930edf3.png)
- **Resources module** > **Right-click on a task** > **Add absence**

  ![resources-module-absence-disabled.png](/cms_trial/assets/2de65d85-eff5-401b-ab84-10ddd5857dcb.png)
- **Resources module** > **Right-click on an individual** > **Add absence**

  ![resources-module-add-absence-disabled.png](/cms_trial/assets/031d1724-9137-4435-b201-301aac544abf.png)