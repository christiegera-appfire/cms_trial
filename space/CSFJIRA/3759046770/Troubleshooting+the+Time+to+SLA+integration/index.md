# Troubleshooting the Time to SLA integration

If SLAs do not show on a Salesforce record, check the token, the integration, and the Salesforce record page, in that order.

## 1. Token (Jira / Connector)

1. In Jira, go to **Apps** > **Connector for Salesforce and Jira** > **Menu** > **App settings** > **Integrations**.
2. Confirm the token status is **ACTIVE**.
3. Confirm the base URL region matches your Time to SLA instance.
4. Confirm the integration is enabled.

   ![image-20261015-090838.png](/cms_trial/assets/969013c1-689e-4115-9d96-d47171548b74.png)

## 2. Integration (Jira / Connector)

- The integration exists in the list with the right connection and Time to SLA scope.
- The entity pair is mapped (for example, Task with Case). Unmapped entities never sync.

## 3. Record page (Salesforce)

- In Lightning App Builder, both **Time to SLA for Jira** and **Jira Issue** components are on the page, and the page is saved with **Activation**.
- The record is associated with a Jira work item that already has SLAs, with automatic pull enabled. Refresh the page afterward.

## Broken token

Signs: status is not **ACTIVE**, or SLAs stopped updating everywhere at once. Likely causes: the token was deleted or regenerated in Time to SLA, was pasted incorrectly, or the region is wrong.

Fix:

1. In Time to SLA, go to **Administration** > **SLAs in Salesforce** and click **+ Token**. Click **Copy and close**.
2. In Connector, open **Integrations** and click **Add Token**.
3. Select the matching region, paste the token, and click **Save**.
4. Wait for **ACTIVE**. The token is shared across the tenant, so this fixes every integration.

## Integration is disabled

If the token is set up but the Status under Connector for Salesforce & Jira Intergations is NOT CONNECTED, the TTS integration is disabled.

![image-20261015-091048.png](/cms_trial/assets/8e2d0950-28fd-417c-811b-750ddfca63c9.png)

Fix:

1. In Time to SLA, go to **Administration** > **Integrations**.
2. Enable the integration.

![image-20261015-091600.png](/cms_trial/assets/6dda5416-daf3-4bf8-80c6-a86acfdde214.png)

Contact support with the integration name, scope, Salesforce URL, Jira work item key, token status, and region.

## Related pages

- [Set up Time to SLA integration](/cms_trial/space/CSFJIRA/3672277145/Set+up+Time+to+SLA+integration/)
- [Integrate Salesforce and Jira for SLA management](/cms_trial/space/CSFJIRA/3688857603/Integrate+Salesforce+and+Jira+for+SLA+management/)