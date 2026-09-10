# Automatically move unresolved issues to next sprint and update story points

## Problem

You need to automatically move unresolved issues from a closed sprint to the next active sprint and update their story points based on remaining estimates.

## Solution

Create a SIL script that automatically moves unresolved issues between sprints and recalculates story points based on remaining estimates. The script finds the last closed sprint, identifies unclosed issues, and moves them to either the current started sprint or the next available sprint while updating story points proportionally.

### Script

```java
string message="";
string brd=getElement(argv, 0);
number lastClosedSprint=0;
number nextSprintInSprints=-1;
string unclosedIssues="";
string[] closedIssuesInClosedSprint;
if (isNull(brd))
{
 message = "Missing parameter: Board name.";
 return message;
}
lastClosedSprint=getElement(closedSprints(brd),size(closedSprints(brd))-1);
if (size(notStartedSprints(brd))>0)
{
 nextSprintInSprints=getElement(notStartedSprints(brd), 0);
}
closedIssuesInClosedSprint=selectIssues("sprint = " + lastClosedSprint + " AND status = 'Closed'");
for (string iss in closedIssuesInClosedSprint)
{
 removeIssueFromSprint(iss, lastClosedSprint);
 if (isNotNull(startedSprints(brd)))
 {
 addIssueToSprint(iss, getElement(startedSprints(brd),0));
 }
 else
 {
 if (nextSprintInSprints>-1)
 {
 addIssueToSprint(iss, nextSprintInSprints);
 }
 }
 
 if (isNotNull(%iss%.originalEstimate) and originalEstimate!=0 and isNotNull(%iss%.estimate))
 {
 interval originalInterval=%iss%.originalEstimate;
 interval remainingInterval=%iss%.estimate;
 number points =#{%iss%.Story Points};
 number originalMillies = originalInterval["TOMILLIS"];
 number remainingMillis = remainingInterval["TOMILLIS"];
 number newPoints=round(points * remainingMillis / originalMillies, 0);
 #{%iss%.Story Points}=newPoints;
 }
 unclosedIssues = unclosedIssues + ", " + iss;
}
if (startsWith(unclosedIssues, ", ") )
{
 unclosedIssues=substring(unclosedIssues, 2, -1);
}
message = "Unclosed issues " + unclosedIssues + " were removed from Sprint " + lastClosedSprint + " and added to Sprint " + nextSprintInSprints + ".";
message = message + "Story points have been updated.";
return message;
```

## Implementation steps

|  |  |
| --- | --- |
| **Step 1: Create the SIL script file:** | 1. Log in as a Jira administrator. 2. Navigate to **Administration** > **Apps** > **Power Scripts** > **SIL Manager**. Power Scripts for Jira Cloud sprint migration script configuration dialog 3. Right-click the **silprograms** folder in the left panel and select **New** > **File**.  Power Scripts for Jira Cloud story points update configuration form  1. Type your script filename (remember to add the `.sil` extension). 2. In the right panel of the SIL Manager, add the script code provided above. 3. Customize the script by replacing:     - `'Closed'` with your actual closed/resolved status name;    - `Story Points` with your exact story points field name. 4. Click **Check** to validate the syntax and save your file.  Power Scripts for Jira Cloud automated sprint migration results panel |
| **Step 2: Configure the SIL Runner gadget** | 1. Add the Power Scripts for Jira gadget to your dashboard. 2. Configure it to run your new script file.  Power Scripts for Jira Cloud issue migration status display  1. Set up any required parameters and save the gadget.   For detailed configuration steps, see [SIL Runner Gadget configuration](/cms_trial/space/PSJC/490996338/SIL+Runner+Gadget+configuration/). |

## Example usage

To run this script:

1. Access the SIL Scripts Gadget on your dashboard.
2. Select your script from the programs dropdown.
3. Enter the board name as a parameter (for example, `SCRUM Board`).

   ![Power Scripts for Jira Cloud sprint completion workflow settings](/cms_trial/assets/6a9fb4c5-1eb7-47c2-9e0c-8e0f26b5ae68.png)
4. Click **Run**.

The script automatically moves unclosed issues from the last closed sprint to the current active sprint (if available) or the next planned sprint, while recalculating story points based on remaining estimates.