# REST APIs

Time to SLA provides REST APIs to help you manage SLA configurations, calendars, actions, permissions, and other settings programmatically. You can also retrieve SLA data for Jira work items, manage SLA extensions, run recalculations, and generate reports.

For detailed endpoint specifications, request parameters, and examples, see the [Time to SLA REST API reference](https://docs.timetosla-appfire.com/).

## Before you begin

To use the Time to SLA REST APIs, you need:

- **Appropriate permissions:** You must have the Time to SLA permissions required for the operations you want to perform.
- **An API token:** Every API request requires a valid JWT (JSON Web Token) for authentication. Follow the [steps below](/cms_trial/space/TTSC/36209134/REST+APIs/) to generate one.
- **An API client:** Use an API client such as Postman or a command-line tool such as curl to send requests.

## Base URL and data residency

Time to SLA uses region-specific REST API base URLs to support data residency.

**Always use the base URL that matches your data residency region.** You can find the correct URL under **Settings > API Token** in Time to SLA.

### Regional base URLs

| **Region** | **Base URL** |
| --- | --- |
| Global and Europe | <https://tts.snapbytesapps.com/>  <https://tts-eu.snapbytesapps.com/> |
| United States | <https://tts-us.snapbytesapps.com/> |
| Germany | <https://tts-de.snapbytesapps.com/> |

## Create an API token

You need a JWT token to authenticate your API requests.

1. Go to **Settings** > **API Token** in Time to SLA.

   ![image-20261111-004140.png](/cms_trial/assets/16a5c6ee-9508-4555-b4c1-93c9ccde675c.png)
2. Click the **+ Token** button. The token creation dialog opens.
3. Configure your token:

   ![The token creation process on the Time to SLA app.](/cms_trial/assets/982d7037-3046-47d0-b714-81d8f8d94528.png)
   - Name your token.
   - Select when it'll expire, or check the *Never expire* box if you want the token to remain active indefinitely.
   - Determine the level of access that the token will have.

**Security note:** We recommend setting an expiration date for your tokens. Tokens that never expire remain active until manually revoked, increasing the risk if they're exposed.

For instructions on reviewing and revoking tokens, see [Manage API tokens](/cms_trial/space/TTSC/3844178089/Manage+API+tokens/).

1. Click **Generate**. The *JWT Token* appears.
2. Copy the generated JWT token and store it securely. **You won't be able to view it again after closing the dialog**.

   ![The JWT token section in the Time to SLA app.](/cms_trial/assets/7f413e09-9bfe-41cc-b593-febdeb811720.png)
3. Click **Cancel** to close the dialog. The token appears in the token list.

### Authenticate API requests

Include your JWT token in the `Authorization` header of every request using the `Bearer` authentication scheme.

The following example retrieves all SLA configurations:

```shell
export BASE_URL="https://tts.snapbytesapps.com"
export JWT_TOKEN="your-token-here"

curl -X GET "$BASE_URL/api/sla" \
  -H "Authorization: Bearer $JWT_TOKEN"
```

Replace the example base URL with your regional URL and `your-token-here` with your generated JWT token.

## Permissions and authentication errors

Your token's access level and your Time to SLA permissions both determine which operations you can perform.

For example, a token with access to SLA endpoints cannot modify SLA configurations unless you also have permission to administer SLAs.

If a request fails, check the following response codes:

| **Status code** | **Meaning** |
| --- | --- |
| `200 OK` | The request succeeded. |
| `401 Unauthorized` | Authentication failed. Check whether your token is valid or expired. |
| `403 Forbidden` | Access was denied. Check your token's access level and the permissions required by the endpoint. |

To find a work item ID on Jira Cloud, you can use the following API call:

```text
BASE_URL/rest/api/3/issue/{issueKey}
```

The response will include the work item ID you need for further API requests.

## API endpoints

Time to SLA provides **36 REST endpoints across nine resources**.

The tables below summarize the available operations. For request parameters, payloads, response schemas, and examples, see the [REST API reference](https://docs.timetosla-appfire.com/).

### SLA API

Retrieve, create, update, delete, and clone SLA configurations.

| **Method** | **Path** | **Description** |
| --- | --- | --- |
| GET | `/api/sla` | Get all SLAs |
| GET | `/api/sla/{slaId}` | Get an SLA by ID |
| POST | `/api/sla` | Create an SLA |
| PUT | `/api/sla` | Update an SLA |
| DELETE | `/api/sla/{slaId}` | Delete an SLA |
| POST | `/api/sla/clone` | Clone an SLA |

### Calendar API

Retrieve and manage calendars used to calculate SLA working hours.

| **Method** | **Path** | **Description** |
| --- | --- | --- |
| GET | `/api/calendar` | Get all calendars |
| GET | `/api/calendar/{id}` | Get a calendar by ID |
| POST | `/api/calendar` | Create a calendar |
| PUT | `/api/calendar` | Update a calendar |
| DELETE | `/api/calendar/{id}` | Delete a calendar |

### SLA actions API

Retrieve and manage SLA-specific and global actions, previously called notifiers.

| **Method** | **Path** | **Description** |
| --- | --- | --- |
| GET | `/api/notifier/sla/{slaId}` | Get all actions for an SLA |
| GET | `/api/notifier/global` | Get all global actions |
| GET | `/api/notifier/{notifierId}/sla/{slaId}` | Get an action by ID |
| POST | `/api/notifier` | Create an action |
| PUT | `/api/notifier` | Update an action |
| DELETE | `/api/notifier/{notifierId}/sla/{slaId}` | Delete an action |

### Work item SLA API

Retrieve SLA details and history for Jira work items. You can also query multiple work items and manage SLA deadline extensions.

| **Method** | **Path** | **Description** |
| --- | --- | --- |
| GET | `/api/issue-sla/{issueId}` | Get a work item's SLAs |
| GET | `/api/issue-sla/{issueId}/sla/{slaId}` | Get one SLA on a work item |
| POST | `/api/issue-sla/` | Query work item SLAs by JQL |
| POST | `/api/issue-sla/multi` | Get work item SLAs in bulk |
| GET | `/api/issue-sla-history/{issueId}/sla/{slaId}` | Get the history of one SLA on a work item |
| GET | `/api/issue-sla-history/{issueId}` | Get a work item's SLA history |
| POST | `/api/issue-sla/{issueId}/sla/{slaId}/extension/preview` | Preview an SLA extension on a work item |
| POST | `/api/issue-sla/{issueId}/sla/{slaId}/extension` | Extend an SLA on a work item |
| DELETE | `/api/issue-sla/{issueId}/sla/{slaId}/extension` | Undo an SLA extension on a work item |

### Recalculation API

Start, monitor, and abort SLA recalculation jobs.

| **Method** | **Path** | **Description** |
| --- | --- | --- |
| GET | `/api/sla-recalculation` | Get all recalculation records |
| POST | `/api/sla-recalculation` | Start a recalculation |
| GET | `/api/sla-recalculation/{jobId}` | Get a recalculation by job ID |
| POST | `/api/sla-recalculation/{jobId}` | Abort a recalculation |

### Permissions API

Retrieve and update Time to SLA permissions.

| **Method** | **Path** | **Description** |
| --- | --- | --- |
| GET | `/api/permissions` | Get all permissions |
| PUT | `/api/permissions` | Update a permission |

### SLA reports API

Retrieve SLA reports and generate background reports.

| **Method** | **Path** | **Description** |
| --- | --- | --- |
| GET | `/api/sla-reports` | Get all SLA reports |
| POST | `/api/sla-background-report` | Queue a background report |

### Settings API

Manage app-level settings.

| **Method** | **Path** | **Description** |
| --- | --- | --- |
| POST | `/api/advanced-settings` | Save advanced settings |

### Account API

Identify the account a token belongs to.

| **Method** | **Path** | **Description** |
| --- | --- | --- |
| GET | `/api/whoami` | Identify the current token |

## SLA response fields

When retrieving SLA data for a Jira work item, the API response includes information about the SLA goal, timing, and status.

The following table explains common response fields.

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