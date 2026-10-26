# Integrate Salesforce and Jira for SLA management

## Overview

When support teams use Salesforce and engineering teams use Jira, critical deadlines can easily get lost. This guide walks you through setting up a seamless integration between Salesforce and Jira using the Connector for Salesforce & Jira app, integrated with Time to SLA, to ensure both teams always know the SLA deadlines, regardless of which tool they're working in.

## Benefits

- Both teams see critical deadlines in their own tools without switching platforms.
- Salesforce records and Jira work items sync automatically.
- You can create Jira work items directly from Salesforce.

## Before you start

Make sure you have:

- Jira administrator access on the Jira instance with Connector for Salesforce & Jira.
- Salesforce administrator access to edit record pages
- [Set up a connection to Salesforce in Jira.](/cms_trial/space/CSFJIRA/1873379599/Set+up+a+connection+to+Salesforce+(Jira+Cloud)/)
- [Set up a connection to Jira in Salesforce](/cms_trial/space/CSFJIRA/1873346949/Set+up+a+connection+to+Jira/).
- [Installed the Time to SLA app.](https://appfire.atlassian.net/wiki/spaces/TTSC/pages/35684371)
- [Connected your Time to SLA token](/cms_trial/space/CSFJIRA/3672277145/Set+up+Time+to+SLA+integration/) and [Created an integration](/cms_trial/space/CSFJIRA/3672277145/Set+up+Time+to+SLA+integration/)
- [Added the SLA component to a Salesforce record page](/cms_trial/space/CSFJIRA/3672277145/Set+up+Time+to+SLA+integration/)
- [Entity and field mapping configured in Connector for Salesforce and Jira](/cms_trial/space/CSFJIRA/3664152459/Configure+entity+and+field+mappings+from+templates/) for **Bug ↔ Case** entity mapping (following the Bug escalation template).

## Steps

### Create SLAs in Time to SLA

For this use case, we’ll use two SLAs: **Time to First Response** and **Time to Resolution**, each with different durations depending on item priority. For details on creating SLAs, see [Defined SLAs in Time to SLA.](https://appfire.atlassian.net/wiki/spaces/TTSC/pages/35651691)

**Time to First Response**

| Priority | Target |
| --- | --- |
| P1 - Critical | 30 min |
| P2 - High | 2 hours |
| P3 - Low | 6 hours |

![SLA Time to first response](/cms_trial/assets/e6208ebe-69c1-4338-ad6e-735fd783a8c0.png)

**Time to Resolution**

| Priority | Target |
| --- | --- |
| P1 - Critical | 6 hours |
| P2 - High | 16 hours |
| P3 - Low | 72 hours |

![SLA Time to Resolution](/cms_trial/assets/48b98983-8660-4e17-9c94-35de1c8a338a.png)

Both SLAs start when the work item is created, pause while the status is **Waiting for customer**, and stop when you add a public comment (First Response) or set the resolution (Resolution).

### Escalate a case and see the SLAs

1. In Salesforce, create a new case:

   - **Subject:** Mobile app crashes when uploading profile photo
   - **Priority:** High
   - **Description:** The iOS app closes unexpectedly when users select a photo larger than 5 MB from their gallery. The issue started after the latest app update.
2. Save the case.
3. On the case record, locate the **Jira Issues** panel and click **Associate**/**Create**.

   ![image-20261002-065523.png](/cms_trial/assets/a9db5ff9-09c2-4908-aa0b-7727d9fc0e50.png)
4. Click **Create Jira Issue**.
5. Select your mapped Jira space and **Bug** as the issue type.   
   If you cannot select the Bug issue type, make sure your administrator has mapped the Case object type with Bug in Connector for Salesforce & Jira. For instructions, see [Configure entity and field mappings from templates](/cms_trial/space/CSFJIRA/3664152459/Configure+entity+and+field+mappings+from+templates/).
6. For **Association Configuration**, enable **Auto pul**l and **Auto push** to ensure updates sync across both platforms.
7. Click **Create**.

   ![Create Jira Issue](/cms_trial/assets/334175ef-5a5a-4b5c-9d08-2d8eefc442ca.png)
8. Refresh the page to allow synchronization to create a new bug and pull SLA data from Jira.   
   The **Jira Issue** panel displays the newly created Jira bug, and the **Time to SLA for Jira** panel shows both **Time to first response** and **Time to resolution** SLAs, already ticking down against the priority-based targets set.

![Jira Issue panel and Time to SLA for Jira panel](/cms_trial/assets/078b1a1c-3397-4a2b-988f-84bfccb02e53.png)

You can also go to Jira to see the new work item created. All updates will sync, and both teams can easily track the time remaining.

### Related resources

- [Configure mappings with Connector for Salesforce and Jira Documentation](/cms_trial/space/CSFJIRA/1854180614/Configure+entity%2C+field%2C+and+value+mappings/)
- [Time to SLA Cloud user guide](https://appfire.atlassian.net/wiki/spaces/TTSC/pages/1678575285)