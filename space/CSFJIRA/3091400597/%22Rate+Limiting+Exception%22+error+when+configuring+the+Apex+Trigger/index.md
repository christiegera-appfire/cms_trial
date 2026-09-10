# "Rate Limiting Exception" error when configuring the Apex Trigger

## Summary

When configuring the Apex Trigger for the connectors, it throws the following error when it is executed:

```text
OpportunityTrigger: execution of AfterUpdate caused by: System.AsyncException: Rate Limiting Exception : AsyncApexExecutions Limit exceeded. (JCFS) Trigger.OpportunityTrigger: line 37, column 1
```

## Environment

- Jira Cloud
- Jira Data Center

## Diagnostics Steps

Check the Salesforce rate limit that is currently configured with the following steps:

1. Access the [Salesforce Workbench](https://workbench.developerforce.com/login.php) site.
2. Ensure the correct Salesforce instance is chosen.
3. Navigate to **Utilities > REST Explorer**.
4. At the end of the URL of the webpage, add the following:

   ```text
   /limits
   ```
5. Expand the **DailyAsyncApexExecutions** section to check how many remaining executions are available today.

![contentId-3091400597](/cms_trial/assets/6cfbe65a-a231-49b7-ac85-32ee23a99c65.png)

## Cause

The error is triggered due to the Apex execution surpassing the daily Apex Trigger execution limit.

## Workaround

- N/A

## Resolution

After running the steps in the Diagnostic Steps section above, check with your Salesforce Administrator on the possibility of increasing the daily execution limit.

For more information, refer to the [Execution Governors and Limits](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_gov_limits.htm) documentation.