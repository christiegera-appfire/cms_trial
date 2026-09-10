# Report problem

## Support request - details to include

If you are reporting a technical issue or a bug to the Support via [our portal](https://appfire.atlassian.net/servicedesk/customer/portal/11) or [e-mail](mailto:support@bigpicture.one), please attach the following information to your request:

- The address of your Jira Cloud site (check the address bar of your browser, e.g., [*myCloudSite.atlassian.net*](http://myCloudSite.atlassian.net)),
- The exact time when you started noticing problems.

## Reporting procedure - fine-grained logs

If you are experiencing issues with any of our applications and wish to help us diagnose them faster, please follow the steps below before submitting a report to our Support.

If you're not a technical user, nor do you have Jira administrator's permissions, reach out to someone who has the permissions and ask them to:

1. Set the logging level to fine-grained.
2. Reproduce the issue.
3. If you managed to reproduce the issue, return to the troubleshooting section and click Download.
4. Revert to Warnings only - logging level.

See the video for more information:

[Unmapped macro: multimedia — no content to fall back on]

## Gathering thread dumps

If your BigPicture website or Boxes are loading slowly and you would like our Support to diagnose this issue, it is recommended to generate a thread dump file.

A thread dump file will provide essential information on the processes and threads currently running within the Java Virtual Machine and help our Support solve the issue faster.

Follow the steps described below.

1. Open your BigPicture in two different tabs (one of them will be needed to go to the technical settings and the other to reproduce the issue).
2. From the first tab, navigate to BigPicture > App configuration > Advanced > Technical Info.

   - Go to the "Support data" section and click "Generate thread dumps".
   - Set "Number of generated thread dumps" to "10" and "Sleep time between each thread dump generation" to "1".
   - Click "Download" and **immediately** switch to another tab to reproduce the issue.
3. From the second tab, reproduce the issue you have encountered before.
4. Once you reproduce the issue, you need to wait until the file is downloaded.
5. Now, you can attach the downloaded file to your Support ticket.

See the video for more information:

[Unmapped macro: multimedia — no content to fall back on]

## Gathering profiling

In case of slow page loading, it is recommended to download a profiling file. It will help our Support detect the issue faster.

Profiling provides essential information about the code's performance.

Follow the steps described below.

1. Open your BigPicture in two different tabs (one of them will be needed to go to the technical settings and the other to reproduce the issue).
2. From the first tab, navigate to BigPicture > App configuration > Advanced > Technical Info.

   - Go to the "Profiling" section.
   - Set "Event type" to "Wall" and define how many seconds you need to reproduce the issue; 30 seconds should be enough.

**You need to reproduce the issue during the countdown. If you need more than 30 seconds to reproduce the issue, define it in the "Profiling time seconds" field.**

1. Click on the "Profile now" button.
2. From the second tab, reproduce the issue you have encountered before.
3. Once you reproduce the issue, switch to the previous tab and wait until the countdown ends.
4. The file will be downloaded automatically.
5. Now, you can attach the downloaded file to your Support ticket.

See the video for more information:

[Unmapped macro: multimedia — no content to fall back on]

## Creating a dedicated BigPicture log file from atlassian-jira.log

### How to set up a separate log file for BigPicture debug data

If you get a sizeable amount of BigPicture debug data sent to atlassian-jira.log but would instead divert it to a dedicated log file, you can do it by manually changing the configuration of Jira’s log4j file.

Here’s how to do it:

1. Add the following snippet to your log4j.properties\* file:

|  |
| --- |
| *log4j.appender.bigpicture=com.atlassian.jira.logging.JiraHomeAppender*  *log4j.appender.bigpicture.File=bigpicture.log*  *log4j.appender.bigpicture.MaxFileSize=20480KB*  *log4j.appender.bigpicture.MaxBackupIndex=5*  *log4j.appender.bigpicture.layout=com.atlassian.logging.log4j.NewLineIndentingFilteringPatternLayout*  *log4j.appender.bigpicture.layout.ConversionPattern=%d %p [%X{jira.mailserver}] %t %X{jira.username} %X{*[*jira.request.id*](http://jira.request.id/)*} %X{*[*jira.request.assession.id*](http://jira.request.assession.id/)*} %X{jira.request.ipaddr} %X{jira.request.url} %m%n*  [*log4j.logger.com*](http://log4j.logger.com/)*.softwareplant = INFO, console, bigpicture*  [*log4j.additivity.com*](http://log4j.additivity.com/)*.softwareplant = false* |

1. Restart your Jira instance.

This will create a separate bigpicture.log file for all logs from our app or com.softwareplant package specifically.

### Where to find the log4.properties file?

The log4.properties is located in "WEB-INF/classes/log4j.properties." You can find this path by going to your Jira Administration > System > Logging and profiling, and scrolling down to the "Default Loggers" section:

![Logging-and-Profiling-BigPicture-demo.png](/cms_trial/assets/602cd049-5b15-4791-a3e0-ab981856403f.png)

You can further configure the granularity of the log file and choose the desired logging levels:

![contentId-1918666463](/cms_trial/assets/78fc34fe-4a9b-4998-9b32-67fc2677c6aa.png)

This is it. You've just set up a separate log file for BigPicture debug data.

## Extracting Jira Support zip (plugin doesn't start)

### When?

If you are experiencing problems preventing our plugin from starting, please follow these guidelines to extract the Jira Support zip that we can analyze while troubleshooting.

### The procedure

- Go to: Jira Administration >> System >> Logging and profiling
- Mark the logs with something like "Logs for BigPicture support". **This helps the team find the relevant logs easily so please do not skip this step**. Thank you 🙂
- Find the "configure logging level for another package" link, click it, and set the "DEBUG" level for "com.softwareplant" package see the screenshot:

![contentId-1918666463](/cms_trial/assets/0db7c257-3112-4a13-96f1-9d03dfb2ce2e.jpeg)

- Try to reproduce the problem(depending on your specific case it can be reinstalling the plugin etc..) Our helpful Support staff will provide more detailed guidelines in that respect.
- Download the log from: Jira Administration >> System >> Troubleshooting and support tools >> create support zip
- Please consider limiting the log file according to the following guidelines:

  ![contentId-1918666463](/cms_trial/assets/7ea36fab-7398-44aa-9f42-169adfde223b.jpeg)

- Finally, attach the extracted file **along with the phrase you used for marking the logs and the date you created the support zip** so the team can analyse it.

Please remember to switch back to WARN as it impacts performance.