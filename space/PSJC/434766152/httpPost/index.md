# httpPost

## Description

Executes an HTTP POST for the given URL using the specified HttpRequest object. The posted data can be either included in the request object (as name-value parameters) or it can be added as a separate parameter (in the case of JSON, struct etc).Requests can also be sent through a proxy.

|  |  |  |  |
| --- | --- | --- | --- |
| **Syntax** | httpPost(url, request [[, proxy] [, postDataObject]]) | **Package** | http |
| **Alias** |  | **Pkg Usage** | post(url, request [[, proxy] [, postDataObject]]) |

## Parameters

| Parameter name | Type | Required | Description |
| --- | --- | --- | --- |
| url | String | Yes | The URL. |
| request | HttpRequest | Yes | A HttpRequest object containing headers, cookies, parameters. |
| proxy | HttpProxy | No | An HttpProxy object containing the host and port of the proxy server. |
| postDataObject | variable: primitive type, array or struct | No | Data to be posted. |

## Return Type

**String**

Variable return type depends on the left hand side operator type.

## Examples

### Part 1 - Setting Up

Using this function, you can create a new ticket in the specified project for instance based on certain conditions, and pass the information for the additional fields to be filled in for this ticket too.  
  
The following example shows how to create a JSON object, transmit it to an external application, and receive data in response. The example simulates creating a user account on another system and receiving back the user ID.  
  
This ID could then be stored in a custom field in Jira creating a reference.This section of code defines the structs that will ultimately determine the JSON structure. The JSON structure is typically defined by the external systems API.

```javascript
//Define structs
struct property {
    string property;
    string value;
}
struct properties {
   property [] properties;
}
struct returnData {
    string status;
    string contactID;
}
```

### Part 2 - Adding Data

This section of code creates the structs and arrays and adds data to them.

```javascript
//Create array/struct
property [] propertyArray;
property p;
properties newContact;
//Add data to array/struct
p.property = "firstname";
p.value = "Merimas";
propertyArray += p;
p.property = "lastName";
p.value = "Fairbairn";
propertyArray += p;
p.property = "email";
p.value = "merimas_fairbairn@aol.com";
propertyArray += p;
p.property = "company";
p.value = "Goodchild";
propertyArray += p;
newContact.properties += propertyArray;
```

### Part 3 - Sending the Post

This section of code sets up the request, posts the data to the external system, and gets the response.

```javascript
//Create request
HttpRequest request;
HttpHeader header = httpCreateHeader("Content-Type", "application/json");
request.headers += header;
//Post data and get response
returnData result = httpPost("https://api.somewebsite.com/contacts/v1/contact/", request, newContact);
//Return ID of newly created user
return result.contactID;
```

The request parameter should have the HttpRequest type described [here](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/). The HttpProxy type is described [here](/cms_trial/space/PSJC/435028065/Predefined+structure+types+reference/).

## See also