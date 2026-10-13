# Use SLA actions with Jira automation

The Trigger a Jira automation rule feature lets you use your SLA notifications to trigger Jira automation rules. For example, when an SLA is breached, you can automatically trigger a Jira automation rule to perform actions like adding comments to work items or creating incident reports.

This document provides step-by-step instructions on how to set up the integration between your Time to SLA notifications and Jira automation.

## Step 1: Create a Jira automation rule

Follow these instructions to create a Jira automation rule. For further details, refer to the [Atlassian documentation](https://support.atlassian.com/cloud-automation/docs/jira-automation-triggers/#Incoming-webhook).

Atlassian [is updating](https://community.atlassian.com/t5/Automation-articles/Update-on-Incoming-Webhooks-Trigger-for-Atlassian-Automation/ba-p/2921233) how incoming webhook triggers are routed. Any automation rules created before January 28, 2025, will continue to work until May 30, 2025, but must be migrated to the new endpoint to remain functional beyond this date. If you use incoming webhooks in your automation rules, we strongly recommend reviewing and updating them as needed.

1. Open the Jira space where you want to apply the rule.
2. Go to **Space settings** from the side menu.
3. Select **Automation** and click **Create rule** > **Create from scratch**.

   ![Time to SLA Jira automation notification rule configuration](/cms_trial/assets/e4335b00-2a24-4434-92d3-45319821ed8e.png)
4. Choose the **Integrations** category, then select **Incoming webhook as the trigger**.

   ![Time to SLA Jira automation notification webhook settings](/cms_trial/assets/961635be-6514-45aa-99bb-d5f163a84196.png)
5. Click **Next** and configure your needed actions. You can add multiple actions, such as sending comments, assigning work items, creating incidents, and more.

Time to SLA provides various smart values to customize your actions dynamically. You can use:

```text
slaDescription: {{webhookData.slaDescription}}
slaValue: {{webhookData.slaValue}}
slaStartDate: {{webhookData.slaStartDate}}
slaTargetDate: {{webhookData.slaTargetDate}}
originStatus: {{webhookData.originStatus}}
targetStatus: {{webhookData.targetStatus}}
startConditions: {{webhookData.startConditions}}
endConditions: {{webhookData.endConditions}}
remainingDuration: {{webhookData.remainingDuration}}
overdueDuration: {{webhookData.overdueDuration}}
elapsedDuration: {{webhookData.elapsedDuration}}
pausedDuration: {{webhookData.pausedDuration}}
elapsedPercentage: {{webhookData.elapsedPercentage}}
```

1. Once you’re satisfied with your rule, click **Turn on rule**.
2. Jira will generate a unique webhook URL and a secret. Copy and save them for later.

   ![Time to SLA Jira automation rule with SLA notification trigger](/cms_trial/assets/f9492e70-d1fc-4273-9cde-2e8d62993b31.png)
3. Ensure the **Issues provided in the webhook HTTP POST body** option is selected.

In this example, we have set up a rule to send a comment utilizing parameters when it's triggered:

![Time to SLA Jira automation action configuration dialog](/cms_trial/assets/9e34da05-ec94-4dce-ac89-948327f3c95c.png)

## Step 2: Create a TTS notification

Next, configure a Time to SLA notification to link with your Jira automation rule.

1. Navigate to the SLA for which you want to add the notification.
2. Open the SLA’s settings, and click **Manage notifiers**.
3. Create a new notification by clicking **Add New SLA Notification**. If you don’t know how, follow the instructions on [this page](/cms_trial/space/TTSC/35881090/Actions/).
4. For *When triggered...*, select **Trigger a Jira automation rule** as the action.
5. Paste the **Automation Webhook URL** and **Automation Webhook Secret** copied in [Step 1.7](/cms_trial/space/TTSC/1464075666/Use+SLA+actions+with+Jira+automation/).

   ![Time to SLA Jira automation field mapping dialog](/cms_trial/assets/f93b4b0d-c0cb-45bb-a5c3-32e6a4422be4.png)
6. Click **Save** to finish the setup.

Now, when the SLA is breached, the Jira automation rule will be triggered, executing the configured action (for example, `Add comment to work item`):

![Time to SLA Jira automation release note image showing rule configuration](/cms_trial/assets/b72075c8-c18e-48d7-a76e-fa584a521e0a.png)

## Jira automation usage limits

Time to SLA will attempt to trigger Jira Automation based on your configuration. However, remember that Jira automation may have usage limits or restrictions. If the automation does not trigger as expected:

- Refer to the [Jira automation documentation](https://support.atlassian.com/cloud-automation/docs/jira-automation-triggers/#Incoming-webhook) and [Automation service limits](https://support.atlassian.com/cloud-automation/docs/automation-service-limits/) to check for potential usage limits.
- Check your usage by opening the **Space settings**, and navigating to **Automation** > **Usage**.

**Automation not triggering?**

If your Jira automation rule isn’t triggered by an SLA notification, this may be related to IP allowlisting in Jira Cloud. For more information, refer to our [FAQ](/cms_trial/space/TTSC/34932181/FAQ%3A+SLAs/).