# Generic HTTP Request (reusable script include)

## Problem

Making an extremal HTTP request is an extremely common task. Much of the work to prepare to send the request is identical from script to script.

## Solution

The easiest way to solve this is to use a include like this one so that the code does not need to be created every time. Another benefit of a script like this is that more time and attention can be placed in areas like logging and debugging.

## Script components

### httpResult struct

The purpose of this struct is to break up the data returned into 3 pieces of information required to process the call:

1. Was the call successful?
2. If the call failed, why did it fail?
3. If the call succeeded, get the data

#### **httpResult struct**

```text
struct _httpResult {
    boolean success;
    string message;
    string data;
}
```

## generateRequest function

With any HTTP request one of the more labor intensive parts is authenticating with the external system. This function was separated from the main function (below) so that multiple system requirements can be used by passing a parameter to the function.

#### **generateRequest function**

```text
function generateRequest(string type) {
    HttpRequest request;
    HttpHeader header = httpCreateHeader("Content-Type", "application/json");
    request.headers += header;
    
    if(type == "SERVER") {
        HttpHeader authHeader = httpBasicAuthHeader("jmuse", "Pc9vfdhssh5B73c");
        request.headers += authHeader;
    } else {
        HttpHeader header2 = httpCreateHeader("Authorization", "Basic am9uYXRoYW4ubXVz6RFdfjghndPVkJQNmhKdGpMSzlBMkM=");
        request.headers += header2;
    }
    
    return request;
}
```

The authentication information (username and passwords) was displayed in this script to help with readability and understanding. In real world applications this information would be encrypted and stored as a persistent variable. See the example below for use of persistent variables.

## genericRequestCall function

This is the main function that will get reused by other scripts. It will actually make the HTTP request. It supports the main methods like GET, PUT, DELETE, and POST. It accepts 4 parameters:

1. **Request URL** (string) - the URL of the system to make the request to
2. **Method** (string) - HTTP methods like GET or POST
3. **Data** (JSON) - JSON data to be passed in the request
4. **HttpRequestion** (object) - SIL object, this is also the output of the generateRequest which is designed to be used in this parameter.

#### **genericRequestCall function**

```text
function genericRestCall(string url, string method, string data, HttpRequest request) {
    
    _httpResult result;
    
    if(method == "GET") {
        result.data = httpGet(url, request); //replace with specific domain name
    } else if (method == "PUT") {
        result.data = httpPut(url, request, data);
    } else if (method == "DELETE") {
        result.data = httpDelete(url, request, data);
    } else {
        result.data = httpPost(url, request, data);
    }

...
```

## Error check and return statement

The final part of this script is checking if the request was successful. If it is successful the script passes the httpResult containing the requested data. If not, it prints the errors to the console and to the Jira log. It also returns the httpResult containing the failure information.

#### **Error check**

```text
    number statusCode = httpGetStatusCode();
    if (statusCode >= 200 && statusCode < 300) {
        result.success = true;
    }
    else {
        string HTMLmsg = "<font color='red'><strong>ERROR: </strong></font>URL - " + url + " <br /> {" + trim(statusCode) + " : " + httpGetErrorMessage() + " : " + httpGetReasonPhrase() + "} " + toJson(data);
        runnerLog(HTMLmsg, true);
        logPrint("ERROR", URL - " + url + " <br /> {" + trim(statusCode) + " : " + httpGetErrorMessage() + " : " + httpGetReasonPhrase() + "} " + toJson(data));
        result.success = false;
        result.message = msg;
    }
    
    return result;
```

## Full Scripts

#### **genericRest.incl**

```javascript
struct _httpResult {
    boolean success;
    string message;
    string data;
}

function generateRequest(string type) {
    HttpRequest request;
    HttpHeader header = httpCreateHeader("Content-Type", "application/json");
    request.headers += header;
    
    if(type == "SERVER") {
        HttpHeader authHeader = httpBasicAuthHeader("jmuse", "Pc9vz%fdgdfg73c");
        request.headers += authHeader;
    } else {
        HttpHeader header2 = httpCreateHeader("Authorization", "Basic am9uYXRoYW4ubXmNvbTpiNUVJsfdgsfdgfgsdgsgJQNmhKdGpMSzlBMkM=");
        request.headers += header2;
    }
    
    return request;
}

function genericRestCall(string url, string method, string data, HttpRequest request) {
    
    _httpResult result;
    
    if(method == "GET") {
        result.data = httpGet(url, request); //replace with specific domain name
    } else if (method == "PUT") {
        result.data = httpPut(url, request, data);
    } else if (method == "DELETE") {
        result.data = httpDelete(url, request, data);
    } else {
        result.data = httpPost(url, request, data);
    }

    
    number statusCode = httpGetStatusCode();
    if (statusCode >= 200 && statusCode < 300) {
        result.success = true;
    }
    else {
        string HTMLmsg = "<font color='red'><strong>ERROR: </strong></font>URL - " + url + " <br /> {" + trim(statusCode) + " : " + httpGetErrorMessage() + " : " + httpGetReasonPhrase() + "} " + toJson(data);
        runnerLog(HTMLmsg, true);
        logPrint("ERROR", URL - " + url + " <br /> {" + trim(statusCode) + " : " + httpGetErrorMessage() + " : " + httpGetReasonPhrase() + "} " + toJson(data));
        result.success = false;
        result.message = msg;
    }
    
    return result;
}
```

#### **Persistent variable version**

This versions is more secure in that the username and password is stored in the database and is not visible in the script. See [persistent variables](/cms_trial/space/PSJC/496205909/Persistent+variables/) on examples on how to set these values.

```text
struct _httpResult {
    boolean success;
    string message;
    string data;
}

persistent string username;
persistent string pass
persistent string apiKey;

function generateRequest(string type) {
    HttpRequest request;
    HttpHeader header = httpCreateHeader("Content-Type", "application/json");
    request.headers += header;
    
    if(type == "SERVER") {
        HttpHeader authHeader = httpBasicAuthHeader(username, password);
        request.headers += authHeader;
    } else {
        HttpHeader header2 = httpCreateHeader(apiKey);
        request.headers += header2;
    }
    
    return request;
}

function genericRestCall(string url, string method, string data, HttpRequest request) {
    
    _httpResult result;
    
    if(method == "GET") {
        result.data = httpGet(url, request); //replace with specific domain name
    } else if (method == "PUT") {
        result.data = httpPut(url, request, data);
    } else if (method == "DELETE") {
        result.data = httpDelete(url, request, data);
    } else {
        result.data = httpPost(url, request, data);
    }

    
    number statusCode = httpGetStatusCode();
    if (statusCode >= 200 && statusCode < 300) {
        result.success = true;
    }
    else {
        string HTMLmsg = "<font color='red'><strong>ERROR: </strong></font>URL - " + url + " <br /> {" + trim(statusCode) + " : " + httpGetErrorMessage() + " : " + httpGetReasonPhrase() + "} " + toJson(data);
        runnerLog(HTMLmsg, true);
        logPrint("ERROR", URL - " + url + " <br /> {" + trim(statusCode) + " : " + httpGetErrorMessage() + " : " + httpGetReasonPhrase() + "} " + toJson(data));
        result.success = false;
        result.message = msg;
    }
    
    return result;
}
```

To see an example of this code in use see [Syncing custom field options with external data (REST)](https://appfire.atlassian.net/wiki/spaces/PSJC/pages/1222738024).