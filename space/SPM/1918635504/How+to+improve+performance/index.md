# How to improve performance

## Introduction

To improve app performance, focus on more than just the hardware. Regularly maintain the app and review its settings. The best practices for maintaining app performance also prevent slowdowns in a self-hosted Jira environment due to data synchronization.

The recommendations on this page focus on four main areas:

- [making data sync faster](#)
- [speeding up module loading](#)
- [improving UI responsiveness](#)
- [lower risks of Jira issue pages slowing down](#)

Performance improves when:

- You **limit the amount of data** you are actively working with. All aggregations and calculations are done only for visible tasks.
- You **decrease the frequency of synchronization** and data refresh.

---

## Optimized and safe data synchronization

If you are experiencing **Jira performance issues** caused by BigPicture data sync, check the performance settings in App Configuration.

The performance settings help you optimize BigPicture syncs with Jira. This can significantly **reduce the chances** of a negative impact on Jira, even if over 30,000 users are working on over 1 million issues.

The following settings can also **speed up the data sync**.

### Access the synchronization settings

A Jira admin can access the *Performance* tab in *App Configuration*:

1. At the top bar, go to **Apps** > **BigPicture**.
2. Go to **App settings** (wrench icon at top right) > **Performance**. You are taken to the *Sync rules* tab in the *Performance* section.

![app-configuration-performance-synch-rules.png](/cms_trial/assets/cd99ec68-c82d-4ebe-b5c2-c67ffd37298c.png)

### Adjust the partial sync settings

| **Settings** | **Description** |
| --- | --- |
| **Synchronization time interval** image-20240703-122800.png | Adjust how often BigPicture syncs data (a range of 1-10 seconds).  Increase the value to boost app performance (synchronization less frequent). |
| **Updates processing control** image-20240703-122719.png | Switch the processing mode to manage better the high volume of BigPicture updates in Jira and vice versa.   - **Simple updates processing** - One queue for processing all updates. The app should process all updates quickly, but when dealing with large volumes of data, it may be inefficient and cause a risk of high CPU load (if only one queue is used, it may run continuously without emptying). - **Optimized updates processing** *(recommended)* - Splits a single long queue into into multiple smaller queues for more efficient management. Updates from Jira to frequently used boxes are the priority (high-priority queue). Updates from less used boxes go to the low-priority queue, which processes them every fifteen minutes. This prevents the app from dealing with excessive data loads at short intervals, reducing the risk of high CPU load and negative impact on Jira. - **Limited updates processing** - This mode continuously updates the boxes you use the most, but there is no low-priority queue. While this mode reduces the risk of negative effects on Jira, syncing less frequently used boxes will take longer. We don't recommend using this mode if you work with large data volumes. |
| **Box activity threshold** image-20240703-122858.png | Defines which boxes are classified by the app as active. Enter a value ranging from 1 to 144 hours. |
| **Active box limit** image-20240703-122921.png | Limits the number of boxes supported by the high-priority queue. Enter a value ranging from 10 - 100 boxes. |
| **Box synchronization threshold** image-20240703-122940.png | Lets you set a synchronization timeout. Enter a value ranging from 5 - 10,000 milliseconds. |

### Schedule full synchronization

Scheduled sync ensures data in all boxes is up to date. Schedule the sync using a [cron expression](https://crontab.guru/).

We recommend scheduling a sync once a week during the off-peak hours. When the sync is running, performance might decrease.

![image-20240703-130027.png](/cms_trial/assets/b100b671-8e83-4ab5-9195-1b74942451f6.png)

### Adjust live sync settings

Live sync eliminates the need to refresh a page to see the changes made by other BigPicture and Jira users. The sync interval, which is expressed in seconds, determines how frequently data from individual modules and markers is synchronized.

To improve performance:

- Increase the sync interval (less frequent syncs) OR
- Use the toggle switch to disable live sync.

**Go to**: Switch to the *Live sync* tab to make adjustments.

![image-20240703-085657.png](/cms_trial/assets/8de47589-b294-4cc7-83e7-e3a9cf1dcdce.png)

### Evaluate custom field mapping

Use custom field mapping only if you need it.

[Field mapping](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297635027) is responsible for bidirectional data synchronization between BigPicture and Jira.

### Clean up the box structure

As the project portfolio in your organization grows, so does the number of boxes in the box hierarchy.

- [Close](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297571607) and [archive](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297930799) boxes that are no longer needed - BigPicture doesn't refresh closed and archived boxes, which results in better app performance.
- Delete unnecessary boxes (e.g., it's just a test box).

You may also want to clean up old and unused Jira projects.

- Archive old Jira projects

  - cloud <https://support.atlassian.com/jira-cloud-administration/docs/archive-a-project/>
  - data center <https://confluence.atlassian.com/adminjiraserver/archiving-a-project-938847621.html>

---

## Faster module page load time

When working with the app, you might notice that a module page doesn't load fast enough. The following changes **speed up data sync**.

### Customize task-related performance settings

The *Performance* tab includes additional settings worth considering to enhance page load time while using BigPicture modules.

| **Settings** | **Description** |
| --- | --- |
| **Maximum tasks to load** image-20240311-075445.png | To enhance loading speed, limit the number of tasks simultaneously displayed by BigPicture. A lower limit will result in improved loading performance. |
| **Task grouping limit** image-20240703-130620.png | Limit the maximum number of tasks the app can group to optimize the process. By reducing the number of tasks, the app can perform grouping faster. |

### Limit the number of structure builders

[Structure builders](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297505404) help you automatically create and maintain the task structure in each box. Hav ng more active structure builders increases the time needed to sync the task tree, which can slow down page loading times. For that reason, we recommend using **up to three structure builders** in a box.

### Keep the number of columns under control

Columns display and aggregate task information. Displaying too many columns can affect the page load times of the Gantt and Scope modules. Avoid having more than **ten columns per view**. Create additional [column views](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298192097) to easily switch between views without slowing down the performance.

### Use filters

If your box spans a long period of time or contains many tasks, use filters, such as [**date filters**](https://appfire.atlassian.net/wiki/spaces/DLP/pages/296851062), to improve the performance.

---

## Better UI responsiveness

BigPicture can process and visualize many issues to help you plan and monitor even the most complex initiatives. That's why a box scope has no upper limit for tasks.

Our load and performance tests confirm that the BigPicture app runs comfortably with even 30,000 tasks in a box. But if you notice user interface responsiveness issues, try the recommendations below.

### Ensure you have the right hardware and software

As a **BigPicture user**, your **device and browser** play an important role in app performance.

A device equipped with a quad-core CPU, preferably an Ice Lake series for Intel, and at least 8 GB RAM (preferably 16) will allow you to work with your project comfortably.

- As for the software, we recommend **using the latest versions** of Chrome, Firefox, or Safari browsers.
- Ensure that your browser **doesn't block caching**.

### Collapse task dependency links

BigPicture lets you hide (collapse) dependencies and display dependencies for only the selected tasks. [De-clutter your dependency view](https://bigpicture.one/blog/more-clarity-in-project-dependencies/) and improve responsiveness on the Gantt and Board modules.

### Use simple JQL queries

In BigPicture, you can narrow the active (visible) data in your box using JQL.

The JQL-based quick filters control what is currently visible in your box. A b x's scope can also be based on JQL (scope based on Jira filters) or narrowed down based on a JQL query.

Complex queries can impact **UI responsiveness and page load times**. For that reason, try to keep your JQL queries simple. If you need to perform more complex operations on your scope, break your query into several simpler, quick filters.

---

## Lower risk of Jira issue pages slowing down

Data Center only.

If your Jira data center's performance drops when using BigPicture, try adjusting the following settings.

### Disable BigPicture widgets

The WBS and Skills [widgets](https://bigpicture.one/articles/bp-widgets/) add information to a Jira issue page, but they might slow down how quickly the issue page loads. To speed things up, turn off one or both of these widgets. Settings can be adjusted per Jira project.

Keep in mind that each additional plugin installed shares Jira's resources.

### Turn off BigPicture comments on Jira issues

Each time a task is updated using BigPicture, the app can add a [comment to a Jira issue](https://appfire.atlassian.net/wiki/spaces/DLP/pages/298387307) to keep track of changes. Dis ble this functionality for better app performance.

**Go to:** The *Fields* tab can be accessed by a Jira admin:

1. At the top bar, go to **Apps** > **App Configuration**. Yo are taken to the *Fields* tab in the *General* section.
2. Change the **Save issue changes to Jira Server issue comments** toggle switch to the off position.

![image-20240311-072811.png](/cms_trial/assets/f6f2b7ed-9292-4042-9155-d7d4756a1b92.png)

### Logs collection

The [fine-grained logs](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297571655) the app collects are helpful if you want to help our Support Team [troubleshoot your problem](https://appfire.atlassian.net/wiki/pages/createpage.action?spaceKey=spm&title=%23Performance&linkCreation=true&fromPageId=1918635504) faster, but it may slow down your application. Red ce the granularity level and let the app collect the "“Warnings only"” or  the "“Information and warning."”

Go to App Configuration > Advanced > [Technical info tab](https://appfire.atlassian.net/wiki/spaces/DLP/pages/297571655) to switch off **fine-grained logging**. Next, scroll down to the **Others** section, where you'll find settings for the **logs collection**.

![image-20240311-071703.png](/cms_trial/assets/5a6b58de-ee25-469f-8151-d1bc328ad248.png)

---

## Performance during screen sharing

When using BigPicture during screen sharing, you might notice a slowdown in performance. To help you maintain a smooth experience, we've compiled a list of practical tips to optimize your browser, call settings, and hardware. By following these suggestions, you can enhance BigPicture’s performance and ensure your screen-sharing sessions run more efficiently.

[Unmapped macro: button-handy — no content to fall back on]