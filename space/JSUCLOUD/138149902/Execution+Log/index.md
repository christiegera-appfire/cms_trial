# Execution Log

The Execution Log is a JSU report that shows you the results of all your JSU workflow rule executions. This helps you determine which rules are adding value to your team and which rules are resulting in errors and not delivering the results you expected.

Whenever a JSU rule runs, an execution event is recorded, and a unique Log ID is assigned. The Execution Log displays the result, when the rule was executed, the rule name, and the Performed As user. You won’t see results for Jira automation or rules created with other third-party apps.

Execution results are retained and accessible from the Execution Log for 90 days; the app automatically deletes results older than this.

**To view the Execution Log:**

On the global navigation bar in JSU, select **Reporting** > **Execution Log**. You can also quickly navigate to a specific rule execution from the execution history in [My Workflows](/cms_trial/space/JSUCLOUD/12519535/My+Workflows/).

![Example Execution Log displaying successes and failures.](/cms_trial/assets/8c9e1403-8b76-4c11-a773-34236a4ace0b.png)

### Result details

The *Result* column shows whether the rule executed successfully or if it encountered errors. You can expand a specific result to view details about updated issues, possible solutions for errors, and the Log ID. See [Guide to Error Messages](https://appfire.atlassian.net/l/cp/RJYWN3tC) for more information on specific error messages.

#### Success

![Example Success message from the Execution Log.](/cms_trial/assets/b4e0c2b1-0598-410c-9db3-4d20e0fccd4f.png)

#### Failure

![contentId-138149902](/cms_trial/assets/1f9d4135-33a7-4c7f-b33e-3bceb1963196.png)

### Filter results

The default log view lists all rule executions with the most recent event at the top. You can refine this list to display only a specific result, Performed As user, or select a specific date range. You can use one or more filters to display the desired results. The date range is set to the previous 30 days by default.

In the example below, the filters are set to display all failures executed between 6 February and 9 February, 2023.

![The Execution Log filters set as described on this page.](/cms_trial/assets/da7f21a6-3bec-4407-8c78-fd1388fe326e.png)

If you want to see visual feedback when a rule is triggered and when the execution is complete, you can enable the [Execution Messages](/cms_trial/space/JSUCLOUD/12519472/Navigation+basics/) option in your JSU settings. This is useful when you are getting started with JSU or when testing your rules before making changes to a production instance. This option is available to Jira admins.

## Related pages

[My Workflows](/cms_trial/space/JSUCLOUD/12519535/My+Workflows/)

<https://appfire.atlassian.net/l/cp/RJYWN3tC>