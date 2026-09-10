# REST APIs

Time to SLA provides powerful REST APIs to help you view and manage your SLA configurations, calendars, notifiers, work items, and permissions.

Here's an overview of what you can do:

**View and manage SLAs**

- Get a list of all SLAs
- Retrieve SLA configuration details by ID
- Create a new SLA configuration
- Update an existing SLA
- Delete an SLA
- Clone an SLA from an existing SLA

**View and manage SLA actions**

- Get all SLA actions for a specific SLA
- Retrieve all actions defined in TTS
- Get a action configuration using SLA ID and action ID
- Create a new action configuration
- Update an existing action configuration
- Delete a action by SLA ID and action ID

**View and manage calendars**

- Get all defined calendars in the plugin
- Retrieve specific calendar configuration by ID
- Create a new calendar
- Update an existing calendar
- Delete a calendar by ID

**View all work items**

- Retrieve all SLAs associated with a specific work item by SLA ID
- Get SLA details for a work item using the work item ID and SLA ID

**Recalculation**

- Get all recalculation records
- Start recalculation using JQL
- Abort recalculation

**Permissions**

- View all permissions
- Update permissions

## Prerequisites

Before you begin using the REST APIs, ensure you meet the following prerequisites:

1. You must have the necessary permissions to access and manage SLAs, calendars, actions, or other configurations.
2. A valid JWT token is required for authorization. Follow the [steps below](/cms_trial/space/TTSC/36209134/REST+APIs/) to generate one.
3. Use Postman or another API testing tool to test and integrate the REST APIs.

For more information, refer to the [REST API documentation](https://documenter.getpostman.com/view/15299464/UVyoXJMy).

## Base URL and data residency

Time to SLA REST API endpoints are region-specific.

Use the base URL that corresponds to your data residency region. You can find your regional base URL on the **Settings** > **API Token** page.

### Regional base URLs

| **Region** | **Base URL** |
| --- | --- |
| Global and Europe | <https://tts.snapbytesapps.com/>  <https://tts-eu.snapbytesapps.com/> |
| United States | <https://tts-us.snapbytesapps.com/> |
| Germany | <https://tts-de.snapbytesapps.com/> |

**IMPORTANT:**

We’re introducing region-specific base URLs for the Time to SLA REST API as part of data residency support.

Starting **April 16, 2026**, you must use the base URL that matches your region. You can find your correct base URL on the **Settings** > **API Token** page.

![A screenshot showing where the Base URL is on the TTS API Token screen.](/cms_trial/assets/1de2b348-606b-49fa-b164-45ed4d4d5cae.png)

Cross-region requests will continue to work temporarily but will be blocked in a future release. To avoid service disruption, make sure your integrations use the correct regional URL.

## How to create a token

To use the REST APIs, you need a JWT token for authentication. Follow these steps:

1. Navigate to **Settings** > **API Token**.

   ![The TTS API Token screen.](/cms_trial/assets/bebb0b1b-bbe1-4efa-9ec8-1f381c1e0821.png)
2. Click the **+** **New Token** button. The token creation dialog opens.
3. Configure your token:

   ![The token creation process on the Time to SLA app.](/cms_trial/assets/9abc570b-e1e0-44e2-929e-8ff6316dac02.png)
   - Name your token.
   - Select when it'll expire, or check the *Never expire* box if you want the token to remain active indefinitely.
   - Determine the level of access that the token will have.

**Security note**

Avoid using tokens that never expire. If such a token is exposed, it must be deleted manually, as it will not expire automatically.

1. Click **Generate**. The *JWT Token* appears.
2. Save the JWT Token by clicking the copy button. Note that you won’t be able to access this code after closing the dialog.

   ![The JWT token section in the Time to SLA app.](/cms_trial/assets/7f413e09-9bfe-41cc-b593-febdeb811720.png)
3. Click **Cancel** after copying the token, and the token will appear on the main page.
4. Replace {{jwtToken}} in the header with your token.

**Important note**

Your JWT must have permission and access to use the APIs. For example, even if your JWT token has access to SLA APIs, you cannot utilize them if you do not have permission to view SLA configurations or administer SLAs.

## How to grant JWT permission (Using Postman)

Here’s how to set up JWT authorization using Postman:

1. Open [the TTS REST APIs documentation](https://documenter.getpostman.com/view/15299464/UVyoXJMy)**.**
2. Click **Run in Postman** > **Postman for Web**.

   ![A screenshot showing how to grant JWT permission using Postman.](/cms_trial/assets/5825178c-4de6-4010-a20b-2697fcaf8444.png)
3. On the Postman main page, click **Workspaces** > **My Workspaces**.

   ![A screenshot showing the Workspaces section on Postman.](/cms_trial/assets/5725a590-cc29-4ff9-b603-167114221afd.png)
4. Click the plus button to add a new permission.

   ![A screenshot showing the Overview section on Postman.](/cms_trial/assets/e5a6794a-c267-4b65-9311-3e1e476a0283.png)
5. Copy and paste the link of the token [you’ve chosen](https://documenter.getpostman.com/view/15299464/UVyoXJMy).

Don't change the link to reflect your own instance. You can only change the parameters (that is, work item ID, SLA ID, etc.).

1. Click **Headers**.
2. Under *KEY*, enter **Authorization**.
3. Under *VALUE*, enter `Bearer {your token}` (replace `{your token}` with the token you generated).
4. Click **Send** to authenticate.

   ![A screenshot showing the steps needed to be taken to create the token on Postman for Time to SLA.](/cms_trial/assets/d774c725-aa08-4e02-ab0f-f31cd915f941.png)

Your JWT authorization is now active.

To find a work item ID on Jira Cloud, you can use the following API call:

```text
BASE_URL/rest/api/3/issue/{issueKey}
```

The response will include the work item ID you need for further API requests.

## Rest call example

Here’s an example API request with definitions for key parameters in the response:

| **Example response for “Get Issue SLA of Issue”** | **Meaning** |
| --- | --- |
| `slaValueType` | This is the SLA’s goal. |
| `slaValue` | This is also related to the SLA goal. We keep this value in milliseconds. |
| `startDate` | If the SLA has started, this will show the start date. We keep this value in a Unix timestamp. If you want to convert it to a human-readable form date, you can use a [converter](https://timestamp.online/). |
| `endDate` | If the SLA has finished, this will show the end date. We keep this value in a Unix timestamp. If you want to convert it to a human-readable form date, you can use a [converter](https://timestamp.online/). |
| `deadline` | This is the Target Date. We keep this value in a Unix timestamp. If you want to convert it to a human-readable form date, you can use a [converter](https://timestamp.online/). |
| `elapsedDuration` | Elapsed time is the total time the SLA has taken until this time. |
| `remainingDuration` | The time left until the SLA breaches. |
| `overdueDuration` | The time that has passed since the SLA was breached. |
| `pausedDuration` | The length of time that the SLA has been paused. |
| `workingDuration` | This value is the same as `elapsedDuration`. |