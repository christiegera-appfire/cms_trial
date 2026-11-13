# Audit logs

The Audit Logs page is your go-to source for tracking all activity within the app. From creating SLAs to editing configurations, every action is meticulously recorded, giving you full visibility and accountability.

You can access the Audit Logs by navigating to **Settings** > **Audit Logs**.

Image — asset pipeline pending  
Time to SLA Audit Logs page with date, author, object type, and event columns

Let's explore the Audit Logs page together:

1. **Date –** This is the date and time when the change was made.
2. **Author –** Displays who made the change. If you click the name, it takes you to the author's profile.
3. **Object type –** Shows where the change was made. It can be SLA Configuration, Notifiers, Calendars, Permissions, Settings, Reports, and API Tokens.
4. **ID –** This is the ID of the changed object. For example, you can read the image below as: A Calendar with the ID 8ecdcfb9-6c1a-4a4d-8877-20c7231b2464 has been updated by Derya Özdemir on 18.08 2022, 12:35 pm.

   Image — asset pipeline pending  
   Time to SLA audit log entry showing a Calendar update event with ID and timestamp
5. **Event type –** Shows the status of the event. It can be Created, Updated, and Deleted.
6. **Object data –** Allows you to see the object data of the event.
7. **Reload –** Click to refresh your audit logs.

Except for the [Clean Old Audit Logs](https://appfire.atlassian.net/wiki/spaces/TTSC/pages/36012475) option, no user can delete items in Audit Logs, which means all activity across the app is meticulously documented.

## How to use object data

Object Data lets you quickly see the differences between two events. On this page, we will explore it case by case.

### Case 1: You've created an object (SLA, Calendar, Notifier, etc.)

Whenever you create a new object, it is documented on the Audit Logs page, as shown below:

Image — asset pipeline pending  
Time to SLA audit log object data view for a newly created SLA configuration

### Case 2: You've updated an object (SLA, Calendar, Notifier, etc.)

On this page, you can simply identify which configuration was updated for an object. The difference is shown at the top:

Image — asset pipeline pending  
Time to SLA audit log diff view highlighting changed configuration values

Below that, you can see the old and new values.

### Case 3. You've deleted an object (SLA, Calendar, Notifier, etc.)

We don't show the Object Data for deleted objects.

Image — asset pipeline pending  
Time to SLA audit log showing a deleted SLA entry with event type

Image — asset pipeline pending  
Time to SLA audit log showing a deleted Calendar entry with event type

## How to delete audit logs

By default, audit logs are stored in the database indefinitely. However, you can configure them to be automatically deleted after a set time period.

To delete audit logs, follow these steps:

1. Navigate to **Settings** > **Advanced**.
2. Select the time interval for audit log disposal.  
   ***Example:*** *If you select 2 months, all logs older than 2 months will be periodically deleted.*

   Image — asset pipeline pending  
   Time to SLA Advanced Settings with Clean Old Audit Logs interval selector

1. Click **Save**.