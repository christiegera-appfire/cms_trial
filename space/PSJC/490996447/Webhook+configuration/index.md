# Webhook configuration

Webhooks in Power Scripts let you extend your Jira functionality by creating custom API endpoints that execute your SIL scripts. This integration enables external systems to interact with your Jira instance through standard REST calls from any HTTP client.

## How webhooks work

1. Create SIL scripts in SIL Manager that contain specific business logic, data processing, or automation requirements.
2. Configure webhooks in Power Scripts that link to these specific SIL scripts, creating unique REST API endpoints accessible via HTTP methods like GET, POST, or PUT.
3. External systems and REST clients can make HTTP requests to these webhook URLs, which triggers the execution of your pre-defined SIL scripts.
4. Your scripts can process incoming data from the external REST call (using the `getWebhookPayload()` function) and send back results (using the `appendToWebhookResponse()` function).
5. The webhook returns either an immediate REST response with your script's output (synchronous) or acknowledges the request while processing continues in the background (asynchronous).

This creates a RESTful integration bridge between your Jira instance and other business systems without requiring complex custom development.

---

## Webhook execution types

Webhooks can be configured to execute in two different ways, depending on your integration needs:

- **Synchronous webhooks**: These webhooks follow a direct request-response pattern. When a client makes a connection and sends a request, Power Scripts processes it immediately and returns a response with the results. This is ideal when the caller needs immediate feedback or data from the operation.
- **Asynchronous webhooks**: These webhooks immediately acknowledge receipt of the request with an HTTP 200 response, but process the actual operation in the background. The script continues running after the initial response is sent, but any results or return codes from the script execution are not communicated back to the caller. Choose this option for operations where immediate results aren't needed or when processing is time-intensive.  
  Asynchronous executions can be monitored in the Runtime tab (Queued Tasks and SIL Threads). Thread pool configuration is available in *General* → *Thread pool* tab.

Consider using asynchronous webhooks when:

- You don't need immediate results from the operation.
- The processing task is large or time-consuming.
- You want to avoid Jira's webhook retry mechanism triggering duplicate executions for long-running processes.

---

## Webhook security context and permissions

Understanding the security context of webhook execution is crucial for proper implementation. Webhooks operate without authentication, using the Jira add-on pseudo-user (an internal component of the cloud integration). This has important implications for your scripts:

- Not all Jira functionality is accessible in this context.
- Functions that require user context (like `currentUser()` and `archiveProject()`) can cause script errors if called directly.
- To perform operations that require specific permissions, you must configure appropriate permissions or explicitly specify a user with the `runAs` function.

Always test your webhooks thoroughly. Scripts that work perfectly in the SIL Manager environment may behave differently when called via webhooks due to these permission differences.

---

## Writing SIL script for Webhooks

When creating SIL scripts for webhooks, you can leverage these special webhook-specific functions to process incoming data and return responses.

- [getWebhookPayload](/cms_trial/space/PSJC/434733710/getWebhookPayload/)
- [appendToWebhookResponse](/cms_trial/space/PSJC/433654676/appendToWebhookResponse/)

These functions enable powerful integration capabilities between external systems and your Jira instance.

### Basic request processing and response

This example demonstrates how to extract information from an incoming webhook request and send a formatted response back to the caller.

```c++
//getting the REST/HTTP call input parameters:
WebhookPayload httpRequestPayload = getWebhookPayload();

//getting the used HTTP method:
string httpMethod = httpRequestPayload.httpMethod;//This can be something like "GET", "POST", "PUT" etc.

//getting the http request payload (body):
string httpPayload = httpRequestPayload.payload;

//getting the http query parameters:
WebhookParam[] httpQueryParams = httpRequestPayload.queryParams;
string firstQueryParamName = httpQueryParams[0].name;
string firstQueryParamValue = httpQueryParams[0].values[0];

//sending the response back to the caller:
appendToWebhookResponse("http method:");
appendToWebhookResponse(httpMethod);
appendToWebhookResponse("payload:");
appendToWebhookResponse(httpPayload);
appendToWebhookResponse("firstQueryParamName:");
appendToWebhookResponse(firstQueryParamName);
appendToWebhookResponse("firstQueryParamValue:");
appendToWebhookResponse(firstQueryParamValue);

//returning a HTTP status code:
return 200;
```

The script above demonstrates how to access various components of an incoming webhook request, including the HTTP method, request body content, and URL query parameters, while also showing how to build a custom response by sequentially appending text elements and returning a successful HTTP status code (200 OK).

The format for the return line is always `return <HTTP status code>;` It is highly recommended that you use valid HTTP status codes.

### Advanced remote script execution

This example demonstrates a more advanced technique where a webhook can execute code sent from the client. Note that this approach can present security risks and should be used with caution.

```text
//this may not be accepted by the security in your environment but it is possible!

WebhookPayload pload = getWebhookPayload(); //gets the payload

string codeToRun = pload.payload; //code is assumed to be in the payload

if(codeToRun == null) {
    logPrint("ERROR", "Nothing to run");
    return 400;
}
try {
    logPrint("INFO", "Executing remote code >>" + codeToRun);
    
    string [] args; //::TODO:: here you can create a protocol to transmit params. for simplicity, no params in this example
    
    string [] ret = runSILInline(codeToRun, args);
    
    logPrint("INFO", "Executing remote code done, results are >>" + ret);
    
    appendToWebhookResponse((string)ret);
    return 200;
} catch {
    appendToWebhookResponse("Exception:" + lastExceptionClass() + "///" + lastExceptionMessage());
    return 400; //we are not happy
}
```

This script demonstrates a more advanced technique for webhook handling, where executable code received within the webhook payload is validated, safely processed using error handling, executed using the `runSILInline` function, and responded to with appropriate HTTP status codes based on whether the execution succeeded or failed.

It is important to note that you're responsible for the security of your webhooks. While they're a powerful tool for integration, it's crucial to use them thoughtfully, especially with features like remote code execution shown in this example.

---

## How to set up a webhook

Configuring webhooks in Power Scripts lets you define what URI and HTTP method(s) will be used to invoke your specific SIL scripts. This process creates accessible endpoints that external systems can call to trigger your custom functionality. Follow these steps to set up your webhook configurations and make them available to integrate with other applications.

1. To access the Webhooks configuration:

   1. Click **Settings** > **Marketplace Apps**.
   2. Go to **Power Scripts** > **Configurations** > **Integrations** > **Web Hooks**.
   3. Click **Add webhook**.
2. To create a webhook entry:

   1. Click **Add webhook**.
   2. Fill in the required settings and parameters.![Power Scripts for Jira Cloud token generation interface](/cms_trial/assets/dfd12bd3-202c-4714-bf34-9ed48afd85fd.png)

### Key configuration settings

| **Configuration setting** | **Description** |
| --- | --- |
| **Name** | Type a name for the webhook. This name will be used as an identifier for the webhook configuration. |
| **Methods** | Select which HTTP method(s) this webhook will respond to. You can choose multiple methods (like GET, POST, PUT) to enable different types of interactions with this endpoint. Each method creates a separate access point using the same URI but allows different operations to be performed. |
| **Script** | Select the SIL script that will execute when this webhook is called. This script contains the business logic that processes incoming requests and generates responses, forming the core functionality of your webhook endpoint. |
| **Synchronous** | The execution type of the webhook: synchronos/asyncronous.  Determines how the script responds to requests.   - In synchronous mode (toggle switched on), the webhook waits for the script to complete and returns its response directly to the caller. - In asynchronous mode (toggle off), the webhook immediately returns a success response (200 OK) while the script executes in the background without returning results to the caller. |

1. Save the configuration.  
   The new webhook entry displays on the configuration page as illustrated in the screenshot below:

   ![Power Scripts for Jira Cloud webhook icon](/cms_trial/assets/3b52e103-a95f-442b-969c-d67afbffb3b5.png)

The **URI** column in the configuration table displays the unique endpoint path for each webhook. To construct the complete URL for calling your webhook, you'll need to combine this path with your Power Scripts base URL.

---

## Making webhook API calls

Webhooks in Power Scripts use token-based security to ensure that only authorized systems can trigger your scripts. Each token is specific to the HTTP method being used, providing granular access control.

### How to generate a token

To generate a token for webhook access:

1. Navigate to your webhook configuration page.
2. Click the lock icon next to the webhook you want to use.
3. Set an appropriate expiration date for the token.
4. Select the HTTP method (GET, POST, PUT, etc.) you intend to use.
5. Copy the generated token immediately, as it will not be displayed again.

![Power Scripts for Jira Cloud JSON escape character demonstration](/cms_trial/assets/0514a0cb-5164-432c-a64f-0a1c2e64f468.png)

### Authenticating your API calls

When calling your webhook, you must include the token using one of these methods:

- Add an HTTP header named `X-SIL-TOKEN` containing your token. This is the preferred approach as it keeps the token out of logs and URLs.
- Include a query parameter named `silToken` in the URL

  - Example: `?silToken=your-token-value`

### Calling your webhook

Once you have generated a token, you can call the webhook using any HTTP client (such as curl, Postman, or your own application code). Your token is provided either as an HTTP header (`X-SIL-TOKEN`) or as a query parameter (`?silToken=<token>`).

The complete URL structure for calling a webhook is:  
`https://<your-power-scripts-url>>/rest/keplerrominfo/refapp/latest/webhooks/<webhook-name>/run`

Where:

- `<your-power-scripts-url>` is your server location
- `<webhook-name>` is the name you gave to your webhook during configuration

For example, if your Power Scripts instance is located at `https://us1.powerscripts.anova.appfire.app/` (the URL for US-based installations at the time of this documentation) and the name of your webhook is `testsupport`, you would access the webhook using:

`https://us1.powerscripts.anova.appfire.app/rest/keplerrominfo/refapp/latest/webhooks/testsupport/run`

The base URL for your Power Scripts installation may vary depending on your deployment region and version. You can find your specific plugin's base URL by examining the connect descriptor's `baseUrl` JSON entry if needed.

Example curl command with header (recommended approach):

```text
curl -X POST \
  "https://us1.powerscripts.anova.appfire.app/rest/keplerrominfo/refapp/latest/webhooks/issue-analyzer/run" \
  -H "X-SIL-TOKEN: eyJhbGciOiJIUzI1NiJ9..." \
  -H "Content-Type: application/json" \
  -d '{"issueKey": "PROJ-123"}'
```

Example with query parameter (not recommended for production):

```text
https://us1.powerscripts.anova.appfire.app/rest/keplerrominfo/refapp/latest/webhooks/issue-analyzer/run?silToken=eyJhbGciOiJIUzI1NiJ9...
```

---

## Token management

All webhook tokens have these important characteristics:

- **Expiration**: Tokens automatically expire after the date you set during generation.
- **Single-use per method**: Each token works only for the specific HTTP method it was generated for.
- **Non-revocable individually**: Individual tokens cannot be selectively invalidated.

If you want to revoke a token that is accidentally shared or compromised:

- Navigate to the *SIL Wehooks Configuration* page and click the **Expire tokens** icon for the selected webhook. This will immediately revoke all existing tokens for all HTTP methods for this webhook, requiring new tokens to be generated for any further access.

![Power Scripts for Jira Cloud JSON quotes demonstration](/cms_trial/assets/cd6d360b-d1ac-4dd1-b564-e2a2528e8a28.png)

---

## Monitoring asynchronous webhooks

When using asynchronous webhooks, you'll need to monitor their execution separately since they don't provide responses directly to the caller. Power Scripts provides several tools to track the status and performance of your asynchronous webhook executions.

| **To…** | **Do this…** | **This helps you to…** |
| --- | --- | --- |
| View running tasks | Navigate to **Administration** > **Manage Apps** > **Power Apps Config** > **Runtime** > **Queued Tasks** to see all webhook operations that are currently being processed. | Verify that your asynchronous webhooks are executing as expected and identify any that may be taking longer than anticipated. |
| Monitor system threads | Navigate to **Administration** > **Manage Apps** > **Power Apps Config** > **Runtime** > **SIL Threads** to view all system threads running scripts, including those triggered by webhooks. | Get visibility into the resource utilization of your webhook operations.  Exercise caution when terminating threads. Forcibly stopping a thread can disrupt critical Jira processes that depend on it, potentially causing system instability that requires a server restart. Only terminate threads when absolutely necessary and when you understand the potential consequences. |
| Set up the Thread pool configuration | Navigate to **Administration** > **Manage Apps** > **Power Apps Config** > **Runtime** > **Thread pool** to adjust the thread pool settings for high-volume webhook usage. | Optimize how many concurrent asynchronous operations can run, balancing system performance with webhook throughput. |

By regularly monitoring these areas, you can ensure your asynchronous webhooks are executing properly and make adjustments to optimize their performance based on your specific usage patterns.

## More configuration guides

## Webhook-specific functions

- [getWebhookPayload](/cms_trial/space/PSJC/434733710/getWebhookPayload/)
- [appendToWebhookResponse](/cms_trial/space/PSJC/433654676/appendToWebhookResponse/)
- [currentUser](/cms_trial/space/PSJC/434507219/currentUser/)
- [runAs](/cms_trial/space/PSJC/434374366/runAs/)
- [admArchiveProject](/cms_trial/space/PSJC/433000656/admArchiveProject/)