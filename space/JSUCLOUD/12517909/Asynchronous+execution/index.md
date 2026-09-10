# Asynchronous execution

There is a fundamental difference between Jira Data Center and Jira Cloud in reference to post functions: In Jira Cloud, post functions of apps are executed **asynchronously** as a *background job*. This means a post function will be executed after the transition has been completed on Jira Cloud.

Note the following behaviors of the asynchronous execution:

- If you are using multiple post functions, there is no guaranteed order in which they are performed. They might be executed in a different order from the one you set up in Jira's workflow configuration. Therefore, you cannot rely on any result of a previous post function. Also, the order in which the post functions are executed might be different every time the transition is performed.
- If a post function encounters a problem (due to misconfiguration or the current data of a Jira work item), the transition (and all other post functions) will be performed regardless of the problem.
- The result of a post function might not be visible immediately in the browser.
- Configured error messages for Conditions and Validators display to the user as expected; errors encountered during the execution of an Action will not necessarily display an error message.