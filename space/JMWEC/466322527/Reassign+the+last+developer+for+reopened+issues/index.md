# Reassign the last developer for reopened issues

| **Goal** | Reassign an issue to the last developer who worked on it. |
| --- | --- |
| **Scenario** | When an issue is reopened by a tester, it should be reassigned to the Developer who last worked on it. |
| **Components** | [Assign issue(s)](/cms_trial/space/JMWEC/1133772861/Assign+issue(s)/) post function |
| **Baseline** | - You have a role in your instance for Developers; in the example below the role is **Developer**. - Your workflow has a status of **Reopened**. |

**Note**: the steps below require your workflow has a status of **Reopened** (or something similar). Figure 1, below, shows the status **Reopened** with an incoming transition from **Done** and and outgoing transition to **In Progress**. Your transitions do not need to match, but you will need a status that represents reopening an issue *after* it has been closed.

## Requirements

- JIRA Administrator login
- [Jira Misc Workflow Extensions Cloud](https://marketplace.atlassian.com/apps/292/jira-misc-workflow-extensions-jmwe)

## 1. Project role for Developers

Verify that your Jira instance has a project role that includes the necessary developers. If that role does not exist, create one and add any necessary team members; see this page for more information: <https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/>.

## 2. Add the *Assign issue(s)* post function

1. Log in to your Jira instance as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Issues**.
3. In the left-hand sidebar, click **Workflows**.
4. From the list of Workflows, click **Actions** ( [menu button icon] ) for the appropriate workflow and select **Edit**.
5. Edit the transition:

   1. When viewing the Workflow in **Diagram** view (Figure 1, right), select the **Issue Reopened** transition (**Point 1**, **Figure 1**, right) and click the **Post Functions** link (**Point 2**, **Figure 1**, right). Click **Add post function** at the top of the list of existing post functions.
   2. When viewing the Workflow in **Text** view, click the **Issue Reopened** transition then select the **Post Functions** tab. Click **Add post function** at the top of the list of existing post functions.
   3. Select *Assign issue(s)* from the list of post-functions and click **Add** at the bottom of the list.

<need new screenshot>

## 3. Configure the post function

Set the following configurations (Figure 2, right):

1. **Issue(s) to operate on** - Set **Target issue(s)** to *Current Issue*.
2. **Assign to**:

   1. Set **Select user** to *Last role member*.
   2. Set **Project Role** to the role you created for Developers.
3. **Assignment behavior** - Set as needed; *Always* is recommended.
4. Under **Advanced options**, set the following as needed:

   1. **Run As** - Set as needed; it is recommended to leave the default *Add-on user* value unless required for specific reasons.
   2. **Run this post-function only if a condition is verified** - Set as needed. See [Conditional execution](/cms_trial/space/JMWEC/466256678/Conditional+Execution/) for more information.
   3. **Delay the execution of this post-function** - Set as needed.
5. Click **Add.**

## Save and Test the Workflow

Save your Workflow and publish the changes. To test that the post function is configured correctly, create a new issue and move it through your Workflow, assigning it to a QA or support person (any member who is not in the Developer role) before closing it. After closing it, reopen it by moving it to the **Reopened** status and verify that JMWE has correctly assigned it.

### 🎉 Congratulations!

Now, when a closed issue is reopened it will automatically be reassigned to the last member of the **Developers** project role to which it was assigned.

![JMWE for Jira Cloud post function configuration for reassigning last developer](/cms_trial/assets/8e1c8709-fdbb-42ab-8b7d-55fc50a0b670.png)