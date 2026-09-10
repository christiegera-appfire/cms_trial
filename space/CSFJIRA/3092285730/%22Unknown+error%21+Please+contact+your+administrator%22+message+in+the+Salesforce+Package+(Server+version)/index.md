# "Unknown error! Please contact your administrator" message in the Salesforce Package (Server version)

## Summary

After applying the [API access token](https://appfire.atlassian.net/wiki/spaces/CSFJIRA/pages/470754678/Setting+up+a+connection+to+Jira) on the Salesforce package, an "*Unknown error! Please contact your administrator*" message appears even though the Connection seems to be successfully established:

![contentId-3092285730](/cms_trial/assets/0990f794-8d1e-44a2-b802-dabe67f4da13.png)

## Environment

- Jira server
- Connector for Salesforce & Jira (server) any version

## Diagnostics Steps

You can use the following Apex code to check the connectivity from Salesforce to Jira:

```text
Http http = new Http();
HttpRequest req = new HttpRequest();
req.setEndpoint('<JIRA URL>');
req.setMethod('GET');
HttpResponse response = http.send(req);
System.debug('STATUS: ' + response.getStatusCode());
System.debug('BODY: ' + response.getBody());
```

⚠️ Replace `<JIRA URL>` with your Jira's base URL.

You can run the code by going to **Salesforce > Developer Console > Debug > Execute Anonymous Window**. Once you hit execute you'll be directed to the results.

## Cause

This is usually caused by a connectivity issue between the Salesforce site and your Jira server instance.

Something might be blocking the connection (for example firewall, proxy, security software, or even redirections configured on Jira like SSO).

Here is an example of a proxy connectivity issue:

![contentId-3092285730](/cms_trial/assets/f6811cad-89bd-47b9-bc53-e27b4903d29e.png)

## Workaround

Not applicable.

## Resolution

You may need to work with the IT team in your company to allow the Salesforce package to access your Jira server instance through the Internet and fix the connectivity issue.