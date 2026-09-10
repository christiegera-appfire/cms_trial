# Working with JSON Data

As happens from time to time, you will want to work with JSON data. For example, when passing JSON data when using httpPut() or httpPost().

## Background

In this example, I will be using the [this REST API example](https://community.atlassian.com/t5/Jira-Service-Management/REST-API-update-Comment-to-internal/qaq-p/1483037) from the Atlassian Community.

## Method 1 - Add JSON Data Inline

As is shown in the example, we start with the example JSON that will be used to input.

|  |
| --- |
| ```text "properties": [    {     "key": "sd.public.comment",     "value": {        "internal": true     }    }   ] } ``` |

## Overview

1. Use the Find/Replace feature of the SIL Manager to add an escape character before every quote.
2. Surround each line with quotes and place a plus sign at the end.
3. Set the newly formatted JSON to a string variable and put a semicolon at the end.

## Step 1 - Add an Escape Character before Every Quote

Use the Find/Replace feature of the SIL Manager to add an escape character before every quote.

![Power Scripts for Jira Cloud JSON accuracy validation demonstration](/cms_trial/assets/711a9f31-58d1-4c3a-8f4c-13a4e083e87f.gif)

## Step 2 - Place Quotes Around Each Line

Surround each line with quotes and place a plus sign at the end. Place a semicolon at the end.

![Power Scripts for Jira Cloud JSON value replacement demonstration](/cms_trial/assets/674ff38a-bbc1-4068-9f41-220e2f299668.gif)

## Step 3 - Set the Formatted JSON to a String Variable

Set the entire code block to a string variable so that it can be passed into the REST endpoint.

|  |
| --- |
| ```text string updateInfo = "{" +                         "\"properties\": [" +                             "{" +                                 "\"key\": \"sd.public.comment\"," +                                 "\"value\": {" +                                     "\"internal\": true" +                                 "}" +                             "}" +                         "]" +                     "}";                       runnerLog(updateInfo); ``` |

## Step 4 - Print Output and Check for Accuracy

The output should match the original JSON from the beginning.

![Power Scripts for Jira Cloud postfunction configuration interface](/cms_trial/assets/04d48c12-440c-45f5-9e9a-a7cb16ad4716.gif)

## Step 5 - Change Desired Hard-Coded Values to Accept Variables

Add a variable and use plus signs to concatenate it to the existing string values. Again, the output should match the original JSON from the beginning.

![Power Scripts for Jira Cloud WSJF scripted field configuration](/cms_trial/assets/2b2d78b9-b2e4-4e54-b418-261e99f65827.gif)

## The Final Script

Below we use [httpPut()](/cms_trial/space/PSJC/434995476/httpPut/) to pass the "updateInfo" values to update the Service Desk value "isPublic" to false.

|  |
| --- |
| ```text string isPublic = "false"; number [] ids = getAllCommentIds(key); number lastComment = ids[size(ids) -1];     string updateInfo = "{" +                         "\"properties\": [" +                         "{" +                         "\"key\": \"sd.public.comment\"," +                         "\"value\": {" +                             "\"internal\": " + isPublic + "" +                         "}" +                         "}" +                         "]" +                     "}";     HttpRequest request;  request.headers += httpCreateHeader("Content-Type", "application/json");  request.headers += httpBasicAuthHeader("admin", "admin");     string result = httpPut("http://localhost:8080/rest/api/3/issue/" + key + "/comment/" + lastComment, request, updateInfo);   // runnerLog(result);   number statusCode = httpGetStatusCode(); if (statusCode >= 200 && statusCode < 300) {     runnerLog("SUCCESS"); } else {     string msg = trim(statusCode) + ":" + httpGetErrorMessage() + ":" + httpGetReasonPhrase();     runnerLog(msg); } ``` |

## Additional Help

Need help implementing this script? Talk to me directly to me by clicking on the bot on this page.