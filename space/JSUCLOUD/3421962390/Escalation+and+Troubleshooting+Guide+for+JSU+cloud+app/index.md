# Escalation and Troubleshooting Guide for JSU cloud app

Welcome! This guide is designed to help L1 and L2 support teams efficiently troubleshoot issues with **JSU Automation Suite for Jira Workflows** before escalating them to L3. Following these steps helps us resolve customer issues much faster.

## Step 1: Check Past Ticket History

Before digging deeper, please check if we have already solved a similar issue in the past.

You can search Jira using this **JQL query** (just replace `rate limit` with the keyword that best describes the customer's problem):

```text
project = "One Appfire Support" AND "App Name[Dropdown]" = "JSU Automation Suite for Jira Workflows" AND text ~ "rate limit"
```

## Step 2: Search AWS CloudWatch Logs

If the history search doesn't help, please look for relevant system errors in AWS.

1. Log into the AWS account: **Appfire Beecom (Prod)**.
2. Navigate to **CloudWatch** -> **Log Management**.
3. Select the log group: `prod.jsucloud.io` and click **View in Log Insights**.
4. Run the following search query:

```text
SOURCE "arn:aws:logs:us-east-2:949069865269:log-group:prod.jsucloud.io" START=-2592000s END=0s |
fields @timestamp, @message
| filter @message like /WOSCHINGFW-38664/
| limit 100
```

💡 **Note:** Replace `WOSCHINGFW-38664` in the query with the specific **issue key** that triggered the post-function error during the workflow transition.

## Step 3: Reproduce and Handle the Issue

Depending on what you find during your investigation, please follow the appropriate path below:

### A. If you CAN reproduce the error (It is a Bug)

- Please **confirm with L3 engineer to have a look and they will answer if a bug ticket on our Development Board needed**.
- Our product managers will review it, check the priorities, and schedule the fix.

### B. If you CANNOT reproduce the error (Potential Misconfiguration)

If everything works fine on your end, the customer might have a configuration issue. Please suggest these best practices to the customer:

- **Test in a new project:** Ask the customer to create a brand-new test project and try the post-function there. Sometimes, different Jira admins accidentally overwrite each other’s configurations.
- **Simplify the configuration:** If the post-function uses multiple fields, ask them to test it with just one simple field first. If it works, they can add fields back one by one to find exactly which field is causing the failure.

### C. If it is a Feature Request

- Create a ticket on our **Development Board** to log the request.
- Reply politely to the customer to let them know we have recorded their feedback.
- **If the customer asks for an ETA:** Please reach out to our Project Manager, **Weronika**, directly. She has the best visibility into our team's current capacity and priorities.

Thank you for your hard work and dedication to providing top-quality support for our users! If you have any questions about this process, please reach out to the L3 team.