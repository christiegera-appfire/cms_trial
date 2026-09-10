# Bi-direction sync with external system

## Overview

This page provides a practical guide to creating a real-time, bi-directional integration between Jira and external systems using Power Scripts. The solution enables seamless data synchronization, allowing changes in either system to be automatically reflected in the other within seconds.

## Key Components

- Field mapping - A configurable CSV-based approach defines relationships between Jira fields and external system fields, enabling flexible and maintainable integrations.
- Incoming data sync - A custom REST endpoint receives webhook events from external systems and updates the corresponding Jira issues using the configured field mappings.
- Outgoing data sync - A SIL Listener detects changes in Jira and pushes updates to external systems through their APIs, ensuring both systems remain synchronized.
- Reusable code structure - Modular design with separate files for struct definitions and mapping functions promotes maintainability and readability.

## Benefits of the implementation

- Real-time updates - Changes propagate between systems within seconds.
- Reduced manual effort - Eliminates duplicate data entry across platforms.
- Improved data accuracy - Ensures consistent information across all systems.
- Enhanced collaboration - Connects teams working on different platforms.
- Scalable architecture - Easily adapt to new fields or external systems.

This solution can be customized for virtually any third-party system with an API, providing the functionality of off-the-shelf integrations with the flexibility to meet your specific requirements.

## Problem

Syncing Jira data with a third-party system enhances cross-team collaboration, streamlines workflows, and improves data accuracy by ensuring real-time updates across platforms. It reduces manual effort through automation, allowing seamless task tracking and status updates between engineering, customer support, and business teams. Integration also enables better reporting and analytics, helping organizations identify bottlenecks and optimize performance. By linking Jira with tools like Zendesk, Salesforce, or BI platforms, companies can accelerate issue resolution, improve customer experience, and maintain data consistency. Additionally, it supports compliance by ensuring accurate audit trails and allows businesses to scale efficiently while maintaining operational efficiency.

An ideal integration with a 3rd party system would be real-time and bi-directional. This means that within seconds of a user updating information in on system the data would be synced with the other system.

## Solution

While there may be existing solutions to integrate Jira with your desired 3rd party system there are so many possibilities for integration that it is also possible there is not an existing solution. It has become a standard with online SaaS products to have public API’s that would make integrations possible. Power Scripts can create a solution using these APIs that would provide the same functionality of an off-the-shelf product.

This example does not use actual APIs or data from a 3rd party system but instead uses simplified example data for the purposes of explanation. The concepts demonstrated would be applicable and transferable to almost any API from a 3rd party system.

The solution will be comprised 2 main parts:

1. **Incoming data sync** - receiving data from the 3rd party system to Jira.
2. **Outgoing data sync** - sending data from Jira to the 3rd party system.

The diagram below provides details about the data flow implemented for this solution:

![Power Scripts for Jira Cloud bidirectional sync workflow diagram](/cms_trial/assets/7e879754-88d3-4bce-80d9-be013d7d2688.png)

## Reused resources

When writing scripts for solutions such as this it is a common best practice to reuse code as much as possible to make the code easier to maintain among many other reasons. This section covers the code that is reused in both the incoming and outgoing parts of the solution.

### Struct definitions

Structures (structs) are required in order to both parse and create JSON data. These struct definitions can cause scripts to grow large and it is a best practice to keep the in a separate [include file](/cms_trial/space/PSJC/433000499/Inclusions/) to keep scripts readable. See more about structs [here](/cms_trial/space/PSJC/435028043/Syntax+and+types+introduction/).

```text
// Define field structure for mapping between systems
struct _field {
    string fieldName;   // Descriptive name of the field
    number fieldId;     // Unique identifier used by external system
    string value;       // The actual field value to be synced
}

// Define container structure for data received from external system
struct _externalData {
    string sourceIssueId;  // External system's identifier for the issue
    _field [] fields;      // Array of fields to be synced
}
// Note: Nested structure allows for flexible field mapping with varying field counts
```

The *externalSystemStructs.incl* struct definitions establish a flexible data contract between systems. Using this pattern allows the integration to handle a variable number of fields without code changes. Each field maintains its metadata (name, ID) alongside its value, making the integration more resilient to schema changes in either system. When expanding the integration to include new fields, you'll only need to update your mapping file.

Note that the first struct *\_field* was used in the definition of the second struct, *\_externalData*. This creates “nested” data structures commonly found in JSON data.

### Field mapping CSV

Often when writing SIL scripts we need to provide the script with additional details. For example, we need to know what the equivalent Jira field is for a field from the external system. A simple way to provide this additional information is through a mapping table. And, to keep script readable we can keep the mapping table in a separate file like a CSV data file. SIL makes it simple to read the CSV data file back into the script as seen in the next script.

```text
jiraField,externalField
summary,123456789        # Maps Jira's summary field to external ID 123456789
description,123456789    # Maps Jira's description field to same external ID
dueDate,123456789        # Maps Jira's dueDate field to same external ID
customfield_123456,123456789  # Maps a Jira custom field to same external ID
```

The *fieldMappings.csv* file defines the relationships between Jira fields and external system fields. Each row represents a mapping pair with the Jira field name in the first column and the corresponding external system field ID in the second column. This example shows multiple Jira fields mapped to the same external field ID, which might occur when systems have different field granularity. In a real implementation, you would typically have unique external field IDs for each Jira field. Custom fields are referenced using their Jira ID (e.g., customfield\_123456) rather than their display name.

For production use, consider adding additional columns for field type conversion rules, validation requirements, or directional flags to indicate if fields should be synced in one or both directions.

### Field mapping include script

This script takes the mapping table stored in a CSV data file and converts it to an array of structs for easy reference in subsequent scripts. This bit of code was separated into an include file since the exact same code is used in the outgoing data sync script and the incoming data sync script. By separating reusable code such as this into separate files and using [inclusions](/cms_trial/space/PSJC/433000499/Inclusions/) to combine them back together, you can keep scripts short and readable.

```text
struct _fieldMapping {
    string jiraField;
    string externalField;
}

//--------------READ FIELD MAPPINGS FROM CSV AND CONVERT FOR USE----------------
_fieldMapping [] rawMappings = readFromCSVFile("fieldMappings.csv", true);
_fieldMapping [] externalMapping;

//prepare data for easier lookup by using indexed array
for(_fieldMapping m in rawMappings) {
    //for mapping from external field to Jira
    externalMapping[m.externalField].jiraField = m.jiraField;
    externalMapping[m.externalField].externalField = m.externalField;
}
```

The *mappingScript.incl* approach separates the field mapping configuration from the integration logic, making it easier to adapt the integration to different external systems or to accommodate changes in field structures over time.

#### How it works

See detailed explanation

- **Lines 1-4** - create a new struct that will be used to store the CSV data
- **Line 7** - reads in the CSV file and automatically converts the data into an array of the \_fieldMapping struct. This will happen automatically as long as there are an equal number of elements in the struct as columns in the data.
- **Line 8** - creates a new array of structs that will be used to store [indexed](/cms_trial/space/PSJC/434962512/Operators+reference/) data since it is the easiest way to look up or reference this data going forward.
- **Lines 11-15** - loop through each row of the CSV data and add a new indexed struct to the array of indexed structs. This is the goal and what will be used in the scripts.

## Incoming data sync

The incoming data sync is accomplished by creating a custom REST endpoint that the external system can use to send outgoing webhook events to. The reason that this is needed is that Jira does not know the data structure of every other system that you may want to use with Jira, it only knows its own data structure. The main purpose of this endpoint will be to receive the incoming data and to be able to parse it and use it to update a Jira issue.

### Incoming webhook script

```text
include "externalSystemStructs.incl";
include "mappingScript.incl"

//-------------------RECIEVE WEBHOOK AND PARSE PAYLOAD-------------------------

WebhookPayload httpRequestPayload = getWebhookPayload();
string httpPayload = httpRequestPayload.payload;

//handle error in the event JSON can not be parsed
try {
    _externalData data = fromJson(httpPayload);
    
    //search for Jira issue given the external issue id
    string [] issues = selectIssues("project = TEST AND \"External ID\" = " + data.sourceIssueId);
    
    //if Jira issue(s) is returned
    if(arraySize(issues) > 0) {
        
        string jiraKey = issues[0]; //use first issue returned
        
        //-----------------LOOP THROUGH JSON AND UPDATE JIRA--------------------
        for(_field f in data.fields) {
            
            string jiraField = externalMapping[f.fieldId].jiraField; //map the field id from data to Jira field
            %jiraKey%.%jiraField% = f.value; //update the jira field from the JSON data
        }
    } else {
        //error could be sent to external system if needed
    }
} catch {
    appendToWebhookResponse("Error parsing payload data!");
    return false, 500;
}

return true, 200;
```

The incoming webhook script demonstrates how to process external data and update Jira. It uses JQL to find the corresponding Jira issue based on the external ID, then leverages SIL's substitution feature (%jiraKey%.%jiraField%) to dynamically update the correct fields. The script includes basic error handling with try/catch blocks and returns appropriate HTTP status codes to the calling system. For production implementations, consider expanding the error handling and adding logging for better troubleshooting.

#### How it works

See detailed explanation

- **Lines 1-2** - read in the reusable files such as the struct definitions and the custom field mapping data script. Using [inclusions](/cms_trial/space/PSJC/433000499/Inclusions/) like this is the same as copying-pasting the code from those files into the top of the script.
- **Lines 6-7** - receive the incoming webhook and retrieve the data payload.
- **Lines 10-11** - line #10 starts with a try statement because the script is anticipating an error. In line #11 the script is attempting to convert the JSON from the payload to the predefined SIL structs. If the data is in an unexpected format this step will fail.
- **Line 14** - within the JSON data we are given an id from the issue in the external system. Ideally this id would be stored in a custom field (other forms of associating this data are also acceptable) so that we can look up the Jira issue according to this stored data.
- **Lines 17-19** - the [selectIssues()](/cms_trial/space/PSJC/434831783/selectIssues/) function returns an array (i.e. multiple issues). We are expecting there to only be a single issue associated with each external issue id. Line #17 checks to make sure at least 1 issue was returned. Line #19 will use the first issue returned. Since we are only expecting 1 this should be the one and only issue that needs updating.
- **Lines 22-26** - loop through the field data in the JSON and update the Jira issue data. On line #24 we can use the external field id as the key to get the necessary mapping data since we did the work to index the mapping data earlier.

  💡 Notice how simple it is to retrieve this data once indexed. Line #25 uses a special feature of the SIL language called [substitution](/cms_trial/space/PSJC/434602568/Variable+types+and+reference+methods/) which can be seen by the percent signs (%) wrapping the variables. What substitution does is it either converts or evaluates the contents of the substitution variable before evaluating the line of SIL code. So with the code `%jiraKey%.%jiraField%` first the jiraKey variable will automatically be converted to a Jira issue object and then the jiraField variable will be evaluated to the specific field from the issue object we wish to set. This makes it possible to use dynamic data like issue keys and custom field names without hard coding them into the script.
- **Lines 32 and 35** - Line #32 will be called when the JSON payload can not be called and will let the system calling the webhook know that it failed. Line #35 is similar but will let the calling system know that the process finished successfully.

### Configuring the webhook

Like any SIL script, the script for the incoming data sync must be added to a configuration of some sort in order for it to be executed automatically. In this case we need to configure a [webhook](https://appfire.atlassian.net/wiki/spaces/PSJC/pages/490998922) which will create a new REST endpoint for the external system to use to send data to Jira.

<https://app.arcade.software/share/v8s8n9AVNcUUKlWclEUr>

See the [webhook documentation](https://appfire.atlassian.net/wiki/spaces/PSJC/pages/490998922) for more detailed information on configuring a webhook however we will cover some key points here.

**Step 1** - A webhook configuration must be made first

![Power Scripts for Jira Cloud external system integration configuration](/cms_trial/assets/1d01759c-b3db-4e89-b851-0a0b1fb623e1.png)

While multiple methods can be used since the data being sent will contain a payload, the POST method should be used.

**Step 2** - Create an API token

![Power Scripts for Jira Cloud sync mapping settings panel](/cms_trial/assets/69f7003a-6f5b-4f7d-8cf1-18ea7e3c8460.png)

1. Notice that the name of the webhook configuration becomes part of the URI. In this example the full endpoint URI would be: <https://us1.powerscripts.anova.appfire.app/rest/keplerrominfo/refapp/latest/webhooks/jiraDataSync/run>
2. Using the icons on the right side of the configuration, an API token can be generated.

   ![Power Scripts for Jira Cloud field mapping configuration](/cms_trial/assets/f1a6bfc3-8e14-4b47-b91b-4bbcbd208e7b.png)

**Step 3** - Configure the external system to use the new REST endpoint for sending outgoing webhook events. See the screenshot above, where details are given on passing the API token for authentication.

## Outgoing data sync

The outgoing data sync is the exact opposite of the incoming data sync. When triggered the script will take data from Jira and use it to create data that will be sent to the external system. Again, the reason this is required is because Jira does not know how to format the data in a way that the external system will understand so that is the pain point of this step.

### Outgoing data sync script

```text
include "externalSystemStructs.incl";
include "mappingScript.incl"

persistent string externalUserName;
persistent string externalPass;

_externalData data;
data.sourceIssueId = externalId;
    
for(_fieldMapping m in externalMapping) {

    string jiraField = m.jiraField;

    _field f;
    f.fieldId = m.externalField;
    f.value = key.%jiraField%;
    
    data.fields += f;
}

HttpRequest request;
HttpHeader authHeader = httpBasicAuthHeader(externalUserName, externalPass);
request.headers += authHeader;
HttpHeader header = httpCreateHeader("Content-Type", "application/json");
request.headers += header;

httpPost("https://www.myExternalSystem.com/API/issue/" + externalId, request, data);
```

The outgoing sync script demonstrates the reverse process - taking Jira data and formatting it for an external system. It uses persistent variables for secure credential storage and dynamically builds the payload based on the field mappings. The script shows how to properly configure HTTP headers for authentication and content type. In production environments, you would want to add response validation and error handling to ensure the external system successfully received and processed the data.

#### How it works

See detailed explanation

- **Lines 1-2** - read in the reusable files such as the struct definitions and the custom field mapping data script. Using [inclusions](/cms_trial/space/PSJC/433000499/Inclusions/) like this is the same as copying-pasting the code from those files into the top of the script.
- **Lines 4-5** - using [persistent variables](/cms_trial/space/PSJC/496205909/Persistent+variables/) such as these allow you to keep sensitive information from being stored inside the script itself and instead stores the information in a secure database.
- **Lines 7-8** - create a new instance of the \_externalData struct so values can be added to it so eventually it can be converted back to JSON and sent to the external system.  
  💡 Notice that line #8 set the value to “externalId” which looks like a variable but no such variable has been defined. That is because this is a [SIL Alias](/cms_trial/space/PSJC/496206057/Custom+fields+aliases/) which is the best practice for referencing custom field data from a Jira issue.
- **Lines 10-19** - loop through the mapping data and use that as a guide for setting values from Jira into the struct (soon to be JSON) data. On line #12 the value of the Jira field id is converted to a simple string since substitution does not work with structs.

  💡 Notice that on line #16 the script references a variable “key” but this variable has not been defined or assigned a value. This is because this is a [standard variable](/cms_trial/space/PSJC/434602568/Variable+types+and+reference+methods/). These variables are automatically defined and the values populated. Standard variables such as this are what make it possible for scripts to be used dynamically. We do know ahead of time which Jira issue will be updated and the SIL script will be called for so variables such as this will allow us to use script without knowing this information ahead of time.
- **Lines 21-25** - prepare to make a call to an external system by setting up the HTTP request. This request contains information such as user credentials for authentication and headers used to make sure the data is being communicated properly. Code of this nature works well as a reusable include file but was included here for example purposes.
- **Line 27** - finally, the call to the external system is made using the [httpPost()](https://appfire.atlassian.net/wiki/spaces/PSJ/pages/15489476) function. This function has 3 parameters (for this example).

  - First is the URL of the external system. Notice that we are adding an issue id into the URL. The need for this would be determined by the actual API of the system being called.
  - Second is the [HTTPRequest](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=psjc&title=Predefined%20Structure%20Types&linkCreation=true&fromPageId=1833959509) object that was set up earlier
  - Third is the JSON data payload. Notice that we are actually passing the function a struct and not actual JSON data. The function will convert the struct to JSON automatically.

### Configuring the outgoing sync script

The outgoing sync script must be configured differently then the incoming script. Unlike the incoming script this script must be triggered by events internal to Jira instead of from an external system. The best way to accomplish this is to use a [SIL Listener](/cms_trial/space/PSJC/490997990/SIL+Listeners/). SIL Listeners are built exactly for this type of purpose. They wait (listen) for specific events to be triggers in Jira and then execute a SIL script when that event is triggered. Listeners can be triggered from a number of events but for the purposes of this script we are only interested in one.

See the [documentation](/cms_trial/space/PSJC/490997990/SIL+Listeners/) for more detailed information on configuring SIL Listeners however we will cover some key points here.

![Power Scripts for Jira Cloud integration status display](/cms_trial/assets/d397930c-b9c8-4164-9f8b-b46265ebcba0.png)

1. Since the script is performing a task on an external system it may be a good idea to select the Asynchronous option since there is no point in the Jira user waiting around for the results of the execution.
2. The purpose of selecting a user to run the script is if there are operations in Jira that the triggering user is unable to perform because of set permissions. Since this script is not performing any actions in Jira a user is not required.
3. The main event that should trigger the script is the `Issue Updated` event. This way, whenever a change is made to a Jira issue, the script will be triggered, and the data can be synced with the external system.
4. Optionally, a project and/or issue type filter can be used on the listener. This will prevent the script from being triggered for projects or issue types that are not part of the external sync. Making sure to filter these events out will ensure performance for all automations on the system.

## Solution considerations and enhancements

1. Note that this solution basically assumes that issues exist on both systems and that the corresponding id for the external systems issue is stored in Jira. To actually accomplish this the existing script would need to be updated or a second script created that would listen for the `Issue Created` event. It would be very similar to the existing script but would be required to call a different API endpoint for the external system that would create a new issue instead of updating it.
2. To keep the scripts small and easier to read not much in the way of error handling was added to these examples. Enhancements could/should be made to the script so that in the event of an error the script can retry the sync or alert the user to the error by adding a comment, for example.