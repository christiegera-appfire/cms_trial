# Importing time (worklogs) into 7pace Timetracker

## Importing time via the Timetracker UI (Times Explorer page)

Importing worklogs via the Timetracker UI can be done from the Times Explorer page. In order to import worklogs that you have tracked outside of 7pace Timetracker, you simply copy data from the source application (like Excel) and paste it into the "Import Times" popup window of the Times Explorer page. You then associate each worklog detail to the specific field in the Timetracker database. Once verified, the imported worklogs are stored in our database.  
Import can be performed via the UI, but it can also be performed by using the ***workLogs*** endpoint from our [REST CRUD API](/cms_trial/space/7TFA/1253540003/7pace+Timetracker+REST+CRUD+API+Version+3/) and also our [NPM package](/cms_trial/space/7TFA/1253540003/7pace+Timetracker+REST+CRUD+API+Version+3/).

If the system finds any errors, the import process will stop and the errors will display for you to correct before attempting to import again.

1. On the 7pace Timetracker menu bar, click **Times Explorer**.

2. On the Times Explorer page, click **Import**.

![FAQ_Import_Worklog.png](/cms_trial/assets/3d4622c7-1e4a-4c35-a071-9f798bd3050d.png)

The **Import Times** page displays:

![FAQ_Import_Worklog_Import_Copy.png](/cms_trial/assets/1bb2aee1-1302-4eb7-903d-fa2aca928fb2.png)

3. Paste the time details that you copied from the source application (like Excel).

![FAQ_Import_Worklog_Import_Paste.png](/cms_trial/assets/88d8743e-d956-474e-8c6a-d3772114fb30.png)

4. Click the **Next** button.

Timetracker analyzes the data that you pasted and displays it in a tabular format so you can properly associate each time detail in the column headers to the appropriate Timetracker field.

![FAQ_Import_Worklog_Table_Format.png](/cms_trial/assets/20947998-169b-4cb1-8f33-b66cfbdd1c18.png)

5. (Optional) In the far-left column, check the boxes for the time details you want to import. By default, all are selected.

6. Select the "Date Format" and the "Time Format" of your preference for the import.\*

![FAQ_Import_Worklog_Date_Time_Format.png](/cms_trial/assets/41ff8a24-35e4-4c8a-8253-aa7aa827b854.png)

\***Note**: If you'd like to customize or change the format for your import, please find additional information at this link - [Custom Date and Format Strings](https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings) - and/or simply use the most popular formats (we used standard .NET Framework DateTime object format settings):

**Basic Format Specifiers:**

mm: minutes

MM: month

dd: day of month

h: hour in format 1-12 without leading zero

hh: hour in format 1-12 with leading zero

H: hour in 24h format without leading zero

HH: hour in 24h format with leading zero

mm: minutes with leading zero

tt: am/pm designator

yyyy: year

**Templates for Date/Time Formats**

|  |  |
| --- | --- |
| Date Format | Time Format |
| MM/dd/yyyy | h:mm tt |
| dd.MM.yyyy | HH:mm |
| yyyy-MM-dd | HH:mm |

7. Copy-paste the **Date Format** and **Time Format** of your choice into the corresponding fields.

8. In the **Column Name** headers, click the dropdown arrows on each and select the appropriate header names for the time details below.

9. Click the **Import Now** button.

While importing, if there are any issues with the data, those issues will be highlighted and an error message will display.

![FAQ_Import_Worklog_Error_Message.png](/cms_trial/assets/f411bda3-17bb-485a-9926-073ea080ebd0.png)

10. (Optional) Check "Rows With Errors Only" to see just the rows that are causing issues in your import.

11. (Optional) After correcting your errors, if any, click the **Import Now** button again.

Once the time details are successfully imported, you can view these details on the "Times Explorer" page.

## Import Time (Worklogs) via REST CRUD API (NPM Package)

We have created an NPM package that can be used to import worklogs which utilizes our CRUD API.

[timetracker-npm-import](https://github.com/7pace/timetracker-npm-import) is a Node.js CLI for importing worklogs(csv/excel) to 7pace Timetracker.

The NPM package is distributed ‘as is’ and will not be developed further, since it was created solely as a showcase of how to use our CRUD API.

## Import Time (Worklogs) via REST CRUD API Manually

You can also manually enter worklogs for specific users by using the REST CRUD API.

The endpoint that you will need to use is the [workLogs endpoint](/cms_trial/space/7TFA/1253540003/7pace+Timetracker+REST+CRUD+API+Version+3/) and you will have to specify the parameters in the JSON body part of your POST request, as in the example below. Please note that the length field is in seconds, so you will need to account for that:

```text
POST https://{your-organization}.timehub.7pace.com/api/rest/workLogs?api-version={version}


JSON body to create worklog:

{

  "timeStamp": "2023-10-16T12:30:00.921Z",

  "length": 14400,

  "billableLength": 0,

  "workItemId": 7,

  "comment": "string",

  "userId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

  "activityTypeId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"

}
```