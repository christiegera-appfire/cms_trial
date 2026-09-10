# Converting a cURL script into a SIL script

Converting a cURL script into a SIL script can be time-consuming. Make the conversion easy by following these steps!

## Instructions

For this example, I will be building off this page, “[Running Scripts Via REST](/wiki/spaces/PSJC/pages/491002010)”.

1. Import the curl script into Postman by following [these instructions](/cms_trial/space/PSJC/491002210/Importing+a+cURL+script+into+Postman/).
2. In the right-hand side of Postman, click on the “</>” symbol to see the code converter.
3. Select the language you would like to convert. “Java - Unirest” is the easiest because it parses the headers in a way that is easiest to refactor into SIL code.

   ![Power Scripts for Jira Cloud cURL conversion example interface](/cms_trial/assets/2abc65fc-fbaf-4bb5-aa03-fd20bcd51738.png)
4. Create headers based on the Java code. The following copied from the Java code…

   ```text
   .header("Accept", "application/json")
   .header("Content-Type", "application/json")
   .header("Authorization", "Basic PFVTRVJOQU1FOlBBU1NXT1JEPg==")
   ```

   …can be converted into:

   ```text
   HttpRequest request;
   request.headers += httpCreateHeader("Accept", "application/json");
   request.headers += httpCreateHeader("Content-Type", "application/json");
   request.headers += httpCreateHeader("Authorization", "Basic PFVTRVJOQU1FOlBBU1NXT1JEPg==");
   ```
5. Now set a string variable using the body. You should be able to paste the string without modification.

   ```text
   string payload = "{ \n  \"source\": {\n    \"type\": \"FILE\", \"code\": \"<PATH/TO/FILE.SIL>\"\n  },\n    \"args\": [<\"ARGUMENTS\", \"FOR\", \"ARGV\", \"GO HERE\">]\n  }";
   ```
6. Lastly, convert the Java post() method to httpPost():

   ```text
   httpPost("http://localhost:8080/rest/keplerrominfo/refapp/latest/async-script/runScript", request, payload);
   ```

## Final Script

Now that we have all the basic building blocks for a script, put them all together and add some error message handling at the end of the script. If you would like to change up the values passed by the payload, see this documentation on [working with JSON](/cms_trial/space/PSJC/491002067/Working+with+JSON+Data/).

```text
string payload = "{ \n  \"source\": {\n    \"type\": \"FILE\", \"code\": \"createIssue.sil\"\n  },\n    \"args\": [\"EX\", \"\", \"Task\", \"summary goes here\"]\n  }";

HttpRequest request;
request.headers += httpCreateHeader("Accept", "application/json");
request.headers += httpCreateHeader("Content-Type", "application/json");
request.headers += httpCreateHeader("Authorization", "Basic PFVTRVJOQU1FOlBBU1NXT1JEPg==");

string value = httpPost("http://localhost:8080/rest/keplerrominfo/refapp/latest/async-script/runScript", request, payload);

runnerLog(value);

number statusCode = httpGetStatusCode();
if (statusCode >= 200 && statusCode < 300) {
    runnerLog("SUCCESS");
}
else {
    string msg = trim(statusCode) + ":" + httpGetErrorMessage() + ":" + httpGetReasonPhrase();
    runnerLog(msg);
}
```