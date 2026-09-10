# Jira Data Center certification error - PKIX path building failed

## Purpose

This error is present in Jira Data Center only. This occurs when there are validation issues with the certificates used on the Jira instance.

## Answer

1. To verify this, run the following test:

   1. Run this query on the Developer console to test the connection between Jira and Salesforce.

      ```text
      Http http = new Http();
      HttpRequest req = new HttpRequest();
      req.setEndpoint('<JIRA URL>');
      req.setMethod('GET');
      HttpResponse response = http.send(req);
      System.debug('STATUS: ' + response.getStatusCode());
      System.debug('BODY: ' + response.getBody());
      ```
2. If the "CALLOUT\_REQUEST" line does not show "Status Code=200", you will see a certificate related error. This error will be recorded in the support .zip file.

   ![contentId-3092056087](/cms_trial/assets/155cbc5c-3f87-493b-a0ee-a14d058868e9.png?version=1&modificationDate=1678796544449&cacheVersion=1&api=v2)
3. Use a publicly available SSL checker page to verify the certificates.
4. You will get an error message indicating that "No SSL certificates were found on your Jira instance".

The SSL checker will only work if the Jira instance is open to public.

1. The certificate error message and SSL checker warning confirms that it is a certificate issue. Reach out to your internal IT/Networking team to resolve this.