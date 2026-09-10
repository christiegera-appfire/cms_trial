# Move parent to 'Done' when all child issues are closed

| **Goal** | Automatically close a Parent issue when all of its Child issues are closed. |
| --- | --- |
| **Scenario** | You want to automatically close a Parent issue (e.g. Epic with Stories or Stories and Tasks with sub-tasks) when all of the child issues have been closed because all work for the Parent has been completed. |
| **Components** | [Event-based Action](/cms_trial/space/JMWEC/465473524/Event-based+actions/): Issue transitioned event, [Transition issue(s)](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/) post function |
| **Baseline** | - The Parent issue and all Children issues share the same Workflow. - Your workflow enables issues to move to **Done** from any other status. |

In these scenarios, some examples of the Parent-Child relationship are:

- Jira Software “Parent/Sub-task”
- Jira Software “Epic/Story”
- Advanced Roadmaps (Portfolio) “Parent link”
- Issues connected through the links available in “Issue Linking”

---

## Requirements

- JIRA Administrator login
- [Jira Misc Workflow Extensions Cloud](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe)

## Workflow configuration

Only one transition is addressed in this Use Case - the transition from any status to **Done**; however, the same steps could be used on nearly any transition.

Nearly any scenario can be addressed where both:

- The Parent issue status needs to match the status of the Child(ren) issue(s) AND
- All Children issues have been transitioned to the destination issue (e.g. all children issues have been moved to **Testing** or moved to **Client Review**).

## 1. Create the Event-based Action

1. Log into your instance as an administrator.
2. Click on the **Settings** icon ⚙️ in the upper right corner.
3. Select **Apps**.
4. In the left-hand panel under *JIRA MISC WORKFLOW EXTENSIONS,* click **Event-based actions** and click **Create new action** in the upper right corner.
5. Give your Event-based action a name and, optionally, a description.
6. Under **WHEN**, make sure **Select Event** is selected. In the right-hand panel, select **Issue Transitioned** (**Figure 1**, right).
7. The *Issue Transitioned* configuration window will open (**Figure 2**, right). For **To status**, select *Done* and click **Save**.
8. Under **IF SCOPE**, select the projects and/or issue types that should trigger the Event-based option. If the post functions should be run for all projects and/or all issue types, leave the values as `Any`, as appropriate.

![Event-based Action Select Event](/cms_trial/assets/29412cf6-4c0b-481a-b49e-b102a5c72bfd.png)![Issue Transitioned configuration](/cms_trial/assets/0da545c2-4cf7-4dda-93bb-e7b6c50bb2f6.png)

## 2. Add the *Transition issue(s)* post-function

1. Under **THEN**, click **Select Post-functions**.
2. In the right-hand panel, select **Transition issue(s)** in the list of post functions. The [Transition issue(s)](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/) configuration screen will open.
3. For **Target issues**, select *Parent issue of the current sub-task* (**Point 1**, **Figure 3**, right)*.*
4. Click the **Transition Picker** button to select a Transition (**Point 2**, **Figure 3**, right).
5. In the *Pick a transition* window:

   1. Select your workflow from the **Workflow name** pulldown menu.
   2. Select the transition for moving issues into the **Done** status.
   3. Click **Use transition name**.
6. Click **Expand all** at the bottom right.
7. Check the box for **Run this post-function only if a condition is verified**.
8. In the script editor, enter the following (**Point 3**, **Figure 3**, right):

   ```text
   {% set subs = targetIssue | subtasks %}
   {% set trigger = true %}
   {% for sub in subs %}
   	{% if sub.fields.status.name != "Done" %}
   		{% set trigger = false %}
   	{% endif %}
   {% endfor %}
   {{ trigger }}
   ```
9. Click **Save** to save your post function configuration (**Point 4**, **Figure 3**, right).

## Save and Test the Action

In the main Event-based Action editor, click **Save** to complete the configuration. To test the new action, create a new issue with at least two sub-tasks. Then move the sub-tasks through your workflow until they are all in the **Done** status. Verify that JMWE moves the Parent issue to **Done**.

### Congratulations!

![Transition Issue configuration screen](/cms_trial/assets/8775c170-f429-45fe-a3f5-02944647aeba.png)