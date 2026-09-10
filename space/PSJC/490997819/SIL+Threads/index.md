# SIL Threads

The SIL Threads section shows a list of all the scripts running at that moment and how long they have been running for. To find this list go to **Power Scripts** > **Performance Monitoring** > **SIL Threads**.

This is a good place to identify scripts that may be ‘stuck’. Perhaps they are waiting on an external system to complete a process or perhaps there is a problem with the logic. Regardless, this section helps you catch this behavior and, if necessary, kill the script that has become ‘stuck’. However, it should be noted that killing the thread can have adverse results in the main application engine and should only be used in case of emergency's.

![Power Scripts for Jira Cloud SQL monitoring interface](/cms_trial/assets/a3be66f2-8100-472d-b9b1-071212da63e0.png)

If a script is not running or has already completed it will not appears in this list.

**See More**