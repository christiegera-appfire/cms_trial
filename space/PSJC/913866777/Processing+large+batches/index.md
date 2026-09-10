# Processing large batches

The `saveModifiedIssues()` function provides robust memory management capabilities when working with large sets of Jira issues. This function optimizes memory usage by efficiently saving changes to issues and releasing memory resources, preventing potential memory overflow errors even as your data processing needs grow. This memory optimization approach is particularly valuable in:

- Scheduled jobs
- SIL Manager ad-hoc scripts
- Scenarios where you need to load, modify, and update many issues efficiently

Implementing this function in your scripts is a best practice for batch processing, ensuring your code remains performant and scalable whether you're currently working with a small number of issues or planning to handle thousands in the future.

## Basic example

The following pattern demonstrates how to process large batches while managing memory usage:

```text
int i = 0;
for(string k in selectIssues("project = TEST", 1000)) {
    i++;
    %k%.description += "\n\nmodified"; //modify here the issues
    if(i % 10 == 0) {
        saveModifiedIssues(); //!!! saves the 10 issues AND clears the memory !!!
    }
}
```

### How it works

1. Selection: we retrieve up to 1000 issues matching our criteria.
2. Batch processing: we process them in batches of 10; we make changes in memory to each issue.
3. Periodic saving: every 10 issues, `saveModifiedIssues()` both saves changes and frees memory.
4. Final cleanup: the final `saveModifiedIssues()` call ensures any remaining issues are saved.

While this approach helps manage memory, you still need sufficient memory to initially load the issues returned by `selectIssues()`.

### Memory management details

When you call `saveModifiedIssues()`, any issues you access afterward will be reloaded from Jira. For example:

```text
TEST-1.description += "\n\nmodified";
saveModifiedIssues(); //saves TEST-1
if(TEST-1.assignee == currentUser()) { //this triggers a reload of the issue, behind the scenes
  //.....
}
```

This memory optimization feature is available only on Jira Cloud. On Jira Data Center/Server, we cannot provide this functionality due to the implicit transaction context when modifying issues.

## Advanced example: batch processing with workflow transitions

The following example demonstrates how to combine batch processing with workflow transitions using the `autotransition` function. This pattern is useful for bulk updating issue statuses.

```text
int count = 0;
int transitioned = 0;

for(string k in selectIssues("project = TEST AND status = 'To Do'", 1000)) {
    count++;
    
    // Only transition issues that meet certain criteria
    if(%k%.priority == "High" && %k%.assignee != null) {
        // Try to transition the issue
        if(autotransition("Start Progress", k)) {
            transitioned++;
        }
    }
    
    // Save modified issues every 10 issues to free memory
    if(count % 10 == 0) {
        saveModifiedIssues();
    }
}

// Save any remaining modified issues
saveModifiedIssues();
```

This script demonstrates:

1. Selecting issues with specific criteria
2. Applying additional filtering logic
3. Using the `autotransition` function to move issues through workflow
4. Periodically saving modifications to free memory

Note that when using `autotransition` in batch processing, the transition must be valid for the current status of each issue. If the transition has conditions or validators, they must be satisfied before calling `autotransition`.