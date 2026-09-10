# Whole Jira or BigPicture is slow

In case of contacting our Support Team using [our portal](https://appfire.atlassian.net/servicedesk/customer/portal/11) or [email](mailto:support@bigpicture.one) **for the first time**, please remember to:

- Describe a problem in detail.
- Collect the required data (described below) and **attach** it to the request.
- Provide an exact timestamp when a problem occurred.

If you have contacted the Atlassian Support Team regarding performance problems and have a preliminary analysis, let us know and add our **Support Team** to that ticket.

**Problem**

You notice low performance throughout Jira and BigPicture (high server resource usage, e.g., high CPU usage), or the whole Jira system does not respond.

**Required data to collect and send to the Support Team:**

- [Jira logs](/cms_trial/space/SPM/1918666463/Report+problem/)
- [Fine-grained logs](/cms_trial/space/SPM/1918666463/Report+problem/)
- [Thread dumps](/cms_trial/space/SPM/1918666463/Report+problem/)

You need to generate thread dumps **while** you are experiencing performance problems. **Collecting thread dumps when issues no longer exist is useless.**

You can generate thread dumps a few times, as comprehensive data can help our Support Team analyze the problem faster.

[Excerpt "" from page "DLP:Technical info." not found]

If Jira or BigPicture is unresponsive and you cannot access the **App Configuration > Advanced > Technical info** page to generate thread dumps, you can create thread dumps [using the commands](https://confluence.atlassian.com/adminjiraserver073/generating-a-thread-dump-861253873.html):

**For** **jstack installed:**

It is recommended to use **jstack**because thread dumps with CPU usage are in one file.

1. When you notice a performance problem, you can Identify the Jira application PID by using a command:

   ```text
   JIRA_PID=`ps aux | grep -i jira | grep -i java | awk  -F '[ ]*' '{print $2}'`;
   ```
2. Run the following command - it generates ten snapshots of CPU usage and thread dumps with 10-second intervals for a minute. You must have a JDK installed for the **jstack** command to work.

   ```text
   for i in $(seq 10); do top -b -H -p $JIRA_PID -n 1 > jira_cpu_usage.`date +%s`.txt; jstack -l $JIRA_PID > jira_threads.`date +%s`.txt; sleep 10; done
   ```
3. Compress generated **jira\_cpu\_usage.txt** and **jira\_threads.txt** files and send them to our Support Team.

**No** **jstack installed:**

1. If you do not have **jstack** installed, use the following command when you notice a performance problem:  
   This command generates ten snapshots of CPU usage and thread dumps with 10-second intervals.

   ```text
   for i in $(seq 10); do top -b -H -p $JIRA_PID -n 1 > jira_cpu_usage.`date +%s`.txt; kill -3 $JIRA_PID; sleep 10; done
   ```

   When "**kill -3"** is used, the thread dump is sent to the standard error stream. If you run your application in tomcat, the thread dump will be sent into <TOMCAT\_HOME>/logs/catalina.out file, which is usually attached to the Jira support zip.
2. Compress generated **jira\_cpu\_usage.txt** files and send them to our Support Team with the Jira support zip file.

You can also find instructions for all scripts recommended by Atlassian [on this page](https://confluence.atlassian.com/jirakb/troubleshooting-jira-performance-with-thread-dumps-644874457.html).