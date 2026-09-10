# 7pace Timetracker Client (Tracking) API

Each of the above tracking API endpoints requires the correct API version to be defined in the API call; the parameters are optional.

### **GET /api/tracking/client/current/{expand}**

This function gets the current state of the active track. If you use the $expand parameter, additional details will be shown.

Example:

`GET https://{your-organization}.timehub.7pace.com/api/tracking/client/current?$expand=true&api-version=3.2`

**POST /api/tracking/client/selected**

Used to set the tracking parameters without starting tracking. The JSON body is required for the API call.

Example:

`POST https://{your-organization}.timehub.7pace.com/api/tracking/client/selected?api-version=3.2`

```json
{
  "tfsId": 0,
  "remark": "string",
  "activityTypeId": "string",
  "calculateTotals": true
}
```

**GET /api/tracking/client/latest/{count}**

Returns a list with the latest tracks. You can specify how many of the latest tracks you want to get details for with the count parameter.

Examples (with count parameter and without):

`GET https://{your-organization}.timehub.7pace.com/api/tracking/client/latest?$count=5&api-version=3.2`  
`GET https://{your-organization}.timehub.7pace.com/api/tracking/client/latest?api-version=3.2`

### **POST /api/tracking/client/startTracking**

This starts a new tracking session. You will need to specify fields in the JSON body portion of the API call. Depending on your settings, at least the TFSID or comment (remark) is required to start tracking.

Example:

`POST https://{your-organization}.timehub.7pace.com/api/tracking/client/startTracking?api-version=3.2`

```json
{
  "timeZone": 0,
  "tfsId": 1349,
  "remark": "string",
  "activityTypeId": "string",
  "isBillable": true
}
```

**TimeZone**: Time zone offset in minutes.  
**TfsId**: Work Item id.  
**Remark**: Comment or non-DevOps identifier.  
**ActivityTypeId**: Activity type id.  
**IsBillable**: Set track to billable or unbillable (null by default)

### **POST /api/tracking/client/stopTracking/{reason}**

Stops the currently active tracking session. If the $reason parameter is not forwarded, it will default to the reason being stopped by the client.

Examples (with reason parameter and without):

`POST https://{your-organization}.timehub.7pace.com/api/tracking/client/stopTracking?$reason=0&api-version=3.2`  
`POST https://{your-organization}.timehub.7pace.com/api/tracking/client/stopTracking?api-version=3.2`

### **POST /api/tracking/client/idleCheck/{selectedOption}**

Notifies the system about the time of the next idle check. This only works if the idle check setting is enabled and there is an activity check running on the server at the moment when you are sending this API call.

### **POST /api/tracking/client/activityCheck**

Notifies the system about the time of the next idle check. This only works if the idle check setting is enabled and there is an activity check running on the server at the moment when you are sending this API call. Sends a notification to the system indicating that you are still active and to continue the currently active tracking.

Example:

`POST https://{your-organization}.timehub.7pace.com/api/tracking/client/activityCheck?api-version=3.2`

### **POST /api/tracking/client/adjust**

Allows you to change the current track, such as change the activity type or comment (remark). The JSON body is required for this API call.

Example:

`POST https://{your-organization}.timehub.7pace.com/api/tracking/client/adjust?api-version=3.2`

```json
{
  "remark": "comment",
  "activityTypeId": "testing"
}
```

### **POST /api/tracking/client/search**

Searches for a work item in DevOps Server/Services by the work item ID. The JSON body can simply contain the work item ID, as in the example, below.

Example:

`POST https://{your-organization}.timehub.7pace.com/api/tracking/client/search?api-version=3.2`

```text
1349
```

### **POST /api/tracking/client/searchByQuery**

Searches for a work item in DevOps Server/Services by either the work item name or work item ID. It is required to define the query in the JSON body of the API call.

Example:

`POST https://{your-organization}.timehub.7pace.com/api/tracking/client/searchByQuery?api-version=3.2`

```text
{
  "query": "Testing workitem"
}
```

### Tracking endpoints for use with the Timetracker Web Client (SignalR)

The SignalR endpoints/functions have the exact same functionality as the Tracking API endpoints, however, they can only be used as a hub for connecting an application to the 7pace Timetracker API. Below, you will find a list of the SignalR endpoints/functions:

#### **GET /signalr/trackingHub/v3.2:current**

Gets the current state of the active track.

#### **GET /signalr/trackingHub/v3.2:selected**

Sets the tracking parameters without starting tracking

#### **GET /signalr/trackingHub/v3.2:latest**

Returns a list with latest tracks

#### **GET /signalr/trackingHub/v3.2:startTracking**

Starts a new tracking session

#### **GET /signalr/trackingHub/v3.2:stopTracking**

Stops the current tracking session

#### **GET /signalr/trackingHub/v3.2:idleCheck**

Notifies the system about the time of the next idle check if there is an active activity check in the moment of the call

#### **GET /signalr/trackingHub/v3.2:activityCheck**

Notifies the system that you are still active

#### **GET /signalr/trackingHub/v3.2:adjust**

Changes the current track parameters

#### **GET /signalr/trackingHub/v3.2:ping**

Sends a ping request

#### **GET /signalr/trackingHub/v3.2:search**

Searches for a work item in DevOps Server/Services