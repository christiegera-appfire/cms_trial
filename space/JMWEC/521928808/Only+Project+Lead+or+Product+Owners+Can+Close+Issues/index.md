# Only Project Lead or Product Owners Can Close Issues

## Scenario

In this scenario, a team is working on a major feature and for organizational purposes, only team leads are enabled to close out these types of issues. When the issue is ready to be closed, only the **Project Lead** or members of the group **Product Owners** should be able to mark it as **Done**.

## Resolution

This solution requires adding the [User Condition](/cms_trial/space/JMWEC/465474547/User+Condition/) extension to **every** transition that leads to the **Done** status. Once added, those transitions will only be available to users who are either a Project Lead or who are members of the Jira Group Product Owners, guaranteeing that only the appropriate team members can close an issue.

**Note**: The steps below require a Jira group to represent **Product Owners**. In this scenario, the Jira Project Lead and a Product Owner are two different people.

## Steps to create

### 1. Create a group for *Product Owners*

Verify that your Jira instance has a group that includes all team members who are Product Owners. If that group does not exist, create one and add the necessary team members; see this page for more information: <https://support.atlassian.com/jira-cloud-administration/docs/create-and-update-groups/>.

### 2. Add the *User Condition* condition

1. Log in to your Jira instance as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Issues**.
3. In the left-hand sidebar, click **Workflows**.
4. From the list of Workflows, click **Actions** ( [menu button icon] ) for the appropriate workflow and select **Edit**.
5. Edit the transition:

   1. When viewing the Workflow in **Diagram** view (Figure 1, right), select the Transition and click the **Conditions** link. Click **Add condition** at the top of the list of existing post functions.
   2. When viewing the Workflow in **Text** view, click the name of the Transition then select the **Condition** tab. Click **Add condition** at the top of the list of existing post functions.
   3. Select ***User Condition (JMWE app)*** from the list of conditions and click **Add**.

![JMWE for Jira Cloud transition editing for project lead and product owner restrictions](/cms_trial/assets/9e876fb1-2ab0-4828-a31d-89473cb81f3b.png)

### 3. Configure the condition

Set the following configurations (Figure 2, right):

1. **User(s) to check** - Set **Which user(s)** to *Current user*.
2. **Mode** - Set **User(s) must meet** to *at least one of the criteria configured below*.
3. **Criteria**

   1. **Groups** - Set to *Product Owners* (the group created in Step 1, above).
   2. **Condition for user(s)** - Enter the following Jira expression:   
      `user.accountId == issue.project.lead.accountId`
   3. Leave all other options blank
4. Click **Add.**

**Note:** When adding Conditions to a Jira Workflow, there is a native configuration for ‘**All of the following conditions’** or ‘**Any of the following conditions’**. You should set this as needed for your workflow.

![JMWE for Jira Cloud condition configuration for rolebased issue closing permissions](/cms_trial/assets/d5050085-606d-427b-be50-a34482d06647.png)

### 4. Repeat as needed

Repeat steps 2 and 3, above, for each of the transitions necessary. In this example, the User Condition is added to a total of three transitions - **Passed QA (above)**, **Client Approval**, and the **All** transition pointing to the **Done** status. You should add the condition as many times as necessary for your workflow.

### You’re done!

Now, only the **Project Lead** of an issue’s project, or a member of the **Product Owner** group, can mark an issue as **Done**.