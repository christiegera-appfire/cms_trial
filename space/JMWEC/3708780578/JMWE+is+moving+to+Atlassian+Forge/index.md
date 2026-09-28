# JMWE is moving to Atlassian Forge

![icon-feature-announcement-blue-light.png](/cms_trial/assets/a6be39a3-9751-4467-9f14-1865fc9ee53e.png)

## **What is happening**

JMWE for Jira Cloud is moving to [**Forge**](https://developer.atlassian.com/platform/forge/), Atlassian’s next-generation platform for cloud apps. Forge apps run natively on Atlassian’s cloud infrastructure, so they share the same security, compliance, and reliability as Jira itself. Appfire is bringing JMWE and our other cloud apps to Forge so that you get these benefits as the platform develops.

![icon-feature-align-blue-light.png](/cms_trial/assets/9c5c6964-9d55-4020-815d-11a7ae74bbee.png)

## **What this means for JMWE**

JMWE Cloud will move to Atlassian Forge in phases, to be completed by the **end of 2026**. For most customers the move is automatic, and JMWE will look and work the way it does today. Some cusotmers may see an option to upgrade when it suits them.

⚠️ After the move, [migrations](/cms_trial/space/JMWEC/466288660/Migrating+JMWE/) using **Configuration Manager for Jira (CMJ)** will no longer be supported.

![icon-feature-reliability-blue-light.png](/cms_trial/assets/2c1ed5ba-5cb3-406d-a01f-fe417610de13.png)

## Enhancements on Forge

**Runs natively on Atlassian’s cloud.** All JMWE processing happens within Atlassian’s infrastructure, covered by the same security and compliance standards you already rely on for Jira!

**Expanded logs in one place.** More detailed JMWE logs are available in the standard Atlassian administration interface, so troubleshooting is faster and easier.

## **What you need to do**

Take a moment to check the steps below. If none of them apply to you, you don’t need to do anything, and JMWE keeps working as usual after the move!

![icon-feature-my-activity-blue-light.png](/cms_trial/assets/3fada8fe-5d34-426a-a9c1-dba35e48e24d.png)

## All users

### 1. Monitor

![icon-feature-processes-blue-light.png](/cms_trial/assets/15256411-1638-4cbc-9e9b-60b4f62702f3.png)

For most users, no action is needed. After the move, check that your automations keep working as expected.

### 2. Review Event-based actions

![icon-feature-charge-blue-light.png](/cms_trial/assets/e7f7dfe3-c8d6-472d-952c-ca74021e940b.png)

The **Work item property Added and Deleted** event trigger isn’t available on Forge. If you’re using these triggers, review those Event-based actions before your site moves and remove them or adjust your setup. Our [support team](https://support.appfire.com/) is happy to help you find the best approach.

### 3. Replace deprecated post functions

![icon-feature-inefficiency-blue-light.png](/cms_trial/assets/adf7a92f-9a78-40f6-9b9e-29b9ebb0596d.png)

Some post functions have been deprecated for several years and have long-standing replacements. These are now retired from the app with the release of JMWE on Forge. If you still use any, [switch to their replacements](/cms_trial/space/JMWEC/2104656018/Migrating+to+current+post+functions/) before your site moves.

![icon-feature-contractor-blue-light.png](/cms_trial/assets/31a9c7d4-9060-495b-8095-526ac71a96d8.png)

## Advanced users

### 1. Declare egress URLs

![icon-feature-cloud-blue-light.png](/cms_trial/assets/f42fbd03-2bd1-4399-b487-d2347db7466b.png)

If your scripted extensions call external systems, for example with [callREST](/cms_trial/space/JMWEC/465242995/callRest/), add those URLs to the allowlist in [JMWE Administration](/cms_trial/space/JMWEC/465503776/JMWE+Administration/). This lets your integrations keep working after the move.

**Why this matters**: JMWE Cloud is working towards **Atlassian Enterprise Certified (AEC)** status. AEC apps only send date to destinations a customer approves. When you declare your URLs now, your external calls keep working, and you’re ready for that next step.