# Close a Story When All Sub-tasks are Closed

## Scenario

When all related Sub-tasks for a Story are completed and closed, automatically transition the Story to Done.

## Resolution

This solution uses the Transition issue post function and requires conditional execution using a Nunjucks script. When an issue is closed, the script refers to the related Story of the issue being closed (if there is one), and checks the status of all sub-tasks for that Story. If it finds a sub-task that has a status other than “Resolved”, the post-function will not run and the Story will not be transitioned. If all sub-tasks for the related Story are closed, the post function will run and the Story will be closed.

**Note**: this configuration is an example of a post function executing on a **target issue** versus the **current issue**. The **current issue** is the issue that triggers the post function to run; the **target issue** is the issue that will be updated by the post-function. The post function configured below will run whenever *any issue is closed*, but it will trigger a transition on a different issue than the one that initiated it.

## Steps to create

### 1. Add *Transition issue(s)* post-function

1. Log in to your Jira instance as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Issues**.
3. In the left-hand sidebar, click **Workflows**.
4. From the list of Workflows, click the **Action** button ( [menu button icon] ) for the appropriate workflow and select **Edit**.
5. Edit the transition:

   1. When viewing the Workflow in **Diagram** view (Figure 1, right), select the Transition and click the **Post Functions** link. Click **Add post function** at the top of the list of existing post functions.
   2. When viewing the Workflow in **Text** view, click the name of the Transition then select the **Post Functions** tab. Click **Add post function** at the top of the list of existing post functions.
6. Select ***Transition Issue(s) (JMWE app)*** from the list of post-functions and click **Add**.

![Edit Transition](/cms_trial/assets/1fa4e481-91ec-414a-a3c1-490974dcb6fd.png)

### 2. Configure the post function

When using the **Transition issue(s)** post function, the target issue will be moved through its workflow based on the post function configuration. Generally, the post function can be configured with a prioritized list of transitions to trigger, and it will move the issue through the first transition that is appropriate to its current status. In this scenario, the post function is configured with a single transition - **Done** - and uses conditional execution to only execute the post function under very specific circumstances. See [Transition issue(s)](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/) for more information.

**Note**: The configuration below has a few pre-requisites in order to function as described.

- The parent Story is in a status immediately preceding the **Done** status, or the transition to **Done** is available from all other statuses.
- The Nunjucks script included under **Conditional execution** checks for a status value of “Resolved” to determine if each sub-task is closed. This value will need to match your status value for the Done status.

Set the following configurations:

1. **Issue(s) to operate on** (**Point 1**, **Figure 2**, right) - Set **Target issue(s)** to *Parent issue of the current sub-task*.
2. **Transition(s)** (**Point 2**, **Figure 2**, right)

   1. Set **Transition(s)** to *Trigger on of the following transitions*.
   2. Set **Transition name or ID** to *Done*, or the appropriate transition to move the issue to a closed status. Click **Transition picker** to open a window where you can search for a specific transition.
   3. Once you have set the Transition Name or ID, click **Add**. (**Point 3**, **Figure 2**, right)
3. **Run As** (**Point 4**, **Figure 2**, right) - Set as needed; it is recommended to leave the default *Add-on user* value unless required for specific reasons.
4. **Transition Screen** (**Point 5**, **Figure 2**, right) - Set as needed.

   1. If any fields are required to transition the issue, add them here.
   2. In the example (Figure 2, right) the **Comment** field has static text added to the parent Story - `This issue has been closed because all sub-tasks have been resolved`.
   3. Set **Comment visibility** as needed.
5. **Conditional execution** (**Point 6**, **Figure 2**, right) - Enter the following:

   1. Check the box **Run this post-function only if a condition is verified**.
   2. In the **Condition** field, enter the code:

      ```none
      {% set subs = targetIssue | subtasks("status") %}
      {% set trigger = true %}
      {% for sub in subs %}
      	{% if sub.fields.status.name != "Done" %}
          	{% set trigger = false %}
          {% endif %}
      {% endfor %}
      {{ trigger }}
      ```
6. **Delayed execution** (**Point 7**, **Figure 2**, right) - Set as needed.
7. Click **Add**.

![contentId-465373402](/cms_trial/assets/a197b2aa-f432-4cc8-9501-0f1d0ce58dbb.png)

### 3. Publish and verify

The last step is to publish your updated workflow and then test the new version to verify that the new extensions have been configured correctly. To test the extensions, you’ll need to trigger the same transition to which they were added and verify the results.

**Note**: it is generally recommended to perform testing in a non-Production environment. After testing is complete, you can **migrate your workflow** to your Production environment; see this page for steps on exporting and importing your workflow: <https://support.atlassian.com/jira-cloud-administration/docs/import-and-export-issue-workflows/>.

To publish your updated workflow:

1. Click **Settings** ⚙️ and select **Issues.**
2. In the left-hand panel, click **Workflows**.
3. For the workflow, click **Actions** [menu button icon] and select **Edit**.
4. At the top of the workflow editor, click **Publish Draft**.

With the workflow published, you should test it to verify that the new extensions execute successfully and that the outcome is expected.

![Publish Workflow](/cms_trial/assets/c19d70d2-ee5a-43f0-b7c1-819bd8216fc6.png)

### You’re done!

Now, when a sub-task is closed, Jira will check the parent issue to determine if it has any remaining sub-tasks that are open. If it does not, the parent issue will be closed!