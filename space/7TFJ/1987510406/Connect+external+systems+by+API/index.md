# Connect external systems by API

![TryItButton (2).png](/cms_trial/assets/cc8bfbf9-b65e-487f-87cb-596c707a4cf1.png)

## About this API

The **7pace Timetracker for Jira** API enables secure and efficient access to your 7pace worklog data and account custom field settings. This lets you access your worklog data in external systems, such as dashboards, PowerBI reports, or HR systems.

Obtain OpenAPI Specification from the **Endpoint specification** section below.

**Note**: When connecting to your 7pace Timetracker API, there are three base URL for all connections (for more information, check the next section).

Additionally, multiple versions of the API are currently available, using the version number in the URL. For example `https://timehubjra.7pace.com/api/v2` will access version 2.

Configure your connection with your API token (see below), and you will be able to access the data for your account.

This URL acts as a bridge to your specific Jira instance. Configure your connection with your API token (see below), and you will be able to access the data for your instance.

## Base Paths for API Access

The 7pace API for fetching worklogs and account settings is available across multiple regions. To ensure the fastest and most efficient access to our services, we recommend using a geographically direct base path based on where your Jira data is hosted:

- <https://us-timehubjra.7pace.com> – Use this if your Jira is pinned to the US region.
- <https://eu-timehubjra.7pace.com> – Use this if your Jira is pinned to the EU region, or if it is not pinned to any specific region.
- <https://timehubjra.7pace.com> – Use this universal path if you are unsure where your data is hosted.

If you use the universal path, your requests will be automatically redirected to the correct region. However, this may result in extra network latency.

## Endpoints

- [API version](/cms_trial/space/7TFJ/2292973587/API+version/)
  - [Worklogs](/cms_trial/space/7TFJ/2233401473/Worklogs/)
  - [Worklog changes](/cms_trial/space/7TFJ/2261123154/Worklog+changes/)
  - [Settings: Custom Fields](/cms_trial/space/7TFJ/2234482689/Settings%3A+Custom+Fields/)

## Contact

If you require assistance, please contact our support team using the [Appfire Support Portal](https://appfire.atlassian.net/servicedesk/customer/portal/11).

## Endpoint Specification

Developer documentation is available! This includes endpoint definitions and all current schemas. You can access those here:

- [Version 1 Endpoint specification](https://timehubjra.7pace.com/swagger/index.html?urls.primaryName=7pace+REST+API+v1)
- [Version 2 Endpoint specification](https://timehubjra.7pace.com/swagger/index.html?urls.primaryName=7pace+REST+API+v2)

## Create an API token

The API requires JWT Bearer Token authentication. Use the following steps to create a new token:

1. In the left hand panel of your Jira instance, click **7pace Timetracker**.
2. Click **Settings** > **API Tokens**.

   ![Timetracker settings with API Tokens selected.](/cms_trial/assets/b9c2aad9-65f6-4490-bcc3-46e4b9cc604e.png)
3. Click **+ Create token**.
4. Name the token and set an expiration date.

   ![Create an API token dialog with calendar displayed.](/cms_trial/assets/f6ae6b85-2f2e-42b8-a9fa-5fcdc61c9c3c.png)
5. Click **Create**.
6. Copy the API token and save it.  
   ⚠️ An API token can’t be recovered after completing this step.

   ![Copy API token and save dialog.](/cms_trial/assets/3209275f-d049-4ba0-b014-1690b0dcba8d.png)

## Authentication

Include your token in the Authorization header of each request.

### Curl

```shell
curl --location '<https://timehubjra.7pace.com/api/v1/worklogs'> \
--header 'Authorization: Bearer YOUR_TOKEN'
```

## Error handling

The 7pace Timetracker API provides consistent error handling, including detailed error messages and developer documentation.

- General Errors:

  - Title: INTERNAL\_ERROR
  - Status: 500
  - Detail: Exception message.
  - Trace ID included (traceId) for debugging.
- Timeout Errors:

  - Title: BAD\_REQUEST
  - Status: 400
  - Special handling for timeouts.
- GraphQL Errors:

  - Title: BAD\_REQUEST
  - Status: 400
  - Detail: Single or multiple GraphQL error messages.
  - Special handling for timeouts.
- Validation Errors:

  - Title: VALIDATION\_ERROR
  - Status: 400
  - Detail: “One or more validation errors occurred. Check your input parameters.”

### Examples:

```json
{
    "title": "VALIDATION_ERROR",
    "status": 400,
    "detail": "One or more validation errors occurred. Check your input parameters.",
    "errors": {
        "queryValues": [
            "Unsupported query value for key 'createdAt.end': 'Provided value '123' is not a valid date.'"
        ],
        "queryParameters": [
            "Unexpected query parameters: createdAt.stat"
        ]
    },
    "traceId": "00-163698a761739c0c-01"
}

{
  "title": "BAD_REQUEST",
  "status": 400,
  "detail": "Your request takes too long, try to simplify it or try again later.",
  "traceId": "00-abc123def456-xyz789-01"
}

{
  "title": "INTERNAL_ERROR",
  "status": 500,
  "detail": "Unexpected error occurred.",
  "traceId": "00-abc123def456-xyz789-01"
}
```

## Rate limiting

The 7pace Reporting API applies dynamic rate limiting to ensure service stability. In Jira Cloud, rate limiting is implemented per tenant so as to ensure performance for each tenant.

Rate limiting is implemented as follows:

- **CRUD operations**

  - Create worklog (POST) - 3000 requests / 15 minutes
  - Update worklog (PUT) - 3000 requests / 15 minutes
  - Remove worklog (DELETE) - 3000 requests / 15 minutes
- **Reporting API**

  - Get worklogs (GET) - 300 requests / 15 minutes
  - Get worklog changes (GET) - 300 requests / 15 minutes
  - Get custom fields (GET) - 300 requests / 15 minutes

If rate limits are exceeded, requests will be throttled and a `429 Too Many Requests` status will be returned. Clients are advised to implement exponential backoff or retry logic as needed.

## Future enhancements

Have a request for future API improvements or updates? [Submit it here!](https://portal.productboard.com/7pace/5-7pace-timetracker-for-jira/tabs/19-in-progress)

We plan to further enhance APIs by allowing customers to obtain incremental changes only (thus increasing the speed of responses) and introducing an improved structure of custom time tracking fields for easier processing. Stay tuned!