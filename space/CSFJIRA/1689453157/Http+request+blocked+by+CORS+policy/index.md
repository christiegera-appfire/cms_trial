# Http request blocked by CORS policy

## Purpose

When trying to access the Jira section in Salesforce, an error is shown. Reviewing the console/HAR file, the following error can be seen:

#### **Error Message**

```text
has been blocked by CORS policy: The 'Access-Control-Allow-Origin' header has a value 'https://backroads--uatsandbox.lightning.force.com' that is not equal to the supplied origin
```

## Answer

This issue is related to [CORS policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS). In the HAR file, the original URL is different from what is shown in the error.

To make sure that Salesforce returns the correct CORS information on the HTTP header (so that the browser will block the request), you need to allow the [origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin#:~:text=The%20Origin%20request%20header%20indicates,be%20included%20in%20the%20request.) in the request header:

1. Go to **Setup** > search for **CORS** and click it.
2. Under **Allowed Origins List**, select **New** and enter the origin URL pattern.

If performing the steps mentioned above does not resolve the issue, contact [Appfire Support](/cms_trial/space/CSFJIRA/1689453157/Http+request+blocked+by+CORS+policy/) to investigate this further.