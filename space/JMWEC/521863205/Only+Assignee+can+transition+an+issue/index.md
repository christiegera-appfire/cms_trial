# Only Assignee can transition an issue

## Scenario

When an issue has a status of **In Progress,** and is ready to move to the next stage, only the Assignee of the issue can move it to the next status.

## Resolution

This requires adding the [User Condition](/cms_trial/space/JMWEC/465474547/User+Condition/) extension to **every** transition that should be limited to just the issue's Assignee. Once added, those transitions will only be available to that one user, guaranteeing that only the appropriate person can advance an issue through its workflow.

**Note**: the steps below detail adding the User Condition to two transitions - from **In Progress** to **Code Review** and from **In Progress** to **To Test**. In this scenario, the developer assigned to the issue has completed work to the extent that it is ready for review or testing. You can, however, apply these same steps to any transition which should be limited in the user who can advance an issue to a specific status.

## Steps to create

### 1. Add the *User Condition* condition

1. Log in to your Jira instance as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Issues**.
3. In the left-hand sidebar, click **Workflows**.
4. From the list of Workflows, click **Actions** ( [menu button icon] ) for the appropriate workflow and select **Edit**.
5. Edit the transition:

   1. When viewing the Workflow in **Diagram** view (Figure 1, right), select the Transition and click the **Conditions** link. Click **Add condition** at the top of the list of existing post functions.
   2. When viewing the Workflow in **Text** view, click the name of the Transition then select the **Condition** tab. Click **Add condition** at the top of the list of existing post functions.
   3. Select ***User Condition (JMWE app)*** from the list of conditions and click **Add**.

![JMWE for Jira Cloud transition editing interface for assigneeonly workflow restrictions](/cms_trial/assets/b8b3f00d-1e2a-4ec6-a18e-3fb2f75f624e.png)

### 2. Configure the condition

Set the following configurations (Figure 2, right):

1. **User(s) to check** - Set **Which user(s)** to *Current user*.
2. **Mode** - Set **User(s) must meet** to *all the criteria configured below*.
3. **Criteria**

   1. **The user is** - Set to *the Assignee*.
   2. Leave all other options blank
4. Click **Add.**

**Note:** When adding Conditions to a Jira Workflow, there is a native configuration for ‘**All of the following conditions’** or ‘**Any of the following conditions’**. You should set this as needed for your workflow.

![JMWE for Jira Cloud condition configuration for assigneebased transition control](/cms_trial/assets/4a1dff37-74f6-4ccc-8f54-6a5c67e6c9dd.png)

### 3. Repeat as needed

Repeat steps 2 and 3 for each necessary transition. In this example, the User Condition is added to two transitions - **Ready to Test** and **Technical Review**. Add the condition as many times as necessary for your workflow.

### You’re done!

Now, only the Assignee of an issue can move the issue out of the **In Progress** status.