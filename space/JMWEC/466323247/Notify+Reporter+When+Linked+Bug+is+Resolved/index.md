# Notify Reporter When Linked Bug is Resolved

## Scenario

A Support Team member creates an issue based on an incoming request; from that issue, a Bug is created. When the Bug is closed as Resolved, an email notification should be sent to the Support Team member assigned to the linked issue, notifying them that the Bug has been resolved.

## Resolution

This solution uses the [Email issue(s)](/cms_trial/space/JMWEC/466322658/Email+issue/) post-function with conditional execution to accomplish the needed outcome. When a issue with the type **Bug** is closed, the post-function refers back to any issue with a link type of “blocks” and sends an email notification to the assignee of that issue (or issues).

**Note**: the steps below are configured for Bugs that are linked to related issues using the link type **blocks**. Depending on your Jira configuration, it may be necessary to select a different link type.

## Steps to Create

### 1. Add *Email issue(s)* post-function

1. Log in to your Jira instance as an Administrator.
2. In the upper right corner of the window, click **Settings** ( ⚙️ ) and select **Issues**.
3. In the left-hand sidebar, click **Workflows**.
4. From the list of Workflows, click **Actions** ( [menu button icon] ) for the appropriate workflow and select **Edit**.
5. Edit the transition:

   1. When viewing the Workflow in **Diagram** view (Figure 1, right), select the Transition and click the **Post Functions** link. Click **Add post function** at the top of the list of existing post functions.
   2. When viewing the Workflow in **Text** view, click the name of the Transition then select the **Post Functions** tab. Click **Add post function** at the top of the list of existing post functions.
   3. Select ***Email issue(s) (JMWE app)*** from the list of post-functions and click **Add**.

![Edit Transition](/cms_trial/assets/acd17c17-e70e-4051-aa3e-d69c8232d65d.png)

### 2. Configure the post-function

Set the following configurations (Figure 2, right):

1. **Issue(s) to operate on** (**Point 1**, **Figure 2**, right)

   1. Set **Target issue(s)** to *Issues linked to the current issue through the following link type*.
   2. Set **Issue Link** to *blocks*.
2. **Email content** (**Point 2**, **Figure 2**, right)- Set the email fields as required; you can use Nunjucks templates to generate dynamic values. See the documentation for [Email issue(s)](/cms_trial/space/JMWEC/466322658/Email+issue/) for more information.
3. **Recipients** (**Point 3**, **Figure 2**, right) - Set **Issue members** to *Assignee*. Set any other recipients as needed.
4. **Run As** (**Point 4**, **Figure 2**, right) - Set as needed; it is recommended to leave the default *Add-on user* value unless required for specific reasons.
5. **Conditional execution** (**Point 5**, **Figure 2**, right)

   1. Check the box for **Run this post-function only if a condition is verified**.
   2. In the **Condition** field, enter `{{ issue.fields.issuetype.name == "Bug" }}`
6. **Delayed execution** (**Point 6**, **Figure 2**, right) - Set as needed.
7. Click **Add.**

## Configuration Options

The configuration of several options above, will depend on your organizational structure and on your specific process. For example:

- **Does the Support Team open issues?** The configuration of the **Recipient** field will vary depending on who opens an issue. If the Support Team member is the Reporter of the issue, you will need to set the **Recipient** field to *Reporter*.

![JMWE for Jira Cloud post function configuration for reporter notification workflows](/cms_trial/assets/3b385e05-70f9-4612-971b-42756288003a.png)

### 3. Publish and Verify

The last step is to publish your updated workflow and then test the new version to verify that the new extensions have been configured correctly. To test the extensions, you’ll need to trigger the same transition to which they were added and verify the results.

**Note**: it is generally recommended to perform testing in a non-Production environment. After testing is complete, you can **migrate your workflow** to your Production environment; see this page for steps on exporting and importing your workflow: <https://support.atlassian.com/jira-cloud-administration/docs/import-and-export-issue-workflows/>.

To publish your updated workflow:

1. Click **Settings** ⚙️ and select **Issues.**
2. In the left-hand panel, click **Workflows**.
3. For the workflow, click **Actions** [menu button icon] and select **Edit**.
4. At the top of the workflow editor, click **Publish Draft**.

With the workflow published, you should test it to verify that the new extensions execute successfully and that the outcome is expected.

![Publish Workflow](/cms_trial/assets/beb49aae-9164-4001-8da4-2c313b85d258.png)

### You’re done!

Now, when a closed issue is reopened it will automatically be reassigned to the last member of the **Developers** project role to which it was assigned.