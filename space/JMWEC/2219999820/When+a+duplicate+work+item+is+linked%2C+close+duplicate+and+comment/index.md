# When a duplicate work item is linked, close duplicate and comment

| **Goal** | When an existing work item is identified and linked as a duplicate to another work item, add a comment to the duplicate issue and automatically close it. |
| --- | --- |
| **Scenario** | An existing work item has been identified as a duplicate of another work item. When adding a `duplicates` link to the work item, a comment should be added for auditability and the duplicate work item should be closed. |
| **Components** | [Event-based action](/cms_trial/space/JMWEC/465473524/Event-based+actions/): Issue linked event, [Comment issue(s)](/cms_trial/space/JMWEC/466322568/Comment+issue(s)/) post function, [Transition issue(s)](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/) post function |
| **Baseline** | - The link type *duplicates/is duplicated by* must exist. - The work item with the Outward link - **duplicates**, in this example - is the work item that will have the comment added and will be closed. - The **Done** status should be accessible from all other status values (enable the option **Allow all statuses to transition to this one**). See **Workflow configuration** below for more info. |

---

## Requirements

- JIRA Administrator login
- [Jira Misc Workflow Extensions Cloud](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe)

## Workflow configuration

For this use case to function as designed, it is best to configure the **Done** status in your workflow to be accessible from all other statuses in your workflow. This is to enable the event-based action to close the duplicate issue, no matter what status it has when it is identified as a duplicate. If the **Done** status is not widely accessible, the Transition issue(s) post-function may fail depending on when the work item is linked as a duplicate.

## 1. Create the Event-based Action

[Unmapped macro: multiexcerpt-include-macro — no content to fall back on]

![JMWE for Jira Cloud event selection interface for duplicate work item management](/cms_trial/assets/9daa1645-ffb9-4896-a067-3a93348242fb.png)

## 2. Add the *Comment issue(s)* post-function

1. Under **THEN**, click **Select Post-functions**.
2. In the right-hand panel, select **Comment issue(s)** in the list of post-functions. The [Coment issue(s)](/cms_trial/space/JMWEC/466322568/Comment+issue(s)/) configuration screen will open.
3. For **Target issues**, select *Current issue* (**Point 1**, **Figure 2**, right)*.*
4. For **Comment**, in the script editor, enter the following (**Point 2**, **Figure 2**, right):

   ```text
   This work item has been flagged as duplicate of: 

   {{ issue | linkedIssues( "duplicates", ["key"] )}} - {{ issue | linkedIssues( "duplicates", ["summary"] )}} 

   This work item will be closed.
   ```
5. Click **Save** to save your post-function configuration (**Point 3**, **Figure 2**, right).

## 3. Add the *Transition issue(s)* post function

1. In the upper right corner of the right-hand panel, click **Add Post-function**.
2. Select **Transition issue(s)** in the list of post functions and click **Add**. The [Transition issue(s)](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/) configuration screen will open.
3. For **Target issues**, select *Current issue* (**Point 1**, **Figure 3**, right)*.*
4. Click the **Transition Picker** button to select a Transition (**Point 2**, **Figure 3**, right).
5. In the *Pick a transition* window:

   1. Select your workflow from the **Workflow name** pulldown menu.
   2. Select the **All** transition for moving issues into the **Done** status. This may be a different transition than any that exist between specific status values and your **Done** status.
   3. Click **Use transition ID**.
6. Set any other options as needed; for example, if any other fields need to be set when closing the duplicate, click **Expand all** to the right and set those under the **Fields** section of **Advanced options**.
7. Click **Save** to save your post function configuration (**Point 3**, **Figure 3**, right).

## Save and Test the Action

In the main Event-based Action editor, click **Save** to complete the configuration. To test the new action, create a new work item. Then link that new work item to an existing work item using the *duplicates* link type. Verify that JMWE adds the comment and moves the work item to **Done**.

### Congratulations!

![JMWE for Jira Cloud comment configuration for duplicate work item closure](/cms_trial/assets/560aedfc-c95e-4312-8ce1-be7a633a258d.png)![JMWE for Jira Cloud transition post function setup for duplicate issue management](/cms_trial/assets/87a3d0ef-10fd-4e88-aa5d-dc4e1fd7b0f4.png)