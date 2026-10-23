# Sync rules

![image-20240506-092529.png](/cms_trial/assets/e0496e7e-6d47-4682-a0d9-304d5f98486d.png)

## Partial sync

### Synchronization time interval

Specify the time interval (in seconds) for the App to synchronize data with connected instances. The minimum value is 1 second, and the maximum is 10 seconds.

### Updates processing control

Partial Sync mechanism is a background process designed to update the status of tasks in BigPicture boxes, based on changes made by users on the Jira side.

Change of the ‘**Updates processing control’** settingsaffects **sync speed between Big Picture and Jira.**

Available settings options:

- **Simple updates processing** - One queue for processing all updates. The app should process all updates quickly, but when dealing with large volumes of data, it may be inefficient (if only one queue is used, it may run continuously without emptying).
- **Optimized updates processing** *(recommended)* - Splits a single long queue into into multiple smaller queues for more efficient management. Updates from Jira to frequently used boxes are the priority (high-priority queue). Updates from less used boxes go to the low-priority queue, which processes them every fifteen minutes. This prevents the app from dealing with excessive data loads at short intervals.
- **Limited updates processing** - This mode continuously updates the boxes you use the most, but there is no low-priority queue. Syncing less frequently used boxes will take longer. We don't recommend using this mode if you work with large data volumes.

## Additional box sync

### Scheduled synchronization

Jira does not always notify the BigPicture App about changes (for example, no updates are triggered when a project is removed) - **the scheduled synchronization**mechanism assures that the scope of your work is always up to date.

![contentId-1918537987](/cms_trial/assets/c3c3bb5f-d2f7-4533-b3e3-5d1a05d1f0b9.png)

## Task limit

### Maximum number of tasks in a box

Set the maximum number of tasks that a single Box can hold to limit BigPicture's performance impact on your Jira instance. The default value is 100,000 tasks, and there is no maximum limit.

For more information, see our [Sizing guide](/cms_trial/space/SPM/1918535738/Sizing+guide/).

The performance can also be improved by increasing the synchronization time interval.

### Task grouping limit

Set a limit on how many tasks a box will perform grouping for. The maximum number is set to 50000 tasks.

![contentId-1918537987](/cms_trial/assets/91171fe9-4959-401c-9a70-a42abe5dc6a4.png)