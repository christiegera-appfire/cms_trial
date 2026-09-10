# Reopen issue when new Bug is linked

| **Goal** | Automatically reopen a closed issue when a new issue - of a specific type - is linked to it. |
| --- | --- |
| **Scenario** | When a new Bug is created for an existing feature, you want to automatically reopen the issue for that feature. The new Bug is linked to the existing issue, and you want JMWE to reopen the issue. Additionally, you want to add a comment indicating why the issue was reopened and copy fields from the original issue to the new Bug. |
| **Components** | [Transition issue(s)](/cms_trial/space/JMWEC/465242612/Transition+issue(s)/) post function, [Copy issue fields](/cms_trial/space/JMWEC/466323304/Copy+issue+fields/) post function |
| **Baseline** | - The workflow includes a **Closed** status and a **Reopened** status (or similar values, see below). - Bugs must be linked to the issue that needs to be reopened. - Bugs are initially only linked to the issue for their associated feature. |

**Note**: the steps below require your workflow to have two specific status values:

- **Closed** (for example, work that is complete but is pre-release or support tickets that have a window for customers to reopen)
- **Reopened** (or something similar)

Figure 1, below, shows these status values at the end of the workflow: **Closed** is used for work that is complete but is not fully Done, and **Reopened** with an incoming transition from **Closed** and and outgoing transition to **In Progress**. Your transitions do not need to match, but you will need either:

- A status that represents issues that are complete, but are not **Done**   
  and
- A status that represents reopening an issue *after* it has been completed or
- A transition from **Closed** to **Backlog** or
- Your **Backlog** status configured to enable *Allow all statuses to transition to this one*.

## Requirements

- JIRA Administrator login
- [Jira Misc Workflow Extensions Cloud](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe)

## 1. Add the *Transition issue(s)* post function

1. Log in to your Jira instance as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Issues**.
3. In the left-hand sidebar, click **Workflows**.
4. From the list of Workflows, click **Actions** ( [menu button icon] ) for the appropriate workflow and select **Edit**.
5. Switch to **Diagram** view if you are not already using it.
6. Select the Create transition (**Point 1**, **Figure 1**, right).
7. Click the **Post Functions** link (**Point 2**, **Figure 1**, right).
8. Click **Add post function** at the top of the list of existing post functions.
9. Select **Transition issue(s)** from the list of post functions and click **Add** at the bottom of the list.

![Workflow Editor Select Transition](/cms_trial/assets/47605213-ff9a-42fe-b40b-46a696f3c1e5.png)

## 3. Configure the post function

**Note**: Leave all fields to their default values unless specified below!

1. For **Target issues**,select *Issues linked to the current issue through the following link type* (**Point 1**, **Figure 2**, right).
2. For **Issue link**, select *relates to* (**Point 2**, **Figure 2**, right).
3. Click the **Transition Picker** button to select a Transition (**Point 3**, **Figure 2**, right).
4. In the *Pick a transition* window:

   1. Select your workflow from the **Workflow name** pulldown menu.
   2. Select the transition between **Done** and **Reopened** (e.g. *Issue Reopened*).
   3. Click **Use transition ID**.
5. Click **Advanced options** and then click **Transition screen**.
6. Check the box for **Add Comment** (**Point 4**, **Figure 2**, right).
7. For the **Comment** field, enter the following script (**Point 5**, **Figure 2**, right):

   ```text
   This issue has been reopened due to: 
   Bug {{ issue.fields.issuekey }} ({{ issue.fields.summary }}).
   ```
8. Click **Settings**.
9. Check the box for **Run this post-function only if a condition is verified** (**Point 6**, **Figure 2**, right).
10. In the **Write a script** editor, enter the following script (**Point 7**, **Figure 2**, right):

    ```text
    {{ issue.fields.issuetype.name == "Bug" }}
    ```
11. Click **Add** (**Point 8**, **Figure 2**, right).

### Link Type Configuration

The configuration above uses a combination of factors to determine which issue should be reopened:

1. The link type **relates to**.
2. Conditional execution of the post function only for issues of the type **Bug**.

Your team may use a different link type to relate Bugs. Select the link type that is appropriate to your Jira instance!

![Transition Issue post function configuration screen](/cms_trial/assets/5936de9f-3ddd-4e42-8424-e698e44607a3.png)

## 4. Add the *Copy issue fields* post function

Lastly, we need to add the [Copy issue fields](/cms_trial/space/JMWEC/466323304/Copy+issue+fields/) post function to the **Create** transition; this post function can run at any point during the Create transition because there are no dependencies between this post function and the **Transition issue(s)** post function from Step 3. The **Copy issue fields** post function will copy three field values from the feature issue to the Bug:

- **Fix version** from the feature issue will be copied to **Affects versions** on the Bug
- **Assignee** and **Watchers** from the feature issue will be copied to **Watchers** on the Bug, ensuring that notifications on the new Bug will be sent appropriately

1. Back in your Workflow Editor, verify that you are still working on the **Create** transition.
2. Select the **Post Functions** tab and click **Add post function**.
3. Select **Copy issue fields** from the list of post functions and click **Add** at the bottom of the list.
4. For **Source issue(s)**,select *Issues linked to the current issue through the following link type* (**Point 1**, **Figure 3**, right).
5. For **Issue link**, select *relates to* (**Point 2**, **Figure 3**, right).
6. Under **Fields to copy,** click **Add** (**Point 3**, **Figure 3**, right) and use the values in the table below.

| **Field** | **From** | **Additional options** |
| --- | --- | --- |
| Affects versions | Fix versions | - Set only if field is empty |
| Watchers | Assignee | - Append value(s) to the field |
| Watchers | Watchers | - Append value(s) to the field |

1. Repeat Step 6 for each field listed. Your configuration of **Fields to copy** should match Figure 3, right.
2. Click **Advanced options > Settings**.
3. Check the box for **Run this post-function only if a condition is verified** (**Point 4**, **Figure 3**, right).
4. Enter the following script in **Write a script** (**Point 5**, **Figure 3**, right):

   ```text
   {{ issue.fields.issuetype.name == "Bug" }}
   ```
5. Check the box for **Allow Jira to send notifications for this change** (**Point 6**, **Figure 3**, right).
6. Click **Add** (**Point 7**, **Figure 3**, right).

### Alternate Configuration

<mention that this might need to be moved to a different transition, in which case the conditional execution needs updating>

## Save and Test the Workflow

Save your Workflow and publish the changes. To test that the post function is configured correctly, create a new Bug and link it to any issue that is closed. Verify that the closed issue is moved to the appropriate status and that the field values from the closed issue have been copied to the Bug.

### 🎉 Congratulations!

The creation of a new Bug will now reopen closed issues (but won’t affect issues in any other status), key values from the closed issue will be copied if needed, and any team member involved in work on the closed issue will be notified of the new Bug!

![Copy Issue Fields post function configuration screen](/cms_trial/assets/c2d88fff-ea1a-4429-bbe0-72953886c052.png)