# Large bulk operations - memory optimization

## Overview

This document addresses memory optimization strategies for Jira scripts that process large volumes of issues. When handling bulk operations, memory consumption can grow rapidly, leading to performance degradation for both the script itself and other operations on your Jira instance.

We present examples of three key approaches to memory management:

- Basic memory optimization: Using the [saveModifiedIssues()](/cms_trial/space/PSJC/865928192/saveModifiedIssues/) function at strategic intervals to commit changes and release memory.
- Simple batch processing: Breaking down issue selection by project, type, or other criteria to process smaller sets.
- Advanced batch processing: Using scheduled scripts to process issues in smaller batches with complete system memory recovery between executions.

These techniques can be implemented individually or combined to handle virtually any volume of issues efficiently. The appropriate strategy depends on your specific use case, the number of issues to be processed, and the complexity of the operations being performed.

## Problem

Large-scale operations in Jira frequently require scripts to process hundreds or thousands of issues simultaneously. When working with substantial issue volumes, scripts can consume excessive memory resources, leading to several critical problems, such as:

- Script performance degradation: As memory usage increases, script execution slows down dramatically, potentially timing out before completion
- System-wide ompact: High memory consumption by one script can starve other scripts and even core Jira functions of necessary resources
- Failed operations: Without proper memory management, bulk operations may fail entirely, requiring manual intervention and repeated attempts

This memory challenge is particularly common in two scenarios:

- Scheduler scripts: Automation that regularly processes batches of issues (such as status updates or field calculations)
- Ad-hoc cleanup scripts: One-time scripts run directly from the SIL Manager, often needed after migrations or for data cleanup projects

Without proper memory optimization techniques, scripts that initially work well with small data sets may fail catastrophically when they encounter larger volumes of issues in production environments.

## Solution

By employing specialized functions and scripting techniques, memory utilization can be optimized, allowing for the efficient processing of numerous issues.

---

## Basic memory optimization example

Using the [saveModifiedIssues()](/cms_trial/space/PSJC/865928192/saveModifiedIssues/) function is a great way to keep the utilized memory from growing too large. This function will commit the changes to issues that have been updated by the script and will release the memory for those issues. Executing the function for every script may cause the scripts to run slowly since it will try to perform these memory optimization steps for every single issue. It is unnecessary and inefficient to include the function on every issue or for every iteration of the loop. A more efficient way would be to call the function once for every 10 issues as seen in the example below.

```text
// Basic memory optimization example
// Processes issues in batches of 10 to prevent memory buildup
int count = 0;
for(string i in selectIssues("project = TEST", 1000)) {
    count++;
    %i%.description += "\n\nmodified"; // Modify here the issues
    if(count % 10 == 0) {
        saveModifiedIssues(); // Saves the 10 issues AND clears the memory
    }
}
```

The number of issues kept in memory before running the [saveModifiedIssues()](/cms_trial/space/PSJC/865928192/saveModifiedIssues/) function can be adjusted and fine-tuned for the specific script to find the perfect combination of speed and efficiency. You may find that waiting every 50 issues is more performant and still keeps the memory optimized effectively.

Here’s what you need to consider when using the basic memory optimization method:

| **This method works for…** | **This method doesn’t work for…** |
| --- | --- |
| - Any script that loops through Jira issues. - Scripts where issue count may grow over time. - Optimizing memory during issue processing. - Making scripts more efficient as they scale. | - Large initial queries (10,000+ issues). - Reducing memory of the initial issue selection. - Scripts where the query itself causes memory problems. - Cases where just selecting issues consumes too much memory. |

---

## Batch processing examples

To solve the issue where selecting large amounts of issues in a query consumes too much memory, batch processing techniques can be used. With these techniques the number of issues that are selected get broken up into smaller batches so that each batch consumes less memory.

### Simple technique

With this technique the issues are selected into smaller batches by using some way to separate them such as project, issue type, or custom field value.

```text
// Simple batch processing technique
// Process issues by project to limit memory usage
for(string proj in allProjects()) {
    // Only select issues from one project at a time
    string[] issues = selectIssues("project = " + proj + " AND issuetype = Bug");
   
    int count = 0;
    for(string i in issues) {
        count++;
        // Do something here with each issue
        if(count % 10 == 0) {
            saveModifiedIssues(); // Saves the 10 issues AND clears the memory
        }
    }
```

### Advanced technique

A more advanced technique that was popular before the [saveModifiedIssues()](/cms_trial/space/PSJC/865928192/saveModifiedIssues/) function was created was to use the [SIL Scheduler](/cms_trial/space/PSJC/490998807/SIL+Scheduler/) to trigger the execution of scripts to break up the script operations into smaller batches. Parameters can be used to tell the script which batch of issues it should process.

Setting up the scheduled scripts to run with parameters could be done in a semi-manual way where a single script could be set up to run multiple times in the scheduler using the parameters to make the script work with a different set of issues each time it runs.

Or, a dynamic solution can be used that uses [functions that schedule](/cms_trial/space/PSJC/434507358/Scheduling+Functions/) the execution of scripts to break up the script operations into smaller batches.

```text
// Advanced batch processing technique
// Processes issues across multiple script executions
string lastIssue = argv[0]; // Read in the last issue from scheduler parameter

int count = 1;
int batchSize = 1000;

if(isNotNull(lastIssue)) { // Prevent errors in logs
    // Order by is very important in the JQL
    for(string i in selectIssues("issuetype = Bug AND key > " + lastIssue + " order by key ASC", batchSize)) {
        count++;
        %i%.description += "\n\nmodified"; // Modify here the issues
        if(count % 10 == 0) {
            saveModifiedIssues(); // Saves the 10 issues AND clears the memory
        }
        lastIssue = i; // Update the lastIssue variable for the next script
    }
    // Only run if there are more issues to process
    if(count >= batchSize) {
        // Schedule next batch to run
        runJobAt("batchIssues.sil", lastIssue, currentDate() + "2m"); // Update script name
    }
}
```

If you experience issues with the script such as it works properly when tested from the SIL Manager but does not appear to work the same when scheduled this could be due to a permissions issue. Scripts executed from the SIL Manager will inherit the user permissions of the user (you) running the script. Since a specific user does not cause a scheduled script to be triggered there are no permissions to inherit. This can be fixed by adding a [runAs()](/cms_trial/space/PSJC/434374366/runAs/) function at the top of the script telling the script which user to use for permissions. Or, make sure the **atlassian-addons-admin** user group has permissions in the projects/issues being used.

#### How it works

This technique forces a more aggressive form of memory management by allowing breaking up the job into multiple script executions. This gives the system an opportunity to reclaim the memory and clean things up before the next batch gets executed.

The way this works is that the script will process a set number of issues. When the script completes the processing of that specific number of issues it will schedule the script to run again with the next set of issues. The number of issues queried and the batch size set in the script determine how many times the script will be scheduled to execute.

The process follows this flow:

1. The script processes its assigned batch of issues.
2. Upon completion, it identifies the last processed issue.
3. It schedules itself to run again after a short delay, passing the last issue as a parameter.
4. The next execution starts where the previous batch ended.
5. This continues until all issues are processed.

The number of executions is determined by your total issue count and batch size. For example, with 3,311 issues and a batch size of 1,000, the script will run exactly 4 times (including the initial run).

This approach prevents memory buildup that would occur if all issues were processed in a single execution, making it ideal for very large datasets.

Review the detailed explanation of key code elements below. Note that the reference table refers to the line number of actual code, excluding the comments.

See detailed explanation

| **Line #** | **Script element** | **Description** |
| --- | --- | --- |
| `1` | `string lastIssue = argv[0];` | Argv variable access The script accesses the parameter passed to it through the `argv` array and reads the `lastIssue` parameter from the previous batch execution. This enables communication between batch runs so each execution knows where to resume processing. |
| `8` | `for(string i in selectIssues("issuetype = Bug AND key > " + lastIssue + " order by key ASC", batchSize)) {` | JQL query The JQL query contains two critical elements:   - First, `key > lastIssue` ensures the new batch starts where the previous batch ended. - Second, `order by key ASC` is critical because it ensures that the order of the issues that are queried is the same from batch to batch. This consistent ordering is essential for the batching process to work correctly. |
| `12` | `saveModifiedIssues()` | Memory optimization Even though we're breaking execution into batches, `saveModifiedIssues()` is still necessary. Each batch processes up to 1,000 issues, which could still consume significant memory without periodic saving. |
| `14` | `lastIssue = i;` | Parameter tracking The `lastIssue` variable is updated with each iteration, tracking the last processed issue. When the loop ends, this becomes the parameter for the next batch execution. |
| `17` | `if(count >= batchSize) {` | Batch continuation logic If the batch size is set to 1,000 issues and there are 3,311 issues in total this is how the executions will be executed:   - Batch 1: 1 through 1,000 - Batch 2: 1,001 through 2,000 - Batch 3: 3,001 through 3,311   At the end of Batch 3, the count variable will be 311. Since there are not enough issues to process a fourth batch of 1000 issues, no next batch is scheduled. |
| `19` | `runJobAt("batchIssues.sil", lastIssue, currentDate() + "2m");` | Next batch scheduling The `runJobAt` function:   1. Schedules the next batch to run after a 2-minute delay 2. Uses "batchIssues.sil" as the script for the next batch execution 3. Passes the lastIssue value as a parameter to the next script 4. Uses currentDate() + "2m" to schedule execution 2 minutes from now 5. Includes this delay to allow for proper system recovery between batches |

Note that it is not only important to add a little bit of time between each batch to give Power Scripts time to recovery and to be ready for the next batch but also for Jira as well. When each issue is updated the issue will need to reindexed, events triggered, subsequent automations run, and notifications sent. It is a good idea to allow Jira to complete all these processes before continuing with the next batch.

#### How to set up the advanced technique

Since this technique requires each script to create the configuration for the next script, it might not be obvious how to start the process. Here are 3 simple ways to start it off:

|  |  |
| --- | --- |
| Manually schedule the first batch | Create a job in the SIL Scheduler by following these steps:   - Select `batchIssues.sil` as your script. - Add a parameter with a key that comes before your first target issue (e.g., "TEST-99" if your first issue is "TEST-100"). - Make sure the job is not scheduled to repeat. This means, the **Does this job repeat?** slider is turned off.  Power Scripts for Jira Cloud memory optimization configuration |
| Start the first batch with a script | Run a one-line ad-hoc script to trigger the first batch:  ```text runJobAt("batchIssues.sil", "TEST-99", currentDate() + "10s"); ``` |
| Self-initializing script approach | In the example above, line #6 (`if(isNotNull(lastIssue)) {`) is there just to prevent unexpected errors, but it could be used as a way to jump-start the batch of scripts. For example, modifying line #6 to the following would allow the batch to start automatically:  ```text // Current version of line #6 if(isNotNull(lastIssue)) {...  // Modified version if(isNull(lastIssue)) {   lastIssue = "TEST-99"; } else {... ```  The `lastIssue` variable would only be null if it was never set or if there was some unforeseen error. So, if it is unset, we can assume it is the first time the script has been run, and we can provide a starting issue key. |

---

## Comparison of the three memory optimization approaches

|  | **Basic memory optimization** | **Simple batch processing** | **Advanced batch processing** |
| --- | --- | --- | --- |
| **Best for** | - Scripts working with < 5,000 issues - Use when you need quick implementation and moderate issue volumes | - Scripts working with 5,000-20,000 issues - Use when you need better memory management without a complex setup | - Scripts working with > 20,000 issues or very complex operations - Use when you have very large volumes or critical memory constraints |
| **Memory efficiency** | Moderate: Releases memory for processed issues | Good: Limits initial query size | Excellent: Complete memory recovery between batches |
| **Implementation complexity** | Low: Just add `saveModifiedIssues()` calls | Medium: Requires segmenting queries | High: Requires scheduled script setup |
| **Overall efficiency** | Fastest execution with moderate system load | Balanced speed and system impact | Slowest execution but lightest system footprint |
| **Limitations** | Doesn't help with initial query memory usage | Requires logical way to segment issues (project, type, etc.) | Higher complexity, longer overall execution time |
| **Maintenance** | Medium: May still have memory issues with very large sets | Low: Better handling of large volumes | Very low: Most resilient approach |