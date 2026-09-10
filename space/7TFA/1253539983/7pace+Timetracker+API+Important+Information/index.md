# 7pace Timetracker API Important Information

## API Version Links

We provide various versions of our API and the documentation for each. Use the links below to access the relevant 7pace Reporting API.

[Reporting API 3.0 and above](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/)

## API Authorization

Authorized access in 7pace Timetracker for Azure DevOps Services cloud and on-prem have different implementations. Click below for the relevant approach:

## Authorized Access in 7pace Timetracker cloud (Azure DevOps Services)

You can authorize your application in 7pace Timetracker using a Timetracker API token (Bearer) or process based on OAuth 2.0 Authorization Framework.

The **Timetracker API token** is used to connect to the Timetracker APIs (Reporting, REST CRUD, Tracking). Once generated, the token is valid for one year. After it expires, it becomes invalid.

### How to generate the Timetracker API token

1. Navigate to your **Timetracker Settings** > **Reporting and API** > **Reporting & API** page.
2. Click **Create New Token***.*

![Generate_API_Token.png](/cms_trial/assets/dd4cfeb3-b4c9-4ffb-a969-11974dda6769.png)

We also have a tutorial video which shows how to generate the Timetracker API token:

### How to obtain OAuth 2.0 Authorization

OAuth 2.0 supports the following grants (by grants, we mean ways of retrieving an access token):

1. Authorization Code Flow is the way that we initially obtain an access token.  
   For more information on the OAuth 2.0 Authorization Code Flow, see section 4.1 of the OAuth 2.0 specification: <https://tools.ietf.org/html/rfc6749#section-4.1>. The first step is different from the specification: instead of relying on User-Agent (web browser), we use PIN codes to validate a user.
2. RefreshTokens is the way we update expired access tokens.  
   For more information on Refresh Tokens, see section 1.5: <https://tools.ietf.org/html/rfc6749#section-1.5>.

Use **OpenApi** as client\_id to authorize any external application.

### Authorized Access in 7pace Timetracker on-prem (Azure DevOps Server)

To use 7pace Timetracker REST/SignalR API in on-prem environment you don’t need tokens. All requests must be authorized with Negotiate authorization.

### Implementation

7pace Timetracker has the following set of APIs:

1. RESTful API
2. OData API
3. SignalR

For an introduction to SignalR, see: (<https://docs.microsoft.com/en-us/aspnet/signalr/overview/getting-started/introduction-to-signalr>)

### Client - API for Tracking

See the corresponding section in [the 7pace Timetracker API Reference](https://timehub.7pace.com/api_reference/index.html#/).

### Reporting API for DevOps Server on-prem

There is an ongoing issue with Tableau. Use Negotiate authentication.

### Using 7pace Timetracker API in Your Own Project

To help you access 7pace Timetracker's data through our API, we've provided the source code of a simple application that demonstrates basic 7pace Timetracker API usage in [GitHub](https://github.com/Berichthaus/timetracker-api-samplecode).

You can get more information about our API model and parameters at Settings -> Reporting and API -> Reporting and REST API -> [7pace Timetracker API Reference](https://timehub.7pace.com/api_reference/index.html).

### Building your own application with 7pace Timetracker

7pace Timetracker allows you to build custom applications that fully meet the requirements of your organization with the Client API. It is up to you what functionality this application should include. This could be integration between any kind of software you currently have and 7pace Timetracker or new stand-alone applications based on just the 7pace Timetracker API.

#### **Requirements**

- A basic level of experience in any programming language.
- Access to a computer running Windows, Linux or Mac OS.

#### **Platform Overview**

7pace Timetracker is lightweight and simple. It's built on JSON and OData, so you can use it with any language or platform that supports HTTP requests or SignalR (including .NET, JavaScript or PHP). The 7pace Timetracker service runs on a server (on-premise for Timetracker for DevOps Server or the Microsoft cloud for Timetracker for DevOps Services) and provides the following set of APIs for developers: RESTful API, OData API, and SignalR.

#### **Getting Started**

To start developing your own application, learn how our API works in more detail at: [7pace Timetracker API Reference](https://timehub.7pace.com/api_reference/index.html#/).

### DevOps Server (on-prem) Workflow

For pairing with DevOps Services, we do not have any tokens. Timetracker uses Negotiate auth for API endpoints and impersonates calls to DevOps Server with this data.

The only thing we need is the address of the 7pace Timetracker application.

If you know your 7pace Timetracker URI, just use %timetracker\_address%/api address to API.

If you only know the DevOps Server URI and want to find the 7pace Timetracker address, please use this procedure:

1. The user enters AD credentials to connect to the DevOps Server.
2. The user enters the DevOps Server URL with the collection.
3. 7pace Timetracker performs GET request to %CollectionName%/\_apis/Contribution/InstalledApps/.
4. In the returned JSON, find the extension with:  
   "extensionId": “TimetrackerOnPremises”,  
   “extensionName”: “Timetracker”,  
   “publisherId”: “7pace”
5. Use baseUri from the found extension to validate access to GET /api/tracking/client/latest?api-version=3.2

### DevOps Services (cloud) Workflow

You can authorize your application in 7pace Timetracker using two options:

1. Use a Reporting API token. Add the "**Authorization**" header to any 7pace Timetracker API request with value "**Bearer %TOKEN%**"  
   The main downside of this approach is that this token is valid for just one (1) year, and you can only refresh it using the 7pace Timetracker Web UI. If you're writing automation, you should use the next option, get proper access, and use refresh tokens for your application.
2. Use OAuth-base flow for obtaining authorization tokens with the PIN-Pairing API:

   1. Perform a POST request to:  
      *https://{your-organization}.timehub.7pace.com/api/pin/create?api-version={version}*  
      The returned object contains a PIN and a security code (secret).  
      Now, go to the 7pace Timetracker Apps page, and in the "Pair Mobile App" field enter your PIN that was returned from the POST request:

      ![DevOps_Service_Cloud_Workflow.png](/cms_trial/assets/87297f0e-f35e-41b8-9ec0-a2f0e3e1d532.png)
   2. Check if the PIN is validated by performing a POST request to:  
      *https://{your-organization}.timehub.7pace.com/api/pin/status?api-version={version}*  
      With the body containing your secret in quotation marks, as such:

      `"Zjk1ZmI3MjJhMDgwNDJmODkzNWVjZjM3ODdjNjhlMWI4ZDJkY2E4NmQ0ZjI0MzRiYjNhYTZmNmM2YjkxNTdjNQ=="`

      ![Validate_Pin.png](/cms_trial/assets/2c873218-1fd9-41ce-bfba-e5235985db7a.png)

      If the PIN is validated, the server will respond with “validated” as the PIN status.
3. Now you can request a token by performing a POST request to the *token* endpoint with data described below in "**Request definition**":  
   *https://{your-organization}.timehub.7pace.com/token*

   ![Request_Definition.png](/cms_trial/assets/a6109e4d-98fe-47e9-9435-40bb2c980f10.png)

Your PIN is valid for one (1) minute. After you enter your PIN, this security code is bound to you, the specific user and the rest of the OAuth flow can now be executed.

4. If the server returns "Invalid" as the state, request a new token by restarting the whole process flow.  
For more information on PIN pairing, see the corresponding section in the [API Reference.](https://timehub.7pace.com/api_reference/index.html#/)

**Request definition:**

Headers:

Content-Type: application/x-www-form-urlencoded

Body:

client\_id=OpenApi&grant\_type=authorization\_code&code=**{secret}**

Server will return the object with access and refresh tokens.

**IMPORTANT:** A token’s lifetime is one (1) hour (3600 seconds); Refresh Token is valid for one (1) year (129600 seconds).

**Diagram of the process described, above:**

![Process_Diagram.png](/cms_trial/assets/5633bb2b-0902-40bd-92d0-ea8b577f9a2d.png)

**Refreshing tokens**:

To obtain a new token with “Refresh Token”, perform this request:  
POST  
*/token*  
Headers:  
Content-Type: application/x-www-form-urlencoded  
Body:  
client\_id=OpenApi&grant\_type=refresh\_token&refresh\_token=%your\_refresh\_token%

Use access token by adding "**Authorization**" header with value "**Bearer %TOKEN%**" when performing any requests to the 7pace Timetracker API.

**NB:**

A token is valid for SignalR until it disconnects.

Therefore, even an outdated token maintains a valid SignalR connection.

## API Common Error Codes

**Introduction**

In newly-introduced CRUD API, our team now starting classification of errors and putting together all possible states and responses of API and system.

Each error will have it's own unique and constant code that you can relate to.

**System state errors**

- **UnexpectedError - Unexpected error occurred.**  
  General unhanded error during internal logic execution. It will contain additional info with original error and original stack trace.
- **UnknownError - Unknown error occurred. See additional details for more information**  
  Represents an error that  has occurred outside of the Timetracker logic environment. This usually happens when server or cloud issues are present.
- **ApiDisabled - API is disabled due account maintenance**  
  When account is migrating between instances of our application API is disabled to maintain data integrity.
- **LicenseReadOnly - System in a read only state (check your license)**  
  For On-Premises (TFS) only. If license is not valid or expired - API will be disabled as well as main system.
- **ActivityTypeDisabled - Activity type feature is not enabled**  
  Error will affect only "/activityTypes/{id}" endpoint if you try to get any specific Activity Type by Id when feature is disabled.
- **ApiVersionError - API Version not specified, or path do not support required version, or supplied parameters has invalid values**  
  Due the way our system handles versioning, it will fail with version error even if you're specifying correct version of API for endpoint, but supplied incorrect types of parameters (eg. not valid GUID). Recheck your request.
- **QuoteExceededError - Quota exceeded**  
  You're making too many requests. Current quota is dependent on plan type per organization. Check header "Retry-After" for value in seconds when block will be lifted.
- **UnauthorizedError - Unauthorized**  
  You're using invalid authorization credentials or not provided any authorization info. Check [here](/cms_trial/space/7TFA/1253539983/7pace+Timetracker+API+Important+Information/) for authorization options, depending on if you're using cloud or on-premise.
- **AccessDenied - Access denied (you don't have enough rights?)**  
  You've been successfully authorized, but you don't have enough rights to execute requested resource.

**Validation errors**

- **EntityNotFound - Entity not found**  
  Occurs when requested by Id entity is not present in Database.
- **WorkItemIdOrCommentRequired - WorkItemId or Comment required**  
  Occurs when creating or updating worklog. It must have either comment or be associated with Work Item.
- **LengthIsRequired - Length is required**  
  Occurs when creating or updating worklog. It must have length and it cannot be automatically set.
- **LengthMustBePositive - Length must be greater than 0**  
  Occurs when creating or updating worklog. It must have length as positive integer value.
- **FutureCheckFailed - Adding worklogs in a future not allowed by settings**  
  Occurs when creating or updating worklog. Managed by setting "Prevent Time Tracking Beyond Present Day". If Timestamp of a worklog is not meeting selected requirements, this error is raised.
- **ApprovalStateFailed - Selected date is locked for editing by approval**  
  Occurs when creating, updating or deleting worklog. If date of worklog is within approved interval, editing is restricted.
- **NoRightsToWorkLogModification - Worklog cannot be modified by you**  
  Occurs when creating, updating or deleting worklog. If worklog doesn't belong to you and (when deleting) you don't have rights to delete it, error is raised.
- **FilterWorkItemIdsCountExceeded - Filter work items ids count exceeding maximum allowed value (100)**  
  Occurs when requesting list of worklogs and using filter "$workItemIds". If amount of Ids is exceeding maximum allowed value (100), error is raised.
- **DbValidationError - Error while committing entity to database**  
  Occurs when creating, updating or deleting worklog. General error if entity is failing validation in Database. Will contain additional information about errors.

## API Request Limits

The number of requests that you can send to 7pace API is rate limited. This practice, also called 'throttling', is commonly used to secure consistent API performance for all customers. Throttling may be applied to all plans.

If you have received a message with a response code '429' that says, 'The request has been canceled because your API usage was exceeded', you will have to wait before sending a new request. Prior to cancellation, our system may attempt to mitigate this by slowing down request processing.

Rate limits are dynamic and may differ per company size and the current traffic, but are generally high enough to accommodate common use cases, as outlined in the table, below.

|  |  |
| --- | --- |
| **Use case** | **Rate limiting** |
| CRUD | Minimal rate limiting. A hundred requests / user / hour or even more should be safe unless you send all the requests within a very short time period (like a minute). |
| Obtaining data - one time or incremental | Tighter rate limiting due to larger responses, but sufficient for handling one-time initial load or incremental refresh with a reasonable frequency and refresh period length (the higher the frequency, the shorter the refresh period should be set). |
| Obtaining data - repeated | If you obtain all historical data repeatedly / multiple times per day, you will probably hit set limits; if this occurs, refer to our [How to avoid rate limiting](/cms_trial/space/7TFA/1253539907/How+to+Avoid+API+Rate+Limiting/) article. |

If the current rate limits do not support your current or planned process, contact us via [our Support Portal](https://appfire.atlassian.net/servicedesk/customer/portals) and we will work with you on a case-by-case basis.

#### Limits per plan

Additional API request limits may be imposed based on your 7pace Timetracker plan type.

The Free plan is limited with 50 requests per hour or 5 requests per minute. Limits for our other plans are listed in detail on the [7pace pricing page](https://www.7pace.com/editions).

#### Final notes

7pace may increase the throttling for a particular organization should we detect extremely excessive usage (e.g. infinite loops, intentional abuse). We will make a reasonable attempt to contact you via email prior to applying the increased throttling.

If you have any additional questions about API usage within your team, visit [our Support Portal](https://appfire.atlassian.net/servicedesk/customer/portals).

## API Lifetime Policies

#### Stable API Policy

The official support for API versions is 2 years from their release.

We guarantee that the API version will be not be affected and will continue working in productive mode for two years from the date of its release, with the possibility of deprecation after this period expires.

Deprecated APIs then eventually become retired (turned off). We give reasonable advance notice of such retirement to 7pace Timetracker administrators, but we also encourage the administrators to follow this article so as they receive notifications about API status changes.

The very latest version of the API is always supported. The latest beta API version is **3.3-beta.**

Release dates for the API versions are listed below:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **API version** | **Release date** | **Status** | **Retirement date** | **Note** |
| 2.1 | - | ⛔ Deprecated | December 1, 2023 | *See* [*API 2.1 Migration FAQ*](https://support.7pace.com/hc/en-us/articles/6902631825425) *for retirement date and migration guide* |
| 3.0 | *2017-11-15* | 🟡 Deprecated | Not set yet |  |
| 3.1 | *2019-09-11* | 🟡 Deprecated | Not set yet |  |
| 3.2 | 2022-09-05 | 🟢 Active | N/A |  |
| 3.3-beta | 2023-08-08 | 🟢 Active | N/A | Introducing SoftDelete |

#### Beta API Policy

As the "Beta API" is actively developed, it might change at any time, including structural changes, changes in models, responses and URLs until it reaches a stable state (indicated by removed “-beta” flag in the version number).  
In some cases, it could also contain specific improvements and fixes that are not present in the production version.  
The latest beta API version is *3.3-beta*.