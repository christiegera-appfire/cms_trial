# JMWE is moving to Atlassian Forge

![icon-feature-announcement-blue-light.png](/cms_trial/assets/d7bc39b9-0a0a-4c01-b97d-9e51cb9f50f7.png)

## **What is happening**

JMWE for Jira Cloud is moving to [**Forge**](https://developer.atlassian.com/platform/forge/), Atlassian’s next-generation platform for cloud apps. Forge apps run natively on Atlassian’s cloud infrastructure, so they share the same security, compliance, and reliability as Jira itself. Appfire is bringing JMWE and our other cloud apps to Forge so that you get these benefits as the platform develops.

![icon-feature-align-blue-light.png](/cms_trial/assets/51b170c1-deb2-4734-beba-85b58df23c26.png)

## **What this means for JMWE**

JMWE Cloud will move to Atlassian Forge in phases, to be completed by the **end of 2026**. For most customers, the move is automatic, and JMWE will look and work the way it does today. Some customers may see an option to upgrade when it suits them.

⚠️ Impersonation does not work on Forge as it did on Connect! **See below** for steps on updating ‘Run as’ configurations in your post functions.

⚠️ After the move, Data Center to Cloud [migrations](/cms_trial/space/JMWEC/466288660/Migrating+JMWE/) using **Configuration Manager for Jira (CMJ)** will no longer be supported. Cloud-to-cloud deployments will still be available.

![icon-feature-reliability-blue-light.png](/cms_trial/assets/a505d818-946b-4332-ad99-c786206a44dd.png)

## Enhancements on Forge

**Runs natively on Atlassian’s cloud.** All JMWE processing happens within Atlassian’s infrastructure, covered by the same security and compliance standards you already rely on for Jira!

**Expanded logs in one place.** More detailed JMWE logs are available in the standard Atlassian administration interface, so troubleshooting is faster and easier.

## **What you need to do**

Take a moment to check the steps below. If none of them apply to you, you don’t need to do anything, and JMWE keeps working as usual after the move!

![icon-feature-my-activity-blue-light.png](/cms_trial/assets/0f81413f-272a-42d1-9088-84b83ba566b2.png)

## All users

### 1. Monitor

![icon-feature-processes-blue-light.png](/cms_trial/assets/c2d33e5a-7e77-4416-84d1-924d7e0cc7ea.png)

For most users, no action is needed. After the move, check that your automations keep working as expected.

### 2. Review Event-based actions

![icon-feature-charge-blue-light.png](/cms_trial/assets/666a1b8d-0bd8-4db8-9326-18f89408d33c.png)

The **Work item property Added and Deleted** event trigger isn’t available on Forge. If you’re using these triggers, review those Event-based actions before your site moves and remove them or adjust your setup. Our [support team](https://support.appfire.com/) is happy to help you find the best approach.

### 3. Replace deprecated post functions

![icon-feature-inefficiency-blue-light.png](/cms_trial/assets/5a53d146-7800-4194-8f72-8f3b18dcb6f3.png)

Some post functions have been deprecated for several years and have long-standing replacements. These are now retired from the app with the release of JMWE on Forge. If you still use any, [switch to their replacements](/cms_trial/space/JMWEC/2104656018/Migrating+to+current+post+functions/) before your site moves.

### 4. Update post function ‘Run as’ configurations

![icon-feature-contract-blue-light.png](/cms_trial/assets/8e9faf3a-adfc-412f-a284-0b5786eb6bc0.png)

User impersonation does not work the same in Forge as it did in Connect; this may cause warnings or errors for any post functions configured to ‘Run as’ specific types of users (JSM guests, for example). If you see warnings, review the related post function and update the ‘Run as’ configuration to use a different account.

![icon-feature-contractor-blue-light.png](/cms_trial/assets/b924588b-9805-438a-a33a-5bbda18079ac.png)

## Advanced users

### 1. Declare egress URLs

![icon-feature-cloud-blue-light.png](/cms_trial/assets/3a548e4b-f942-4f80-86e8-81cad86a3ab6.png)

If your scripted extensions call external systems, for example with [callREST](/cms_trial/space/JMWEC/465242995/callRest/), add those URLs to the allowlist in [JMWE Administration](/cms_trial/space/JMWEC/465503776/JMWE+Administration/). This lets your integrations keep working after the move.

**Why this matters**: JMWE Cloud is working towards **Atlassian Enterprise Certified (AEC)** status. AEC apps only send date to destinations a customer approves. When you declare your URLs now, your external calls keep working, and you’re ready for that next step.