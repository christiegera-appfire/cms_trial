# Sum up story points for issues in an Epic

## Problem

You want to have a field that contains the sum of all the story points under an Epic.

## Solution

Create a scripted field that calculates the total story points by checking if the current issue is an Epic, then finding all child issues and summing their story point values. The script only processes issues with story points greater than 0 to avoid null value errors.

### Script

```text
integer sum = 0;
if(issueType == "Epic") {
    for(string i in selectIssues("parent = " + key)) {
        if(i.storyPoints > 0) {
            sum += i.storyPoints;
        }
    }
}
return sum;
```

Example output: `7`

### Implementation steps

1. Navigate to **Power Apps Config** > **Advanced** > **Scripted Fields** and click **Add custom field**.

For detailed information, see the [Scripted Fields configuration](/cms_trial/space/PSJC/856361791/Scripted+Fields+Configuration/) page.

1. In the **Add custom field configuration** window:

   1. Add the script provided above to the scripted field.
   2. Select the **Child update** trigger option. This ensures that the scripted field on the Epic gets updated when a Story (or other child issue type) is updated.
   3. Set the appropriate filters as needed—project categories, projects, and issue types.

Include child issue types (such as Story, Task, Bug) in the **Select issue types** filter so the scripted field triggers when those children are updated.

1. Save the configuration.

## Example usage

This scripted field automatically calculates and displays the total story points for each Epic based on its child issues. When you view an Epic, the field will show the sum of all story points from its associated Stories and other child issue types.

The field updates automatically when:

- Story points are modified on child issues;
- Child issues are added or removed from the Epic;
- Child issue types are updated (if properly configured).