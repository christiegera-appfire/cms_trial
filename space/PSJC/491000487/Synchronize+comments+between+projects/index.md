# Synchronize comments between projects

## Problem

Often a body of work is not able to be captured within a single issue in Jira since it requires multiple teams or business units to accomplish. Information added to a ticket in one teams project does not automatically flow through to the other teams project and important updates can become lost.

## Solution

To solve this problem, a listener script from Power Scripts can be used to add new comments from one teams project to the corresponding issue in another project.

### Step 1: Create the script

1. Create a script similar to the one below to be called by the listener

   ```text
   string [] links = linkedIssues(key, "Cloners");

   if(size(links) > 0) {   
       JComment lastComment = getLastComment(links[0]);
       addComment(clone, lastComment.author, lastComment.text, lastComment.securityLevel);
   }
   ```

The above script finds the corresponding issue by using links. This script uses the “Cloners” link type specifically but any link type can be used. Please note that the **link type name** should be used. This name is different the outward and inward link descriptions. For example, with the Cloners link type the outward description is “clones” and the inward is “is cloned by” but the name for the link type is “Cloners”. The link type names can be found on the **Issue Linking** page in the Jira admin.

The above script assumes that there should only be one link of type “Cloners” for the issue since the issue can only be cloned from a single source. If using a different link type the script will select the **first** link it finds for the given type.

### Step 2: Configure the listener

1. Navigate to the listeners configuration page by going to **Power Apps Config > Power Scripts > Listeners**
2. Click the **Add listener** button
3. Select the script created above for the listener script

   1. Leave the **Asynchronous** option unchecked
4. Leave the user input blank
5. Select **Issue Commented** for the event type
6. *Optionally* you can add a project and issue type filter to limit the listener so it only triggers for specific project/issue types

   ![Power Scripts for Jira Cloud system load monitoring display](/cms_trial/assets/d651ab83-affe-42e1-8200-818138f1f395.png)
7. Click the **Add** button to save the listener

The above script attempts to add the comment to the linked issue using the same user profile as the user who created the comment originally. If that user does not have permissions to edit issues in the linked project another user profile can be used as the author for the comment. Line 5 of the script would need to be modified.