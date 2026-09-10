# Create story subtasks and close them when story is closed

## Problem

You want to create story subtasks and close them when the story is closed.

## Solution

The following script runs on an **Issue Created** event listener.

When you create either a **Story**, **New Feature**, or **Improvement**, subtasks oriented to modern application development are automatically created.

Also, the **Component** field is set to the value equivalent to the issue type. This is because the use case assumes that all area-specific tasks should be automatically assigned to the team member specialized in that area. For example, if you have one database developer on your team, it is preferred that all database subtasks be automatically assigned to that developer.

This requires to:

- set up the **Components** field in your project to precisely map to your subtask issue types,
- ensure the issue is automatically assigned to the component owner.

This is handled in the project configuration, not within this script.

#### Script - CreateAppDevSubtasks.sil

```text
string [] subTaskIssueTypes="Visual Design|UI/UX|Front-End Development|API|Back-End Development|Database";

if(project=="SMSW") {
    if(issueType=="Story" || issueType=="New Feature" || issueType=="Improvement") {
        for(string issue in subTaskIssueTypes) {
            string[] custom_fields_mapping;
            custom_fields_mapping = "";
            string newIssueKey = createIssue(
                        project, // Project Key
                        key, // Parent Issue Key (Blank if Standard Issue Type)
                        issue, // Issue Type
                        summary, // Summary
                        priority, // Priority
                        description, // Description
                        issue, // Components
                        "", // Due Date
                        "", // Estimate
                        "", // Security Level
                        custom_fields_mapping // Custom Field Map
                       );
        }
    }
}
```

## Example story workflow

![Power Scripts for Jira Cloud SDLC workflow automation diagram](/cms_trial/assets/14cd95f1-4191-4343-b9c9-5baf8ee55617.png)

## Example subtask workflow

![Power Scripts for Jira Cloud automated development workflow example](/cms_trial/assets/e1b53798-7231-4284-9476-e6e06a35220f.png)

## Story workflow resolution transition action

This script is called from a action on a resolution transition of a parent issue. When the issue is resolved, all subtasks are automatically closed. Also, the resolution is set to **Automated**. This indicates that the subtasks were closed through an automated process (not through a manually completed transition).

This example assumes that your workflow includes a **Kill** transition, and an **Automated** resolution configured in your system.

#### Script - AutoResolveAllSubtasks.sil

```text
string[] issues = subtasks(key);
for(string issue in issues) {
    autotransition("Kill", issue);
    %issue%.resolution="Automated";
}
```

## Story workflow reopen transition action

This script is called from a action on a **Reopen** transition of a parent issue. When the issue is reopened, all subtasks are automatically reopened and the resolution is cleared.

This example assumes that your workflow includes a **Reopen** transition that becomes available based on the state of subtasks.

#### Script - AutoReopenAllSubtasks.sil

```text
string[] issues = subtasks(key);
for(string issue in issues) {
    autotransition("Reopen", issue);
    %issue%.resolution="";
}
```

## Event listener

When using this example, it is recommended to synchronize fields among parent and child issues.

If the description changes on any parent or child issue, the below script synchronizes the **Description** field across all dependent issues.

The script listens for **Issue Edit** events. For all applicable parent, child, and sibling issues, the **Description** field is synchronized across them.

Because this is an event listener, set the scope to a single project (SMSW) to reduce it to a minimum.

To prevent all issue types from having the same behavior, declare them separately.

#### Script - SyncDescriptionBetweenParentAndChildren.sil

```text
if(project=="SMSW") {
    if (issueType=="Story" || issueType=="New Feature" || issueType=="Improvement"){
        // The issue is a parent and must be copied to all children
        string [] issues = subtasks(key);
        string issue;
        
        // Loop over all sub-tasks and copy fields
        for (issue in issues) {
            %issue%.description = description;
        }
    }
    else if(isNotNull(parent.key) && (parent.issueType=="Story" || parent.issueType=="New Feature" || parent.issueType=="Improvement")) {
        // The issue is a sub-task and must be copied to parent and all siblings
        // Copy to parent
        parent.description = description;
        
        // Copy to siblings
        string [] issues = subtasks(parent.key);
        string issue;
             
        // Loop over all sub-tasks and copy fields
        for (issue in issues) {
            // Don't update the issue that was just updated.
            if (%issue%.key != key) {
                %issue%.description = description;
            }
        }
    }
    
}
```