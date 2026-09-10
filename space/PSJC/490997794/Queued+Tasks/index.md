# Queued Tasks

The Queued Tasks monitoring tool keeps track of individual script executions to help you understand the performance implications associated with running scripts. The chart shows the number of script executions add to the script queue over time. The chart can be found at **Power Apps Config → Runtime → Queued Tasks.**

If more scripts are executed and are simultaneously running than there are available threads in the thread pool, these script will sit in the queue until additional threads become available. You may want to increase the number of threads by configuring the thread pool size in **Power Apps Config → General → Thread Pool**. However, there may be additional performance implications. For more information see the [Thread Pool documentation](/cms_trial/space/PSJC/490996420/Thread+pool+configuration/) page.

If there is a large number of apps running consistently then there may be some configuration issues that need to be addressed:

- Are scripts scheduled to run at very frequent intervals?
- Are listener scripts filtered to only run for specific project and issue types?
- Are scripted custom fields made only to run in specified project and issue type contexts?

The settings and others could dramatically reduce the number of times a script is executed.

![Power Scripts for Jira Cloud boomerang issue scheduler configuration](/cms_trial/assets/8d8209e2-a636-4de7-a66e-0805f86aa6eb.png)

**See More**