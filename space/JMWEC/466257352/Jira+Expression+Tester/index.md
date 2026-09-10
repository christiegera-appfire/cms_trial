# Jira Expression Tester

**JMWE for Jira Cloud** includes a tool for testing Jira expressions; with this tool, an expression can be built and verified before adding it to a condition or validator configuration. The main advantage of this tool is that expressions can be built and debugged quickly, and changes can be made without having to actually trigger a transition and/or look at the JMWE logs to see the result.

The expression tester is available through the *JIRA MISC WORKFLOW EXTENSIONS* section of Jira App Administration. To access the Jira expression tester:

1. In Jira, click the **Settings** icon ⚙️ in the upper right corner of the page and select **Apps**.
2. In the left-hand panel, under *JIRA MISC WORKFLOW EXTENSIONS*, click **Nunjucks and Jira expression tester**.
3. Under **Type** select **Jira expression**.

![JMWE for Jira Cloud Jira expression tester with expanded testing interface](/cms_trial/assets/193420f9-e96f-49d0-859f-c50f2d02ab1e.png)

## Using the Tester

The **transition** variable will not reflect transition information during testing.

After writing your Jira expressions script in the editor, click **Test Jira expression** in the upper right corner of the editor. A window will open; from this window, select an issue against which to run the Jira expression. Any `issue` variable used in your script will point to this issue.

## Test Results

After selecting the issue against which the script should be tested, click on `Test.`The following information will be displayed. This information can be used for debugging.

1. **Message**: Success/error message based on the test result.
2. **Result value**: Value of the result.

This information can be used for debugging.