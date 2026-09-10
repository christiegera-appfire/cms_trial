# Navigation basics

You can use the following options to access JSU from your Jira instance:

## Global navigation

The global navigation bar is displayed at the top of our *Get Started*, *My Workflows*, *Reporting*, and *Settings* pages. If you are already familiar with JSU for Jira Cloud, you will see that it is now quicker to access these pages without navigating via your Admin *Settings* menu. A *Resources* menu ([png icon]) provides access to our support portal and JSU user documentation.

![contentId-12519472](/cms_trial/assets/11b6b887-87c7-4b20-a20a-af39467e008b.png)

### **Get Started**

Our *Get Started* page is your default entry page for the app. Click **Create rule** to quickly go to the workflow you want to customize. *Get Started* also provides interactive use case examples and links to our user documentation, migration guide, and support portal.

![Screenshot of the JSU Get Started page.](/cms_trial/assets/c903fc7f-2229-47b9-a6cc-51abbc2dad81.png)

### My Workflows

[*My Workflows*](/cms_trial/space/JSUCLOUD/12519535/My+Workflows/) is a single-page overview of your saved JSU rules where you can quickly see how JSU has been implemented across your entire instance. Click **Create new rule** to start creating a rule from this page.

### Reporting

The *Reporting* menu provides access to the [Execution Log](/cms_trial/space/JSUCLOUD/138149902/Execution+Log/) and your [JSU migration reports](/cms_trial/space/JSUCLOUD/710181330/JSU+migration+reports/). Space admins for team-managed spaces won’t have access to migration reports.

### **Settings**

The *Settings* page is where Jira admins can configure the JSU options:

![Screenshot of the Settings page in JSU Cloud.](/cms_trial/assets/11e05d58-52a6-4b01-8751-d6fc452276a0.png)

- **Show Hints & Tips**: Enabled by default, this option displays contextual hints and tips throughout the app to help you onboard faster and make informed decisions. If you need a visual clue when using a feature, click **Show Me**.

  ![An example of JSU's Hints and Tips as shown in a draft workflow.](/cms_trial/assets/006e9f6f-1957-49a0-95c3-0d7fc5927978.png)

  To hide Hints & Tips, turn off the **Hints & Tips** toggle.

- **Execution messages:**This option is enabled by default for evaluation licenses to help you see when a JSU rule is triggered and when the execution is complete. Pop-up messages are displayed when viewing the work item that triggered the rule. Messages are displayed only to Jira administrators who have triggered the rule. If there are multiple rules executed within the same time frame, a summary message is displayed.

  ![An example of the execution message displayed when a rule is first executed.](/cms_trial/assets/354f6d0e-f696-402b-b897-9617d0b925a8.png)
- **Email notifications**: The JSU product team would like to keep you informed of new features, security notifications, and occasional feedback requests. Off by default, this option lets you opt in or out of receiving emails from the team.
- **Initiating user falls back to app user**: This global option lets you set the behaviour for JSU run-as-user when a post function fails due to a permission error. If this option is selected, JSU will run the post function using the JSU App User as a fallback user. The original initiating user is displayed in the *Execution Log* page. See [Perform As User](https://appfire.atlassian.net/wiki/x/eAW-/) to learn more.

## JSU menu button

The **JSU** menu button is available from your Agile space boards. To edit a workflow for the current space, click the **More actions** ellipses, then select **JSU** > **Edit workflow**.

## Jira Apps menu

You can also use the *Apps* menu in the left sidebar in Jira to display JSU’s app menu.

![Screenshot of Jira's Apps menu with JSU's Get Started page selected.](/cms_trial/assets/147c38dc-3fee-4de9-a9d1-35d684101e51.png)