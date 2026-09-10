# Track completion progress

## Problem

You want to track the overall completion progress in terms of hours spent vs. estimated for a time-boxed Jira project.

## Solution

The solution runs the following steps:

- When an issue is created or edited in the project, or a worklog is generated, the script below runs.
- It sums all the estimated hours on all issues in the project, sums all the logged work hours on all issues in the project, calculates the project percentage complete (in terms of hours), and then adds a human-readable comment to a "master tracker" issue with the latest data.
- e.g. "This project has \*200h\* estimated work with \*120h\* spent for a total of \*80h\* remaining. It is \*60%\* complete."
- It can easily be modified to populate custom fields instead of generating a comment. This has now been reflected in the example script.

## Prerequisites

1. You have Jira Core, Software, or Service Desk installed
2. You have Power Scripts™ for Jira installed
3. You have created four custom fields of type "interval" and mapped those custom field IDs to the following aliases in the sil.aliases file:

   1. `projectTotalTimeEstimated`
   2. `projectTotalWorkLogged`
   3. `projectTotalTimeRemaining`
   4. `projectPercentComplete`

## Modifications Required

1. Modify the script to reference a single project to calculate totals
2. Modify the script to reference a single issue to append comments to

## Configuration

Trigger this script on the following system events:

- Issue Created
- Issue Edited
- Work Logged on Issue

## Script

This script will run whenever an issue is created, updated, or work is logged on an issues in the applicable project.

It adds a comment to a specific issue to explain, in human readable terms, how many total hours are esimated and logged in the project, and gives a percentage complete value. One could mod the script to populate fields instead of adding a comment.

```text
string projectInScope="SMSW"; // the project you want to sum up
string masterIssue="SMSW-23"; // issue where you want to capture this info

if(project==projectInScope) { // if invoked via listener, limit the scope
 string jql="project="+projectInScope; 
 string [] allProjectIssues=selectIssues(jql);
 string issue;
 string commentText;
 
 interval sumOriginalEstimate;
 interval sumTimeSpent;
 interval sumTimeRemaining;
 
 number hoursOriginalEstimate;
 number hoursTimeSpent;
 number completePercent;
 
 number countIssues=0;
 
 for(issue in allProjectIssues) {
   sumOriginalEstimate += %issue%.originalEstimate;
   sumTimeSpent += %issue%.timeSpent;
   countIssues +=1;
 }

 sumTimeRemaining = sumOriginalEstimate - sumTimeSpent;
 hoursTimeSpent = sumTimeSpent;
 hoursOriginalEstimate = sumOriginalEstimate;
 completePercent = round((hoursTimeSpent/hoursOriginalEstimate)*100,0);
 
 %masterIssue%.projectTotalTimeEstimated = sumOriginalEstimate;
 %masterIssue%.projectTotalWorkLogged = sumTimeSpent;
 %masterIssue%.projectTotalTimeRemaining = sumTimeRemaining;
 %masterIssue%.projectPercentComplete = completePercent;
 
 string commentTextA = "This project has *"+sumOriginalEstimate+"* estimated work";
 string commentTextB = " with *"+sumTimeSpent+"* spent for a total of *";
 string commentTextC = ""+sumTimeRemaining+"* remaining. ";
 string commentTextD = "It is *"+completePercent+"%* complete. ";
 string commentTextE = "This update brought to you changes made in "+key+".";
 commentText = commentTextA + commentTextB + commentTextC + commentTextD + commentTextE;
 addComment(masterIssue, currentUser(), commentText);
}
```