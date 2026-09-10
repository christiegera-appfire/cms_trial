# Nunjucks Template Tester

JMWE includes a tool for testing Nunjucks templates; with this tool, a template can be built and tested before adding it to a post-function configuration. The main advantage of this tool is that templates can be tested and debugged quickly, and changes can be made without having to actually trigger a transition and/or look at the JMWE logs to see the result.

The tool is available through the *JIRA MISC WORKFLOW EXTENSIONS* section of Jira App Administration. To access the Nunjucks Template Tester:

1. In Jira, click the **Settings** icon ⚙️ in the upper right corner of the page and select **Apps**.
2. In the left-hand panel, click **Nunjucks and Jira expression tester** under the **Jira Misc Workflow** Extensions section.
3. Under **Type** select **Nunjucks script**.

![JMWE for Jira Cloud Nunjucks template tester with validation and testing tools](/cms_trial/assets/95fda9cc-2df6-4413-ad47-dd1a1e28da42.png)

## Using the Tester

When testing a Nunjucks template, if the test should access only a specific type of linked issue, please be sure to select that issue type in the **Issue Link Type** pulldown below the editor. The default value for this field is *Any*, meaning the test will run against any linked issues.

![JMWE for Jira Cloud Nunjucks template test confirmation dialog with results](/cms_trial/assets/6d352690-a466-45f2-8861-33e6935f0d06.png)

After entering a Nunjucks template in the editor, click **Test Nunjucks template** in the upper right of the editor. A window will open (pictured right); from this window, select an issue to run the template against and, where applicable, select a linked issue. Any `issue` and `linkedIssue` variables used in the template will refer to these issues.

In post-functions that process linked issues, after an issue is selected, all issues linked to it through the link type selected in **Issue Link Type** are displayed under **Linked issue key**. The `linkedIssue` variable used in the template will point to the linked issue.

In the post-functions that process the parent issue, after an issue is selected, its parent is displayed under **Parent issue key**. The `parentIssue` variable used in the template will point to the parent issue.

The `transition` variable will not reflect any transition information during testing.

## Test Results

After selecting an issue against which the template should be tested, click **Test**. The template will run against the selected issue and the following information will be displayed:

1. **Message**: Success/error message based on the test result.
2. **Result value**: Value of the result.

This information can be used for debugging.