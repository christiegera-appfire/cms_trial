# 7pace Timetracker REST CRUD API Version 3

7pace Timetracker supports CRUD API. This means that you can create, read, update, and delete worklogs.

The CRUD API also lets you get information about the following:

- Current and other Timetracker users
- User roles and assigned licenses (and to manage it)
- Activity types
- Approval state of weeks

All the available endpoints in the 7pace Timetracker REST CRUD API can be found in our API Reference: [REST CRUD API Reference](https://timehub.7pace.com/api_reference/index.html).

## Connecting to API

Connecting to the REST CRUD API is the same process as connecting to the 7pace Reporting API, which is described here: [Connecting to API](/cms_trial/space/7TFA/1253540266/7pace+Timetracker+Reporting+API+Version+3/).

## Important information

The REST CRUD API returns results in batches (usually of up to 500 rows). If your results contain more than 500 rows, you must use the **$skip** and **$count** parameters. The maximum value for the **$count** parameter is **500**.

## API endpoints overview

All endpoint information can be found in the [7pace Timetracker API Reference](https://timehub.7pace.com/apireference/?urls.primaryName=7pace%20Timetracker%20API%20documentation%20v3.2-beta#/) page, along with all the fields returned by the endpoints, and the parameters that can be used with each endpoint. The following endopints are available:

- [me](#me)
- [users](#users)
- [users/roles](#users%20roles)
- [activityTypes](#activityTypes)
- [workLogs](#workLogs)
- [timeApproval](#timeApproval)

### GET

- `me` - get information about yourself
- `users` - get list of system users
- `users/roles` - get list of 7pace Timetracker licensed users with roles/permissions
- `activityTypes` - get information about activity type state in the system
- `workLogs` - gets list of worklogs for current user
- `workLogs/all` - gets list of worklogs for whole system
- `timeApproval/all` - gets list of time approval for whole system

### POST

- `users/roles` -  set roles/permissions for the list of 7pace Timetracker licensed users
- `workLogs` - creates new worklog
- `workLogs/batch` - creates batch of new worklogs
- `timeApproval/week` - send week for approval

### PATCH

- `workLogs/{id}` - updates worklog

### DELETE

- `workLogs/{id}` - deletes worklog from system
- `timeApproval/week` - revoke week that is in a submitted state

#### me

This endpoint allows you to get information about yourself.  
It is possible to use the **$expand** parameter with this endpoint. The possible options are `{ user.displayName }`*.*

#### users

This endpoint returns a list of all 7pace Timetracker system users. The parameters that can be used with this endpoint are **$count**, **$skip** and **$expand**. The possible options for the **$expand**parameter are `{ user.displayName }`*.*

#### users/roles

This endpoint can be used to get a list of 7pace Timetracker licensed users with their roles. By using the POST command, the user roles can be set. The parameters that can be used with this endpoint are **includeNoneRoles**, **$count**, **$skip** and **$expand***.* The possible options for the **$expand**parameter are `{ user.displayName }`*.*  
User can be specified by **id**, **vstsId** or **email** (only one field is required) and the role can be specified by **id** or **name** (only one field is required).

#### activityTypes

This endpoint can be used to get information about the activity type state in the system.

#### workLogs

This endpoint can be used to get a list of worklogs for the current user, or by using the POST command, a new worklog can be created. The below parameters can be used with this endpoint:  
**$count** - Number of items to take. Maximum value: 500  
**$skip** - Number of items to skip  
**$expand** - The expand parameters for model attributes. Possible options are { user.displayName }  
**$workItemIds** - Filter worklogs by Work Item Ids. Comma separated array, no more than 100 at once  
**$fromTimestamp** - Return worklogs with timestamp greater than value.  
**$toTimestamp** - Return worklogs with timestamp less than value.  
**$fromCreatedTimestamp** - Return worklogs with created timestamp greater than value  
**$toCreatedTimestamp** - Return worklogs with created timestamp less than value  
Date format example: 2021-11-06T10:28:00

#### timeApproval

This endpoint can be used to send a week for approval (POST) or to revoke a week that has been submitted for approval (DELETE). Using this endpoint requires at least the Team user role in 7pace Timetracker.

By using the `timeApproval/all` endpoint you can get a list of time approval for the entire system and get all approval information. This requires the Approval Manager rights. `timeApproval` has an approval state of the specific weeks and has a date range of `[weekStartDate - weekEndDate]`, while the worklog record has one exact date (**createdTimestamp**). By matching **createdTimestamp** from the worklogs for which you are looking to the specific `timeApproval` weeks with the corresponding date range `[weekStartDate - weekEndDate]`, you can find the approval state of these worklogs. If there are no results, all available approval weeks in the system are in an *unsubmitted* state. The parameters which can be used with the `timeApproval/all` endpoint are listed below:  
**$count** - Number of items to take. Maximum value: 500  
**$skip** - Number of items to skip  
**$expand** - The expand parameters for model attributes. Possible options are { user.displayName }  
**$fromTimestamp** - Return time approval with week date that includes current week or greater than value.  
**$toTimestamp** - Return time approval with a week date that includes the current week or less than value.  
Date format example: 2021-12-06T12:35:00

The possible timesheet statuses for Approval that can be returned are the following:

**ID    Approval state**  
*1    Submitted for approval*  
*2    Reopened*  
*3    Approved*  
*99    Closed*

Timesheets only get an approval status value once they are submitted. Unsubmitted timesheets do not have a status assigned.  
The *Closed* status only applis to unsubmitted timesheets that were closed by an approval manager, and approved timesheets are ones that had been sent for approval and have been approved.

## Import time (worklogs) via REST CRUD API (NPM package)

An NPM package is available that can be used to import worklogs which utilizes our CRUD API.

[timetracker-npm-import](https://github.com/7pace/timetracker-npm-import) is a Node.js CLI for importing worklogs(csv/excel) to 7pace Timetracker.

The NPM package is distributed ‘as is’ and will not be developed further, since it was created solely as a showcase of how to use our CRUD API.

### Examples

Get user roles and show the user's display name:

`GET https://{your-organization}.timehub.7pace.com/api/rest/users/roles?api-version={version}&$expand=user.displayName`

Get worklogs for current user from specified timestamp:

`GET https://{your-organization}.timehub.7pace.com/api/rest/workLogs?api-version={version}&$fromTimestamp=2021-12-06T12:35:00`

Get worklogs from the organization (in this example we are taking only 500 worklogs results (**$count**), and not from the very beginning, but skipping (**$skip**) the first 500 worklogs:

`GET https://{your-organization}.timehub.7pace.com/api/rest/workLogs/all?api-version={version}&$skip=500&$count=500`

Set multiple users Timetracker permissions:

```text
POST https://{your-organization}.timehub.7pace.com/api/rest/users/roles?api-version={version}

JSON body to set multiple users roles/permissions:
{
    "users":  [
                  {
                      "email":  "email1@email.com",
                      "role":  {
                                   "name":  "Team"
                               }
                  },
                  {
                      "email":  "email2@email.com",
                      "role":  {
                                   "name":  "Administrator"
                               }
                  },
                  {
                      "email":  "email3@email.com",
                      "role":  {
                                   "name":  "Budget"
                               }
                  }
              ]
}
```

Create a new time entry for specified user:

```text
POST https://{your-organization}.timehub.7pace.com/api/rest/workLogs?api-version={version}

JSON body to create worklog:
{
  "timeStamp": "2021-12-17T12:42:03.921Z",
  "length": 0,
  "billableLength": 0,
  "workItemId": 0,
  "comment": "string",
  "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "activityTypeId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

Send week for approval:

```text
POST https://{your-organization}.timehub.7pace.com/api/rest/timeApproval/week?api-version={version}

JSON request body:
{
  "weekStart": "2021-11-15",
  "assignedManagerId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

Fetch the approval state from a specific date:

`GET https://{your-organization}.timehub.7pace.com/api/rest/timeApproval/all?api-version={version}&$fromTimestamp=2022-10-01T13:45:25.572Z`

Update the specified worklog:

```text
PATCH https://{your-organization}.timehub.7pace.com/api/rest/workLogs/3fa85f64-5717-4562-b3fc-2c963f66afa6?api-version={version}

Body:
{
  "timeStamp": "2021-12-17T13:42:03.921Z",
  "length": 0,
  "billableLength": 0,
  "workItemId": 0,
  "comment": "string",
  "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "activityTypeId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

Delete the specified worklog based on the worklog ID:

`DELETE https://{your-organization}.timehub.7pace.com/api/rest/workLogs/3fa85f64-5717-4562-b3fc-2c963f66afa6?api-version={version}`

### Example Excel file for a quick start

You can use the attached excel file [Get users and roles - example.xlsx](https://appfire.atlassian.net/wiki/download/attachments/1253540003/Get%20users%20and%20roles%20-%20example.xlsx)to quickly get your first report up and running. By following the instructions, you can obtain a list of all users and their roles in under five minutes.

Please be aware of certain limitations:

- The instructions inside of the file only works for the Windows version of Excel.
- You must have a 7pace Timetracker Administrator or a Project Collection Administrator role assigned in order for the API to work (for security reasons).   
  Alternatively, you can use the Service Account token, but this is out of the scope of this article, you can refer to the [7pace Timetracker Service Account](https://appfire.atlassian.net/wiki/x/qoO3Sg) article for more information.