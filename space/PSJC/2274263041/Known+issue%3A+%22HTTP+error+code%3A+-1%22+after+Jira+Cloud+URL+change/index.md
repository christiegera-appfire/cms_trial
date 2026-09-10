# Known issue: "HTTP error code: -1" after Jira Cloud URL change

---

### Overview

This article addresses a known issue where users of **Power Scripts for Jira Cloud** encounter an `HTTP error code: -1` after their Jira Cloud site's URL is changed. The error prevents users from accessing most Power Scripts UI elements and can cause automations to fail.

This issue typically occurs shortly after Jira URL renaming (for example, `oldname.atlassian.net` to `newname.atlassian.net`). The Power Scripts app, which stores the Jira site's URL for internal communication, is unable to successfully connect to the renamed Jira instance, leading to a connection error.

---

### Symptoms

Users experiencing this issue will observe the following behaviors:

- An `HTTP error code: -1` message appears in the Power Scripts UI.
- Inability to access most Power Scripts pages, such as SIL Manager.
- Power Scripts automations might fail to run.
- The error message appears in an overlay on the screen, often obscuring the entire app UI.

You might see an error message similar to this:

```text
HTTP error code: -1. Path :
```

---

### Root cause

The underlying problem is a dependency on Atlassian Jira Cloud's behavior during a URL change. When you rename your Jira Cloud URL, Jira is expected to send a Site rename event to notify all installed apps of the change. However, in some cases, this event is not triggered or delivered to the Power Scripts app. As a result, the app is not notified that the base URL has changed and continues to reference outdated configuration data tied to the old URL. This leads to a connection failure and the `HTTP error code: -1` message.

---

### Solution

The most reliable way to fix this issue is to reinstall the app. This forces the app to register with the new Jira Cloud URL and re-establish a secure connection.

Due to recent changes introduced by Atlassian’s new Cloud Billing Engine, you might not be able to uninstall and reinstall apps with active subscriptions.

Here are the steps to resolve this issue.

#### **Step 1: Uninstall the app**

1. In Jira, click the **Settings** gear icon and select **Apps**.
2. Go to **Manage apps**.
3. In the list, find the app you want to remove and click its dropdown icon.
4. Depending on the available action, do this:

   - If the **Uninstall** button is available, confirm the action.
   - If the **Uninstall** button is unavailable or greyed out, click **Manage subscription**, cancel the app, wait until the cancellation completes, then return to uninstall.

When you cancel your subscription, the app is scheduled for deletion after a 30-day cancellation period. To expedite this, you must contact Atlassian's billing team directly.

See the Atlassian support article [Can't uninstall Jira Cloud apps after cancellation](https://support.atlassian.com/jira/kb/cant-uninstall-apps-after-cancellation/) for more information.

#### **Step 2: Reinstall the app**

1. In Jira, click the **Apps** menu at the top and select **Explore apps** (or **Find new apps**).
2. Use the search bar to find the desired app.
3. Click **Try it free** (or **Get app**), select your Jira Cloud site if prompted, and confirm installation.
4. Once installed, complete any required setup or grant permissions if prompted.

---

### Prevention

This issue is a direct result of a Jira Cloud URL change. To prevent it, you must be prepared to reinstall the Power Scripts app immediately following the change.

- **Plan ahead:** If you plan to rename your Jira Cloud URL, inform your administrators that an app reinstall will be required as part of the post-migration checklist.
- **Post-migration checklist:** Always include reinstalling Power Scripts in your checklist after Jira URL renaming.
- **Testing:** After a URL change, verify that all app functions are working properly by navigating to the Power Scripts UI.

---

### Additional Information

- **When to contact support:** If the problem persists after you have reinstalled the app, or if you are unable to uninstall the app, please contact our support team.
- **Atlassian documentation:** For more information on the updated process for uninstalling Jira Cloud apps, see [Atlassian documentation](https://support.atlassian.com/jira/kb/cant-uninstall-apps-after-cancellation/).
- **Future fixes:** We are actively investigating ways to make the app more resilient to Jira URL changes, but the current recommended resolution is to perform a fresh installation of the app.